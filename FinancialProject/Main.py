
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymongo
from home import Home
import dns
import sys
from mainStockData import Ui_mainStockData
server = "mongodb+srv://iBobby:1234@cluster0.1npcu.mongodb.net/<dbname>?retryWrites=true&w=majority"

class Register(QtWidgets.QDialog, Ui_mainStockData):
    def __init__(self, parent=None):
        super(Register, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    StockData = Ui_mainStockData()
    sys.exit(app.exec_())