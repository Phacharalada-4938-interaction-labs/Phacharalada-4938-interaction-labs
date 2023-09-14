import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel,QToolBar
from PyQt6.QtCore import Qt 
from PyQt6.QtGui import QAction

class MenuBarAction(QMainWindow):
    def __init__(self):
        super(MenuBarAction, self).__init__()  
        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(400, 200)
        
        self.label = QLabel("Hello!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        self._createMenuBar()
        self._createToolBars()
        self._addMenus()

    def _createMenuBar(self):
        self.menuBar = self.menuBar()
        self.menuBar.setNativeMenuBar(False)
        self.fileMenu = self.menuBar.addMenu("File")
        self.editMenu = self.menuBar.addMenu("Edit")
        self.helpMenu = self.menuBar.addMenu("Help")

    def _createToolBars(self):
        self.fileToolBar = self.addToolBar("File")
        self.editToolBar = QToolBar("Edit", self)
        self.addToolBar(self.editToolBar)
        helpToolBar = QToolBar("Help", self)
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, helpToolBar)

    def _addMenus(self):
        self._addFileMenu()
        self._addEditMenu()
        self._addHelpMenu()
        
    def _addFileMenu(self):
        self.openAction = QAction("Open", self)
        self.saveAction = QAction("Save", self)
        self.exitAction = QAction("Exit", self)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.exitAction)
        
    def _addEditMenu(self):
        self.copyAction = QAction("Copy", self)
        self.pasteAction = QAction("Paste", self)
        self.cutAction = QAction("Cut", self)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addAction(self.cutAction)
        
    def _addHelpMenu(self):
        self.aboutAction = QAction("About", self)
        self.helpMenu.addAction(self.aboutAction)
        
     
app = QApplication(sys.argv)
window = MenuBarAction() 
window.show()
app.exec()