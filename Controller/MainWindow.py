import os
from sys import platform

from PyQt5 import QtWidgets, QtCore

import View.MainWindowView

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = View.MainWindowView()
        self.ui.setupUi(self)
        self.ui.caminhoPasta.setDisabled(True)
        self.ui.extrair.setDisabled(True)

        self.caminhoPasta = ''

        self.ui.abrirPasta.clicked.connect(self.abrirPasta)
        self.ui.extrair.clicked.connect(self.extrair)

    @QtCore.pyqtSlot()
    def abrirPasta(self):
        file =str(QtWidgets.QFileDialog.getExistingDirectory(self, 'Selecionar Pasta'))
        self.ui.extrair.setDisabled(True)
        if file:
            self.caminhoPasta = file
            self.ui.caminhoPasta.setText(file)
            self.ui.extrair.setDisabled(False)

    @QtCore.pyqtSlot()
    def extrair(self):
        if not self.caminhoPasta:
            self.ui.extrair.setDisabled(True)
            return

        self.ui.programa.setDisabled(True)
        
        if not os.path.exists(self.caminhoPasta + "\\Arquivos .dat"):
            os.makedirs(self.caminhoPasta + "\\Arquivos .dat")

        for subdir, dirs, files in os.walk(self.caminhoPasta):
            for file in files:
                nomeArquivo , extensao = file.split('.')
                if extensao == "VHD":
                    if platform == "linux" or platform == "linux2":
                        separator = '/'
                    elif platform == "win32":
                        separator = '\\'

                    subdir_name = subdir.split(separator)[-1]

                    arquivo = open(os.path.join(subdir, file)).read().splitlines()
                    arquivo_saida = open(self.caminhoPasta + separator + "Arquivos .dat" + separator + subdir_name + "__" + nomeArquivo + '.dat', 'w')

                    for i in range(0, len(arquivo)):
                        line = arquivo[i]		
                        if ': Applied Field For Plot' in line:
                            aux = list(filter(str.isdigit, line))
                            aux = ''.join(aux)
                            H_column = int(aux)
                        if ': Signal X direction' in line: 
                            aux = list(filter(str.isdigit, line))
                            aux = ''.join(aux)
                            Mx_column  = int(aux)
                        if ': Signal Y direction' in line: 
                            aux = list(filter(str.isdigit, line))
                            aux = ''.join(aux)
                            My_column  = int(aux)
                        if '@@End of Header.' in line: 
                            begin_table = i + 5
                        if '@@END Data.' in line: 
                            end_table = i
                            break

                    
                    #para pegar as colunas com os dados do arquivo VHD
                    for i in range(begin_table, end_table):
                        columns = arquivo[i].split()
                        arquivo_saida.write("%s %s\n" % (columns[H_column], columns[Mx_column]))
        
        QtWidgets.QMessageBox.about(self, "Sucesso", "Extração realizada com sucesso!")

        self.ui.programa.setDisabled(False)
        self.caminhoPasta = ''
        self.ui.caminhoPasta.setText('')
        self.ui.extrair.setDisabled(True)




