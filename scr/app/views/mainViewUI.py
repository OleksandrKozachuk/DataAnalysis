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
        icon.addPixmap(QtGui.QPixmap(":/imgRc/images/analytics.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
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
                                 "        stop:0.4 #343434/*,\n"
                                 "        stop:0.2 #343434,\n"
                                 "        stop:0.1 #ffaa00*/\n"
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
                                 "QWidget:focus\n"
                                 "{\n"
                                 "    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
                                 "    padding: 1px;\n"
                                 "    border-style: solid;\n"
                                 "    border: 1px solid #1e1e1e;\n"
                                 "    border-radius: 5;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton\n"
                                 "{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
                                 "    border-width: 1px;\n"
                                 "    border-color: #1e1e1e;\n"
                                 "    border-style: solid;\n"
                                 "    border-radius: 6;\n"
                                 "    padding: 3px;\n"
                                 "    font-size: 12px;\n"
                                 "    padding-left: 5px;\n"
                                 "    padding-right: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox\n"
                                 "{\n"
                                 "    selection-background-color: #ffaa00;\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
                                 "    border-style: solid;\n"
                                 "    border: 1px solid #1e1e1e;\n"
                                 "    border-radius: 5;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox:hover,QPushButton:hover\n"
                                 "{\n"
                                 "    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QComboBox:on\n"
                                 "{\n"
                                 "    padding-top: 3px;\n"
                                 "    padding-left: 4px;\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
                                 "    selection-background-color: #ffaa00;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox QAbstractItemView\n"
                                 "{\n"
                                 "    border: 2px solid darkgray;\n"
                                 "    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::drop-down\n"
                                 "{\n"
                                 "     subcontrol-origin: padding;\n"
                                 "     subcontrol-position: top right;\n"
                                 "     width: 15px;\n"
                                 "\n"
                                 "     border-left-width: 0px;\n"
                                 "     border-left-color: darkgray;\n"
                                 "     border-left-style: solid; /* just a single line */\n"
                                 "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                 "     border-bottom-right-radius: 3px;\n"
                                 " }\n"
                                 "\n"
                                 "QComboBox::down-arrow\n"
                                 "{\n"
                                 "     image: url(:/down_arrow.png);\n"
                                 "}\n"
                                 "\n"
                                 "QGroupBox:focus\n"
                                 "{\n"
                                 "border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                 "}\n"
                                 "\n"
                                 "QTextEdit:focus\n"
                                 "{\n"
                                 "    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
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
                                 "QTextEdit\n"
                                 "{\n"
                                 "    background-color: #242424;\n"
                                 "}\n"
                                 "\n"
                                 "QPlainTextEdit\n"
                                 "{\n"
                                 "    background-color: #242424;\n"
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
                                 "QCheckBox:disabled\n"
                                 "{\n"
                                 "color: #414141;\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::title\n"
                                 "{\n"
                                 "    text-align: center;\n"
                                 "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::close-button, QDockWidget::float-button\n"
                                 "{\n"
                                 "    text-align: center;\n"
                                 "    spacing: 1px; /* spacing between items in the tool bar */\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
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
                                 "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                 "}\n"
                                 "\n"
                                 "QMainWindow::separator:hover\n"
                                 "{\n"
                                 "\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    border: 1px solid #6c6c6c;\n"
                                 "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                 "}\n"
                                 "\n"
                                 "QToolBar::handle\n"
                                 "{\n"
                                 "     spacing: 3px; /* spacing between items in the tool bar */\n"
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
                                 "QProgressBar::chunk\n"
                                 "{\n"
                                 "    background-color: #d7801a;\n"
                                 "    width: 2.15px;\n"
                                 "    margin: 0.5px;\n"
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
                                 "    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
                                 "    border-top-right-radius: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:first:!selected\n"
                                 "{\n"
                                 " margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
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
                                 "    /*border-top: 2px solid #ffaa00;\n"
                                 "    padding-bottom: 3px;*/\n"
                                 "    border-top-left-radius: 3px;\n"
                                 "    border-top-right-radius: 3px;\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: #323232;\n"
                                 "    border: 1px solid #b1b1b1;\n"
                                 "    border-radius: 6px;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:checked\n"
                                 "{\n"
                                 "    background-color: qradialgradient(\n"
                                 "        cx: 0.5, cy: 0.5,\n"
                                 "        fx: 0.5, fy: 0.5,\n"
                                 "        radius: 1.0,\n"
                                 "        stop: 0.25 #ffaa00,\n"
                                 "        stop: 0.3 #323232\n"
                                 "    );\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: #323232;\n"
                                 "    border: 1px solid #b1b1b1;\n"
                                 "    width: 9px;\n"
                                 "    height: 9px;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator\n"
                                 "{\n"
                                 "    border-radius: 6px;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
                                 "{\n"
                                 "    border: 1px solid #ffaa00;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:checked\n"
                                 "{\n"
                                 "    image:url(:/images/checkbox.png);\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
                                 "{\n"
                                 "    border: 1px solid #444;\n"
                                 "}")
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
        brush = QtGui.QBrush(QtGui.QColor(2, 36, 32))
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
        self.dockWidgetDataView.setMinimumSize(QtCore.QSize(162, 264))
        self.dockWidgetDataView.setAccessibleName("")
        self.dockWidgetDataView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dockWidgetDataView.setAutoFillBackground(False)
        self.dockWidgetDataView.setFloating(False)
        self.dockWidgetDataView.setObjectName("dockWidgetDataView")
        self.dockWidgetContentsDataSet = QtWidgets.QWidget()
        self.dockWidgetContentsDataSet.setObjectName("dockWidgetContentsDataSet")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dockWidgetContentsDataSet)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBoxFileData = QtWidgets.QGroupBox(self.dockWidgetContentsDataSet)
        self.groupBoxFileData.setObjectName("groupBoxFileData")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBoxFileData)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textBrowserFileData = QtWidgets.QTextBrowser(self.groupBoxFileData)
        self.textBrowserFileData.setObjectName("textBrowserFileData")
        self.gridLayout_5.addWidget(self.textBrowserFileData, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBoxFileData, 1, 0, 1, 1)
        self.listWidgetDataView = QtWidgets.QListWidget(self.dockWidgetContentsDataSet)
        self.listWidgetDataView.setObjectName("listWidgetDataView")
        self.gridLayout_4.addWidget(self.listWidgetDataView, 0, 0, 1, 1)
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
        self.menuMore = QtWidgets.QMenu(self.menuView)
        self.menuMore.setObjectName("menuMore")
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
        self.groupBoxProtocolDetails = QtWidgets.QGroupBox(self.dockWidgetContentsProtocol)
        self.groupBoxProtocolDetails.setObjectName("groupBoxProtocolDetails")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxProtocolDetails)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowserProtocolDetails = QtWidgets.QTextBrowser(self.groupBoxProtocolDetails)
        self.textBrowserProtocolDetails.setObjectName("textBrowserProtocolDetails")
        self.gridLayout_3.addWidget(self.textBrowserProtocolDetails, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBoxProtocolDetails, 1, 0, 1, 1)
        self.treeViewProtocol = QtWidgets.QTreeView(self.dockWidgetContentsProtocol)
        self.treeViewProtocol.setObjectName("treeViewProtocol")
        self.gridLayout_2.addWidget(self.treeViewProtocol, 0, 0, 1, 1)
        self.dockWidgetProtocol.setWidget(self.dockWidgetContentsProtocol)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetProtocol)
        self.toolBarFileActions = QtWidgets.QToolBar(MainWindow)
        self.toolBarFileActions.setObjectName("toolBarFileActions")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarFileActions)
        self.toolBarViewActions = QtWidgets.QToolBar(MainWindow)
        self.toolBarViewActions.setObjectName("toolBarViewActions")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarViewActions)
        self.toolBarOtherActions = QtWidgets.QToolBar(MainWindow)
        self.toolBarOtherActions.setObjectName("toolBarOtherActions")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarOtherActions)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imgRc/images/inbox.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDataAnalysisHelp = QtWidgets.QAction(MainWindow)
        self.actionDataAnalysisHelp.setObjectName("actionDataAnalysisHelp")
        self.actionAboutUI = QtWidgets.QAction(MainWindow)
        self.actionAboutUI.setObjectName("actionAboutUI")
        self.actionUsage = QtWidgets.QAction(MainWindow)
        self.actionUsage.setObjectName("actionUsage")
        self.actionSaveAll = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imgRc/images/outbox.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.actionSaveAll.setIcon(icon2)
        self.actionSaveAll.setObjectName("actionSaveAll")
        self.actionDataView = QtWidgets.QAction(MainWindow)
        self.actionDataView.setCheckable(True)
        self.actionDataView.setChecked(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imgRc/images/file.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.actionDataView.setIcon(icon3)
        self.actionDataView.setObjectName("actionDataView")
        self.actionProtocolRender = QtWidgets.QAction(MainWindow)
        self.actionProtocolRender.setCheckable(True)
        self.actionProtocolRender.setChecked(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imgRc/images/analytics-2.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.actionProtocolRender.setIcon(icon4)
        self.actionProtocolRender.setObjectName("actionProtocolRender")
        self.actionShowFileData = QtWidgets.QAction(MainWindow)
        self.actionShowFileData.setCheckable(True)
        self.actionShowFileData.setChecked(False)
        self.actionShowFileData.setObjectName("actionShowFileData")
        self.actionShowAdditionalDetails = QtWidgets.QAction(MainWindow)
        self.actionShowAdditionalDetails.setCheckable(True)
        self.actionShowAdditionalDetails.setChecked(False)
        self.actionShowAdditionalDetails.setObjectName("actionShowAdditionalDetails")
        self.actionCloseAll = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/imgRc/images/close.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.actionCloseAll.setIcon(icon5)
        self.actionCloseAll.setObjectName("actionCloseAll")
        self.actionShowFileDialog = QtWidgets.QAction(MainWindow)
        self.actionShowFileDialog.setCheckable(True)
        self.actionShowFileDialog.setChecked(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/imgRc/images/openFileDialog.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.actionShowFileDialog.setIcon(icon6)
        self.actionShowFileDialog.setObjectName("actionShowFileDialog")
        self.actionMaximize = QtWidgets.QAction(MainWindow)
        self.actionMaximize.setObjectName("actionMaximize")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSaveAll)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuNelp.addAction(self.actionDataAnalysisHelp)
        self.menuNelp.addSeparator()
        self.menuNelp.addAction(self.actionUsage)
        self.menuMore.addAction(self.actionShowFileData)
        self.menuMore.addAction(self.actionShowAdditionalDetails)
        self.menuView.addAction(self.actionDataView)
        self.menuView.addAction(self.actionProtocolRender)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionShowFileDialog)
        self.menuView.addSeparator()
        self.menuView.addSeparator()
        self.menuView.addAction(self.menuMore.menuAction())
        self.menuView.addAction(self.actionCloseAll)
        self.menuAnalysisTools.addAction(self.actionMaximize)
        self.menuAnalysisTools.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAnalysisTools.menuAction())
        self.menubar.addAction(self.menuNelp.menuAction())
        self.toolBarFileActions.addAction(self.actionOpen)
        self.toolBarFileActions.addAction(self.actionSaveAll)
        self.toolBarViewActions.addAction(self.actionDataView)
        self.toolBarViewActions.addAction(self.actionProtocolRender)
        self.toolBarOtherActions.addAction(self.actionCloseAll)

        self.retranslateUi(MainWindow)
        self.actionDataView.toggled['bool'].connect(self.dockWidgetDataView.setVisible)
        self.actionProtocolRender.toggled['bool'].connect(self.dockWidgetProtocol.setVisible)
        self.dockWidgetProtocol.visibilityChanged['bool'].connect(
            self.actionProtocolRender.setChecked)
        self.dockWidgetDataView.visibilityChanged['bool'].connect(self.actionDataView.setChecked)
        self.actionShowAdditionalDetails.toggled['bool'].connect(
            self.groupBoxProtocolDetails.setVisible)
        self.actionShowFileData.toggled['bool'].connect(self.groupBoxFileData.setVisible)
        self.actionCloseAll.triggered['bool'].connect(self.groupBoxFileData.setVisible)
        self.actionCloseAll.triggered['bool'].connect(self.groupBoxProtocolDetails.setVisible)
        self.actionCloseAll.triggered['bool'].connect(self.dockWidgetDataView.setVisible)
        self.actionCloseAll.triggered['bool'].connect(self.dockWidgetProtocol.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data analysis"))
        self.dockWidgetDataView.setWindowTitle(_translate("MainWindow", "Data view"))
        self.groupBoxFileData.setTitle(_translate("MainWindow", "File data"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuNelp.setTitle(_translate("MainWindow", "&Help"))
        self.menuView.setTitle(_translate("MainWindow", "&View"))
        self.menuMore.setTitle(_translate("MainWindow", "More..."))
        self.menuAnalysisTools.setTitle(_translate("MainWindow", "&Window"))
        self.dockWidgetProtocol.setWindowTitle(_translate("MainWindow", "Protocol"))
        self.groupBoxProtocolDetails.setTitle(_translate("MainWindow", "Additional details"))
        self.toolBarFileActions.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBarViewActions.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBarOtherActions.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save selected"))
        self.actionSave.setToolTip(_translate("MainWindow", "Save selected"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDataAnalysisHelp.setText(_translate("MainWindow", "About"))
        self.actionAboutUI.setText(_translate("MainWindow", "About UI"))
        self.actionUsage.setText(_translate("MainWindow", "Usage"))
        self.actionUsage.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionSaveAll.setText(_translate("MainWindow", "Save all"))
        self.actionSaveAll.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionDataView.setText(_translate("MainWindow", "Data view"))
        self.actionDataView.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionProtocolRender.setText(_translate("MainWindow", "Protocol render"))
        self.actionProtocolRender.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionShowFileData.setText(_translate("MainWindow", "Show file data"))
        self.actionShowAdditionalDetails.setText(
            _translate("MainWindow", "Show additional details"))
        self.actionCloseAll.setText(_translate("MainWindow", "Close all"))
        self.actionCloseAll.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionShowFileDialog.setText(_translate("MainWindow", "Open file dialog"))
        self.actionShowFileDialog.setToolTip(_translate("MainWindow", "Open file dialog"))
        self.actionMaximize.setText(_translate("MainWindow", "&Minimize"))


from scr.app import dataAnalysisRC
