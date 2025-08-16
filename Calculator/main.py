#Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLineEdit,QPushButton,QGridLayout

#Main App Objects and Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator")
main_window.resize(250,300)

#Create All App object
master_layout = QVBoxLayout()
grid = QGridLayout()

text_box = QLineEdit()
text_box.setAlignment(Qt.AlignRight)
text_box.setReadOnly(True)

delete_button = QPushButton("C")
clear_button = QPushButton("<")


#variables
buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","+","="
]

#Function 
def button_click():
    
    #get which button is clicked
    button = app.sender()

#All Design Here

row = 0
col = 0

for text in buttons:
    print("function ")
    button = QPushButton(text)
    #add event to the button 
    button.clicked.connect(button_click)

    #button to insert,Row,column
    grid.addWidget(button,row,col)

    col+=1
    #move to next row if column is last
    if col>3:
        col = 0
        row+=1
    


#create buttons
button_row = QHBoxLayout()
button_row.addWidget(delete_button)
button_row.addWidget(clear_button)

clear_button.clicked.connect(button_click)
delete_button.clicked.connect(button_click)

#add to master layout 
master_layout.addWidget(text_box)
master_layout.addLayout(button_row)
master_layout.addLayout(grid)


#set master layout in main layout
main_window.setLayout(master_layout)

#Events

#Show/Run our App
main_window.show()
app.exec_()