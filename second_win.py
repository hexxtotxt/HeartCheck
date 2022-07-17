from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
from instr import *
from final_win import *
class TestWin(QWidget):
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
    def next_click_1(self):
        self.hide()
        self.tw = FinalWin()
    def initUI(self):
        self.FIO = QLabel(txt_FIO)
        self.age = QLabel(txt_age)
        self.instr_1 = QLabel(txt_instr_1)
        self.instr_2 = QLabel(txt_instr_2)
        self.instr_3 = QLabel(txt_instr_3)  
        self.timer = QLabel(txt_timer)  
        self.btn_test_1 = QPushButton(txt_test_1)
        self.btn_test_2 = QPushButton(txt_test_2)
        self.btn_test_3 = QPushButton(txt_test_3)
        self.btn_next_1 = QPushButton(txt_btn_next)
        self.FIO_edit = QLineEdit(txt_FIO_edit)
        self.age_edit = QLineEdit(txt_age_edit)
        self.instr_1_edit = QLineEdit(txt_instr_1_edit)
        self.instr_2_edit = QLineEdit(txt_instr_2_edit)
        self.instr_3_edit = QLineEdit(txt_instr_3_edit) 
        self.h_line = QHBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line.addWidget(self.FIO)
        self.l_line.addWidget(self.FIO_edit)
        self.l_line.addWidget(self.age)
        self.l_line.addWidget(self.age_edit)
        self.l_line.addWidget(self.instr_1)
        self.l_line.addWidget(self.btn_test_1)
        self.l_line.addWidget(self.instr_1_edit)
        self.l_line.addWidget(self.instr_2)
        self.l_line.addWidget(self.btn_test_2)
        self.l_line.addWidget(self.instr_3)
        self.l_line.addWidget(self.btn_test_3)
        self.l_line.addWidget(self.instr_2_edit)
        self.l_line.addWidget(self.instr_3_edit)
        self.l_line.addWidget(self.btn_next_1, alignment=Qt.AlignCenter)
        self.r_line.addWidget(self.timer)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)


    def connects(self):
        self.btn_next_1.clicked.connect(self.next_click_1)