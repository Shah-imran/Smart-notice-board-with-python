# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pi_image.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(997, 837)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("background-color:  #4AAAA5;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.softwareName = QtWidgets.QLabel(self.centralwidget)
        self.softwareName.setGeometry(QtCore.QRect(260, 10, 471, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.softwareName.setFont(font)
        self.softwareName.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.softwareName.setStyleSheet("font: 48pt \"Times New Roman\";\n"
"color:  #0C3B40;\n"
"background-color: #4AAAA5;\n"
"")
        self.softwareName.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.softwareName.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.softwareName.setObjectName("softwareName")
        self.mainPage = QtWidgets.QTabWidget(self.centralwidget)
        self.mainPage.setEnabled(True)
        self.mainPage.setGeometry(QtCore.QRect(-10, 60, 1011, 781))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.mainPage.setFont(font)
        self.mainPage.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.mainPage.setToolTipDuration(-1)
        self.mainPage.setAutoFillBackground(False)
        self.mainPage.setStyleSheet("color:   #3A4055;\n"
"font: 75 18pt \"Times New Roman\";\n"
"background-color:  #4AAAA5;\n"
"")
        self.mainPage.setTabPosition(QtWidgets.QTabWidget.North)
        self.mainPage.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.mainPage.setIconSize(QtCore.QSize(40, 40))
        self.mainPage.setElideMode(QtCore.Qt.ElideNone)
        self.mainPage.setObjectName("mainPage")
        self.tab_control = QtWidgets.QWidget()
        self.tab_control.setObjectName("tab_control")
        self.post = QtWidgets.QTextBrowser(self.tab_control)
        self.post.setGeometry(QtCore.QRect(5, 1, 1001, 741))
        self.post.setStyleSheet(" background-color: #e1f5fe;")
        self.post.setObjectName("post")
        self.mainPage.addTab(self.tab_control, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 40, 201, 20))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(15, 180, 985, 491))
        self.tableWidget.setStyleSheet(" background-color: #e1f5fe;")
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(313)
        self.resultStatus = QtWidgets.QLabel(self.tab)
        self.resultStatus.setGeometry(QtCore.QRect(160, 690, 661, 31))
        self.resultStatus.setText("")
        self.resultStatus.setObjectName("resultStatus")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(240, 31, 741, 41))
        self.comboBox.setObjectName("comboBox")
        self.mainPage.addTab(self.tab, "")
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.mainPage.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ehut LTD."))
        self.softwareName.setText(_translate("MainWindow", "Notice Board"))
        self.mainPage.setTabText(self.mainPage.indexOf(self.tab_control), _translate("MainWindow", "Post"))
        self.label.setText(_translate("MainWindow", "Choose Course :"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Registration ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Grade/Mark"))
        self.mainPage.setTabText(self.mainPage.indexOf(self.tab), _translate("MainWindow", "Results"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
