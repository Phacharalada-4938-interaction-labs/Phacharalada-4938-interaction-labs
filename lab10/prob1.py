import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction,QIcon
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from lab8.prob2 import MainWindowMenus

class CalculatorApp(MainWindowMenus):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator with Menus and Toolbar")
        self._createActions()
        self._createTooBars()

    def _createActions(self):
        path = os.path.dirname(__file__)
        os.chdir(path)
        self.openAction.setIcon(QIcon("file-open.svg"))
        self.saveAction.setIcon(QIcon("file-save.png"))
        self.clearAction.setIcon(QIcon("edit-clear.png"))
        self.cutAction.setIcon(QIcon("edit-cut.png"))

    def _createTooBars(self):
        fileToolBar = self.addToolBar('File')
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        fileToolBar.addAction(self.clearAction)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())