from PySide2.QtWidgets import(QApplication, QMainWindow, QWidget)
from PyQt5.QtWidgets import QMessageBox
from login import Ui_Form
from principal import Ui_MainWindow
import sys
import mysql.connector
import variaveisControle


#Variaveis de conexao com o Banco de dados
host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database

perfil = variaveisControle.perfil

class Login(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Login')

        self.pushButton.clicked.connect(self.open_system)

    #metodo para abrir o sistema
    def open_system(self):
        mydb = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        mycursor = mydb.cursor()
        login = self.lineEdit.text()
        senha = self.lineEdit_2.text()
        query = "SELECT * FROM tb_usuario WHERE login=%s AND senha=%s"
        dados = (str(login), str(senha))
        mycursor.execute(query, dados)
        myresult = mycursor.fetchall()
        

        if myresult:
            variaveisControle.perfil = myresult[0][3]
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            print('Erro')     


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Tela Principal')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
