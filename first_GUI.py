import os
from PyQt5.QtWidgets import QLabel, QGridLayout, QHBoxLayout, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import argparse, sys
import requests, re
from secondGUI import Window2

class Intruder():
    def req(self, url):
        r = requests.request('GET', url)
        response = r.text
        print('hello world')
        return response

    def req_manipulation(self):
        try:
            with open(self.args.wordlist, 'r', encoding='utf-8') as file:
                for newstring in file:
                    url = input('Please provide a URI Adress! ')
                    paragraphliste = []
                    paragraphliste += re.findall('§', url)
                    if len(paragraphliste) > 1:
                        substring = (re.findall(r'§.*?§', url))
                        newURL = url.replace(substring[0], newstring)
                        print(newURL)
                    '''
                    resp = requests.get(newURL)
                    status_code = resp.status_code
                    text = resp.text
                    size = text.__sizeof__()
                    header = resp.headers
                    print(substring)
                    '''
        except:
            print(os.error)

class Pentestin(QWidget):
    def __init__(self):
        super().__init__()
        self.top = 200
        self.left = 200
        self.width = 1000
        self.height = 500
        self.Window1()

    def Window1(self):
        # Grundsätzlicher Application Aufbau
        self.first_window = QMainWindow()
        self.UI = Pentestin()
        self.UI.Utils_one()
        self.first_window.setGeometry(self.top, self.left, self.width, self.height)
        self.first_window.setWindowIcon(
            QIcon(r"C:\Users\Blick\PycharmProjects\pythonProject1\Bilder\resized_Anonymous.png"))
        self.first_window.setWindowTitle('Pentestin')
        self.show()

    def Utils_one(self):


        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(
            QIcon(r"C:\Users\Blick\PycharmProjects\pythonProject1\Bilder\resized_Anonymous.png"))
        self.setWindowTitle('Pentestin')
        # Background image initsialisieren
        background_f_i = QImage('Bilder\\background_first.jfif')
        background_f_o = background_f_i.scaled(self.width, self.height)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(background_f_o))
        self.setPalette(palette)

        #URL Labels und User Input erstellen
        self.label = QLabel('URL:')
        self.label.setStyleSheet('font-family: "Cabin Sketch", cursive, sans-serif;' +
                                 'font-size: 20px;' +
                                 'color: #0F0'
                                 )
        self.input = QLineEdit(self.first_window)
        self.input.setStyleSheet('border: 2px double "#0A0";' +
                                 'background: rgba(100, 100, 100, 0.4);' +
                                 'color: #0F0;' +
                                 'margin: 0px 0px'


                                 )
        self.input.setFont(QFont('Arial', 13))

        # Button erstellen, der den Input weiterleitet
        button = QPushButton('Forward', self)
        button.setToolTip('this requests the Source Code of the Page')
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(
            '*{border-radius: 15px;' +
            'background-color: #0A0;' +
            'font-size: 23px;}' +
            '*:hover{background-color: "orange"; border: 3px solid red;}')
        # Ausrichtung der Buttons und des Input Feldes!
        h = QHBoxLayout()
        h.addWidget(self.label)
        h.addWidget(self.input)
        h.addStretch(1)
        h.addWidget(button)

        #Vertikale VBOX zum ausrichten
        v = QVBoxLayout()
        v.addStretch(1)
        v.addLayout(h)
        self.first_window.setLayout(v)

        QToolTip.setFont(QFont('Arial', 13))

        #hier ist die Weiterleitung
        button.clicked.connect(self.secondWindow)

    def qline(self):
        url = self.url_input.text()
        print('url output' + url)
        Intruder.req(self,url)

    def secondWindow(self):
        self.window = QMainWindow()
        self.message = 'hello World'
        self.ui = Window2(self.message)
        self.window.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pentestin.Window1(QMainWindow)
    sys.exit(app.exec_())