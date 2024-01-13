from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


class FileSelectorWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.setWindowTitle("File Selector")
        self.resize(width, height)

        self.show()
