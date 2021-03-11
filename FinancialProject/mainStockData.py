# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StockData.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymongo
from home import Home
import dns
server = "mongodb+srv://iBobby:1234@cluster0.1npcu.mongodb.net/<dbname>?retryWrites=true&w=majority"

class Ui_mainStockData(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(519, 510)
        Dialog.setMouseTracking(False)
        Dialog.setTabletTracking(False)
        self.txtStockName = QtWidgets.QTextEdit(Dialog)
        self.txtStockName.setGeometry(QtCore.QRect(250, 140, 141, 31))
        self.txtStockName.setObjectName("txtStockName")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 240, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lblRealPrice = QtWidgets.QLabel(Dialog)
        self.lblRealPrice.setGeometry(QtCore.QRect(190, 510, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblRealPrice.setFont(font)
        self.lblRealPrice.setText("")
        self.lblRealPrice.setObjectName("lblRealPrice")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(120, 290, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txtStockCurrentPrice = QtWidgets.QTextEdit(Dialog)
        self.txtStockCurrentPrice.setGeometry(QtCore.QRect(250, 240, 141, 31))
        self.txtStockCurrentPrice.setObjectName("txtStockCurrentPrice")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(120, 140, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnSave = QtWidgets.QPushButton(Dialog)
        self.btnSave.setGeometry(QtCore.QRect(100, 410, 131, 31))
        self.btnSave.setObjectName("btnSave")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(170, 80, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnClear = QtWidgets.QPushButton(Dialog)
        self.btnClear.setGeometry(QtCore.QRect(270, 410, 131, 31))
        self.btnClear.setObjectName("btnClear")
        self.txtfleefloat = QtWidgets.QTextEdit(Dialog)
        self.txtfleefloat.setGeometry(QtCore.QRect(250, 340, 141, 31))
        self.txtfleefloat.setObjectName("txtfleefloat")
        self.txtDevidend = QtWidgets.QTextEdit(Dialog)
        self.txtDevidend.setGeometry(QtCore.QRect(250, 290, 141, 31))
        self.txtDevidend.setObjectName("txtDevidend")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(120, 190, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setObjectName("label_9")
        self.txtCatetagory = QtWidgets.QTextEdit(Dialog)
        self.txtCatetagory.setGeometry(QtCore.QRect(250, 190, 141, 31))
        self.txtCatetagory.setObjectName("txtCatetagory")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(120, 340, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 470, 75, 23))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")


        self.pushButton.clicked.connect(self.backMain)
        self.btnSave.clicked.connect(self.SaveData)
        self.btnClear.clicked.connect(self.clear)

        self.thiswindow = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def SaveData(self):
        msg = self.MessageBox()
        if self.txtStockName.toPlainText() == "" or self.txtCatetagory.toPlainText() == "" or self.txtfleefloat.toPlainText() == "" or self.txtStockCurrentPrice.toPlainText() == "" or self.txtDevidend.toPlainText() == "":
            msg.setText("Please input all fields")
            msg.exec_()
        else:
            stock_name = self.txtStockName.toPlainText()
            category = self.txtCatetagory.toPlainText()
            ff = float(self.txtfleefloat.toPlainText())
            current_price = float(self.txtStockCurrentPrice.toPlainText())
            dividend = float(self.txtDevidend.toPlainText())
            with pymongo.MongoClient(server) as conn:
                db = conn.get_database('StockDividend')
                currID = db.sample_stock.insert_one({'stock_name': stock_name,
                                                     'category': category,
                                                     'fleefloat': ff,
                                                     'current_price': current_price,
                                                     'dividend': dividend
                                                     })
                # print("new record _id = {}".format(currID.inserted_id))
                msg.setText("Your Data has been saved!" + str(currID))
                msg.exec_()
                self.txtStockName.clear()
                self.txtCatetagory.clear()
                self.txtfleefloat.clear()
                self.txtStockCurrentPrice.clear()
                self.txtDevidend.clear()

    def backMain(self):
        #self.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Home()
        self.ui.setupUi(self.window)
        self.thiswindow.hide()
        self.window.show()


    def clear(self):
        self.txtStockName.clear()
        self.txtCatetagory.clear()
        self.txtfleefloat.clear()
        self.txtStockCurrentPrice.clear()
        self.txtDevidend.clear()

    def MessageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        return msg

    def retranslateUi(self, StockDataDialog):
        _translate = QtCore.QCoreApplication.translate
        StockDataDialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "ราคาปัจจุบัน"))
        self.label_7.setText(_translate("Dialog", "ปันผลปัจจุบัน %"))
        self.label_4.setText(_translate("Dialog", "ชื่อหุ้น"))
        self.btnSave.setText(_translate("Dialog", "Save"))
        self.label_5.setText(_translate("Dialog", "เพิ่มรายการหุ้นที่น่าสนใจ"))
        self.btnClear.setText(_translate("Dialog", "Clear"))
        self.label_9.setText(_translate("Dialog", "หมวดธุรกิจ"))
        self.label_8.setText(_translate("Dialog", "flee float %"))
        self.pushButton.setText(_translate("Dialog", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainStockData = QtWidgets.QDialog()
    ui = Ui_mainStockData()
    ui.setupUi(mainStockData)
    mainStockData.show()
    sys.exit(app.exec_())
