import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.__init__()

    def initUI(self):
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15,10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)


        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Absolute')
        self.show()
