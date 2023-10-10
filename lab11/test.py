import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QPropertyAnimation, QParallelAnimationGroup, QPoint
import os
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QToolBar,QWidget, QGraphicsOpacityEffect
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from lab11.prob2 import ColorOfTheDayApp

class AnimationWindow(ColorOfTheDayApp):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Color of the Day with Animation')
        self._createMenuBar()
        self._createToolBars()
        self._setStatusBar()

    def _createMenuBar(self):
        menu_bar = self.menuBar()
        animation_menu = menu_bar.addMenu("Animation")

        size_action = QAction("Size", self)
        size_action.setShortcut(QtGui.QKeySequence("Ctrl+Shift+S"))
        size_action.triggered.connect(self.animate_size)
        animation_menu.addAction(size_action)

    def _createToolBars(self):
        toolbar = QToolBar(self)
        size_icon = QtGui.QIcon("icon-size.png")  
        size_action = QAction(size_icon, "Size", self)
        size_action.triggered.connect(self.animate_size)
        toolbar.addAction(size_action)
        self.addToolBar(toolbar)

    def _setStatusBar(self):
        status_bar = self.statusBar()
        status_bar.showMessage("Ready")

    def animate_size(self):
        self.statusBar().showMessage("Animate the size of the label")
        self.start_animation()

    def animate_size(self):
        self.statusBar().showMessage("Animate the size of the label")
        self.start_animation()

    def start_animation(self):
        self.statusBar().showMessage("Animate the size of the label")
        self.label = self.day_label

        animation_pos = QtCore.QPropertyAnimation(self.label, b"pos")
        animation_pos.setDuration(3000)
        animation_pos.setStartValue(QtCore.QPoint(10, 10))
        animation_pos.setEndValue(QtCore.QPoint(100, 20))

        animation_size = QtCore.QPropertyAnimation(self.label, b"size")
        animation_size.setDuration(3000)
        animation_size.setStartValue(QtCore.QSize(100, 30))
        animation_size.setEndValue(QtCore.QSize(150, 40))

        animation_group = QtCore.QParallelAnimationGroup()
        animation_group.addAnimation(animation_pos)
        animation_group.addAnimation(animation_size)

        animation_group.start()




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AnimationWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
