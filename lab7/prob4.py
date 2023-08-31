import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit
from PyQt6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(300, 150, 300, 400)

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.result_display = QLineEdit()
        self.result_display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.result_display.setStyleSheet("background-color: yellow")
        self.grid.addWidget(self.result_display, 0, 0, 1, 4)
        font = self.result_display.font()
        font.setPointSize(20)
        self.result_display.setFont(font)

        self.names = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        self.positions = [(i, j) for i in range(1, 5) for j in range(4)]

        self.buttons = []
        for position, name in zip(self.positions, self.names):
            button = QPushButton(name)
            self.buttons.append(button)
            self.grid.addWidget(button, *position)
            button.clicked.connect(lambda _, btn=button: self.handle_button_click(btn))

        self.current_input = ""
        self.result_shown = False  

    def handle_button_click(self, button):
        button_text = button.text()

        if button_text == "=":
            if self.current_input:
                try:
                    result = eval(self.current_input)
                    if result == 0:
                        self.result_display.setText('Eror')
                    else:
                        self.result_display.setText(str(result))
                    self.current_input = str(result)
                    self.result_shown = True
                except Exception as e:
                    self.result_display.setText("Error")
                    self.current_input = ""
        else:
            if self.result_shown:
                self.result_display.setText("") 
                self.result_shown = False
                self.current_input = "" 
            if button_text.isdigit() or button_text in ['+', '-', '*', '/']:
                self.current_input += button_text
                self.result_display.setText(self.current_input)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
