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
    def __init__(self, text = "", parent=None):
        super().__init__(parent)
        # Create layout
        layout = QVBoxLayout()

        # Create "Open file" button with icon below text
        open_file_button = QWidget()
        open_file_layout = QVBoxLayout()

        open_file_text = QLabel(text)
        open_file_layout.addWidget(open_file_text)

        open_file_icon = QLabel()
        icon_path = QDir.current().filePath("Icons/icons8-plus-24.png")
        open_file_icon.setPixmap(QPixmap(icon_path))
        open_file_icon.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        open_file_layout.addWidget(open_file_icon)

        open_file_button.setLayout(open_file_layout)
        layout.addWidget(open_file_button)

        # Set layout
        self.setLayout(layout)
        self.setFixedSize(300, 100)
