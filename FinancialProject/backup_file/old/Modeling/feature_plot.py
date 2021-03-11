import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtWidgets
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from pandas_datareader._utils import RemoteDataError



class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=150)
        super().__init__(fig)
        self.setParent(parent)
        ticket = "bts"
        start_date = "2010-01-01"
        now = datetime.datetime.now()
        end_date = now.strftime("%Y-%m-%d")
        try:
            df = web.DataReader(ticket + '.bk', data_source='yahoo', start=start_date, end=end_date)
            self.ax.plot(df['Close'])
            self.ax.set(xlabel='year',ylabel='Close Price Baht (฿) thai',title='Close Price History')
            #fig.savefig("test.png")
            #self.ax.grid()
        except RemoteDataError:
            print('ชื่อหุ้นนี้ไม่มีอยู่ในระบบ')


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1290, 720)
        chart = Canvas(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())

