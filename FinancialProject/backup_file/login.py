# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from home import Ui_Home
from Register import Ui_Register
import pymongo
from PyQt5.QtWidgets import QMessageBox
import dns
server = "mongodb+srv://iBobby:1234@cluster0.1npcu.mongodb.net/<dbname>?retryWrites=true&w=majority"

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(582, 340)
        self.txtUsername = QtWidgets.QTextEdit(login)
        self.txtUsername.setGeometry(QtCore.QRect(230, 140, 161, 31))
        self.txtUsername.setObjectName("txtUsername")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(150, 140, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(150, 180, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnLogin = QtWidgets.QPushButton(login)
        self.btnLogin.setGeometry(QtCore.QRect(190, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.btnExit = QtWidgets.QPushButton(login)
        self.btnExit.setGeometry(QtCore.QRect(310, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName("btnExit")
        self.label_3 = QtWidgets.QLabel(login)
        self.label_3.setGeometry(QtCore.QRect(130, 40, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtPassword = QtWidgets.QLineEdit(login)
        self.txtPassword.setGeometry(QtCore.QRect(230, 180, 161, 31))
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)

        self.btnLogin.clicked.connect(self.showMain)
        self.btnExit.clicked.connect(self.toRegister)

        self.thiswindow = login
        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def toRegister(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Register()
        self.ui.setupUi(self.window,self.thiswindow)
        self.thiswindow.hide()
        self.window.show()

    def showMain(self):
        msg = self.MessageBox()
        user = self.txtUsername.toPlainText()
        password = self.txtPassword.text()
        check_user = self.checkUser()
        check_pass = self.checkPass()
        if user == "" or password == "":
            msg.setText("กรุณาป้อน username และ password ให้ครบทุกช่อง")
            msg.exec_()
        else:
            if user in check_user and password in check_pass:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_Home()
                self.ui.setupUi(self.window, self.thiswindow,user)
                self.thiswindow.hide()
                self.window.show()
            else:
                msg.setText("username หรือ password ไม่ถูกต้อง")
                msg.exec_()


    def checkUser(self):
        user = []
        with pymongo.MongoClient(server) as conn:
            db = conn.get_database("StockDividend")
            where = {}
            cursor = db.credentials.find(where)
            for i in cursor:
                user.append(i['username'])
        return user

    def checkPass(self):
        password = []
        with pymongo.MongoClient(server) as conn:
            db = conn.get_database("StockDividend")
            where = {}
            cursor = db.credentials.find(where)
            for i in cursor:
                password.append(i['password'])
        return password

    def MessageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        return msg

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Dialog"))
        self.txtUsername.setHtml(_translate("login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("login", "Username"))
        self.label_2.setText(_translate("login", "Password"))
        self.btnLogin.setText(_translate("login", "เข้าสู่ระบบ"))
        self.btnExit.setText(_translate("login", "ออก"))
        self.label_3.setText(_translate("login", "Stock Dividend Calc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QDialog()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
