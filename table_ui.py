
# WARNING! All changes made in this file will be lost!
import sqlite3
import math
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form(object):
    def return_uploadcv(self):
        print("returnclick")
        
        
        

    def load_to_table(self):
        connection=sqlite3.connect('details.db')
        sad=connection.execute("SELECT count(*) FROM final")
        numberOfRows = sad.fetchone()[0]
        display=numberOfRows/10
        count=math.ceil(display)
        connection.close()
        self.increase=self.increase+1
        cou=count+1
        #print(self.row)
        if self.increase<cou:
            data=(self.increase*10)-10
            com=sqlite3.connect('details.db')   
            result=com.execute("SELECT * FROM final LIMIT ? OFFSET ?",(10,data))
            self.score_table.setRowCount(4)
            for row_number,row_data in enumerate(result):
                self.score_table.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.score_table.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
            com.close()
        #print(row_number+1)
        else:
        	print("can't go furth")
                
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1000, 600)
        
        self.label_2 = QtWidgets.QWidget(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 800, 171))
        self.label_2.setStyleSheet("background-image:url(images/image1.jpg)")
        self.label_2.setObjectName("label_2")
        
        
        
        self.score_table = QtWidgets.QTableWidget(Form)
        self.score_table.setEnabled(False)
        self.score_table.setGeometry(QtCore.QRect(100, 220, 800, 331))
        self.score_table.setBaseSize(QtCore.QSize(0, 0))
        self.score_table.setAutoScrollMargin(17)
        self.score_table.setIconSize(QtCore.QSize(0, 0))
        
        self.score_table.setRowCount(10)
        self.score_table.setColumnCount(4)
       
        self.score_table.setObjectName("score_table")
        item = QtWidgets.QTableWidgetItem()
        
        self.score_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setItem(1, 4, item)
        
        self.score_table.horizontalHeader().setVisible(False)
        self.score_table.horizontalHeader().setCascadingSectionResizes(False)
        self.score_table.horizontalHeader().setDefaultSectionSize(150)
        self.score_table.horizontalHeader().setHighlightSections(True)
        self.score_table.horizontalHeader().setMinimumSectionSize(40)
        self.score_table.horizontalHeader().setSortIndicatorShown(False)
        self.score_table.horizontalHeader().setStretchLastSection(True)
        self.score_table.verticalHeader().setVisible(False)
        self.score_table.verticalHeader().setDefaultSectionSize(30)
        self.score_table.verticalHeader().setHighlightSections(False)
        self.score_table.verticalHeader().setMinimumSectionSize(23)
        self.btn_return = QtWidgets.QPushButton(Form)
        self.btn_return.setGeometry(QtCore.QRect(260, 560, 75, 23))
        self.btn_return.setObjectName("btn_return")
        self.btn_return.clicked.connect(self.return_uploadcv)
    
        self.btn_Next = QtWidgets.QPushButton(Form)
        self.btn_Next.setGeometry(QtCore.QRect(560, 560, 75, 23))
        self.btn_Next.setObjectName("btn_Next")
        self.btn_Next.clicked.connect(self.load_to_table)
        self.increase=0
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(360, 160, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEnabled(False)
        self.tableWidget.setGeometry(QtCore.QRect(100, 180, 801, 41))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        
        
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.score_table.isSortingEnabled()
        self.score_table.setSortingEnabled(False)
        self.score_table.setSortingEnabled(__sortingEnabled)
        self.btn_return.setText(_translate("Form", "Return"))
        self.btn_Next.setText(_translate("Form", "Next"))
        self.label.setText(_translate("Form", "Detail info"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
       
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "Registration No."))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "Score"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Form", "Remarks"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

