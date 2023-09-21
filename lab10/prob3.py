import sys 
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction,QIcon,QKeySequence
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from lab10.prob2 import ActionConfiguration

class MessageBox(ActionConfiguration):
    def __init__(self):
        super (MessageBox, self).__init__()

        self.first_number_edit.returnPressed.connect(self.checkinput) 
        self.second_number_edit.returnPressed.connect(self.checkinput)

    def checkinput(self):
        if self.first_number_edit.text().isnumeric() == False:
            QMessageBox.warning(self,"","Plese enter the first number")
        elif self.second_number_edit.text().isnumeric() == False:
            QMessageBox.warning(self,"","Plese enter the second number")


if __name__== "__main__": 
    app = QApplication(sys.argv) 
    window = MessageBox()
    window.show()
    app.exec()