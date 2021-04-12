import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QLineEdit, QMainWindow, QSizePolicy, QWidget, QPushButton
import clipboard
import os
from pytube import YouTube

estilo_botao = '''
color: black; 
background: white; 
font-family: "Lucida Console", "Courier New", monospace;
font-size: 25px;
border-style: double;
border-width: 2px;
border-color: black
'''


class Sistema(QMainWindow):
    def funcao(self):
        pass

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('YouTube Download')
        self.setFixedSize(400, 200)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 3)
        self.setStyleSheet(  # Style and design of program why a all
            '* {background: white;'
            'color: black ;'
            'font-size: 30px;'
            'width: 300px;}'
        )
        self.butonstyle = estilo_botao
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.setCentralWidget(self.cw)
        self.add_btn(QPushButton(
            'Baixar'), 3, 0, 1, 3,
            lambda: self.downloadvideo(clipboard.paste()),
            self.butonstyle
        )

        # Button responsible for downloading
        self.add_btn(QPushButton(
            'Colar'), 2, 0, 1, 3,
            lambda: self.display.setText(clipboard.paste()),
            self.butonstyle
        )

    #  function responsible of add several types of button
    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        if not funcao:
            pass
        else:
            btn.clicked.connect(funcao)
        if style:
            btn.setStyleSheet(style)
        self.grid.addWidget(btn, row, col, rowspan, colspan)

    @staticmethod
    def downloadvideo(link):
        path_actual = os.getcwd()
        if not os.path.exists(f'{path_actual}\\Videos'):
            os.makedirs(f'{path_actual}\\Videos')
        yt = YouTube(link)
        stream = yt .streams.first()
        stream.download(f'{path_actual}\\Videos')

    @staticmethod
    def path():
        path_actual = os.getcwd()
        if os.path.exists(f'{path_actual}\\Videos'):
            pass
        else:
            return os.makedirs(f'{path_actual}\\Videos')


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    sistema = Sistema()
    sistema.show()
    qt.exec_()
