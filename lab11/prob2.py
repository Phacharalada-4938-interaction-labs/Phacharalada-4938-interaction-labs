import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

class ColorOfTheDayApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color of the Day")
        self.setGeometry(200, 200, 400, 450)  

        self.day_label = QtWidgets.QLabel(self)
        self.day_label.setFont(QtGui.QFont("", 40))
        self.day_label.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.day_label.setStyleSheet("color: black; background-color: white;")  

        self.color_buttons = []
        color_names = ["#E8ABB5", "#FCF6BD", "#FADCDC", "#D0F4DE", "#FFE2D1", "#E1FEFE", "#E7DCFC"]
        for color_name in color_names:
            button = QtWidgets.QPushButton(self)
            button.setStyleSheet(f"background-color: {color_name.lower()}")
            button.clicked.connect(self.show_day)
            button.setMaximumSize(24, 24)
            self.color_buttons.append((color_name, button))

        self.canvas = QtGui.QPixmap(400, 400) 
        self.canvas.fill(QtGui.QColor(Qt.GlobalColor.white))
        self.circle_size = QtCore.QSize(100, 100)
        self.circle_position = QtCore.QPoint(
            round((self.canvas.width() - self.circle_size.width()) / 2),
            round((self.canvas.height() - self.circle_size.height()) / 2)
        )

        self.show_layout()

    def show_layout(self):
        central_widget = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(central_widget)

        day_label_layout = QtWidgets.QHBoxLayout()
        day_label_layout.addWidget(self.day_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(day_label_layout)


        color_buttons_layout = QtWidgets.QHBoxLayout()
        for color_name, button in self.color_buttons:
            color_buttons_layout.addWidget(button)

        layout.addStretch()
        layout.addLayout(color_buttons_layout)
        self.setCentralWidget(central_widget)

    def show_day(self):
        sender = self.sender()
        color_name = next(name for name, button in self.color_buttons if button is sender)
        day = self.get_day_from_color_name(color_name)
        self.day_label.setText(day)
        self.day_label.setStyleSheet(f"color: black; background-color: {color_name.lower()};") 
        self.draw_circle(sender)

    def get_day_from_color_name(self, color_name):
        color_day_map = {
            "#E8ABB5": "Sunday",
            "#FCF6BD": "Monday",
            "#FADCDC": "Tuesday",
            "#D0F4DE": "Wednesday",
            "#FFE2D1": "Thursday",
            "#E1FEFE": "Friday",
            "#E7DCFC": "Saturday"
        }
        return color_day_map.get(color_name, "")

    def draw_circle(self, button):
        color_name, _ = next(item for item in self.color_buttons if item[1] == button)
        color = QtGui.QColor(color_name.lower())
        painter = QtGui.QPainter(self.canvas)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.setBrush(QtGui.QBrush(color))

        self.circle_position = QtCore.QPoint(
            round((self.canvas.width() - self.circle_size.width()) / 2),
            round((self.canvas.height() - self.circle_size.height()) / 2)
        )

        ellipse_rect = QtCore.QRect(
            self.circle_position,
            self.circle_size
        )

        painter.drawEllipse(ellipse_rect)
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.canvas)
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ColorOfTheDayApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()