# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\StockCalc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymongo
import csv
from datetime import datetime
# from home import Ui_Home
import dns
from PyQt5.QtWidgets import QTableWidgetItem
server = "mongodb+srv://iBobby:1234@cluster0.1npcu.mongodb.net/<dbname>?retryWrites=true&w=majority"

class Ui_StockCalc(object):
    def setupUi(self, StockCalc,prewindow):
        StockCalc.setObjectName("StockCalc")
        StockCalc.resize(844, 411)
        StockCalc.setLayoutDirection(QtCore.Qt.LeftToRight)
        StockCalc.setStyleSheet("background-color: rgb(205, 219, 231);")
        self.txtStockHolding = QtWidgets.QTextEdit(StockCalc)
        self.txtStockHolding.setGeometry(QtCore.QRect(700, 150, 131, 31))
        self.txtStockHolding.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.txtStockHolding.setObjectName("txtStockHolding")
        self.label_3 = QtWidgets.QLabel(StockCalc)
        self.label_3.setGeometry(QtCore.QRect(540, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(105, 147, 184);")
        self.label_3.setObjectName("label_3")
        self.lblRealPrice = QtWidgets.QLabel(StockCalc)
        self.lblRealPrice.setGeometry(QtCore.QRect(190, 510, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblRealPrice.setFont(font)
        self.lblRealPrice.setText("")
        self.lblRealPrice.setObjectName("lblRealPrice")
        self.label_4 = QtWidgets.QLabel(StockCalc)
        self.label_4.setGeometry(QtCore.QRect(540, 80, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(105, 147, 184);")
        self.label_4.setObjectName("label_4")
        self.btnSave = QtWidgets.QPushButton(StockCalc)
        self.btnSave.setGeometry(QtCore.QRect(550, 330, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSave.setFont(font)
        self.btnSave.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(105, 147, 184);\n"
"color: rgb(255, 255, 255)")
        self.btnSave.setObjectName("btnSave")
        self.label_5 = QtWidgets.QLabel(StockCalc)
        self.label_5.setGeometry(QtCore.QRect(20, -10, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(105, 147, 184);")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(StockCalc)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 330, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(105, 147, 184);\n"
"color: rgb(255, 255, 255)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.txtStockYear = QtWidgets.QTextEdit(StockCalc)
        self.txtStockYear.setGeometry(QtCore.QRect(700, 270, 131, 31))
        self.txtStockYear.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.txtStockYear.setObjectName("txtStockYear")
        self.txtStockDisposit = QtWidgets.QTextEdit(StockCalc)
        self.txtStockDisposit.setGeometry(QtCore.QRect(700, 210, 131, 31))
        self.txtStockDisposit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.txtStockDisposit.setObjectName("txtStockDisposit")
        self.label_8 = QtWidgets.QLabel(StockCalc)
        self.label_8.setGeometry(QtCore.QRect(540, 210, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(105, 147, 184);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(StockCalc)
        self.label_9.setGeometry(QtCore.QRect(540, 270, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(105, 147, 184);")
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(StockCalc)
        self.label_6.setGeometry(QtCore.QRect(540, 170, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(105, 147, 184);")
        self.label_6.setObjectName("label_6")
        self.choStockName = QtWidgets.QComboBox(StockCalc)
        self.choStockName.setGeometry(QtCore.QRect(700, 90, 131, 31))
        self.choStockName.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(105, 147, 184);\n"
"color: rgb(255, 255, 255)")
        self.choStockName.setObjectName("choStockName")
        self.btnLogout = QtWidgets.QPushButton(StockCalc)
        self.btnLogout.setGeometry(QtCore.QRect(760, 380, 75, 23))
        self.btnLogout.setStyleSheet("color: rgb(105, 147, 184);")
        self.btnLogout.setCheckable(False)
        self.btnLogout.setAutoRepeat(False)
        self.btnLogout.setAutoExclusive(False)
        self.btnLogout.setDefault(False)
        self.btnLogout.setFlat(True)
        self.btnLogout.setObjectName("btnLogout")
        self.tableWidget = QtWidgets.QTableWidget(StockCalc)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 511, 331))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_10 = QtWidgets.QLabel(StockCalc)
        self.label_10.setGeometry(QtCore.QRect(560, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(105, 147, 184);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(StockCalc)
        self.label_11.setGeometry(QtCore.QRect(670, 0, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(69, 111, 147);")
        self.label_11.setObjectName("label_11")
        self.btnExport = QtWidgets.QPushButton(StockCalc)
        self.btnExport.setGeometry(QtCore.QRect(380, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnExport.setFont(font)
        self.btnExport.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(105, 147, 184);\n"
"color: rgb(255, 255, 255)")
        mylist = self.stock_pickup()
        self.btnExport.setObjectName("btnExport")
        for i in mylist:
                self.choStockName.addItem(i[0])
        self.btnSave.clicked.connect(self.showDividend)
        self.btnLogout.clicked.connect(self.back)
        self.btnExport.clicked.connect(self.Export)
        self.pushButton_2.clicked.connect(self.Clear)

        self.prewindow = prewindow
        self.thiswindow = StockCalc
        self.retranslateUi(StockCalc)
        QtCore.QMetaObject.connectSlotsByName(StockCalc)

    def Clear(self):
        self.txtStockYear.clear()
        self.txtStockDisposit.clear()
        self.txtStockHolding.clear()

    def Export(self):
        msg = self.MessageBox()
        StockName = self.choStockName.currentText()
        StockHolding = self.txtStockHolding.toPlainText()
        StockDisposit = self.txtStockDisposit.toPlainText()
        StockYear = self.txtStockYear.toPlainText()
        now = datetime.now()
        date_time = now.strftime("%m_%d_%Y")
        with open('csv_file/' + StockName + '_' + date_time + '.csv', mode='w',encoding="utf-8") as csv_file:
                writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
                if StockDisposit and StockYear != "":
                        month = 12
                        StockHolding = 0
                        num = 1
                        dv_list = self.Calc(str(StockName), float(StockHolding), float(StockDisposit), int(StockYear))
                        writer.writerow(["year","deposit","desposit year","dividend","total deposit"])
                        for i in range(int(StockYear)):
                                row_1 = "{:,.2f}".format(float(StockDisposit))
                                row_2 = "{:,.2f}".format(float(StockDisposit) * month)
                                row_3 = "{:,.2f}".format(dv_list[i])
                                holding_collect = float(StockDisposit) * month
                                row_4 = "{:,.2f}".format((holding_collect + (i * month * float(StockDisposit))))
                                writer.writerow([num,row_1,row_2,row_3,row_4])
                                num += 1
                        msg.setText("Export CSV Success!!")
                        msg.exec_()
                elif StockDisposit != "" and StockYear != "" and StockHolding != "":
                        month = 12
                        num = 1
                        dv_list = self.Calc(str(StockName), float(StockHolding), float(StockDisposit), int(StockYear))
                        writer.writerow(["year", "deposit", "desposit year", "dividend", "total deposit"])
                        for i in range(int(StockYear)):
                                row_1 = "{:,.2f}".format(float(StockDisposit))
                                row_2 = "{:,.2f}".format(float(StockDisposit) * month)
                                row_3 = "{:,.2f}".format(dv_list[i])
                                holding_collect = float(StockDisposit) * month
                                row_4 = "{:,.2f}".format((holding_collect + (i * month * float(StockDisposit))))
                                writer.writerow([num, row_1, row_2, row_3, row_4])
                                num += 1
                        msg.setText("Export CSV Success!!")
                        msg.exec_()

    def back(self):
            self.thiswindow.hide()
            self.prewindow.show()

    def showDividend(self):
            msg = self.MessageBox()
            StockName = self.choStockName.currentText()
            StockHolding = self.txtStockHolding.toPlainText()
            StockDisposit = self.txtStockDisposit.toPlainText()
            StockYear = self.txtStockYear.toPlainText()
            if StockYear == "" and StockHolding == "" and StockDisposit == "":
                    msg.setText("กรุณาป้อนหุ้นออมต่อปีและจำนวนหุ้นที่ต้องการเพิ่มปีละกี่บาท")
                    msg.exec_()
            elif StockYear == "" or StockDisposit == "":
                    msg.setText("กรุณาป้อนหุ้นออมต่อปีและจำนวนหุ้นที่ต้องการเพิ่มปีละกี่บาท")
                    msg.exec_()
            elif StockDisposit != "" and StockYear != "" and StockHolding != "":
                    month = 12
                    row = 0
                    num = 1
                    sum = 0
                    dv_list = self.Calc(str(StockName), float(StockHolding), float(StockDisposit), int(StockYear))
                    self.tableWidget.setRowCount(int(StockYear))
                    self.tableWidget.setColumnCount(5)
                    for n in dv_list:
                            sum += n;
                    self.label_11.setText("{:,.2f}".format(sum))
                    for i in range(int(StockYear)):
                            self.tableWidget.setRowCount(int(StockYear))
                            self.tableWidget.setColumnCount(5)
                            header1 = QtWidgets.QTableWidgetItem("ปีที่")
                            header2 = QtWidgets.QTableWidgetItem("ส่งหุ้นต่อเดือน")
                            header3 = QtWidgets.QTableWidgetItem("หุ้นสะสมในปี")
                            header4 = QtWidgets.QTableWidgetItem("เงินปันผล")
                            header5 = QtWidgets.QTableWidgetItem("หุ้นสะสมรวม")

                            self.tableWidget.setHorizontalHeaderItem(0, header1)
                            self.tableWidget.setHorizontalHeaderItem(1, header2)
                            self.tableWidget.setHorizontalHeaderItem(2, header3)
                            self.tableWidget.setHorizontalHeaderItem(3, header4)
                            self.tableWidget.setHorizontalHeaderItem(4, header5)
                            self.tableWidget.setItem(row, 0, QTableWidgetItem("{}".format(num)))
                            self.tableWidget.setItem(row, 1, QTableWidgetItem("{:,.2f}".format(float(StockDisposit))))
                            self.tableWidget.setItem(row, 2,
                                                     QTableWidgetItem("{:,.2f}".format(float(StockDisposit) * month)))
                            holding_collect = float(StockDisposit) * month
                            self.tableWidget.setItem(row, 3, QTableWidgetItem("{:,.2f}".format(dv_list[i])))
                            self.tableWidget.setItem(row, 4, QTableWidgetItem(
                                    "{:,.2f}".format((holding_collect + (i * month * float(StockDisposit))))))
                            # print(sum)
                            holding_collect *= month
                            num += 1
                            row += 1

            elif StockDisposit != "" and StockYear != "":
                    self.tableWidget.setRowCount(int(StockYear))
                    self.tableWidget.setColumnCount(5)
                    header1 = QtWidgets.QTableWidgetItem("ปีที่")
                    header2 = QtWidgets.QTableWidgetItem("ส่งหุ้นต่อเดือน")
                    header3 = QtWidgets.QTableWidgetItem("หุ้นสะสมในปี")
                    header4 = QtWidgets.QTableWidgetItem("เงินปันผล")
                    header5 = QtWidgets.QTableWidgetItem("หุ้นสะสมรวม")

                    self.tableWidget.setHorizontalHeaderItem(0, header1)
                    self.tableWidget.setHorizontalHeaderItem(1, header2)
                    self.tableWidget.setHorizontalHeaderItem(2, header3)
                    self.tableWidget.setHorizontalHeaderItem(3, header4)
                    self.tableWidget.setHorizontalHeaderItem(4, header5)

                    StockHolding = 0
                    dv_list = self.Calc(str(StockName), float(StockHolding), float(StockDisposit), int(StockYear))
                    month = 12
                    row = 0
                    num = 1
                    sum = 0
                    for n in dv_list:
                            sum += n;
                    self.label_11.setText("{:,.2f}".format(sum))
                    for i in range(int(StockYear)):
                            self.tableWidget.setItem(row, 0, QTableWidgetItem("{}".format(num)))
                            self.tableWidget.setItem(row, 1, QTableWidgetItem("{:,.2f}".format(float(StockDisposit))))
                            self.tableWidget.setItem(row, 2,
                                                     QTableWidgetItem("{:,.2f}".format(float(StockDisposit) * month)))
                            holding_collect = float(StockDisposit) * month
                            self.tableWidget.setItem(row, 3, QTableWidgetItem("{:,.2f}".format(dv_list[i])))
                            self.tableWidget.setItem(row, 4, QTableWidgetItem(
                                    "{:,.2f}".format((holding_collect + (i * month * float(StockDisposit))))))
                            holding_collect *= month
                            num += 1
                            row += 1

    def Calc(self, name, holding, dp, year):
            sum = 0
            month = 12
            total_year = year
            disposit = holding
            disposit_month = dp
            dividend = self.get_divident(name)  # 9.0
            dv = dividend[0]
            total_disposit = disposit * (12 / 12) * (dv / 100)  # 60
            num = 12
            collect = 0
            dividend_all = 0
            devident_list = []
            for i in range(total_year, 0, -1):
                    if num > 0:
                            for n in range(month, 0, -1):
                                    sum += (disposit_month) * (num / 12) * (dv / 100)
                                    num = num - 1
                    total = sum + collect + total_disposit
                    collect = (disposit_month * month) * (dv / 100)
                    month = month + 12
                    dividend_all += total
                    devident_list.append(total)
                    # print(total)
            return devident_list

    def get_divident(self, name):
            stock_name = name
            dividend = []
            with pymongo.MongoClient(server) as conn:
                    db = conn.get_database("StockDividend")
                    where = {'stock_name': {'$eq': stock_name}}
                    cursor = db.sample_stock.find(where)
                    for i in cursor:
                            dividend.append(i['dividend'])
            return dividend

    def stock_pickup(self):
            mylist = []
            # stock_name = self.choStockName.currentText()
            with pymongo.MongoClient(server) as conn:
                    db = conn.get_database("StockDividend")
                    where = {}
                    cursor = db.sample_stock.find(where)
                    for i in cursor:
                            mylist.append([i['stock_name'], i['current_price'], i['dividend']])
            return mylist

    def MessageBox(self):
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            return msg

    def retranslateUi(self, StockCalc):
        _translate = QtCore.QCoreApplication.translate
        StockCalc.setWindowTitle(_translate("StockCalc", "Dialog"))
        self.label_3.setText(_translate("StockCalc", "ปัจจุบันมีหุ้นสะสม"))
        self.label_4.setText(_translate("StockCalc", "ชื่อหุ้นที่ต้องการสะสม"))
        self.btnSave.setText(_translate("StockCalc", "คำนวณ"))
        self.label_5.setText(_translate("StockCalc", "\n"
"คำนวณเงินออมจากการสะสมหุ้น"))
        self.pushButton_2.setText(_translate("StockCalc", "ล้างข้อมูล"))
        self.label_8.setText(_translate("StockCalc", "ออมเพิ่มปีละ"))
        self.label_9.setText(_translate("StockCalc", "ระยะเวลาออม/ปี"))
        self.label_6.setText(_translate("StockCalc", "(จำนวนหุ้นที่ถืออยู่ ณ ปัจจุบัน)"))
        self.btnLogout.setText(_translate("StockCalc", "ย้อนกลับ"))
        self.label_10.setText(_translate("StockCalc", "ปันผลสะสม ="))
        self.label_11.setText(_translate("StockCalc", "ปันผลสะสม"))
        self.btnExport.setText(_translate("StockCalc", "EXPORT TO CSV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StockCalc = QtWidgets.QDialog()
    ui = Ui_StockCalc()
    ui.setupUi(StockCalc)
    StockCalc.show()
    sys.exit(app.exec_())

