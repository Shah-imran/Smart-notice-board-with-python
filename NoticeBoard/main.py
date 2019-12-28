from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QTableWidget, QTableWidgetItem
import sys
import os
import var 
import threading
import time
import db


class MyGui(Ui_MainWindow, QtWidgets.QWidget):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(dialog)


class myMainClass():
    def __init__(self):

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.monitor)
        self.timer.start(1000)
        GUI.comboBox.currentIndexChanged.connect(self.getResult)

        # self.timer1 = QtCore.QTimer()
        # self.timer1.timeout.connect(self.updateList)
        # self.timer1.start(5000)
        threading.Thread(target=self.updateList, daemon=True).start()
        threading.Thread(target=self.post, daemon=True).start()

    def getResult(self):
        course = GUI.comboBox.currentText()
        data = course.split(" - ")
        # print(data)
        data = db.getResults(data)
        print(data)
        print("data here")
        print(len(data))
        GUI.tableWidget.setRowCount(len(data))
        for i in range(GUI.tableWidget.rowCount()):
            GUI.tableWidget.setItem(i,0, QTableWidgetItem(data[i][0]))
            GUI.tableWidget.setItem(i,1, QTableWidgetItem(data[i][1]))
            GUI.tableWidget.setItem(i,2, QTableWidgetItem(data[i][2]))

        print("get result")

    def updateList(self):
        while True:
            GUI.comboBox.clear()
            time.sleep(2)
            GUI.comboBox.addItems(var.courseList)
            # GUI.comboBox.setItems(var.courseList)
            time.sleep(8)

    def post(self):
        while True:
            db.dbPost()
            db.getList()
            time.sleep(5)

    def monitor(self):
        cursor = GUI.post.textCursor()
            
        while not var.postQ.empty():
            data = var.postQ.get()
                # cursor.insertHtml('''<p><span style="color: #D60000; font-size: 30px;">{} </span><br>'''.format("started"))
                # cursor.insertHtml('''<p><span style="color: #0C5E3E; font-size: 30px;">{} </span>'''.format("started"))
            print(data)
                # for i in data:
                #     # cursor.insertHtml(data)
                #     # print(i[1])
                #     # print(i[0])
            cursor.insertHtml('''<p><span style="color: #D60000; font-size: 30px;">{} </span><br>'''.format(data))


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    try:
        def resource_path(relative_path):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)

        p = resource_path('favicon.ico')
        dialog.setWindowIcon(QtGui.QIcon(p))
    except Exception as e:
        print(e)
        pass

    dialog.setWindowFlags(dialog.windowFlags() |
                          QtCore.Qt.WindowMinimizeButtonHint |
                          QtCore.Qt.WindowSystemMenuHint)
    dialog.setWindowFlags(dialog.windowFlags() |
                          QtCore.Qt.WindowSystemMenuHint |
                          QtCore.Qt.WindowMinMaxButtonsHint)

    GUI = MyGui(dialog)
    dialog.show()

    myMC = myMainClass()

    app.exec_()
    print("Exit")
    sys.exit()