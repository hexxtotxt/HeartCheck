from instr import *
from second_win import *
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout, QHBoxLayout

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instructions = QLabel(txt_instruction)
        self.btn_next = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instructions)
        self.layout.addWidget(self.btn_next)
        self.setLayout(self.layout)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)


app = QApplication([])
mw = MainWin()
app.exec_()
