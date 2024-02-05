from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
)
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel, QSizePolicy
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize, Qt, QDir


# Remove the unused import statement for Qt
# from PySide6.QtCore import Qt


class UploadButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(parent)  
        open_file_layout = QVBoxLayout()

        open_file_text = QLabel(text)
        open_file_layout.addWidget(open_file_text)       

        # Set layout
        self.setLayout(open_file_layout)
        self.setFixedSize(300, 100)
