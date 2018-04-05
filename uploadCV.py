# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'uploadCV.ui'
# Created by: PyQt5 UI code generator 5.10.1
# WARNING! All changes made in this file will be lost!
from table_ui import Ui_Form 
from keywordchecking import Check_keyword
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
import string
import docx2txt
import sqlite3
from PyQt5.QtWidgets import QMessageBox
from nltk.tokenize import sent_tokenize 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
class Ui_CvWindow(object):
    def error_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Enter valid input")
        msg.setInformativeText("Details to follow")
        msg.setWindowTitle("Warning")
        msg.setDetailedText("open cv file(*.docx) from choose file only after filling form")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #msg.buttonClicked.connect(self.openwindow)
        retval = msg.exec_()
        print ("value of pressed message box button:", retval)
    
    def store_database(self):
        Name=self.line_job.text()
        degination=self.line_designation.text()
        salary=self.line_salary.text()
        self.registration=randint(0, 1564)
        connect=sqlite3.connect('details.db')
        connect.execute('''INSERT INTO CvScore(name,regno,designation, salary) VALUES(?,?,?,?)''', (Name,self.registration, degination, salary))
        connect.commit()
        #print(Name)
        #print(salary)
    
    
    def table_window(self):
        if self.line_job.text():
            print("upload is clicked")
            self.tablewindow=QtWidgets.QWidget()
            self.ui=Ui_Form()
            self.ui.setupUi(self.tablewindow)
            self.ui.load_to_table()
            self.tablewindow.show()
        #MainWindow.hide()
       
    
    def SingleBrowse(self):
        if self.line_job.text():
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Document Files (*.docx);;Text files(*.txt)", options=options)
            my_text = docx2txt.process(fileName)
            words = word_tokenize(my_text)
            words = [w.lower() for w in words]
    #words = my_text.split()
            self.store_database()
            sentence=sent_tokenize(my_text)
            sentence=[w.lower() for w in sentence]
            stop_words = stopwords.words('english')
            table = str.maketrans('', '', string.punctuation)
            stripped = [w.translate(table) for w in words]
            words = [word for word in stripped if word.isalpha()]
               #filter out stop word
            stop_words = set(stopwords.words('english'))
            words = [w for w in words if not w in stop_words]
        #sending value to another class keywordchecking
            self.keyobject=Check_keyword()
            self.keyobject.qualification_score(words)
            self.keyobject.expirence_score(my_text,self.line_job.text(),self.registration)
        else:
            self.error_msg()
       
                 
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 250, 191, 41))
        self.label.setObjectName("label")
        
        self.label_label = QtWidgets.QLabel(self.centralwidget)
        self.label_label.setGeometry(QtCore.QRect(110, 300, 191, 41))
        self.label_label.setObjectName("label_label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 80, 800, 171))
        self.label_2.setStyleSheet("background-image:url(images/image1.jpg)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        
        self.label_des = QtWidgets.QLabel(self.centralwidget)
        self.label_des.setGeometry(QtCore.QRect(110, 360, 191, 41))
        self.label_des.setObjectName("label_des")
        
        self.label_sal = QtWidgets.QLabel(self.centralwidget)
        self.label_sal.setGeometry(QtCore.QRect(110, 440, 191, 41))
        self.label_sal.setObjectName("label_sal")
        
        self.label_cv = QtWidgets.QLabel(self.centralwidget)
        self.label_cv.setGeometry(QtCore.QRect(110, 520, 191, 41))
        self.label_cv.setObjectName("label_cv")
        
        self.line_job = QtWidgets.QLineEdit(self.centralwidget)
        self.line_job.setGeometry(QtCore.QRect(300, 310, 531, 25))
        self.line_job.setObjectName("line_job")
        
        self.line_designation = QtWidgets.QLineEdit(self.centralwidget)
        self.line_designation.setGeometry(QtCore.QRect(300, 370, 531, 25))
        self.line_designation.setObjectName("line_designation")
        
        self.line_salary = QtWidgets.QLineEdit(self.centralwidget)
        self.line_salary.setGeometry(QtCore.QRect(300, 450, 531, 25))
        self.line_salary.setObjectName("line_salary")
        
        self.chosose_files = QtWidgets.QPushButton(self.centralwidget)
        self.chosose_files.setGeometry(QtCore.QRect(300, 520, 171, 34))
        self.chosose_files.setObjectName("chosose_files")
        self.chosose_files.clicked.connect(self.SingleBrowse)
        
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(500, 520, 112, 34))
        self.upload.setObjectName("upload")
        self.upload.clicked.connect(self.table_window)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Upload Prefered CV"))
        self.label_label.setText(_translate("MainWindow", "Name"))
        self.label_des.setText(_translate("MainWindow", "Designation"))
        self.label_sal.setText(_translate("MainWindow", "phone no"))
        self.label_cv.setText(_translate("MainWindow", "prefered CVs"))
        self.chosose_files.setText(_translate("MainWindow", "Choose Files"))
        self.upload.setText(_translate("MainWindow", "Analysis"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_CvWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

