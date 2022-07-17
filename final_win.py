from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
from instr import *
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.result = QLabel(txt_result)
        self.rec = QLabel(txt_rec)
        self.line = QVBoxLayout()
        self.line.addWidget(self.result, alignment=Qt.AlignCenter)
        self.line.addWidget(self.rec, alignment=Qt.AlignCenter)
        self.setLayout(self.line)

