from PyQt5.QtCore import Qt
from window4 import *
from window3 import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_apper()
        self.initUI()
        self.connects()
        self.show()
    def set_apper(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.fio = QLabel(name)
        self.age = QLabel(agee)
        self.exisice = QLabel(dd)
        self.exisice2 = QLabel(dd2)
        self.exisice3 = QLabel(dd3)
        self.btn1 = QPushButton(begin)
        self.btn2 = QPushButton(begin_sit)
        self.btn3 = QPushButton(begin_end)
        self.btn4 = QPushButton(resullts)
        self.line_name = QLineEdit("Ф.И.О")
        self.line_name1= QLineEdit("0")
        self.line_name2 = QLineEdit("0")
        self.line_name3 =QLineEdit("0")
        self.line_name4 = QLineEdit("0")

        self.l_line.addWidget(self.fio)
        self.l_line.addWidget(self.line_name)

        self.l_line.addWidget(self.age)
        self.l_line.addWidget(self.line_name1)

        self.l_line.addWidget(self.exisice)
        self.l_line.addWidget(self.btn1)
        self.l_line.addWidget(self.line_name2)

        self.l_line.addWidget(self.exisice2)
        self.l_line.addWidget(self.btn2)
        self.l_line.addWidget(self.btn3)
        self.l_line.addWidget(self.exisice3)
        self.l_line.addWidget(self.line_name3)
        self.l_line.addWidget(self.line_name4)
        self.l_line.addWidget(self.btn4)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.btn4.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.fv = FinalWin()