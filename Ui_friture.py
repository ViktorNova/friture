# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'friture.ui'
#
# Created: Thu Jun 10 17:13:18 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(869, 573)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/window-icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("None")
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.dockWidgetStatistics = QtGui.QDockWidget(MainWindow)
        self.dockWidgetStatistics.setStyleSheet("None")
        self.dockWidgetStatistics.setObjectName("dockWidgetStatistics")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 82, 227))
        self.scrollAreaWidgetContents.setStyleSheet("QWidget {\n"
"background: white\n"
"}\n"
"")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LabelLevel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.LabelLevel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.LabelLevel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.LabelLevel.setObjectName("LabelLevel")
        self.verticalLayout.addWidget(self.LabelLevel)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.dockWidgetStatistics.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetStatistics)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.dockWidgetLog = QtGui.QDockWidget(MainWindow)
        self.dockWidgetLog.setObjectName("dockWidgetLog")
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_9 = QtGui.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.scrollArea_2 = QtGui.QScrollArea(self.dockWidgetContents_3)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget(self.scrollArea_2)
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 74, 240))
        self.scrollAreaWidgetContents_2.setStyleSheet("QWidget {\n"
"background: white\n"
"}\n"
"")
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_10 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.LabelLog = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.LabelLog.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.LabelLog.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.LabelLog.setObjectName("LabelLog")
        self.gridLayout_10.addWidget(self.LabelLog, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_9.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.dockWidgetLog.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetLog)
        self.actionStart = QtGui.QAction(MainWindow)
        self.actionStart.setCheckable(True)
        self.actionStart.setChecked(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/start.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/start.svg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/start.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/start.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.actionStart.setIcon(icon1)
        self.actionStart.setObjectName("actionStart")
        self.actionSettings = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/tools.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon2)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName("actionAbout")
        self.actionNew_dock = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/new-dock.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_dock.setIcon(icon3)
        self.actionNew_dock.setObjectName("actionNew_dock")
        self.toolBar.addAction(self.actionStart)
        self.toolBar.addAction(self.actionNew_dock)
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Friture", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetStatistics.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelLevel.setText(QtGui.QApplication.translate("MainWindow", "No statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetLog.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Log", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart.setToolTip(QtGui.QApplication.translate("MainWindow", "Start/Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setToolTip(QtGui.QApplication.translate("MainWindow", "Display settings dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About Friture", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_dock.setText(QtGui.QApplication.translate("MainWindow", "New dock", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_dock.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a new dock to Friture window", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
