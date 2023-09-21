import sys
from PyQt6.QtWidgets import QApplication, QFileDialog, QColorDialog, QFontDialog
import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from lab10.prob4 import FileDialog

class CalculatorDialogs(FileDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator Dialogs")
        self._addConfigMenu()  # Add the Config menu actions

    def _addConfigMenu(self):
        super()._addConfigMenu()  # Call the parent class method to add existing actions
        self.colorAction.triggered.connect(self._handleColor)
        self.sizeAction.triggered.connect(self._handleSize)

    def _handleColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.result_edit.setStyleSheet(f"background-color: {color.name()};")

    def _handleSize(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.result_edit.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorDialogs()
    window.show()
    sys.exit(app.exec())

