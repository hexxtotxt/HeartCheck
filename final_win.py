from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
from instr import *
class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
    def result(self):
        self.index = (4 * (int(self.exp.test_1) + int(self.exp.test_2) + int(self.exp.test_3)) - 200) / 10 
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.result()

        if (int(self.exp.age) >= 7) and (int(self.exp.age) <= 8):
            if (self.index >= 21):
                self.rec = QLabel(txt_rec + txt_res_1)
            if (self.index >= 17) and (self.index < 21):
                self.rec = QLabel(txt_rec + txt_res_2)
            if (self.index >= 12) and (self.index < 17):
                self.rec = QLabel(txt_rec + txt_res_3)
            if (self.index >= 6.5) and (self.index < 12):
                self.rec = QLabel(txt_rec + txt_res_4)
            if (self.index < 6.5):
                self.rec = QLabel(txt_rec + txt_res_5)

        if (int(self.exp.age) >= 9) and (int(self.exp.age) <= 10):
            if (self.index >= 19.5):
                self.rec = QLabel(txt_rec + txt_res_1)
            if (self.index >= 15.5) and (self.index < 19.5):
                self.rec = QLabel(txt_rec + txt_res_2)
            if (self.index >= 10.5) and (self.index < 15.5):
                self.rec = QLabel(txt_rec + txt_res_3)
            if (self.index >= 5) and (self.index < 10.5):
                self.rec = QLabel(txt_rec + txt_res_4)
            if (self.index < 5):
                self.rec = QLabel(txt_rec + txt_res_5)

        if (int(self.exp.age) >= 11) and (int(self.exp.age) <= 12):
            if (self.index >= 18):
                self.rec = QLabel(txt_rec + txt_res_1)
            if (self.index >= 14) and (self.index < 18):
                self.rec = QLabel(txt_rec + txt_res_2)
            if (self.index >= 9) and (self.index < 14):
                self.rec = QLabel(txt_rec + txt_res_3)
            if (self.index >= 3.5) and (self.index < 9):
                self.rec = QLabel(txt_rec + txt_res_4)
            if (self.index < 3.5):
                self.rec = QLabel(txt_rec + txt_res_5)

        if (int(self.exp.age) >= 13) and (int(self.exp.age) <= 14):
            if (self.index >= 16.5):
                self.rec = QLabel(txt_rec + txt_res_1)
            if (self.index >= 12.5) and (self.index < 16.5):
                self.rec = QLabel(txt_rec + txt_res_2)
            if (self.index >= 7.5) and (self.index < 12.5):
                self.rec = QLabel(txt_rec + txt_res_3)
            if (self.index >= 2) and (self.index < 7.5):
                self.rec = QLabel(txt_rec + txt_res_4)
            if (self.index < 2):
                self.rec = QLabel(txt_rec + txt_res_5)

        if (int(self.exp.age) >= 15):
            if (self.index >= 15):
                self.rec = QLabel(txt_rec + txt_res_1)
            if (self.index >= 11) and (self.index < 15):
                self.rec = QLabel(txt_rec + txt_res_2)
            if (self.index >= 6) and (self.index < 11):
                self.rec = QLabel(txt_rec + txt_res_3)
            if (self.index >= 0.5) and (self.index < 6):
                self.rec = QLabel(txt_rec + txt_res_4)
            if (self.index < 0.5):
                self.rec = QLabel(txt_rec + txt_res_5)


        self.result = QLabel(txt_result + str(self.index))
        self.line = QVBoxLayout()
        self.line.addWidget(self.result, alignment=Qt.AlignCenter)
        self.line.addWidget(self.rec, alignment=Qt.AlignCenter)
        self.setLayout(self.line)
