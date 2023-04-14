import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.uic import loadUi


# nitip masih yg kmrn :)
class MainMenu(QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        loadUi("main.ui", self)

        self.generateKeyButton.clicked.connect(self.generateKey)
        self.digiSignButton.clicked.connect(self.digiSign)
        self.verifyButton.clicked.connect(self.verify)

    def generateKey(self):
        keys = GenerateKey()
        widget.addWidget(keys)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def digiSign(self):
        digiSign = GenerateKey()
        widget.addWidget(digiSign)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def verify(self):
        verify = Verify()
        widget.addWidget(verify)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class GenerateKey(QMainWindow):
    def __init__(self):
        super(GenerateKey, self).__init__()
        loadUi("generate_key.ui", self)
        self.importMessageButton.clicked.connect(self.importMessage)
        self.backButton.clicked.connect(self.back)

    def importMessage(self):
        fileName = self.fileTextEdit.toPlainText()
        with open(fileName + ".pri", 'w') as f:
            f.write("hasil priv key")

        with open(fileName + ".pub", 'w') as f:
            f.write("hasil pub key")

    def back(self):
        back = MainMenu()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class DigitalSign(QMainWindow):
    def __init__(self):
        super(DigitalSign, self).__init__()
        loadUi("digital_sign.ui", self)
        self.importMessageButton.clicked.connect(self.importMessage)
        self.importPrivButton.clicked.connect(self.importPriv)
        self.generateButton.clicked.connect(self.generate)
        self.backButton.clicked.connect(self.back)

    def importMessage(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File", "")
        self.fileLoc = fname[0]
        self.label_4.setText("File Imported Successfully")

    # def importPriv(self):
    #     fname = QFileDialog.getOpenFileName(self, "Choose File", "")
    #     self.privKey = p.read_from_file(fname[0])
    #     self.label_4.setText("Private Key Imported Successfully")
    

    # def generate(self):
    #     sign_text_file(self.fileLoc, '\output.txt', self.pubKey)
    #     self.label_4.setText("Generated Successfully")

    def back(self):
        back = MainMenu()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    

class Verify(QMainWindow):
    def __init__(self):
        super(Verify, self).__init__()
        loadUi("verify.ui", self)
        self.importMessageButton.clicked.connect(self.importMessage)
        self.importDSButton.clicked.connect(self.importDS)
        self.importPubButton.clicked.connect(self.importPub)
        self.verifyButton.clicked.connect(self.verify)
        self.backButton.clicked.connect(self.back)

    def importMessage(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File", "")
        self.fileLoc = fname[0]
        self.label.setText("File Imported Successfully")

    # def importDS(self):
    #     fname = QFileDialog.getOpenFileName(self, "Choose File", "")
    #     self.fileLoc = fname[0]
    #     self.label.setText("File Imported Successfully")

    # def importPub(self):
    #     fname = QFileDialog.getOpenFileName(self, "Choose File", "")
    #     self.pubKey = p.read_from_file(fname[0])
    #     self.label.setText("Public Key Imported Successfully")
    

    # def verify(self):
    #     # sign_text_file(self.fileLoc, '\output.txt', self.pubKey)
    #     # if bener
    #     self.label.setText("File verified")
    #     # if salah
    #     self.label.setText("File has been modified")

    def back(self):
        back = MainMenu()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)

app = QApplication(sys.argv)
mainmenu = MainMenu()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainmenu)
widget.show()

sys.exit(app.exec())