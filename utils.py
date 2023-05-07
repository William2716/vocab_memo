import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os
from PyQt5 import QtWidgets
#import windows
from main_window import Ui_MainWindow
from window_a import Ui_Form as Ui_Form_A
from window_b import Ui_Form as Ui_Form_B

day=[0,2,7,30]#the timedelta for review words

class Word:
    def __init__(self,name,date):
        self.name=name
        self.date=date
    def storage(self):
        for i in day:
            with open((self.date+timedelta(days=i)).strftime('%Y_%m_%d')+'/'+self.name+'.txt', 'w', encoding='utf-8') as file:
                looking_up(self.name, file)

def looking_up(name, file):
    url = f'https://dictionary.cambridge.org/dictionary/english-chinese-simplified/{name}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/55.0.2883.87 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'lxml')

    class_of_words = bs.find_all(class_='pr entry-body__el')

    for class_of_word in class_of_words:
        word_header = class_of_word.find(class_='pos-header dpos-h')

        file.write(f"{word_header.find(class_='pos dpos').text.strip()}\n"
                    f"{word_header.find(class_='uk dpron-i').find(class_='region dreg').text.strip()}\n"
                    f"{word_header.find(class_='uk dpron-i').find(class_='pron dpron').text.strip()}\n"
                    f"{word_header.find(class_='us dpron-i').find(class_='region dreg').text.strip()}\n"
                    f"{word_header.find(class_='us dpron-i').find(class_='pron dpron').text.strip()}\n")

        word_parts = class_of_word.find_all(class_='pr dsense')

        if word_parts:
            for word_part in word_parts:
                file.write(f"{word_part.find(class_='def-block ddef_block').text.strip()}\n")
        else:
            file.write(f"{class_of_word.find(class_='def-block ddef_block').text.strip()}\n")

def creat_folder():#create folder for each day
    for i in day:    
        if not os.path.exists((datetime.now()+timedelta(days=i)).strftime('%Y_%m_%d')):
            os.makedirs((datetime.now()+timedelta(days=i)).strftime('%Y_%m_%d'))

class WindowA(QtWidgets.QWidget, Ui_Form_A):
    def __init__(self, parent=None):
        super(WindowA, self).__init__(parent)
        self.setupUi(self)
        self.search_pushButton.clicked.connect(self.lookup_word)

    def lookup_word(self):
        word = Word(name=self.input_lineEdit.text(), date=datetime.now())
        word.storage()
        with open(f"{datetime.now().strftime('%Y_%m_%d')}/{word.name}.txt", "r", encoding='utf-8') as file:
            self.textEdit.setPlainText(file.read())


class WindowB(QtWidgets.QWidget, Ui_Form_B):
    def __init__(self, parent=None):
        super(WindowB, self).__init__(parent)
        self.setupUi(self)
        self.current_file = 0
        self.files = os.listdir(datetime.now().strftime('%Y_%m_%d'))
        self.update_display()
        self.show_pushButton.clicked.connect(self.show_meaning)
        self.next_pushButton_2.clicked.connect(self.next_file)

    def update_display(self):
        if self.current_file < len(self.files):
            
            file_name = self.files[self.current_file].replace('.txt', '')
            self.textEdit.setPlainText(file_name)
        else:
            self.textEdit.setPlainText("No more words")

    def show_meaning(self):
        if self.current_file < len(self.files):
            with open(f"{datetime.now().strftime('%Y_%m_%d')}/{self.files[self.current_file]}", "r", encoding='utf-8') as file:
                self.textEdit.setPlainText(file.read())

    def next_file(self):
        self.current_file += 1
        self.update_display()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_window_a)
        self.pushButton_2.clicked.connect(self.open_window_b)

    def open_window_a(self):
        self.window_a = WindowA()
        self.window_a.show()

    def open_window_b(self):
        self.window_b = WindowB()
        self.window_b.show()