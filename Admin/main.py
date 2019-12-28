from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
import os
# import var 
import threading
import db
import datetime

class MyGui(Ui_MainWindow, QtWidgets.QWidget):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(dialog)


class myMainClass():
    def __init__(self):
        GUI.submitResults.clicked.connect(self.resultsSubmit)
        GUI.postSubmit.clicked.connect(self.post)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.tableRow)
        self.timer.start(10)

        self.prev = 100
        GUI.postStatus.setAlignment(QtCore.Qt.AlignCenter)
        GUI.resultStatus.setAlignment(QtCore.Qt.AlignCenter)

    def post(self):
        post = GUI.post.toPlainText()
        if db.dbPost(post) == True:
            GUI.postStatus.setText("Successfully uploaded")
        else:
            GUI.postStatus.setText("Error Occurred")

    def resultsSubmit(self):
        courseName = GUI.courseName.text()
        courseCode = GUI.courseCode.text()
        threading.Thread(target=self.tableRead, daemon=True, args=[courseName, courseCode,]).start()

    def tableRead(self, courseName, courseCode):
        data = []
        temp = dict()
        timestamp = str(datetime.datetime.now())
        for i in range(GUI.tableWidget.rowCount()):
            print(i)
            temp['courseName'] = courseName
            temp['courseCode'] = courseCode
            temp['timestamp'] = timestamp
            temp['studentName'] = GUI.tableWidget.item(i, 0).text()
            temp['regNo'] = GUI.tableWidget.item(i, 1).text()
            temp['markGrade'] = GUI.tableWidget.item(i, 2).text()
            # print(temp)
            data.append(temp.copy())

        # print(data)

        if db.dbResult(data) == True:
            GUI.resultStatus.setText("Successfully uploaded")
        else:
            GUI.resultStatus.setText("Error Occurred")
            



    def tableRow(self):
        row = GUI.rowNumber.text()
        if self.prev != row and row.isnumeric() == True and row != '':
            self.prev = row
            GUI.tableWidget.setRowCount(int(row))

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