# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/ExtracaoConcluida.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(396, 300)
		self.mensagem = QtWidgets.QLabel(Dialog)
		self.mensagem.setGeometry(QtCore.QRect(120, 110, 47, 13))
		self.mensagem.setText("")
		self.mensagem.setObjectName("mensagem")
		self.okButton = QtWidgets.QPushButton(Dialog)
		self.okButton.setGeometry(QtCore.QRect(300, 210, 75, 23))
		self.okButton.setObjectName("okButton")

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
		self.okButton.setText(_translate("Dialog", "OK"))
