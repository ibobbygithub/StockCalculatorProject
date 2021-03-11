from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import datetime
import pandas_datareader as web
from pandas_datareader._utils import RemoteDataError

class Ui_Dialog:
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 500)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "output window"))


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        ticket = "bts"
        start_date = "2010-01-01"
        now = datetime.datetime.now()
        end_date = now.strftime("%Y-%m-%d")
        try:
            self.ax.set(xlabel='year', ylabel='Close Price Baht (฿) thai', title='Close Price History')
            # fig.savefig("test.png")
            # self.ax.grid()
        except RemoteDataError:
            print('ชื่อหุ้นนี้ไม่มีอยู่ในระบบ')
        df = web.DataReader(ticket + '.bk', data_source='yahoo', start=start_date, end=end_date)
        self.ax.plot(df['Close'])
        self.draw()



class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.canvas = Canvas(self, width=8, height=4)
        self.canvas.move(0, 0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Dialog()
    w.show()
    sys.exit(app.exec_())