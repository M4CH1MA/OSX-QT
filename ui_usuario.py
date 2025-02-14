# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_usuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import variaveisControle
import mysql.connector


class Ui_ui_usuario(object):
    def setupUi(self, ui_usuario):
        ui_usuario.setObjectName("ui_usuario")
        ui_usuario.resize(571, 406)
        ui_usuario.setStyleSheet("QFrame:\n"
"{\n"
"    background-color:#3F48CC;\n"
"}")
        self.frame = QtWidgets.QFrame(ui_usuario)
        self.frame.setGeometry(QtCore.QRect(0, 0, 571, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 280, 47, 13))
        self.label_6.setObjectName("label_6")
        self.txt_loginUser = QtWidgets.QLineEdit(self.frame)
        self.txt_loginUser.setGeometry(QtCore.QRect(100, 160, 251, 20))
        self.txt_loginUser.setObjectName("txt_loginUser")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 47, 13))
        self.label_3.setObjectName("label_3")
        self.txt_senhaUser = QtWidgets.QLineEdit(self.frame)
        self.txt_senhaUser.setGeometry(QtCore.QRect(100, 220, 251, 20))
        self.txt_senhaUser.setObjectName("txt_senhaUser")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 41, 16))
        self.label_2.setObjectName("label_2")
        self.txt_idUser = QtWidgets.QLineEdit(self.frame)
        self.txt_idUser.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.txt_idUser.setObjectName("txt_idUser")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 220, 47, 13))
        self.label_5.setObjectName("label_5")
        self.txt_foneUser = QtWidgets.QLineEdit(self.frame)
        self.txt_foneUser.setGeometry(QtCore.QRect(100, 110, 113, 20))
        self.txt_foneUser.setObjectName("txt_foneUser")
        self.cmb_perfil = QtWidgets.QComboBox(self.frame)
        self.cmb_perfil.setGeometry(QtCore.QRect(100, 270, 151, 22))
        self.cmb_perfil.setObjectName("cmb_perfil")
        self.txt_nomeUser = QtWidgets.QLineEdit(self.frame)
        self.txt_nomeUser.setGeometry(QtCore.QRect(100, 60, 271, 20))
        self.txt_nomeUser.setObjectName("txt_nomeUser")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 20, 21, 16))
        self.label.setObjectName("label")
        self.bt_addUser = QtWidgets.QPushButton(self.frame)
        self.bt_addUser.setGeometry(QtCore.QRect(30, 340, 75, 61))
        self.bt_addUser.setStyleSheet("image:url(:/icon_addCli/icon/adicionar.png)")
        self.bt_addUser.setText("")
        self.bt_addUser.setObjectName("bt_addUser")
        self.bt_conUser = QtWidgets.QPushButton(self.frame)
        self.bt_conUser.setGeometry(QtCore.QRect(120, 340, 75, 61))
        self.bt_conUser.setStyleSheet("image:url(:/icon_conCli/icon/consultar.png)")
        self.bt_conUser.setText("")
        self.bt_conUser.setObjectName("bt_conUser")
        self.bt_altUser = QtWidgets.QPushButton(self.frame)
        self.bt_altUser.setGeometry(QtCore.QRect(210, 340, 75, 61))
        self.bt_altUser.setStyleSheet("image:url(:/icon_altCli/icon/alterar.png)")
        self.bt_altUser.setText("")
        self.bt_altUser.setObjectName("bt_altUser")
        self.bt_delUser = QtWidgets.QPushButton(self.frame)
        self.bt_delUser.setGeometry(QtCore.QRect(300, 340, 75, 61))
        self.bt_delUser.setStyleSheet("image:url(:/icon_delCli/icon/excluir.png)")
        self.bt_delUser.setText("")
        self.bt_delUser.setObjectName("bt_delUser")
        self.bt_retUser = QtWidgets.QPushButton(self.frame)
        self.bt_retUser.setGeometry(QtCore.QRect(480, 340, 75, 61))
        self.bt_retUser.setStyleSheet("image:url(:/icon_retornar/icon/retornar.png)")
        self.bt_retUser.setText("")
        self.bt_retUser.setObjectName("bt_retUser")

        self.retranslateUi(ui_usuario)
        QtCore.QMetaObject.connectSlotsByName(ui_usuario)

    def retranslateUi(self, ui_usuario):
        _translate = QtCore.QCoreApplication.translate
        ui_usuario.setWindowTitle(_translate("ui_usuario", "Usuario"))
        self.label_6.setText(_translate("ui_usuario", "Perfil:"))
        self.label_3.setText(_translate("ui_usuario", "Fone:"))
        self.label_2.setText(_translate("ui_usuario", "Nome:"))
        self.label_5.setText(_translate("ui_usuario", "Senha:"))
        self.label_4.setText(_translate("ui_usuario", "Login:"))
        self.label.setText(_translate("ui_usuario", "ID:"))
        #comboBox
        self.cmb_perfil.addItems(["Administrador", "User"])

        self.txt_idUser.setEnabled(False)

        self.bt_addUser.clicked.connect(self.telaAddUser)

    def telaAddUser(self):
        nomeUsuario = self.txt_nomeUser.text()
        foneUsuario = self.txt_foneUser.text()
        loginUsuario = self.txt_loginUser.text()
        senhaUsuario = self.txt_senhaUser.text()
        perfilUsuario = self.cmb_perfil.currentText() #ComboBox

        mydb = mysql.connector.connect(
            host = variaveisControle.host,
            user = variaveisControle.user,
            password = variaveisControle.password,
            database = variaveisControle.database
        )

        mycursor = mydb.cursor()
        sql = "INSERT INTO tb_usuario(login, senha, perfil)VALUES(%s, %s, %s)"
        val = (loginUsuario, senhaUsuario, perfilUsuario)
        mycursor.execute(sql, val)
        mydb.commit()

        mycursor.close()
        #Limpando Tela
        self.txt_nomeUser.setText("")
        self.txt_foneUser.setText("")
        self.txt_loginUser.setText("")
        self.txt_senhaUser.setText("")

    def telaPesqUser(self):
        self.txt_nomeUser.setText("")
        self.txt_foneUser.setText("")
        self.txt_loginUser.setText("")
        self.txt_senhaUser.setText("")

        mydb = mysql.connector.connect(
            host = variaveisControle.host,
            user = variaveisControle.user,
            password = variaveisControle.password,
            database = variaveisControle.database
        )

        mycursor = mydb.cursor()
        sql = "SELECT * FROM usuario WHERE id=%s"

import icon_addCli
import icon_altCli
import icon_conCli
import icon_delCi
import icon_retornar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui_usuario = QtWidgets.QWidget()
    ui = Ui_ui_usuario()
    ui.setupUi(ui_usuario)
    ui_usuario.show()
    sys.exit(app.exec_())
