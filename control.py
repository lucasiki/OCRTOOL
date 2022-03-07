import sys
from time import sleep
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QDialog, QMainWindow
from PyQt5.uic import loadUi

import Encoders
import ScanLib
import Toolib as TL




class formulario(QMainWindow):
    def __init__(self, parent = None):
        super(formulario,self).__init__(parent)
        loadUi('ocrUI.ui', self)

        #Variaveis self
        self.var = '' ## Texto disponível
        self.Enc = '' ## Encoder selecionado
        self.text = '' ## Texto resultado
        self.textoFinal = '' ## Texto resultado fnal
        self.group2.setEnabled(False)
        self.group3.setEnabled(False)
        self.group4.setEnabled(False)
        print(dir(self.Encoder))
        #Variaveis self

        self.UploadFiles.clicked.connect(self.getfile)

        #Select de tipo changed
        self.Tipo.currentTextChanged.connect(self.changed)
        
        
        #Envia grupo1
        self.submit1.clicked.connect(self.enviaFile)

        #Envia grupo2
        self.submit2.clicked.connect(self.enviaBusca)


    def changed(self):
            self.jump.setEnabled(True)
            self.ignore.setEnabled(True)
            self.reduce.setEnabled(True)
            self.Delimitador.setEnabled(True)

            if self.Tipo.currentText() == 'Find':
                self.reduce.setEnabled(False)
            elif self.Tipo.currentText() == 'FindSimple':
                self.jump.setEnabled(False)
                self.ignore.setEnabled(False)
                self.reduce.setEnabled(False)
            elif self.Tipo.currentText() == 'Count':
                self.jump.setEnabled(False)
            elif self.Tipo.currentText() == 'Exists?':
                self.jump.setEnabled(False)
                self.ignore.setEnabled(False)
                self.reduce.setEnabled(False)
                self.Delimitador.setEnabled(False)

    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 
           'c:\\',"Image files (*.jpg *.png *.pdf *.jpeg *.xlsx *.xls)")
        print(fname[0])
        if fname[0] != '':
            self.OCRresult.setText(fname[0] + ' carregado com sucesso, favor selecionar o seu encoder.')

            self.var = fname[0]

    def enviaFile(self):
        self.OCRresult.setText('')

        if self.Encoder.currentText() == 'Selecione*':
            print('Selecione um encoder')
            self.OCRresult.setText(self.var + " " + 'Selecione um encoder')
        elif self.var == '':
            self.OCRresult.setText(self.Encoder.currentText() + " " + 'Selecione um arquivo!')
        else:
            Enc = self.Encoder.currentText()
            print(Enc)
            self.OCRresult.setText(self.var + " " + self.Encoder.currentText())

            self.enc = Enc

            
            if (self.enc != '' and self.var != ''):
                self.OCRresult.setText('Aguarde conversão do texto')
                print('Aguarde conversão do texto')
                self.show()
                try:
                    if self.enc == 'PdfMiner':
                        self.text = Encoders.ler_miner(self.var)
                    elif self.enc == 'Py2pdf':
                        self.text = Encoders.ler_py2pdf(self.var)
                    elif self.enc == 'Tesseract':
                        self.text = Encoders.ler_tesseract(self.var)
                    elif self.enc == 'Textract':
                        self.text = Encoders.ler_textract(self.var)

                    print('FOI')
                except:
                    print('NÃO FOI')
                    pass
            if self.text == '':
                self.text = self.OCRresult.setText('Falha na conversão do arquivo')
                return
            if(self.decoded.isChecked() == True):
                self.text = repr(self.text)


            self.OCRresult.setText(str(self.text))
            #self.var = ''
            if self.text != '':
                self.group2.setEnabled(True)
                

    def enviaBusca(self):

        self.group3.setEnabled(True)
        self.group4.setEnabled(True)
        if self.Tipo.currentText() == 'Selecione*':
            self.resultado.setText('Selecione um tipo de busca')
            return()
        if self.TextoA.text() == 'textoA':
            self.resultado.setText('Selecione um  texto para busca')
            return()
        if self.Delimitador.text() == 'Delimitador' and self.Tipo.currentText() != 'Exists?':
            self.resultado.setText('Selecione um tipo de delimitador')
            return()

        textoA = str(self.TextoA.text())
        deli = str(self.Delimitador.text())
        jump =int(TL.sumAllnumbers(self.jump.text()))
        ignore =int(TL.sumAllnumbers(self.ignore.text()))
        reduce =int(TL.sumAllnumbers(self.reduce.text()))

        if self.Tipo.currentText() == 'Find':
            self.result = ScanLib.find(self.text, textoA, deli, ignore, jump)
        elif self.Tipo.currentText() == 'FindSimple':
            self.result =ScanLib.findSimple(self.text, textoA, deli) 
        elif self.Tipo.currentText() == 'Count':
            self.result =str(ScanLib.count(self.text, textoA, deli, ignore, reduce ) )   
        elif self.Tipo.currentText() == 'Exists?':
            self.result =ScanLib.Exists(self.text, textoA)
            
        self.resultado.setText(self.result)
        self.resultado_trans.setText(self.result)

def main():
    
    app = QApplication(sys.argv)
    form = formulario()
    
    
        
        
    form.show()
  
        
        
        
    app.exec()


def func():
    print('test')









