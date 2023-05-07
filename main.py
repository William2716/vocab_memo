import utils
from datetime import datetime 




import sys
from PyQt5 import QtWidgets
from main_window import Ui_MainWindow
from window_a import Ui_Form as Ui_Form_A
from window_b import Ui_Form as Ui_Form_B
from datetime import datetime
import os
import utils

class WindowA(QtWidgets.QWidget, Ui_Form_A):
    def __init__(self, parent=None):
        super(WindowA, self).__init__(parent)
        self.setupUi(self)
        self.search_pushButton.clicked.connect(self.lookup_and_display_word)

    def lookup_and_display_word(self):
        word = utils.Word(name=self.input_lineEdit.text(), date=datetime.now())
        word.storage()
        with open(f"{datetime.now().strftime('%Y_%m_%d')}/{word.name}.txt", "r", encoding='utf-8') as file:
            self.textEdit.setPlainText(file.read())


class WindowB(QtWidgets.QWidget, Ui_Form_B):
    def __init__(self, parent=None):
        super(WindowB, self).__init__(parent)
        self.setupUi(self)
        self.current_file = 0
        self.files = os.listdir(datetime.now().strftime('%Y_%m_%d'))
        self.update_file_display()
        self.show_pushButton.clicked.connect(self.show_meaning)
        self.next_pushButton_2.clicked.connect(self.next_file)

    def update_file_display(self):
        if self.current_file < len(self.files):
            self.textEdit.setPlainText(self.files[self.current_file])
        else:
            self.textEdit.setPlainText("No more words")

    def show_meaning(self):
        if self.current_file < len(self.files):
            with open(f"{datetime.now().strftime('%Y_%m_%d')}/{self.files[self.current_file]}", "r", encoding='utf-8') as file:
                self.textEdit.setPlainText(file.read())

    def next_file(self):
        self.current_file += 1
        self.update_file_display()


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


if __name__ == "__main__":
    utils.creat_folder()
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
