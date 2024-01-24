import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QGuiApplication

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set up your UI components here
        self.setWindowTitle("My Responsive UI")

        # Get the screen geometry
        screen_geometry = QGuiApplication.primaryScreen().geometry()

        # Set the window size to the screen size
        self.setGeometry(screen_geometry)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())

