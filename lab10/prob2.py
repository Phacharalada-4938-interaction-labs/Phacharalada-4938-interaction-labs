import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QStatusBar
from PyQt6.QtGui import QIcon, QAction, QKeySequence
from PyQt6.QtCore import Qt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from lab10.prob1 import CalculatorApp

class ActionConfiguration(CalculatorApp):
    def __init__(self):
        super(ActionConfiguration, self).__init__()

        self.setWindowTitle("Calculator with Status and Shortcuts")

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Ready")

        self.open_action = QAction("Open", self)
        self.save_action = QAction("Save", self)
        self.clear_action = QAction("Clear", self)
        self.exit_action = QAction("Exit", self)

        self.open_action.setShortcut(QKeySequence("Ctrl+O"))
        self.save_action.setShortcut(QKeySequence("Ctrl+S"))
        self.clear_action.setShortcut(QKeySequence("Ctrl+R"))
        self.exit_action.setShortcut(QKeySequence("Ctrl+Q"))

        self.exit_action.triggered.connect(self.exit_app)

        self.open_action.setStatusTip("Open a file")
        self.save_action.setStatusTip("Save a file")
        self.clear_action.setStatusTip("Clear the result")
        self.exit_action.setStatusTip("Exit the application")

    def exit_app(self):
        QApplication.quit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ActionConfiguration() 
    window.show()
    sys.exit(app.exec())