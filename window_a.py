# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_a.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.input_lineEdit = QtWidgets.QLineEdit(Form)
        self.input_lineEdit.setGeometry(QtCore.QRect(10, 20, 171, 31))
        self.input_lineEdit.setObjectName("input_lineEdit")
        self.search_pushButton = QtWidgets.QPushButton(Form)
        self.search_pushButton.setGeometry(QtCore.QRect(290, 20, 81, 31))
        self.search_pushButton.setObjectName("search_pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 70, 371, 221))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.input_lineEdit.setText(_translate("Form", "please input a word"))
        self.search_pushButton.setText(_translate("Form", "Search"))