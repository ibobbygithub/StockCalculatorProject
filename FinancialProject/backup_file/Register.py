# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymongo
import re
from datetime import datetime
#from home import Ui_Home
import dns
server = "mongodb+srv://iBobby:1234@cluster0.1npcu.mongodb.net/<dbname>?retryWrites=true&w=majority"


class Ui_Register(object):
    def setupUi(self, Register, prewindow):
        Register.setObjectName("Register")
        Register.resize(586, 359)
        self.label = QtWidgets.QLabel(Register)
        self.label.setGeometry(QtCore.QRect(160, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtUsername = QtWidgets.QTextEdit(Register)
        self.txtUsername.setGeometry(QtCore.QRect(240, 100, 161, 31))
        self.txtUsername.setObjectName("txtUsername")
        self.txtEmail = QtWidgets.QTextEdit(Register)
        self.txtEmail.setGeometry(QtCore.QRect(240, 140, 161, 31))
        self.txtEmail.setObjectName("txtEmail")
        self.label_2 = QtWidgets.QLabel(Register)
        self.label_2.setGeometry(QtCore.QRect(190, 140, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Register)
        self.label_3.setGeometry(QtCore.QRect(110, 220, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Register)
        self.label_5.setGeometry(QtCore.QRect(200, 10, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(28)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnConfirm = QtWidgets.QPushButton(Register)
        self.btnConfirm.setGeometry(QtCore.QRect(180, 290, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnConfirm.setFont(font)
        self.btnConfirm.setObjectName("btnConfirm")
        self.btnCancel = QtWidgets.QPushButton(Register)
        self.btnCancel.setGeometry(QtCore.QRect(300, 290, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.txtPassword = QtWidgets.QLineEdit(Register)
        self.txtPassword.setGeometry(QtCore.QRect(240, 180, 161, 31))
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword2 = QtWidgets.QLineEdit(Register)
        self.txtPassword2.setGeometry(QtCore.QRect(240, 220, 161, 31))
        self.txtPassword2.setObjectName("txtPassword2")
        self.txtPassword2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_4 = QtWidgets.QLabel(Register)
        self.label_4.setGeometry(QtCore.QRect(160, 180, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.btnConfirm.clicked.connect(self.confirm)
        self.btnCancel.clicked.connect(self.toLogin)

        self.thiswindow = Register
        self.prewindow = prewindow
        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def toLogin(self):
        self.thiswindow.hide()
        self.prewindow.show()

    def confirm(self):
        msg = self.MessageBox()
        username = self.txtUsername.toPlainText().strip()
        email = self.txtEmail.toPlainText().strip()
        password_1 = self.txtPassword.text().strip()
        password_2 = self.txtPassword2.text().strip()
        user_check = self.checkUserAtlas()
        email_check = self.checkEmailAtlas()
        if username == "" or email == "" or password_1 == "" or password_2 == "":
            msg.setText("???????????????????????????????????????????????????????????????")
            msg.exec_()
        else:
            if password_2 == password_1:
                confirm_password = password_1
                if self.checkEmail(email) == True:
                    if username in user_check:
                        msg.setText("username ?????????????????????????????????")
                        msg.exec_()
                    else:
                        if email in email_check:
                            msg.setText("email ?????????????????????????????????")
                            msg.exec_()
                        else:
                            with pymongo.MongoClient(server) as conn:
                                db = conn.get_database('StockDividend')
                                db.credentials.insert_one({'username': username,
                                                               'email': email,
                                                               'password': confirm_password,
                                                               })
                                msg.setText("Your Data has been saved!")
                                msg.exec_()
                                self.txtUsername.clear()
                                self.txtEmail.clear()
                                self.txtPassword.clear()
                                self.txtPassword2.clear()
                else:
                    msg.setText("????????????????????????????????????????????????????????????????????????")
                    msg.exec_()
            else:
                msg.setText("??????????????????????????????????????????????????????????????????????????????")
                msg.exec_()

    def checkEmail(self,mail):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,mail)):
            check = True
        else:
            check = False
        return (check)

    def checkUserAtlas(self):
        user = []
        with pymongo.MongoClient(server) as conn:
            db = conn.get_database("StockDividend")
            where = {}
            cursor = db.credentials.find(where)
            for i in cursor:
                user.append(i['username'])
        return user

    def checkEmailAtlas(self):
        email = []
        with pymongo.MongoClient(server) as conn:
            db = conn.get_database("StockDividend")
            where = {}
            cursor = db.credentials.find(where)
            for i in cursor:
                email.append(i['email'])
        return email

    def MessageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        return msg

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Dialog"))
        self.label.setText(_translate("Register", "Username"))
        self.txtUsername.setHtml(_translate("Register", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Register", "email"))
        self.label_3.setText(_translate("Register", "Confirm Password"))
        self.label_5.setText(_translate("Register", "Register Form"))
        self.btnConfirm.setText(_translate("Register", "??????????????????"))
        self.btnCancel.setText(_translate("Register", "??????????????????"))
        self.label_4.setText(_translate("Register", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QMainWindow()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())
