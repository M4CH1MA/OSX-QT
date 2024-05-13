# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

#telas
from ui_cliente import Ui_Form
from ui_sobre import Ui_formSobre
from ui_usuario import Ui_ui_usuario
#from main import Login

import mysql.connector
import variaveisControle


import icon_logo

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(853, 366)
        self.actionCliente = QAction(MainWindow)
        self.actionCliente.setObjectName(u"actionCliente")
        self.actionOS = QAction(MainWindow)
        self.actionOS.setObjectName(u"actionOS")
        self.actionUsuarios = QAction(MainWindow)
        self.actionUsuarios.setObjectName(u"actionUsuarios")
        self.actionClientes = QAction(MainWindow)
        self.actionClientes.setObjectName(u"actionClientes")
        self.actionSobre = QAction(MainWindow)
        self.actionSobre.setObjectName(u"actionSobre")
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.actionSair = QAction(MainWindow)
        self.actionSair.setObjectName(u"actionSair")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #ffffff;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"image:url(:/icon_logo/icon/logo.jpg)")

        self.verticalLayout.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 853, 21))
        self.menuCadastros = QMenu(self.menubar)
        self.menuCadastros.setObjectName(u"menuCadastros")
        self.menuRelatorio = QMenu(self.menubar)
        self.menuRelatorio.setObjectName(u"menuRelatorio")
        self.menuAjuda = QMenu(self.menubar)
        self.menuAjuda.setObjectName(u"menuAjuda")
        self.menuSair = QMenu(self.menubar)
        self.menuSair.setObjectName(u"menuSair")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCadastros.menuAction())
        self.menubar.addAction(self.menuRelatorio.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.menubar.addAction(self.menuSair.menuAction())
        self.menuCadastros.addAction(self.actionCliente)
        self.menuCadastros.addAction(self.actionOS)
        self.menuCadastros.addAction(self.actionUsuarios)
        self.menuRelatorio.addAction(self.actionClientes)
        self.menuAjuda.addAction(self.actionSobre)
        self.menuSair.addAction(self.actionLogout)
        self.menuSair.addAction(self.actionSair)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionCliente.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.actionOS.setText(QCoreApplication.translate("MainWindow", u"OS", None))
        self.actionUsuarios.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.actionClientes.setText(QCoreApplication.translate("MainWindow", u"Relatorios", None))
        self.actionSobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.actionSair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#0967fc;\">OS_X</span></p><p align=\"center\"><span style=\" font-size:26pt; color:#0967fc;\">Sistema de Ordem de Servi\u00e7o</span></p></body></html>", None))
        self.label_2.setText("")
        self.menuCadastros.setTitle(QCoreApplication.translate("MainWindow", u"Cadastros", None))
        self.menuRelatorio.setTitle(QCoreApplication.translate("MainWindow", u"Relatorio", None))
        self.menuAjuda.setTitle(QCoreApplication.translate("MainWindow", u"Ajuda", None))
        self.menuSair.setTitle(QCoreApplication.translate("MainWindow", u"Sair", None))
    # retranslateUi

        #Menus
        self.actionCliente.triggered.connect(self.telaCliente)
        self.actionLogout.triggered.connect(self.logoutTela)
        self.actionSair.triggered.connect(self.telaSair)
        self.actionSobre.triggered.connect(self.telaSobre)
        self.actionUsuarios.triggered.connect(self.telaUsuario)




    #Funcoes

    def telaSair(self):
        sys.exit()

    def logoutTela(self):
        pass


    def telaSobre(self):
        self.formSobre = QtWidgets.QWidget()
        self.ui = Ui_formSobre()
        self.ui.setupUi(self.formSobre)
        self.formSobre.show()

    def telaUsuario(self):
        self.ui_usuario = QtWidgets.QWidget()
        self.ui = Ui_ui_usuario()
        self.ui.setupUi(self.ui_usuario)
        self.ui_usuario.show()    

    def telaCliente(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()


        #Perfil
        if variaveisControle.perfil != 'Administrador':
            self.actionUsuarios.setEnabled(False)