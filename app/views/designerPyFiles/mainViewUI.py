# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainViewUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(997, 518)
        MainWindow.setTabletTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgRc/images/mainWindow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px;\n"
"    \n"
"    background-color: rgb(4, 98, 100);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px;\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px;\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px;\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setAutoFillBackground(False)
        self.mdiArea.setStyleSheet("")
        self.mdiArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mdiArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mdiArea.setLineWidth(1)
        self.mdiArea.setMidLineWidth(0)
        self.mdiArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        brush = QtGui.QBrush(QtGui.QColor(3, 61, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setActivationOrder(QtWidgets.QMdiArea.CreationOrder)
        self.mdiArea.setViewMode(QtWidgets.QMdiArea.SubWindowView)
        self.mdiArea.setDocumentMode(False)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setTabsMovable(True)
        self.mdiArea.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidgetDataView = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetDataView.setMinimumSize(QtCore.QSize(298, 264))
        self.dockWidgetDataView.setAccessibleName("")
        self.dockWidgetDataView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dockWidgetDataView.setAutoFillBackground(False)
        self.dockWidgetDataView.setFloating(False)
        self.dockWidgetDataView.setObjectName("dockWidgetDataView")
        self.dockWidgetContentsDataSet = QtWidgets.QWidget()
        self.dockWidgetContentsDataSet.setObjectName("dockWidgetContentsDataSet")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContentsDataSet)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableView = QtWidgets.QTableView(self.dockWidgetContentsDataSet)
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 1, 0, 1, 3)
        self.toolButtonObjectsSettings = QtWidgets.QToolButton(self.dockWidgetContentsDataSet)
        self.toolButtonObjectsSettings.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolButtonObjectsSettings.setAutoFillBackground(False)
        self.toolButtonObjectsSettings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imgRc/images/moreOperationsOnData.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonObjectsSettings.setIcon(icon1)
        self.toolButtonObjectsSettings.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButtonObjectsSettings.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButtonObjectsSettings.setAutoRaise(True)
        self.toolButtonObjectsSettings.setObjectName("toolButtonObjectsSettings")
        self.gridLayout_3.addWidget(self.toolButtonObjectsSettings, 0, 1, 1, 1)
        self.lineEditFilter = QtWidgets.QLineEdit(self.dockWidgetContentsDataSet)
        self.lineEditFilter.setInputMask("")
        self.lineEditFilter.setText("")
        self.lineEditFilter.setObjectName("lineEditFilter")
        self.gridLayout_3.addWidget(self.lineEditFilter, 0, 0, 1, 1)
        self.dockWidgetDataView.setWidget(self.dockWidgetContentsDataSet)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetDataView)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNelp = QtWidgets.QMenu(self.menubar)
        self.menuNelp.setObjectName("menuNelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuAnalysisTools = QtWidgets.QMenu(self.menubar)
        self.menuAnalysisTools.setObjectName("menuAnalysisTools")
        MainWindow.setMenuBar(self.menubar)
        self.dockWidgetProtocol = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetProtocol.setTabletTracking(False)
        self.dockWidgetProtocol.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dockWidgetProtocol.setFloating(False)
        self.dockWidgetProtocol.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidgetProtocol.setObjectName("dockWidgetProtocol")
        self.dockWidgetContentsProtocol = QtWidgets.QWidget()
        self.dockWidgetContentsProtocol.setObjectName("dockWidgetContentsProtocol")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContentsProtocol)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.treeViewProtocol = QtWidgets.QTreeView(self.dockWidgetContentsProtocol)
        self.treeViewProtocol.setObjectName("treeViewProtocol")
        self.gridLayout_2.addWidget(self.treeViewProtocol, 0, 0, 1, 1)
        self.dockWidgetProtocol.setWidget(self.dockWidgetContentsProtocol)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetProtocol)
        self.toolBarViewActions = QtWidgets.QToolBar(MainWindow)
        self.toolBarViewActions.setObjectName("toolBarViewActions")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBarViewActions)
        self.toolBarAnalysisActions = QtWidgets.QToolBar(MainWindow)
        self.toolBarAnalysisActions.setObjectName("toolBarAnalysisActions")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBarAnalysisActions)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imgRc/images/inbox.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDataAnalysisHelp = QtWidgets.QAction(MainWindow)
        self.actionDataAnalysisHelp.setObjectName("actionDataAnalysisHelp")
        self.actionUsage = QtWidgets.QAction(MainWindow)
        self.actionUsage.setObjectName("actionUsage")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imgRc/images/outbox.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")
        self.actionDataView = QtWidgets.QAction(MainWindow)
        self.actionDataView.setCheckable(True)
        self.actionDataView.setChecked(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imgRc/images/objects.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDataView.setIcon(icon4)
        self.actionDataView.setObjectName("actionDataView")
        self.actionProtocolRender = QtWidgets.QAction(MainWindow)
        self.actionProtocolRender.setCheckable(True)
        self.actionProtocolRender.setChecked(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/imgRc/images/protocol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProtocolRender.setIcon(icon5)
        self.actionProtocolRender.setObjectName("actionProtocolRender")
        self.actionCloseAll = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/imgRc/images/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCloseAll.setIcon(icon6)
        self.actionCloseAll.setObjectName("actionCloseAll")
        self.actionOneDimensionalAnalysis = QtWidgets.QAction(MainWindow)
        self.actionOneDimensionalAnalysis.setObjectName("actionOneDimensionalAnalysis")
        self.actionTwoDimensionalAnalysis = QtWidgets.QAction(MainWindow)
        self.actionTwoDimensionalAnalysis.setObjectName("actionTwoDimensionalAnalysis")
        self.actionMultiDimensionalAnalysis = QtWidgets.QAction(MainWindow)
        self.actionMultiDimensionalAnalysis.setObjectName("actionMultiDimensionalAnalysis")
        self.actionPrimaryAnalysis = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/imgRc/images/primaryAnalysis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrimaryAnalysis.setIcon(icon7)
        self.actionPrimaryAnalysis.setObjectName("actionPrimaryAnalysis")
        self.actionDeleteObjects = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/imgRc/images/removeObject.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteObjects.setIcon(icon8)
        self.actionDeleteObjects.setObjectName("actionDeleteObjects")
        self.actionPreviewObjects = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/imgRc/images/previewData.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreviewObjects.setIcon(icon9)
        self.actionPreviewObjects.setObjectName("actionPreviewObjects")
        self.actionShiftData = QtWidgets.QAction(MainWindow)
        self.actionShiftData.setObjectName("actionShiftData")
        self.actionLogData = QtWidgets.QAction(MainWindow)
        self.actionLogData.setObjectName("actionLogData")
        self.actionStandartizeData = QtWidgets.QAction(MainWindow)
        self.actionStandartizeData.setObjectName("actionStandartizeData")
        self.actionDeleteAbnormalData = QtWidgets.QAction(MainWindow)
        self.actionDeleteAbnormalData.setObjectName("actionDeleteAbnormalData")
        self.actionConvertToCSV = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/imgRc/images/convert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConvertToCSV.setIcon(icon10)
        self.actionConvertToCSV.setObjectName("actionConvertToCSV")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionConvertToCSV)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuNelp.addAction(self.actionDataAnalysisHelp)
        self.menuNelp.addAction(self.actionUsage)
        self.menuView.addAction(self.actionDataView)
        self.menuView.addAction(self.actionProtocolRender)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionOneDimensionalAnalysis)
        self.menuView.addAction(self.actionTwoDimensionalAnalysis)
        self.menuView.addAction(self.actionMultiDimensionalAnalysis)
        self.menuAnalysisTools.addAction(self.actionCloseAll)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAnalysisTools.menuAction())
        self.menubar.addAction(self.menuNelp.menuAction())
        self.toolBarViewActions.addAction(self.actionDataView)
        self.toolBarViewActions.addAction(self.actionProtocolRender)
        self.toolBarAnalysisActions.addAction(self.actionPrimaryAnalysis)

        self.retranslateUi(MainWindow)
        self.actionDataView.toggled['bool'].connect(self.dockWidgetDataView.setVisible)
        self.actionProtocolRender.toggled['bool'].connect(self.dockWidgetProtocol.setVisible)
        self.dockWidgetProtocol.visibilityChanged['bool'].connect(self.actionProtocolRender.setChecked)
        self.dockWidgetDataView.visibilityChanged['bool'].connect(self.actionDataView.setChecked)
        self.actionCloseAll.triggered['bool'].connect(self.dockWidgetDataView.setVisible)
        self.actionCloseAll.triggered['bool'].connect(self.dockWidgetProtocol.setVisible)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Програмне забезпечення для аналізу даних."))
        self.dockWidgetDataView.setWindowTitle(_translate("MainWindow", "Об\'єкти"))
        self.toolButtonObjectsSettings.setToolTip(_translate("MainWindow", "Додаткові налаштування даних"))
        self.lineEditFilter.setPlaceholderText(_translate("MainWindow", "Фільтр"))
        self.menuFile.setTitle(_translate("MainWindow", "&Файл"))
        self.menuNelp.setTitle(_translate("MainWindow", "&Допомога"))
        self.menuView.setTitle(_translate("MainWindow", "&Перегляд"))
        self.menuAnalysisTools.setTitle(_translate("MainWindow", "&Вікно"))
        self.dockWidgetProtocol.setWindowTitle(_translate("MainWindow", "Протокол"))
        self.toolBarViewActions.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBarAnalysisActions.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Відкрити..."))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "Вийти"))
        self.actionDataAnalysisHelp.setText(_translate("MainWindow", "Про програму"))
        self.actionUsage.setText(_translate("MainWindow", "Як використовувати"))
        self.actionUsage.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionSave.setText(_translate("MainWindow", "Зберегти"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionDataView.setText(_translate("MainWindow", "Об\'єкти"))
        self.actionDataView.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionProtocolRender.setText(_translate("MainWindow", "Протокол"))
        self.actionProtocolRender.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionCloseAll.setText(_translate("MainWindow", "Приховати відкрите"))
        self.actionCloseAll.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionOneDimensionalAnalysis.setText(_translate("MainWindow", "Аналіз одновимірних даних"))
        self.actionTwoDimensionalAnalysis.setText(_translate("MainWindow", "Аналіз двовимірних даних"))
        self.actionMultiDimensionalAnalysis.setText(_translate("MainWindow", "Аналіз багатовимірних даних"))
        self.actionPrimaryAnalysis.setText(_translate("MainWindow", "Провести первинний статистичний аналіз"))
        self.actionDeleteObjects.setText(_translate("MainWindow", "Видалити об\'єкт"))
        self.actionPreviewObjects.setText(_translate("MainWindow", "Продивитись дані"))
        self.actionShiftData.setText(_translate("MainWindow", "Зсув даних"))
        self.actionLogData.setText(_translate("MainWindow", "Логарифмувати дані"))
        self.actionStandartizeData.setText(_translate("MainWindow", "Стандартизувати дані"))
        self.actionDeleteAbnormalData.setText(_translate("MainWindow", "Видалити аномальні спостереження"))
        self.actionConvertToCSV.setText(_translate("MainWindow", "Конвертувати у csv"))


from app import dataAnalysisRC
