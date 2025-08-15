#Import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget


#Main App and Settings
app = QApplication([])#create object of app which will execute app
main_window = QWidget()#crate main window object which is main window
main_window.setWindowTitle("App")#this is title of the app
main_window.resize(300,200)#this is size of app


#Create All App objects


#All Design here


#Events


#Show/Run our App
main_window.show()
app.exec_()