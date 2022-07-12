from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox
from random import randint

def show_win():
    victory_win = QMessageBox()
    victory_win.setWindowTitle('Викторина')
    victory_win.setText('Верно!')
    victory_win.exec_()


def show_lose():
    lose_win = QMessageBox()
    lose_win.setWindowTitle('Викторина')
    lose_win.setText('Попробуйте еще раз!')
    lose_win.exec_()



app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Викторина')
main_win.resize(500, 200)
question = QLabel('В каком году была основана алгоритмика?')
btn_ans1 = QRadioButton('2010')
btn_ans2 = QRadioButton('2013')
btn_ans3 = QRadioButton('2016')
btn_ans4 = QRadioButton('2019')

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layout_main = QVBoxLayout()

layoutH1.addWidget(question, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_ans1, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_ans2, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_ans3, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_ans4, alignment=Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)

main_win.setLayout(layout_main)


btn_ans3.clicked.connect(show_win)
btn_ans1.clicked.connect(show_lose)
btn_ans2.clicked.connect(show_lose)
btn_ans4.clicked.connect(show_lose)
main_win.show()
app.exec_()