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
		MainWindow.resize(800, 153)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/icons/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		self.programa = QtWidgets.QWidget(MainWindow)
		self.programa.setEnabled(True)
		self.programa.setObjectName("programa")
		self.caminhoPasta = QtWidgets.QLineEdit(self.programa)
		self.caminhoPasta.setGeometry(QtCore.QRect(20, 11, 641, 41))
		self.caminhoPasta.setObjectName("caminhoPasta")
		self.abrirPasta = QtWidgets.QPushButton(self.programa)
		self.abrirPasta.setGeometry(QtCore.QRect(670, 10, 111, 41))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/icons/icons/iconfinder_General_Office_03_3592873.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.abrirPasta.setIcon(icon1)
		self.abrirPasta.setObjectName("abrirPasta")
		self.extrair = QtWidgets.QPushButton(self.programa)
		self.extrair.setGeometry(QtCore.QRect(670, 60, 111, 41))
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(":/icons/icons/iconfinder_General_Office_10_3592815.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.extrair.setIcon(icon2)
		self.extrair.setObjectName("extrair")
		self.groupBox = QtWidgets.QGroupBox(self.programa)
		self.groupBox.setGeometry(QtCore.QRect(20, 60, 641, 81))
		self.groupBox.setAutoFillBackground(False)
		self.groupBox.setTitle("")
		self.groupBox.setObjectName("groupBox")
		self.label = QtWidgets.QLabel(self.groupBox)
		self.label.setGeometry(QtCore.QRect(10, 10, 641, 16))
		self.label.setObjectName("label")
		self.label_3 = QtWidgets.QLabel(self.groupBox)
		self.label_3.setGeometry(QtCore.QRect(10, 50, 621, 16))
		self.label_3.setObjectName("label_3")
		self.label_2 = QtWidgets.QLabel(self.groupBox)
		self.label_2.setGeometry(QtCore.QRect(10, 30, 631, 16))
		self.label_2.setObjectName("label_2")
		MainWindow.setCentralWidget(self.programa)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "LAM - Extrator de Curvas de Histerese"))
		self.caminhoPasta.setToolTip(_translate("MainWindow", "Caminho da pasta contendo os arquivos .vhd"))
		self.caminhoPasta.setPlaceholderText(_translate("MainWindow", "Caminho dos arquivos do VSM"))
		self.abrirPasta.setText(_translate("MainWindow", "Selecionar"))
		self.extrair.setText(_translate("MainWindow", "Extrair"))
		self.label.setText(_translate("MainWindow", "Você deve selecionar a pasata onde estão todas as medidas. O programa percorrerá todos os arquivos .vhd e extrairá a curva de"))
		self.label_3.setText(_translate("MainWindow", "modo que o nome de cada arquivo é {pasta original}__{nome original do arquivo}.dat"))
		self.label_2.setText(_translate("MainWindow", "cada medida.    Será gerada uma pasta chamada \"Arquivos .dat\" dentro da pasta selecionada com um arquivo para cada curva de"))
from View import resources_rc
