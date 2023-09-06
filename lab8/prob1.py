import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMenuBar, QMessageBox
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Calculator')

        # Create layout for the main window
        self.mainLayout = QVBoxLayout()

        # Create layout for input fields
        self.numbersLayout = QVBoxLayout()
        self._createNumbersLayout()

        # Create layout for buttons
        self.buttonsLayout = QVBoxLayout()
        self._createButtonsLayout()

        # Create layout for result display
        self.resultLayout = QVBoxLayout()
        self._createResultLayout()

        # Add layouts to the main layout
        self.mainLayout.addLayout(self.numbersLayout)
        self.mainLayout.addLayout(self.buttonsLayout)
        self.mainLayout.addLayout(self.resultLayout)

        # Create central widget and set the main layout
        self.container = QWidget()
        self.container.setLayout(self.mainLayout)
        self.setCentralWidget(self.container)

        # Create and set up the menu bar
        self._createMenuBar()

        # Connect button click events to corresponding functions
        self._handleEvents()

    def _createNumbersLayout(self):
        self.firstNumberLabel = QLabel("Enter the first number:")
        self.firstNumberEdit = QLineEdit()
        self.firstNumberEdit.setAlignment(Qt.AlignmentFlag.AlignRight)  # Right-align the input field

        self.secondNumberLabel = QLabel("Enter the second number:")
        self.secondNumberEdit = QLineEdit()
        self.secondNumberEdit.setAlignment(Qt.AlignmentFlag.AlignRight)  # Right-align the input field

        self.numbersLayout.addWidget(self.firstNumberLabel)
        self.numbersLayout.addWidget(self.firstNumberEdit)
        self.numbersLayout.addWidget(self.secondNumberLabel)
        self.numbersLayout.addWidget(self.secondNumberEdit)

    def _createButtonsLayout(self):
        self.addButton = QPushButton("+")
        self.subtractButton = QPushButton("-")
        self.multiplyButton = QPushButton("*")
        self.divideButton = QPushButton("/")

        self.buttonsLayout.addWidget(self.addButton)
        self.buttonsLayout.addWidget(self.subtractButton)
        self.buttonsLayout.addWidget(self.multiplyButton)
        self.buttonsLayout.addWidget(self.divideButton)

    def _createResultLayout(self):
        self.resultLabel = QLabel("Result:")
        self.resultTextEdit = QTextEdit()
        self.resultTextEdit.setReadOnly(True)
        self.resultTextEdit.setStyleSheet("background-color: lightgreen;")

        self.resultLayout.addWidget(self.resultLabel)
        self.resultLayout.addWidget(self.resultTextEdit)

    def _createMenuBar(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")
        config_menu = menubar.addMenu("Config")

    def _handleEvents(self):
        self.addButton.clicked.connect(self.addNumbers)
        self.subtractButton.clicked.connect(self.subtractNumbers)
        self.multiplyButton.clicked.connect(self.multiplyNumbers)
        self.divideButton.clicked.connect(self.divideNumbers)

    def addNumbers(self):
        try:
            num1 = float(self.firstNumberEdit.text())
            num2 = float(self.secondNumberEdit.text())
            result = num1 + num2
            self.resultTextEdit.setPlainText(str(result))
        except ValueError:
            self.showErrorMessageBox("Invalid input. Please enter valid numbers.")

    def subtractNumbers(self):
        try:
            num1 = float(self.firstNumberEdit.text())
            num2 = float(self.secondNumberEdit.text())
            result = num1 - num2
            self.resultTextEdit.setPlainText(str(result))
        except ValueError:
            self.showErrorMessageBox("Invalid input. Please enter valid numbers.")

    def multiplyNumbers(self):
        try:
            num1 = float(self.firstNumberEdit.text())
            num2 = float(self.secondNumberEdit.text())
            result = num1 * num2
            self.resultTextEdit.setPlainText(str(result))
        except ValueError:
            self.showErrorMessageBox("Invalid input. Please enter valid numbers.")

    def divideNumbers(self):
        try:
            num1 = float(self.firstNumberEdit.text())
            num2 = float(self.secondNumberEdit.text())
            if num2 == 0:
                self.showErrorMessageBox("Error: Division by zero")
            else:
                result = num1 / num2
                self.resultTextEdit.setPlainText(str(result))
        except ValueError:
            self.showErrorMessageBox("Invalid input. Please enter valid numbers.")

    def showErrorMessageBox(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.exec()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
