import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.uic import loadUi
import tools, utils

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
        digiSign = DigitalSign()
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
        self.generateButton.clicked.connect(self.generate)
        self.backButton.clicked.connect(self.back)

    def generate(self):
        fileName = self.fileTextEdit.toPlainText()
        tools.writekey(fileName)
        self.label_2.setText("Key Pair Generated")

    def back(self):
        back = MainMenu()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class DigitalSign(QMainWindow):
    filename = ''
    privKey = ''

    def __init__(self):
        super(DigitalSign, self).__init__()
        loadUi("digital_sign.ui", self)
        self.importMessageButton.clicked.connect(self.importMessage)
        self.importPrivButton.clicked.connect(self.importPriv)
        self.generateButton.clicked.connect(self.generate)
        self.backButton.clicked.connect(self.back)

    def importMessage(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File", "")
        self.filename = fname[0]
        self.label_4.setText("File Imported Successfully")

    def importPriv(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File", "")
        self.privKey = fname[0]
        self.label_4.setText("Private Key Imported Successfully")
    
    def generate(self):
        utils.sign(self.filename, self.privKey)
        self.label_4.setText("Digital Sign Generated Successfully")

    def back(self):
        back = MainMenu()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    

class Verify(QMainWindow):
    filename = ''
    digisign = ''
    pubKey = ''

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
        self.filename = fname[0]
        self.label.setText("File Imported Successfully")

    def importDS(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File", "")
        self.digisign = fname[0]
        self.label.setText("Digital Signature Imported Successfully")

    def importPub(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File", "")
        self.pubKey = fname[0]
        self.label.setText("Public Key Imported Successfully")
    

    def verify(self):
        result = utils.validate(self.filename, self.pubKey, self.digisign)
        if result == "VALID.":
            self.label.setText("File verified")
        else:
            self.label.setText("File has been modified")

    def back(self):
        back = MainMenu()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)

app = QApplication(sys.argv)
mainmenu = MainMenu()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainmenu)
widget.setFixedHeight(900)
widget.setFixedWidth(900)
widget.show()

sys.exit(app.exec())