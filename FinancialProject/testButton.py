# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testButton.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import plotGraph

class MainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 100, 161, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.showplot)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def showplot(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = plotGraph.MyPlot
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
