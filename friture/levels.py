#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2009 Timoth?Lecomte

# This file is part of Friture.
#
# Friture is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as published by
# the Free Software Foundation.
#
# Friture is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Friture.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import log10, abs, arange
from friture.levels_settings import Levels_Settings_Dialog # settings dialog
from friture.qsynthmeter import qsynthMeter
from friture.audioproc import audioproc
from friture.logger import PrintLogger

from friture.exp_smoothing_conv import pyx_exp_smoothed_value

from friture.audiobackend import SAMPLING_RATE

STYLESHEET = """
qsynthMeter {
#border: 1px solid gray;
#border-radius: 2px;
padding: 1px;
}
"""

SMOOTH_DISPLAY_TIMER_PERIOD_MS = 25
LEVEL_TEXT_LABEL_PERIOD_MS = 250

LEVEL_TEXT_LABEL_STEPS = LEVEL_TEXT_LABEL_PERIOD_MS/SMOOTH_DISPLAY_TIMER_PERIOD_MS

class Levels_Widget(QtWidgets.QWidget):
	def __init__(self, parent = None, logger = PrintLogger()):
		super().__init__(parent)
		self.setObjectName("Levels_Widget")
		
		self.gridLayout = QtWidgets.QGridLayout(self)
		self.gridLayout.setObjectName("gridLayout")

		font = QtGui.QFont()
		font.setPointSize(14)
		font.setWeight(75)
		font.setBold(True)

		self.label_peak = QtWidgets.QLabel(self)
		self.label_peak.setFont(font)
		#QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft
		self.label_peak.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight)
		self.label_peak.setObjectName("label_peak")

		self.label_peak_legend = QtWidgets.QLabel(self)
		self.label_peak_legend.setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignRight)
		self.label_peak_legend.setObjectName("label_peak_legend")

		self.label_rms = QtWidgets.QLabel(self)
		self.label_rms.setFont(font)
		self.label_rms.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight)
		self.label_rms.setObjectName("label_rms")

		self.label_rms_legend = QtWidgets.QLabel(self)
		self.label_rms_legend.setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignRight)
		self.label_rms_legend.setObjectName("label_rms_legend")

		self.meter = qsynthMeter(self)
		self.meter.setStyleSheet(STYLESHEET)
		self.meter.setObjectName("meter")

		self.gridLayout.addWidget(self.label_peak, 0, 0, 1, 1)
		self.gridLayout.addWidget(self.label_peak_legend, 1, 0, 1, 1)
		self.gridLayout.addWidget(self.label_rms, 2, 0, 1, 1)
		self.gridLayout.addWidget(self.label_rms_legend, 3, 0, 1, 1)

		self.gridLayout.addWidget(self.meter, 0, 1, 4, 1)

		self.label_rms.setText("-100.0")
		self.label_peak.setText("-100.0")
		self.label_rms_legend.setText("dB FS\n RMS")
		self.label_peak_legend.setText("dB FS\n Peak")
		self.label_rms.setTextFormat(QtCore.Qt.PlainText)
		self.label_peak.setTextFormat(QtCore.Qt.PlainText)
		#self.label_rms.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
		#self.label_rms_legend.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
		#self.label_peak.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
		#self.label_peak_legend.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
		
		self.logger = logger
		self.audiobuffer = None
		
		# initialize the settings dialog
		self.settings_dialog = Levels_Settings_Dialog(self, self.logger)
		
		# initialize the class instance that will do the fft
		self.proc = audioproc(self.logger)
		
		#time = SMOOTH_DISPLAY_TIMER_PERIOD_MS/1000. #DISPLAY
		#time = 0.025 #IMPULSE setting for a sound level meter
		#time = 0.125 #FAST setting for a sound level meter
		#time = 1. #SLOW setting for a sound level meter
		self.response_time = 0.300 #300ms is a common value for VU meters
		# an exponential smoothing filter is a simple IIR filter
		# s_i = alpha*x_i + (1-alpha)*s_{i-1}
		#we compute alpha so that the n most recent samples represent 100*w percent of the output
		w = 0.65
		n = self.response_time*SAMPLING_RATE
		N = 4096
		self.alpha = 1. - (1.-w)**(1./(n+1))
		self.kernel = (1. - self.alpha)**(arange(0, N)[::-1])
		# first channel
		self.old_rms = 1e-30
		self.old_max = 1e-30
		# second channel
		self.old_rms_2 = 1e-30
		self.old_max_2 = 1e-30
		
		response_time_peaks = 0.025 # 25ms for instantaneous peaks
		n2 = response_time_peaks/(SMOOTH_DISPLAY_TIMER_PERIOD_MS/1000.)
		self.alpha2 = 1. - (1.-w)**(1./(n2+1))
  
		self.two_channels = False

		self.i = 0

	# method
	def set_buffer(self, buffer):
		self.audiobuffer = buffer

	# method
	def update(self):
		if not self.isVisible():
			return

		self.i += 1		

		# get the fresh data
		floatdata = self.audiobuffer.newdata()

		if floatdata.shape[0] > 1 and self.two_channels == False:
			self.meter.setPortCount(2)
			self.two_channels = True
		elif floatdata.shape[0] == 1 and self.two_channels == True:
			self.meter.setPortCount(1)
			self.two_channels = False

		# first channel
		y1 = floatdata[0,:]
		
		# exponential smoothing for max
		if len(y1) > 0:
			value_max = abs(y1).max()
			if value_max > self.old_max*(1.-self.alpha2):
				self.old_max = value_max
			else:
				# exponential decrease
				self.old_max *= (1.-self.alpha2)
		
		# exponential smoothing for RMS
		value_rms = pyx_exp_smoothed_value(self.kernel, self.alpha, y1**2, self.old_rms)
		self.old_rms = value_rms
		
		level_rms = 10.*log10(value_rms + 0.*1e-80)
		level_max = 20.*log10(self.old_max + 0.*1e-80)
  
		if self.i == LEVEL_TEXT_LABEL_STEPS:
	    		if level_rms > -150.:
	    			string_rms = "%+05.01f" % level_rms
	    		else:
	    			string_rms = "-Inf"
	    		if level_max > -150.:
	    			string_peak = "%+05.01f" % level_max
	    		else:
	    			string_peak = "-Inf"

		if not self.two_channels:
			self.meter.setValue(0, level_rms, level_max)
			if self.i == LEVEL_TEXT_LABEL_STEPS:
				self.label_rms.setText(string_rms)
				self.label_peak.setText(string_peak)
		else:
			# second channel
			y2 = floatdata[1,:]
		
			# exponential smoothing for max
			if len(y2) > 0:
				value_max = abs(y2).max()
				if value_max > self.old_max_2*(1.-self.alpha2):
					self.old_max_2 = value_max
				else:
					# exponential decrease
					self.old_max_2 *= (1.-self.alpha2)
			
			# exponential smoothing for RMS
			value_rms = pyx_exp_smoothed_value(self.kernel, self.alpha, y2**2, self.old_rms_2)
			self.old_rms_2 = value_rms
			
			level_rms_2 = 10.*log10(value_rms + 0.*1e-80)
			level_max_2 = 20.*log10(self.old_max_2 + 0.*1e-80)

			#self.meter.m_iPortCount = 3
			self.meter.setValue(0, level_rms, level_max)
			self.meter.setValue(1, level_rms_2, level_max_2)

			if self.i == LEVEL_TEXT_LABEL_STEPS:
				if level_rms_2 > -150.:
					string_rms_2 = "%+05.01f" % level_rms_2
				else:
					string_rms_2 = "-Inf"
				if level_max > -150.:
					string_peak_2 = "%+05.01f" % level_max_2
				else:
					string_peak_2 = "-Inf"

				self.label_rms.setText("1: %s\n2: %s" %(string_rms, string_rms_2))
				self.label_peak.setText("1: %s\n2: %s" %(string_peak, string_peak_2))

		if self.i == LEVEL_TEXT_LABEL_STEPS:
			self.i = 0

		if 0:
			fft_size = time*SAMPLING_RATE #1024
			maxfreq = SAMPLING_RATE/2
			sp, freq, A, B, C = self.proc.analyzelive(floatdata, fft_size, maxfreq)
			print(level_rms, 10*log10((sp**2).sum()*2.), freq.max())

	# slot
	def settings_called(self, checked):
		self.settings_dialog.show()

	# method
	def saveState(self, settings):
		self.settings_dialog.saveState(settings)
	
	# method
	def restoreState(self, settings):
		self.settings_dialog.restoreState(settings)
