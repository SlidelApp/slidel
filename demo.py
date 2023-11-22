
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fullscreen Demo")
        self.setGeometry(100, 100, 400, 300)

        self.enter_fullscreen_button = QPushButton("Enter Fullscreen", self)
        self.enter_fullscreen_button.clicked.connect(self.enter_fullscreen)
        self.enter_fullscreen_button.setGeometry(100, 100, 200, 50)

        self.exit_fullscreen_button = QPushButton("Exit Fullscreen", self)
        self.exit_fullscreen_button.clicked.connect(self.exit_fullscreen)
        self.exit_fullscreen_button.setGeometry(100, 200, 200, 50)
        self.exit_fullscreen_button.setEnabled(False)

    def enter_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
            self.enter_fullscreen_button.setText("Enter Fullscreen")
        else:
            self.showFullScreen()
            self.enter_fullscreen_button.setText("Maximize")
        self.enter_fullscreen_button.setEnabled(True)
        self.exit_fullscreen_button.setEnabled(True)

    def exit_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
            self.enter_fullscreen_button.setText("Enter Fullscreen")
        else:
            self.showMaximized()
            self.enter_fullscreen_button.setText("Minimize")
        self.enter_fullscreen_button.setEnabled(True)
        self.exit_fullscreen_button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
