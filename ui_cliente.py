# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem


import mysql.connector
import variaveisControle
import pandas as pd

host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(635, 450)
        self.txt_pesqCli = QtWidgets.QLineEdit(Form)
        self.txt_pesqCli.setGeometry(QtCore.QRect(20, 20, 371, 20))
        self.txt_pesqCli.setObjectName("txt_pesqCli")
        self.bt_pesquisar = QtWidgets.QPushButton(Form)
        self.bt_pesquisar.setGeometry(QtCore.QRect(410, 20, 21, 23))
        self.bt_pesquisar.setStyleSheet("background-image: url(:/icon_pesCli/icon/pesquisar.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.bt_pesquisar.setText("")
        self.bt_pesquisar.setObjectName("bt_pesquisar")
        self.tabel_cliente = QtWidgets.QTableWidget(Form)
        self.tabel_cliente.setGeometry(QtCore.QRect(20, 50, 611, 111))
        self.tabel_cliente.setObjectName("tabel_cliente")
        self.tabel_cliente.setColumnCount(6)
        self.tabel_cliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_cliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_cliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_cliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_cliente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_cliente.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_cliente.setHorizontalHeaderItem(5, item)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 180, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 210, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 250, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 290, 47, 13))
        self.label_4.setObjectName("label_4")
        self.txt_nomeCli = QtWidgets.QLineEdit(Form)
        self.txt_nomeCli.setGeometry(QtCore.QRect(90, 180, 301, 20))
        self.txt_nomeCli.setObjectName("txt_nomeCli")
        self.txt_enderecoCli = QtWidgets.QLineEdit(Form)
        self.txt_enderecoCli.setGeometry(QtCore.QRect(90, 210, 301, 20))
        self.txt_enderecoCli.setObjectName("txt_enderecoCli")
        self.txt_foneCli = QtWidgets.QLineEdit(Form)
        self.txt_foneCli.setGeometry(QtCore.QRect(90, 250, 131, 20))
        self.txt_foneCli.setObjectName("txt_foneCli")
        self.txt_emailCli = QtWidgets.QLineEdit(Form)
        self.txt_emailCli.setGeometry(QtCore.QRect(90, 280, 301, 20))
        self.txt_emailCli.setObjectName("txt_emailCli")
        self.rd_feminino = QtWidgets.QRadioButton(Form)
        self.rd_feminino.setGeometry(QtCore.QRect(180, 320, 82, 17))
        self.rd_feminino.setObjectName("rd_feminino")
        self.rd_masculino = QtWidgets.QRadioButton(Form)
        self.rd_masculino.setGeometry(QtCore.QRect(90, 320, 82, 17))
        self.rd_masculino.setObjectName("rd_masculino")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 320, 47, 13))
        self.label_5.setObjectName("label_5")
        self.bt_addCli = QtWidgets.QPushButton(Form)
        self.bt_addCli.setGeometry(QtCore.QRect(20, 360, 75, 71))
        self.bt_addCli.setStyleSheet("background-image: url(:/icon_addCli/icon/adicionar.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.bt_addCli.setText("")
        self.bt_addCli.setObjectName("bt_addCli")
        self.bt_altCli = QtWidgets.QPushButton(Form)
        self.bt_altCli.setGeometry(QtCore.QRect(120, 360, 75, 71))
        self.bt_altCli.setStyleSheet("background-image: url(:/icon_altCli/icon/alterar.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.bt_altCli.setText("")
        self.bt_altCli.setObjectName("bt_altCli")
        self.bt_delCli = QtWidgets.QPushButton(Form)
        self.bt_delCli.setGeometry(QtCore.QRect(220, 360, 75, 71))
        self.bt_delCli.setStyleSheet("background-image: url(:/icon_delCli/icon/excluir.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.bt_delCli.setText("")
        self.bt_delCli.setObjectName("bt_delCli")
        self.bt_retornar = QtWidgets.QPushButton(Form)
        self.bt_retornar.setGeometry(QtCore.QRect(540, 360, 75, 71))
        self.bt_retornar.setStyleSheet("background-image: url(:/icon_retornar/icon/retornar.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.bt_retornar.setText("")
        self.bt_retornar.setObjectName("bt_retornar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastrar Cliente"))
        item = self.tabel_cliente.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tabel_cliente.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nome"))
        item = self.tabel_cliente.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Endereço"))
        item = self.tabel_cliente.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Fone"))
        item = self.tabel_cliente.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Genero"))
        item = self.tabel_cliente.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Email"))
        self.label.setText(_translate("Form", "Nome:"))
        self.label_2.setText(_translate("Form", "Endereço:"))
        self.label_3.setText(_translate("Form", "Fone:"))
        self.label_4.setText(_translate("Form", "Email:"))
        self.rd_feminino.setText(_translate("Form", "Feminino"))
        self.rd_masculino.setText(_translate("Form", "Masculino"))
        self.label_5.setText(_translate("Form", "Genero:"))

        self.bt_pesquisar.clicked.connect(self.pesquisarClientes)
        
        #self.txt_nomeCli.setEnabled(False)
        #self.txt_emailCli.setEnabled(False)
        #self.txt_enderecoCli.setEnabled(False)
        #self.txt_foneCli.setEnabled(False)

    def pesquisarClientes(self):
        mydb = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM tb_cliente")
        myresult = mycursor.fetchall()
        print(myresult)
        df = pd.DataFrame(myresult, columns= ["idCliente", "nome", "endereco", "fone", "email", "genero"])
        self.all_data = df
        #Carrega os arquivos para a tabela do sistema
        numRows = len(self.all_data.index)
        self.tabel_cliente.setColumnCount(len(self.all_data.columns))
        self.tabel_cliente.setRowCount(numRows)
        self.tabel_cliente.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
                for j in range(len(self.all_data.columns)):
                        self.tabel_cliente.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i,j])))

        self.tabel_cliente.resizeColumnsToContents()
        self.tabel_cliente.resizeRowsToContents()

        mycursor.close()


import icon_addCli
import icon_altCli
import icon_delCi
import icon_pesCli
import icon_retornar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
