from Components.fileUploder import FileUploder
from Components.fileUploder import UploadButton
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QWidget,
    QLabel,
)


class FileSelectorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Selector")

        layout = QGridLayout()  # Set the layout directly on the main window

        layout.addWidget(QLabel("Last Used File"), 0, 0)
        layout.addWidget(UploadButton(), 1, 0)

        layout.addWidget(QLabel("Open File"), 0, 1)
        layout.addWidget(FileUploder(), 1, 1)

        layout.addWidget(QLabel("Blank Canvas"), 2, 0)
        layout.addWidget(UploadButton("Open Blank Canvas"), 3, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.showMaximized()
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication([])

    # Get the screen resolution
    screen_resolution = app.primaryScreen().geometry()

    # Create the FileSelectorWindow instance
    window = FileSelectorWindow()
    window.show()

    app.exec()
