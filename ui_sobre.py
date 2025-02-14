# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sobre.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_formSobre(object):
    def setupUi(self, formSobre):
        formSobre.setObjectName("formSobre")
        formSobre.resize(743, 412)
        formSobre.setStyleSheet("*\n"
"{\n"
"    background-color\n"
"}\n"
"")
        self.label_2 = QtWidgets.QLabel(formSobre)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 815, 140))
        self.label_2.setStyleSheet("image:url(:/icon_logo/icon/logo.jpg)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(formSobre)
        self.label.setGeometry(QtCore.QRect(0, 0, 815, 141))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(formSobre)
        self.label_3.setGeometry(QtCore.QRect(220, 310, 101, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(formSobre)
        self.label_4.setGeometry(QtCore.QRect(330, 300, 291, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(formSobre)
        self.label_5.setGeometry(QtCore.QRect(280, 350, 281, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(formSobre)
        self.pushButton.setGeometry(QtCore.QRect(390, 380, 75, 23))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color:#0080FF;\n"
"    color:white;\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(formSobre)
        QtCore.QMetaObject.connectSlotsByName(formSobre)

    def retranslateUi(self, formSobre):
        _translate = QtCore.QCoreApplication.translate
        formSobre.setWindowTitle(_translate("formSobre", "Form"))
        self.label.setText(_translate("formSobre", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#0967fc;\">OS_X</span></p><p align=\"center\"><span style=\" font-size:26pt; color:#0967fc;\">Sistema de Ordem de Serviço</span></p></body></html>"))
        self.label_3.setText(_translate("formSobre", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0446f9;\">Criado por:</span></p></body></html>"))
        self.label_4.setText(_translate("formSobre", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#005cf0;\">Jonathan V. Dalla Vecchia</span></p></body></html>"))
        self.label_5.setText(_translate("formSobre", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#0271e7;\">Email: jonathandallavecchia23@gmail.com</span></p></body></html>"))
        self.pushButton.setText(_translate("formSobre", "OK"))

        self.pushButton.clicked.connect(self.sairTela)

    def sairTela(self):
        sys.exit()
        
import icon_logo


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formSobre = QtWidgets.QWidget()
    ui = Ui_formSobre()
    ui.setupUi(formSobre)
    formSobre.show()
    sys.exit(app.exec_())
