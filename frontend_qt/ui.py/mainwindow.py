from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize


import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1320, 900)
        self.setWindowTitle("Main Window 1")
        self.setStyleSheet('background-color:#000000')

        # Create a new frame
        self.side_frame = QWidget(self)
        self.side_frame.setGeometry(1150, 20, 100, 865)  # Adjust the position and size as needed
        self.side_frame.setStyleSheet('background-color:#19222A;  border-radius: 50px;')

        # Create a vertical layout for the frame
        layout = QVBoxLayout(self.side_frame)
        layout.setSpacing(40)  # Set vertical spacing between buttons to 0

        # Add some empty space at the top
        layout.addSpacing(40)

        # List of icon paths
        icon_paths = [
            "zoomin.png",
            "zoomout.png",
            "eraser.png",
            "pre.png",
            "nextslide.png",
            "exit.png"
        ]

        # Add push buttons to the layout with icons
        for i, icon_path in enumerate(icon_paths[:5]):  # Loop through the first 5 icons
            button = QPushButton(self.side_frame)
            button.setStyleSheet("background-color: #F8C40D; color: white; font-size: 16px; font-weight: bold ; border: 1px solid #F8C40D; padding: 5px; border-radius: 5px;")
            button.setFixedSize(70, 40)  # Set fixed size for each button
            button.setIcon(QIcon(icon_path))
            button.setIconSize(QSize(30, 30))
            layout.addWidget(button)

        # Load the image
        image_path = "slidemodel-presentations.png"  # Replace "image.jpg" with the actual path to your image file
        image = QPixmap(image_path)

        # Add a QLabel for the image
        image_label = QLabel(self)
        image_label.setGeometry(60, 115, 1050, 700)  # Adjust the position and size as needed
        image_label.setPixmap(image)


        # Adjust spacing between buttons and frame
        layout.addStretch()

        # Add another push button at the bottom (6th button)
        bottom_button = QPushButton(self.side_frame)
        bottom_button.setStyleSheet("background-color: #F8C40D; color: white; font-size: 16px; font-weight: bold ; border: 1px solid #F8C40D; padding: 5px; border-radius: 5px;")
        bottom_button.setFixedSize(70, 40)
        bottom_button.setIcon(QIcon(icon_paths[5]))  # Set icon for the bottom button
        bottom_button.setIconSize(QSize(30, 30))
        layout.addWidget(bottom_button)


        # Add some empty space at the bottom
        layout.addSpacing(40)

       # Load the icon image for the label
        icon_path = "download.png"  # Replace with the actual path to your icon image
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
