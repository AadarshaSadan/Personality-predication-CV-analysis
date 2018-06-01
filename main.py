#from docreader import 
from  docreader import create_table
import sqlite3
from uploadCV import Ui_CvWindow  
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenu,QMenuBar,QAction,QStatusBar
from table_ui import Ui_Form 
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow():
    
    def pop_application(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("username password error")
        #msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Warning")
        #msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #msg.buttonClicked.connect(self.openwindow)
        retval = msg.exec_()
        print ("value of pressed message box button:", retval)
    
    
    def exit_Application(self):
        sys.exit()
    
    def table_windowss(self):
            print("dataview is clicked")
            self.tablewindow=QtWidgets.QWidget()
            self.ui=Ui_Form()
            self.ui.setupUi(self.tablewindow)
            self.ui.load_to_table()
            self.tablewindow.show()
    
    def logincheck(self):
        
        print("login button is clicke")
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_CvWindow()
        self.ui.setupUi(self.window)
        password=self.lineEdit_2.text()
        username=self.lineEdit.text()
        #connection=sqlite3.connect("details.db")
        #result=connection.execute("SELECT * FROM details WHERE username")
        if(username and password=='admin'):
            print("right")
            MainWindow.close()
            #MainWindow.hide()
            self.window.show()
        else:
            self.pop_application()
            
    
    
    def openwindow(self):
        self.ui.setupUi(self.window)
        self.window.show()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)    
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.u_name_label = QtWidgets.QLabel(self.centralwidget)
        self.u_name_label.setGeometry(QtCore.QRect(240, 260, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.u_name_label.setFont(font)
        self.u_name_label.setObjectName("u_name_label")
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(240, 350, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(430, 290, 161, 41))
        self.lineEdit.setObjectName("lineEdit")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 360, 161, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        ########################################LOgin button click#333
        self.pushButton.clicked.connect(self.logincheck)
        #########Button event#########################3333333
        self.pushButton.setGeometry(QtCore.QRect(400, 450, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
       
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 450, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(10) 
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 200, 161, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 80, 800, 171))
        self.label_2.setStyleSheet("background-image:url(images/image1.jpg)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        self.menuTool = QtWidgets.QMenu(self.menubar)
        self.menuTool.setObjectName("menuTool")
        
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        self.actionDataView = QtWidgets.QAction(MainWindow)
        self.actionDataView.setObjectName("actionDataView")
        self.actionDataView.triggered.connect(self.table_windowss)
        
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.exit_Application)
        
        self.actionTool = QtWidgets.QAction(MainWindow)
        self.actionTool.setObjectName("actionTool")
        
        self.actionInstruction = QtWidgets.QAction(MainWindow)
        self.actionInstruction.setObjectName("actionInstruction")
        self.actionInstruction.triggered.connect(self.pop_application)
        
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionDeletedata = QtWidgets.QAction(MainWindow)
        self.actionDeletedata.setObjectName("actionDeletedata")
        #self.actionDeletedata.triggered.connect(self.detetedatadata)
        
        self.menuFile.addAction(self.actionDataView)
        
        
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionInstruction)
        self.menuHelp.addAction(self.actionVersion)
        self.menuTool.addAction(self.actionDeletedata)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main"))
        self.u_name_label.setText(_translate("MainWindow", "User Name"))
        self.pass_label.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Sign up"))
        self.label.setText(_translate("MainWindow", "Admin login"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTool.setTitle(_translate("MainWindow", "Tool"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionDataView.setText(_translate("MainWindow", "DataView"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionInstruction.setText(_translate("MainWindow", "Instruction"))
        self.actionVersion.setText(_translate("MainWindow", "version"))
        self.actionDeletedata.setText(_translate("MainWindow", "Deletedata"))




if __name__ == '__main__':
    import sys
    create_table()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
    
    
