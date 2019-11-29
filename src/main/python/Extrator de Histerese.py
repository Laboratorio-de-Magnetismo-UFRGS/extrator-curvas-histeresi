# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets

import Controller.MainWindow

class ApplicationHandler():
    def __init__(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    appHandler = Controller.MainWindow()
    appHandler.show()

    sys.exit(app.exec())