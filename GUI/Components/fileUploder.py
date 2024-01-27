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
from Components.UploadButton import UploadButton

# Remove the unused import statement for Qt
# from PySide6.QtCore import Qt

class FileUploder(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("File Uploader")
        self.setFixedSize(300, 100)

        layout = QVBoxLayout()

        self.button = UploadButton("Open File (PDF)")
        self.button.clicked.connect(self.open_file_dialog)

        layout.addWidget(self.button)

        self.setLayout(layout)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select a file",
            "",
            "PDF Files (*.pdf);;All Files (*)",
            options=options,
        )

        if file_name:
            print(file_name)
