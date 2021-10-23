from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json

from PyQt5.QtWidgets import QMessageBox, QComboBox, QPushButton, QLabel

_translate = QtCore.QCoreApplication.translate

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.entrada_moedas = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_moedas.setGeometry(QtCore.QRect(180, 100, 113, 20))
        self.entrada_moedas.setObjectName("entrada_moedas")
        self.tipos_moedas_2 = QtWidgets.QComboBox(self.centralwidget)
        self.tipos_moedas_2.setGeometry(QtCore.QRect(240, 160, 91, 16))
        self.tipos_moedas_2.setObjectName("tipos_moedas_2")
        self.tipos_moedas_2.addItem("")
        self.tipos_moedas_2.addItem("")
        self.tipos_moedas_2.addItem("")
        self.moeda_3 = QtWidgets.QLabel(self.centralwidget)
        self.moeda_3.setGeometry(QtCore.QRect(70, 160, 171, 20))
        self.moeda_3.setObjectName("moeda_3")
        self.botao_converter = QtWidgets.QPushButton(self.centralwidget)
        self.botao_converter.setGeometry(QtCore.QRect(70, 230, 111, 41))
        self.botao_converter.setObjectName("botao_converter")
        self.botao_sair = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sair.setGeometry(QtCore.QRect(220, 230, 111, 41))
        self.botao_sair.setObjectName("botao_sair")
        self.moeda_2 = QtWidgets.QLabel(self.centralwidget)
        self.moeda_2.setGeometry(QtCore.QRect(70, 130, 180, 31))
        self.moeda_2.setObjectName("moeda_2")
        self.moeda = QtWidgets.QLabel(self.centralwidget)
        self.moeda.setGeometry(QtCore.QRect(70, 100, 101, 20))
        self.moeda.setObjectName("moeda")
        self.moeda_4 = QtWidgets.QLabel(self.centralwidget)
        self.moeda_4.setGeometry(QtCore.QRect(70, 190, 150, 20))
        self.moeda_4.setObjectName("moeda_4")
        self.tipos_moedas = QtWidgets.QComboBox(self.centralwidget)
        self.tipos_moedas.setGeometry(QtCore.QRect(240, 130, 91, 21))
        self.tipos_moedas.setObjectName("tipos_moedas")
        self.tipos_moedas.addItem("")
        self.tipos_moedas.addItem("")
        self.tipos_moedas.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.botao_sair.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.botao_converter.clicked.connect(self.converte)
        self.tipos_moedas_2.findData(self.combobox)

    def converte(self):

        # captura o valor do campo "inserir valor"
        valEntrada = float(self.entrada_moedas.text())
        resultado = valEntrada
        # captura o valor do combo box selecionado da moeda inserida
        tipomodDe = self.tipos_moedas.currentText()
        # captura o valor do combo box selecionado da moeda a ser convertida
        tipomodTo = self.tipos_moedas_2.currentText()

        ####################### QUANDO FOR SELECIONADO DE REAL (1º COMBO) ###################3333
        if tipomodDe == 'Real':
            # busca  o usd e euro transformado em real
            getJsonMoeda = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL")
            cotacoes_dic = getJsonMoeda.json()

            # CONVERTE DOLAR EM REAL
            if tipomodTo == 'Dólar':
                valcotacao = float(cotacoes_dic['USDBRL']['bid'])
                resultado = valEntrada * valcotacao
            elif tipomodTo == 'Euro':
                valcotacao = float(cotacoes_dic['EURBRL']['bid'])
                resultado = valEntrada * valcotacao

        ####################### QUANDO FOR SELECIONADO DOLAR (1º COMBO) ###################3333
        if tipomodDe == 'Dólar':
            # busca  o usd e euro transformado em real
            getJsonMoeda = requests.get("https://economia.awesomeapi.com.br/json/last/BRL-USD,EUR-USD")
            cotacoes_dic = getJsonMoeda.json()

            # CONVERTE REAL em DOLAR
            if tipomodTo == 'Real':
                valcotacao = float(cotacoes_dic['BRLUSD']['bid'])
                resultado = valEntrada * valcotacao
            # CONVERTE EURO EM DOLAR
            elif tipomodTo == 'Euro':
                valcotacao = float(cotacoes_dic['EURUSD']['bid'])
                resultado = valEntrada * valcotacao

        ####################### QUANDO FOR SELECIONADO EURO (1º COMBO) ###################3333
        if tipomodDe == 'EURO':
            # busca  o usd e euro transformado em real
            getJsonMoeda = requests.get("https://economia.awesomeapi.com.br/json/last/BRL-EUR,USD-EUR")
            cotacoes_dic = getJsonMoeda.json()

            # CONVERTE REAL em EURO
            if tipomodTo == 'Real':
                valcotacao = float(cotacoes_dic['BRLEUR']['bid'])
                resultado = valEntrada * valcotacao
            # CONVERTE  DOLAR EM EURO
            elif tipomodTo == 'Dólar':
                valcotacao = float(cotacoes_dic['USDEUR']['bid'])
                resultado = valEntrada * valcotacao

        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle("Sucesso")
        resultado = round(resultado,3)
        msg.setText("Resultado do dólar é : " + str(resultado))
        self.moeda_4.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\"color:white; background-color:blue; padding:10px; font-size:12pt; font-weight:600;\">"\
                                                      f"A saída é: {str(resultado)}</span></p><p><br/></p></body></html>"))
        msg.exec()

    def combobox(self):
        self.entrada_moedas = QComboBox(self)
        self.entrada_moedas.setGeometry(200, 150, 120, 30)
        moedas = ["Real", "Dólar", "Euro"]
        self.entrada_moedas.addItems(moedas)
        botao_converter = QPushButton("Show content ", self)
        self.label = QLabel(self)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tipos_moedas_2.setItemText(0, _translate("MainWindow", "Real"))
        self.tipos_moedas_2.setItemText(1, _translate("MainWindow", "Dólar"))
        self.tipos_moedas_2.setItemText(2, _translate("MainWindow", "Euro"))
        self.moeda_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Irá ser convertido para:</span></p><p><br/></p><p><br/></p></body></html>"))
        self.botao_converter.setText(_translate("MainWindow", "Converter"))
        self.botao_sair.setText(_translate("MainWindow", "Sair"))
        self.moeda_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">O tipo de moeda inserida:</span></p><p><br/></p></body></html>"))
        self.moeda.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Insira o valor: </span></p></body></html>"))
        self.tipos_moedas.setItemText(0, _translate("MainWindow", "Real"))
        self.tipos_moedas.setItemText(1, _translate("MainWindow", "Dólar"))
        self.tipos_moedas.setItemText(2, _translate("MainWindow", "Euro"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi((Principal))
    Principal.show()
    sys.exit(app.exec_())