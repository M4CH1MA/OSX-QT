# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setStyleSheet(u"QMainWindow, QWidget {\n"
"	background-color:#00FFB3;\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:#0080FF;\n"
"	color:white;\n"
"}")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 50, 361, 191))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 70, 31, 16))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 70, 271, 20))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 110, 31, 16))
        self.label_2.setFont(font)
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(60, 110, 271, 20))
        self.lineEdit_2.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 150, 75, 23))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 19, 101, 21))
        font1 = QFont()
        font1.setFamily(u"Javanese Text")
        font1.setPointSize(12)
        self.label_3.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Login:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Senha:", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Logar", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600; color:#00aaff; font-family:Arial\">EstoqueX</span></p></body></html>", None))
    # retranslateUi

