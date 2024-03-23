import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame
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

        # Create a QFrame with a blue background
        frame = QFrame(self)
        frame.setStyleSheet("background-color: #2C3E50;")

        # Add a yellow border to the QFrame
        border_style = "2px solid #FBC400;"
        frame.setStyleSheet(f"{frame.styleSheet()} border: {border_style}")

        # Create a QVBoxLayout and set it for the QWidget
        layout = QVBoxLayout(self)
        layout.addWidget(frame)

        # Show the widget in full screen
        self.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec())
