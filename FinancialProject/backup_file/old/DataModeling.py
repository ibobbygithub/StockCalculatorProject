# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataModeling.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
import datetime
import pandas_datareader as web
from pandas_datareader._utils import RemoteDataError
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from Modeling import test3
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
class Ui_Dialog(QDialog):
    def setupUi(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(979, 564)
        self.txtStock = QtWidgets.QTextEdit(Dialog)
        self.txtStock.setGeometry(QtCore.QRect(800, 80, 141, 31))
        self.txtStock.setObjectName("txtStock")
        self.btnPredictionPage = QtWidgets.QPushButton(Dialog)
        self.btnPredictionPage.setGeometry(QtCore.QRect(800, 500, 141, 41))
        self.btnPredictionPage.setObjectName("btnPredictionPage")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(800, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(800, 130, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtStartYear = QtWidgets.QTextEdit(Dialog)
        self.txtStartYear.setGeometry(QtCore.QRect(800, 170, 141, 31))
        self.txtStartYear.setObjectName("txtStartYear")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(800, 150, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(800, 60, 131, 16))
        self.label_2.setObjectName("label_2")
        self.btnExportCSV = QtWidgets.QPushButton(Dialog)
        self.btnExportCSV.setGeometry(QtCore.QRect(800, 260, 141, 41))
        self.btnExportCSV.setObjectName("btnExportCSV")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(800, 200, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(800, 230, 151, 16))
        self.label_8.setObjectName("label_8")
        self.btnExportMongo = QtWidgets.QPushButton(Dialog)
        self.btnExportMongo.setGeometry(QtCore.QRect(800, 320, 141, 41))
        self.btnExportMongo.setObjectName("btnExportMongo")
        self.btnGraphPrice = QtWidgets.QPushButton(Dialog)
        self.btnGraphPrice.setGeometry(QtCore.QRect(800, 380, 141, 41))
        self.btnGraphPrice.setObjectName("btnGraphPrice")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 520, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnTableModelPrice = QtWidgets.QPushButton(Dialog)
        self.btnTableModelPrice.setGeometry(QtCore.QRect(800, 440, 141, 41))
        self.btnTableModelPrice.setObjectName("btnTableModelPrice")
        self.lblRealPrice = QtWidgets.QLabel(Dialog)
        self.lblRealPrice.setGeometry(QtCore.QRect(190, 510, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblRealPrice.setFont(font)
        self.lblRealPrice.setText("")
        self.lblRealPrice.setObjectName("lblRealPrice")

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        self.btnGraphPrice.clicked.connect(self.plot)
        # creating a Vertical Box layout
        layout = QVBoxLayout()

        # adding tool bar to the layout
        layout.addWidget(self.toolbar)

        # adding canvas to the layout
        layout.addWidget(self.canvas)

        # adding push button to the layout
        layout.addWidget(self.button)

        # setting layout to the main window
        self.setLayout(layout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # def showPrice(self):
    #     Dialog(self.txtStock.toPlainText())
    def plot(self):
        ticket = "bts"
        start_date = "2010-01-01"
        now = datetime.datetime.now()
        end_date = now.strftime("%Y-%m-%d")
        try:
            df = web.DataReader(ticket + '.bk', data_source='yahoo', start=start_date, end=end_date)
        except RemoteDataError:
            print('ชื่อหุ้นนี้ไม่มีอยู่ในระบบ')
        #self.ax.plot(df['Close'])
        #self.ax.set(xlabel='year', ylabel='Close Price Baht (฿) thai', title='Close Price History')
        # random data
        data = df['Close']

        # clearing old figure
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # plot data
        ax.plot(data)
        ax.set(xlabel='year', ylabel='Close Price Baht (฿) thai', title='Close Price History')
        # refresh canvas
        self.canvas.draw()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnPredictionPage.setText(_translate("Dialog", "Prediction Page"))
        self.label_3.setText(_translate("Dialog", "Input Stock Name"))
        self.label_6.setText(_translate("Dialog", "Start Year"))
        self.label.setText(_translate("Dialog", "eg. 2012, 2010, 2008"))
        self.label_2.setText(_translate("Dialog", "eg. AOT, BIS, MRT"))
        self.btnExportCSV.setText(_translate("Dialog", "Export to CSV"))
        self.label_4.setText(_translate("Dialog", "Export file"))
        self.label_8.setText(_translate("Dialog", "stock price from start date"))
        self.btnExportMongo.setText(_translate("Dialog", "Export to Mongo"))
        self.btnGraphPrice.setText(_translate("Dialog", "Graph Price"))
        self.label_5.setText(_translate("Dialog", "Real Price Value ="))
        self.btnTableModelPrice.setText(_translate("Dialog", "Table Model Price"))

class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # self.canvas = Canvas(self, width=8, height=4)
        # self.canvas.move(0, 0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #Dialog = QtWidgets.QDialog()
    ui = Dialog()
    #ui.setupUi(Dialog)
    ui.show()
    sys.exit(app.exec_())
