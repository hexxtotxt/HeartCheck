from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from instr import *
from final_win import *
class Experiment():
    def __init__(self, age, test_1, test_2, test_3):
        self.age = age
        self.test_1 = test_1
        self.test_2 = test_2
        self.test_3 = test_3
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
    def timer_test(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1event)
        self.timer.start(1000)
    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2event)
        self.timer.start(1500)
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3event)
        self.timer.start(1000)
    def timer1event(self):
        global time 
        time = time.addSecs(-1)
        self.timeline.setText(time.toString("hh:mm:ss"))
        self.timeline.setFont(QFont("Times", 24, QFont.Bold))
        self.timeline.setStyleSheet("color : rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer2event(self):
        global time 
        time = time.addSecs(-1)
        self.timeline.setText(time.toString("hh:mm:ss")[6:8])
        self.timeline.setFont(QFont("Times", 24, QFont.Bold))
        self.timeline.setStyleSheet("color : rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer3event(self):
        global time 
        time = time.addSecs(-1)
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.timeline.setStyleSheet("color : rgb(0,255,0)")   
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.timeline.setStyleSheet("color : rgb(0,255,0)")  
        else:
            self.timeline.setStyleSheet("color : rgb(0,0,0)")  
        self.timeline.setText(time.toString("hh:mm:ss"))
        self.timeline.setFont(QFont("Times", 24, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def next_click_1(self):
        self.hide()
        self.exp = Experiment(self.age_edit.text(), self.instr_1_edit.text(), self.instr_2_edit.text(), self.instr_3_edit.text())
        self.tw = FinalWin(self.exp)
    def initUI(self):
        self.FIO = QLabel(txt_FIO)
        self.age = QLabel(txt_age)
        self.instr_1 = QLabel(txt_instr_1)
        self.instr_2 = QLabel(txt_instr_2)
        self.instr_3 = QLabel(txt_instr_3)  
        self.timeline = QLabel(txt_timer)  
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
        self.r_line.addWidget(self.timeline)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)


    def connects(self):
        self.btn_next_1.clicked.connect(self.next_click_1)
        self.btn_test_1.clicked.connect(self.timer_test)
        self.btn_test_2.clicked.connect(self.timer_sits)
        self.btn_test_3.clicked.connect(self.timer_final)
