import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel, QComboBox, QLineEdit)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        items = ['Name', 'Age', 'Score']
        okButton = QLabel('Amount')
        cancelButton = QLineEdit(self)
        okButton2 = QLabel('key ',self)
        cancelButton2 = QComboBox(self)
        cancelButton2.addItems(items)

        hbox = QHBoxLayout()

        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addWidget(okButton2)
        hbox.addWidget(cancelButton2)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)


        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

