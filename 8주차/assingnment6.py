# import
from PyQt5.QtCore import Qt
import sys, pickle
from PyQt5.QtWidgets import *



# readfile
def readScoreDB(dbfilename):
    fH = open(dbfilename, 'rb')
    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb



# writefile
def writeScoreDB(dbfilename,scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


# test3_2.dat
# 파일 open
fname = "assignment6.dat"  ##input("Enter data file name: ")


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        items = ['Name', 'Age', 'Score']

        # hbox1
        name_label = QLabel('Name: ')
        self.name_lineedit = QLineEdit(self)
        age_label = QLabel('Age: ')
        self.age_lineedit = QLineEdit(self)
        score_label = QLabel('Score: ')
        self.score_lineedit = QLineEdit(self)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(name_label)
        hbox1.addWidget(self.name_lineedit)
        hbox1.addWidget(age_label)
        hbox1.addWidget(self.age_lineedit)
        hbox1.addWidget(score_label)
        hbox1.addWidget(self.score_lineedit)

        # hbox2
        amount_label = QLabel('Amount: ')
        self.amount_lineedit = QLineEdit(self)
        key_label = QLabel('key: ', self)
        self.key_combobox = QComboBox(self)
        self.key_combobox.addItems(items)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(amount_label)
        hbox2.addWidget(self.amount_lineedit)
        hbox2.addWidget(key_label)
        hbox2.addWidget(self.key_combobox)

        # hbox3
        add_button = QPushButton("Add", self)
        del_button = QPushButton("Del", self)
        find_button = QPushButton("Find", self)
        inc_button = QPushButton("Inc", self)
        show_button = QPushButton("Show", self)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(add_button)
        hbox3.addWidget(del_button)
        hbox3.addWidget(find_button)
        hbox3.addWidget(inc_button)
        hbox3.addWidget(show_button)

        # hbox4
        result_label = QLabel('Result: ', self)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(result_label)
        hbox4.addStretch(1)

        # hbox5
        self.result_textedit = QTextEdit(self)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.result_textedit)
        self.result_textedit.setReadOnly(True)

        # vbox
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addStretch(1)

        # window set
        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Score DB')

        self.show()
        add_button.clicked.connect(self.Add)
        del_button.clicked.connect(self.Del)
        find_button.clicked.connect(self.Find)
        inc_button.clicked.connect(self.Inc)
        show_button.clicked.connect(self.Show)




    def Add(self):
        print("add")
        #입력값을 받을 변수 초기화
        names, ages, scores = '', '' , ''
        #입력값을 받고 예외처리
        try:
            names = self.name_lineedit.text()
            ages = int(self.age_lineedit.text())
            scores = int(self.score_lineedit.text())
        except ValueError:
            self.result_textedit.setPlainText("WRONG INPUT! you should type Name, Age, score")
        #lineedit 비우기
        self.name_lineedit.clear()
        self.age_lineedit.clear()
        self.score_lineedit.clear()
        self.amount_lineedit.clear()
        # adding
        db = readScoreDB(fname)
        db.append({'Score': str(scores), 'Age': str(ages), 'Name': str(names)})
        writeScoreDB(fname, db)
        # 출력
        showing = ''
        for i in range(len(db)):
            showing = showing + str(db[i]) + '\n'
        self.result_textedit.setPlainText(showing)
    def Del(self):
        print("del")
        # 입력값을 받을 변수 초기화
        names = ''
        # 입력값을 받고 예외처리
        try :
            names = self.name_lineedit.text()
        except ValueError:
            self.result_textedit.setPlainText("WRONG INPUT! you should type Name")
        # lineedit 비우기
        self.name_lineedit.clear()
        self.age_lineedit.clear()
        self.score_lineedit.clear()
        self.amount_lineedit.clear()
        #deleting
        db = readScoreDB(fname)
        i = 0
        while i<len(db):
            if db[i]['Name'] == names:
                del db[i]
                i = i-1
            i = i+1
        writeScoreDB(fname, db)
        # 출력
        showing = ''
        for i in range(len(db)):
            showing = showing + str(db[i]) + '\n'
        self.result_textedit.setPlainText(showing)

    def Find(self):# 과제 설명에서 그리고 전체학생을 보여줌이 무엇을 의미하는지 물어보기,
                    # 출력후 다 지우고 전체 출력인지 출력후 나머지를 출력인지
        print("find")
        # 입력값을 받을 변수 초기화
        names = ''
        # 입력값을 받고 예외처리
        try :
            names = self.name_lineedit.text()
        except ValueError:
            self.result_textedit.setPlainText("WRONG INPUT! you should type Name")
        # lineedit 비우기
        self.name_lineedit.clear()
        self.age_lineedit.clear()
        self.score_lineedit.clear()
        self.amount_lineedit.clear()
        #finding
        db = readScoreDB(fname)
        showing = ''
        for i in range(len(db)):
            if db[i]['Name'] == names:
                showing = showing + str(db[i]) + "\n"
        writeScoreDB(fname, db)
        # 출력
        self.result_textedit.setPlainText(showing)

    def Inc(self):
        print("inc")
        # 입력값을 받을 변수 초기화
        names, ages, scores, amounts  = '', '', '', ''
        # 입력값을 받고 예외처리
        try:
            names = self.name_lineedit.text()
            amounts = int(self.amount_lineedit.text())
        except ValueError:
            self.result_textedit.setPlainText("WRONG INPUT! you should type Name, Amount")
        try:
            ages = self.name_lineedit.text()
            scores = self.amount_lineedit.text()
        except ValueError:
            self.result_textedit.setPlainText("WRONG INPUT! you should type Name, Amount")


        # lineedit 비우기
        self.name_lineedit.clear()
        self.age_lineedit.clear()
        self.score_lineedit.clear()
        self.amount_lineedit.clear()
        #increasing
        db = readScoreDB(fname)
        for i in range(len(db)):
            if db[i]['Name'] == names:
                db[i]['Score'] = str(int(db[i]['Score']) + amounts)
        writeScoreDB(fname, db)
        # 출력
        showing = ''
        for i in range(len(db)):
            showing = showing + str(db[i]) + '\n'
        self.result_textedit.setPlainText(showing)

    def Show(self):
        print("show")
        keys = self.key_combobox.currentText()
        print("key = "+keys)

        #sorting
        db = readScoreDB(fname)
        db = sorted(db, key=(lambda x : str(x[keys])))

        writeScoreDB(fname,db)
        #출력
        showing = ''
        for i in range(len(db)):
            showing = showing + str(db[i]) + '\n'
        self.result_textedit.setPlainText(showing)
        self.name_lineedit.clear()
        self.age_lineedit.clear()
        self.score_lineedit.clear()
        self.amount_lineedit.clear()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
