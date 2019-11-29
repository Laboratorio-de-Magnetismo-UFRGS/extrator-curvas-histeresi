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
		MainWindow.resize(800, 313)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/icons/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		self.programa = QtWidgets.QWidget(MainWindow)
		self.programa.setEnabled(True)
		self.programa.setObjectName("programa")
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.programa)
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.caminhoPasta = QtWidgets.QLineEdit(self.programa)
		self.caminhoPasta.setMinimumSize(QtCore.QSize(0, 38))
		self.caminhoPasta.setObjectName("caminhoPasta")
		self.verticalLayout.addWidget(self.caminhoPasta)
		self.groupBox_2 = QtWidgets.QGroupBox(self.programa)
		self.groupBox_2.setMinimumSize(QtCore.QSize(0, 55))
		self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 51))
		self.groupBox_2.setObjectName("groupBox_2")
		self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
		self.horizontalLayout_5.setObjectName("horizontalLayout_5")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.pastaUnica = QtWidgets.QCheckBox(self.groupBox_2)
		self.pastaUnica.setChecked(True)
		self.pastaUnica.setObjectName("pastaUnica")
		self.horizontalLayout_2.addWidget(self.pastaUnica)
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label_4 = QtWidgets.QLabel(self.groupBox_2)
		self.label_4.setObjectName("label_4")
		self.horizontalLayout.addWidget(self.label_4)
		self.pastaSaida = QtWidgets.QLineEdit(self.groupBox_2)
		self.pastaSaida.setObjectName("pastaSaida")
		self.horizontalLayout.addWidget(self.pastaSaida)
		self.horizontalLayout_2.addLayout(self.horizontalLayout)
		self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
		self.verticalLayout.addWidget(self.groupBox_2)
		self.groupBox = QtWidgets.QGroupBox(self.programa)
		self.groupBox.setAutoFillBackground(False)
		self.groupBox.setTitle("")
		self.groupBox.setObjectName("groupBox")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.textEdit = QtWidgets.QTextEdit(self.groupBox)
		self.textEdit.setEnabled(False)
		self.textEdit.setObjectName("textEdit")
		self.horizontalLayout_4.addWidget(self.textEdit)
		self.verticalLayout.addWidget(self.groupBox)
		self.horizontalLayout_3.addLayout(self.verticalLayout)
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.abrirPasta = QtWidgets.QPushButton(self.programa)
		self.abrirPasta.setMinimumSize(QtCore.QSize(111, 41))
		self.abrirPasta.setMaximumSize(QtCore.QSize(16777215, 41))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/icons/icons/iconfinder_General_Office_03_3592873.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.abrirPasta.setIcon(icon1)
		self.abrirPasta.setObjectName("abrirPasta")
		self.verticalLayout_2.addWidget(self.abrirPasta)
		self.extrair = QtWidgets.QPushButton(self.programa)
		self.extrair.setMinimumSize(QtCore.QSize(111, 41))
		self.extrair.setMaximumSize(QtCore.QSize(16777215, 41))
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(":/icons/icons/iconfinder_General_Office_10_3592815.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.extrair.setIcon(icon2)
		self.extrair.setObjectName("extrair")
		self.verticalLayout_2.addWidget(self.extrair)
		spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_2.addItem(spacerItem1)
		self.horizontalLayout_3.addLayout(self.verticalLayout_2)
		MainWindow.setCentralWidget(self.programa)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "LAM - Extrator de Curvas de Histerese"))
		self.caminhoPasta.setToolTip(_translate("MainWindow", "Caminho da pasta contendo os arquivos .vhd"))
		self.caminhoPasta.setPlaceholderText(_translate("MainWindow", "Caminho dos arquivos do VSM"))
		self.groupBox_2.setTitle(_translate("MainWindow", "Configurações"))
		self.pastaUnica.setText(_translate("MainWindow", "Pasta Única"))
		self.label_4.setText(_translate("MainWindow", "Nome da Pasta de Saída dos Arquivos:"))
		self.pastaSaida.setText(_translate("MainWindow", "Arquivos .dat"))
		self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">INTRUÇÕES</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1) Você pode tanto selecionar a pasta contendo todas as medidas de todas as amostras, quanto selecionar a pasta de uma amostra específica contendo as várias medidas dessa única amostra.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2) Você deve selecionar se essa pasta é única, ou seja, se os arquivos .VHD de interesse estão diretamente dentro dela. Caso você queira iterar sobre várias pastas, ou seja, várias amostras, você deve desativar esta opção.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3) Será criada uma pasta dentro da pasta selecionada com o nome que você definir no campo <span style=\" font-style:italic;\">Nome da Pasta de Saída dos Arquivos</span>. Por padrão o nome dessa pasta é <span style=\" font-style:italic;\">Arquivos.dat</span>. Este nome não pode conter caracteres especiais, tais como <span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#d7ba7d;\">\\ </span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#ce9178;\">/ : * ? </span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#d7ba7d;\">&quot; </span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#ce9178;\">&lt; &gt; |</span> e nem pode ser deixado em branco!</p></body></html>"))
		self.abrirPasta.setText(_translate("MainWindow", "Selecionar"))
		self.extrair.setText(_translate("MainWindow", "Extrair"))
from View import resources_rc
