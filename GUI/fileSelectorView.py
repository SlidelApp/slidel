from Components.fileUploder import FileUploder 


from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QFileDialog,
    QGridLayout,
    QWidget,
)


class FileSelectorWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.setWindowTitle("File Selector")
        self.resize(width, height)

        layout = QGridLayout()  # Set the layout directly on the main window

        # layout.addWidget(QPushButton("Red"), 0, 0)
        layout.addWidget(FileUploder(), 0, 1)
        # layout.addWidget(QPushButton("Fgh"), 1, 0)
        # layout.addWidget(QPushButton("Selfdfvect File"), 1, 1)
        # layout.addWidget(QPushButton("Sele"), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication([])

    # Get the screen resolution
    screen_resolution = app.primaryScreen().size()

    # Create the FileSelectorWindow instance
    window = FileSelectorWindow(screen_resolution.width(), screen_resolution.height())
    window.show()

    app.exec()
