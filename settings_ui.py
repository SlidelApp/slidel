from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PySide6.QtGui import QFont
import os

class SettingsUI(QWidget):
    def __init__(self):
        super(SettingsUI, self).__init__()

        self.displayed_name = "John Doe"
        self.username = "johndoe"
        self.password = "pass1234"

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("My Profile")
        self.setGeometry(100, 100, 400, 300)
