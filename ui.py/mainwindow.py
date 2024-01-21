from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1320, 900)
        self.setWindowTitle("Main Window 1")
        self.setStyleSheet('background-color:#000000')

        # Create a new frame
        self.side_frame = QWidget(self)
        self.side_frame.setGeometry(1000, 20, 300, 865)  # Adjust the position and size as needed
        self.side_frame.setStyleSheet('background-color:#19222A;  border-radius: 50px;')

        # Create a vertical layout for the frame
        layout = QVBoxLayout(self.side_frame)
        layout.setSpacing(40)  # Set vertical spacing between buttons to 0

        # Add some empty space at the top
        layout.addSpacing(40)

        # Add five push buttons to the layout
        for _ in range(5):
            button = QPushButton(self.side_frame)
            button.setStyleSheet("background-color: #F8C40D; color: white; font-size: 16px; font-weight: bold ; border: 1px solid #F8C40D; padding: 5px; border-radius: 5px;")
            button.setFixedSize(70, 40)  # Set fixed size for each button
            layout.addWidget(button)

        # Adjust spacing between buttons and frame
        layout.addStretch()

        # Add another push button at the bottom
        bottom_button = QPushButton(self.side_frame)
        bottom_button.setStyleSheet("background-color: #F8C40D; color: white; font-size: 16px; font-weight: bold ; border: 1px solid #F8C40D; padding: 5px; border-radius: 5px;")
        bottom_button.setFixedSize(70, 40)
        layout.addWidget(bottom_button)

        # Add some empty space at the bottom
        layout.addSpacing(40)

        
       # Load the icon image
        icon_path = "D:/slidel/slidel/download.png"  # Replace with the actual path to your icon image
        icon = QPixmap(icon_path)

        # Add a label to the top-left corner of the main window
        label = QLabel(self)
        label.setGeometry(60, 50, 200, 60)
        label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label.setStyleSheet("color: white; font-size: 20px; font-weight: bold ; border: 1px solid #F8C40D; padding: 2px;")
        label.setText(f'<img src="{icon.toImage()}" width="30" height="30"> Eren Jaeger')

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
