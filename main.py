#Import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QPushButton
from random import choice

#Main App and Settings
app = QApplication([])#create object of app which will execute app
main_window = QWidget()#crate main window object which is main window
main_window.setWindowTitle("App")#this is title of the app
main_window.resize(300,200)#this is size of app


#Create All App objects
title = QLabel("Random Word")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click Me")
button2 = QPushButton("Click Me")
button3 = QPushButton("Click Me")


#All Design here
#first create master layout in which layout is gonna go
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

#add widget to the row
row1.addWidget(title,alignment=Qt.AlignCenter)

row2.addWidget(text1,alignment=Qt.AlignCenter)
row2.addWidget(text2,alignment=Qt.AlignCenter)
row2.addWidget(text3,alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)


#add all layout to the master layout
master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

#add master layout to the main window
main_window.setLayout(master_layout)


words = ["this","is","random","word"]

#Functions
def randomWord1():
    word = choice(words)
    text1.setText(word)

def randomWord2():
    word = choice(words)
    text2.setText(word)

def randomWord3():
    word = choice(words)
    text3.setText(word)


#Events

#add event to the buttons
button1.clicked.connect(randomWord1)
button2.clicked.connect(randomWord2)
button3.clicked.connect(randomWord3)




#Show/Run our App
#creating window for the app
main_window.show()
#executing app
app.exec_()