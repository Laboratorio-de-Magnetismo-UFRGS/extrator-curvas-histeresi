# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 151)
		self.programa = QtWidgets.QWidget(MainWindow)
		self.programa.setEnabled(True)
		self.programa.setObjectName("programa")
		self.caminhoPasta = QtWidgets.QLineEdit(self.programa)
		self.caminhoPasta.setGeometry(QtCore.QRect(20, 31, 641, 41))
		self.caminhoPasta.setObjectName("caminhoPasta")
		self.abrirPasta = QtWidgets.QPushButton(self.programa)
		self.abrirPasta.setGeometry(QtCore.QRect(670, 30, 111, 41))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/icons/icons/iconfinder_General_Office_03_3592873.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.abrirPasta.setIcon(icon)
		self.abrirPasta.setObjectName("abrirPasta")
		self.extrair = QtWidgets.QPushButton(self.programa)
		self.extrair.setGeometry(QtCore.QRect(670, 80, 111, 41))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/icons/icons/iconfinder_General_Office_10_3592815.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.extrair.setIcon(icon1)
		self.extrair.setObjectName("extrair")
		MainWindow.setCentralWidget(self.programa)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Extrator de Curvas de Histerese"))
		self.caminhoPasta.setToolTip(_translate("MainWindow", "Caminho da pasta contendo os arquivos .vhd"))
		self.caminhoPasta.setPlaceholderText(_translate("MainWindow", "Caminho dos arquivos do VSM"))
		self.abrirPasta.setText(_translate("MainWindow", "Selecionar"))
		self.extrair.setText(_translate("MainWindow", "Extrair"))
from View import resources_rc
