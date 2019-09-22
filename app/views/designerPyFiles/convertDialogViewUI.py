# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convertDialogViewUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_convertFileDialog(object):
    def setupUi(self, convertFileDialog):
        convertFileDialog.setObjectName("convertFileDialog")
        convertFileDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        convertFileDialog.resize(412, 96)
        convertFileDialog.setMaximumSize(QtCore.QSize(412, 96))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgRc/images/mainWindow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        convertFileDialog.setWindowIcon(icon)
        convertFileDialog.setWindowOpacity(1.0)
        convertFileDialog.setStyleSheet("QWidget\n"
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
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
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
"    font-size: 11px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"")
        convertFileDialog.setSizeGripEnabled(False)
        convertFileDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(convertFileDialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(129, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 2)
        self.lineEditDelimiter = QtWidgets.QLineEdit(convertFileDialog)
        self.lineEditDelimiter.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditDelimiter.setToolTip("")
        self.lineEditDelimiter.setWhatsThis("")
        self.lineEditDelimiter.setInputMask("")
        self.lineEditDelimiter.setObjectName("lineEditDelimiter")
        self.gridLayout.addWidget(self.lineEditDelimiter, 0, 2, 1, 2)
        self.labelInputDelimeter = QtWidgets.QLabel(convertFileDialog)
        self.labelInputDelimeter.setObjectName("labelInputDelimeter")
        self.gridLayout.addWidget(self.labelInputDelimeter, 0, 0, 1, 2)
        self.lineEditHeaderNames = QtWidgets.QLineEdit(convertFileDialog)
        self.lineEditHeaderNames.setEnabled(True)
        self.lineEditHeaderNames.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditHeaderNames.setText("")
        self.lineEditHeaderNames.setObjectName("lineEditHeaderNames")
        self.gridLayout.addWidget(self.lineEditHeaderNames, 1, 1, 1, 5)
        self.pushButtonConvert = QtWidgets.QPushButton(convertFileDialog)
        self.pushButtonConvert.setEnabled(True)
        self.pushButtonConvert.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButtonConvert.setObjectName("pushButtonConvert")
        self.gridLayout.addWidget(self.pushButtonConvert, 2, 3, 1, 2)
        self.labelHeaderNames = QtWidgets.QLabel(convertFileDialog)
        self.labelHeaderNames.setObjectName("labelHeaderNames")
        self.gridLayout.addWidget(self.labelHeaderNames, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(179, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 3)
        self.pushButtonCancel = QtWidgets.QPushButton(convertFileDialog)
        self.pushButtonCancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout.addWidget(self.pushButtonCancel, 2, 5, 1, 1)

        self.retranslateUi(convertFileDialog)
        self.pushButtonCancel.clicked.connect(convertFileDialog.close)
        QtCore.QMetaObject.connectSlotsByName(convertFileDialog)

    def retranslateUi(self, convertFileDialog):
        _translate = QtCore.QCoreApplication.translate
        convertFileDialog.setWindowTitle(_translate("convertFileDialog", "Конвертація файлу в csv."))
        self.lineEditDelimiter.setPlaceholderText(_translate("convertFileDialog", "Приклад: ;,./ _ ..."))
        self.labelInputDelimeter.setText(_translate("convertFileDialog", "Введіть розділювач файлу:"))
        self.lineEditHeaderNames.setPlaceholderText(_translate("convertFileDialog", "Приклад: \"Стовпець1\",\"Стовпець2\",..."))
        self.pushButtonConvert.setText(_translate("convertFileDialog", "&Провести конвертування"))
        self.labelHeaderNames.setText(_translate("convertFileDialog", "Задайте імена стовпців:"))
        self.pushButtonCancel.setText(_translate("convertFileDialog", "&Відмінити"))

from app import dataAnalysisRC
