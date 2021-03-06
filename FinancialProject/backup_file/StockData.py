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
from datetime import datetime
#from home import Ui_Home
import dns
server = "mongodb+srv://iBobby:1234@cluster0.1npcu.mongodb.net/<dbname>?retryWrites=true&w=majority"

class Ui_StockData(object):
    def setupUi(self, StockData, prewindow):
        StockData.setObjectName("StockData")
        StockData.resize(519, 510)
        StockData.setMouseTracking(False)
        StockData.setTabletTracking(False)
        self.txtStockName = QtWidgets.QTextEdit(StockData)
        self.txtStockName.setGeometry(QtCore.QRect(250, 110, 141, 31))
        self.txtStockName.setObjectName("txtStockName")
        self.label_3 = QtWidgets.QLabel(StockData)
        self.label_3.setGeometry(QtCore.QRect(120, 210, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lblRealPrice = QtWidgets.QLabel(StockData)
        self.lblRealPrice.setGeometry(QtCore.QRect(190, 510, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblRealPrice.setFont(font)
        self.lblRealPrice.setText("")
        self.lblRealPrice.setObjectName("lblRealPrice")
        self.label_7 = QtWidgets.QLabel(StockData)
        self.label_7.setGeometry(QtCore.QRect(120, 260, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txtStockCurrentPrice = QtWidgets.QTextEdit(StockData)
        self.txtStockCurrentPrice.setGeometry(QtCore.QRect(250, 210, 141, 31))
        self.txtStockCurrentPrice.setObjectName("txtStockCurrentPrice")
        self.label_4 = QtWidgets.QLabel(StockData)
        self.label_4.setGeometry(QtCore.QRect(120, 110, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnSave = QtWidgets.QPushButton(StockData)
        self.btnSave.setGeometry(QtCore.QRect(100, 410, 131, 31))
        self.btnSave.setObjectName("btnSave")
        self.label_5 = QtWidgets.QLabel(StockData)
        self.label_5.setGeometry(QtCore.QRect(180, 40, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnClear = QtWidgets.QPushButton(StockData)
        self.btnClear.setGeometry(QtCore.QRect(270, 410, 131, 31))
        self.btnClear.setObjectName("btnClear")
        self.txtfleefloat = QtWidgets.QTextEdit(StockData)
        self.txtfleefloat.setGeometry(QtCore.QRect(250, 310, 141, 31))
        self.txtfleefloat.setObjectName("txtfleefloat")
        self.txtDevidend = QtWidgets.QTextEdit(StockData)
        self.txtDevidend.setGeometry(QtCore.QRect(250, 260, 141, 31))
        self.txtDevidend.setObjectName("txtDevidend")
        self.label_9 = QtWidgets.QLabel(StockData)
        self.label_9.setGeometry(QtCore.QRect(120, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(StockData)
        self.label_8.setGeometry(QtCore.QRect(120, 310, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(StockData)
        self.pushButton.setGeometry(QtCore.QRect(10, 470, 75, 23))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.cboCategory = QtWidgets.QComboBox(StockData)
        self.cboCategory.setGeometry(QtCore.QRect(250, 161, 141, 31))
        self.cboCategory.setObjectName("cboCategory")

        self.cboCategory.setObjectName("cboCategory")
        self.cboCategory.addItem("?????????????????????????????????????????????????????????????????????")
        self.cboCategory.addItem("??????????????????????????????????????????????????????")
        self.cboCategory.addItem("???????????????????????????????????????")
        self.cboCategory.addItem("????????????????????????????????????????????????")
        self.cboCategory.addItem("??????????????????????????????????????????????????????????????????????????????")
        self.cboCategory.addItem("????????????????????????")
        self.cboCategory.addItem("??????????????????")
        self.cboCategory.addItem("???????????????????????????")

        self.pushButton.clicked.connect(self.backMain)
        self.btnSave.clicked.connect(self.SaveData)
        self.btnClear.clicked.connect(self.clear)

        self.prewindow = prewindow
        self.thiswindow = StockData
        self.retranslateUi(StockData)
        QtCore.QMetaObject.connectSlotsByName(StockData)

    def SaveData(self):
        msg = self.MessageBox()
        if self.txtStockName.toPlainText() == "" or self.cboCategory.currentText() == "" or self.txtfleefloat.toPlainText() == "" or self.txtStockCurrentPrice.toPlainText() == "" or self.txtDevidend.toPlainText() == "":
            msg.setText("Please input all fields")
            msg.exec_()
        else:
            now = datetime.now()
            stock_name = str(self.txtStockName.toPlainText()).upper()
            category = self.cboCategory.currentText()
            ff = float(self.txtfleefloat.toPlainText())
            current_price = float(self.txtStockCurrentPrice.toPlainText())
            dividend = float(self.txtDevidend.toPlainText())
            with pymongo.MongoClient(server) as conn:
                db = conn.get_database('StockDividend')
                currID = db.sample_stock.insert_one({'stock_name': stock_name,
                                                     'category': category,
                                                     'current_price': current_price,
                                                     'dividend': dividend,
                                                     'fleefloat': ff,
                                                     'date_time': now
                                                     })
                msg.setText("Your Data has been saved!")
                msg.exec_()
                self.txtStockName.clear()
                self.txtfleefloat.clear()
                self.txtStockCurrentPrice.clear()
                self.txtDevidend.clear()

    def backMain(self):
        self.thiswindow.hide()
        self.prewindow.show()


    def clear(self):
        self.txtStockName.clear()
        self.txtfleefloat.clear()
        self.txtStockCurrentPrice.clear()
        self.txtDevidend.clear()

    def MessageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        return msg

    def retranslateUi(self, StockData):
        _translate = QtCore.QCoreApplication.translate
        StockData.setWindowTitle(_translate("StockData", "Dialog"))
        self.label_3.setText(_translate("StockData", "????????????????????????????????????"))
        self.label_7.setText(_translate("StockData", "??????????????????????????????????????? %"))
        self.label_4.setText(_translate("StockData", "????????????????????????"))
        self.btnSave.setText(_translate("StockData", "Save"))
        self.label_5.setText(_translate("StockData", "???????????????????????????????????????????????????????????????????????????"))
        self.btnClear.setText(_translate("StockData", "Clear"))
        self.label_9.setText(_translate("StockData", "??????????????????????????????"))
        self.label_8.setText(_translate("StockData", "flee float %"))
        self.pushButton.setText(_translate("StockData", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StockData = QtWidgets.QDialog()
    ui = Ui_StockData()
    ui.setupUi(StockData)
    StockData.show()
    sys.exit(app.exec_())
