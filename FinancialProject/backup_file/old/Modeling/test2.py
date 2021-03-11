from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget,QLineEdit

import pandas_datareader as web
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from pandas_datareader._utils import RemoteDataError
# main window
# which inherits QDialog
import sys
class Window(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.textbox = QLineEdit(self)
        self.textbox.move(300, 10)
        self.textbox.resize(200, 20)

        # Just some button connected to 'plot' method
        self.button = QPushButton('Plot')

        # adding action to the button
        self.button.clicked.connect(self.plot)

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

        # action called by thte push button

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

    # driver code

if __name__ == '__main__':
    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = Window()

    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())