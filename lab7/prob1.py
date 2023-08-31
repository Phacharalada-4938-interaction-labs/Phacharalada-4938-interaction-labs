import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

class Name(QMainWindow):
    def __init__(self, *args, ** kwargd):
        super().__init__(*args, ** kwargd)

        button_layout=QHBoxLayout()
        main_layout=QVBoxLayout()

        firstname_layout=self.set_name_widget("First Name:")
        lastname_layout=self.set_name_widget("Last Name:")
        self.cancel_button=self.config_button(QPushButton("Cancel"), "red")
        self.submit_button=self.config_button(QPushButton("Submit"), "green")

        main_layout.addLayout(firstname_layout)
        main_layout.addLayout(lastname_layout)

        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.submit_button)
        main_layout.addLayout(button_layout)

        container=QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def set_name_widget(self, name_str):
        layout=QVBoxLayout()
        label=QLabel(name_str)
        font=label.font()
        font.setPointSize(20)
        label.setFont(font)
        line_edit=QLineEdit()
        line_edit.setFont(font)
        layout.addWidget(label)
        layout.addWidget(line_edit)
        return layout

    def config_button(self, button, color):
        button.setStyleSheet(f"color: {color};")
        return button

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Name()
    form.show()
    sys.exit(app.exec())