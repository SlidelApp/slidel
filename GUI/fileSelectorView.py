from Components.fileUploder import FileUploder
from Components.fileUploder import UploadButton
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QWidget,
    QLabel,
    QPushButton
)


class FileSelectorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Selector")

        layout = QGridLayout()

        layout.addWidget(QPushButton(), 0, 1)

        layout.addWidget(QLabel("Last Used File"), 1, 0)
        layout.addWidget(UploadButton(), 2, 0)

        layout.addWidget(QLabel("Open File"), 1, 1)
        layout.addWidget(FileUploder(), 2, 1)

        layout.addWidget(QLabel("Blank Canvas"), 3, 0)
        layout.addWidget(UploadButton("Open Blank Canvas"), 4, 0)

        layout.addWidget(QLabel("Recent Files"), 3, 1)

        
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        


if __name__ == "__main__":
    app = QApplication([])

    # Get the screen resolution


    # Create the FileSelectorWindow instance
    window = FileSelectorWindow()
    window.setFixedSize(600,400)
    window.show()

    app.exec()
