import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QMessageBox,QPushButton, QComboBox, QCheckBox, QGridLayout, QLineEdit 
from PyQt6.QtCore import Qt
class Calculator (QWidget): 
    def __init__(self): 
        super().__init__() 
        grid = QGridLayout() 
        self.setLayout(grid)
        text = QLineEdit()
        text.setAlignment (Qt.AlignmentFlag.AlignRight) 
        text.setStyleSheet ("background-color: yellow") 
        grid.addWidget(text, 0, 0, 1, 4) 
        font = text.font()
        font.setPointSize(20) 
        text.setFont(font)

        names=['7','8','9','/',
               '4','5','6','*',
               '1','2','3','-',
               '0','.','=','+']
        positions = [(i, j) for i in range(1,6) for j in range(4)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
            self.move(300,150)
            self.setWindowTitle("Calculator")


if __name__=="__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    app.exec()