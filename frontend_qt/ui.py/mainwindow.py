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
            "frontend_qt\icons\zoomin.png",
            "frontend_qt\icons\zoomout.png",
            "frontend_qt\icons\eraser.png",
            "frontend_qt\icons\pre.png",
            "frontend_qt\icons\slidenext.png",
            "frontend_qt\icons\exit.png"
        ]


        # Add push buttons to the layout with icons
        for i, icon_path in enumerate(icon_paths[:5]):  # Loop through the first 5 icons
            button = QPushButton(self.side_frame)
            button.setStyleSheet("background-color: #F8C40D; color: white; font-size: 16px; font-weight: bold ; border: 1px solid #F8C40D; padding: 5px; border-radius: 5px;")
            button.setFixedSize(70, 40)  # Set fixed size for each button
            button.setIcon(QIcon(icon_path))
            button.setIconSize(QSize(30, 30))
            layout.addWidget(button)
            # Change cursor to a pointer when hovering over the button
            button.setCursor(Qt.PointingHandCursor)

            # Assign actions to each button
            if i == 0:
                button.clicked.connect(self.zoom_in_action)
            elif i == 1:
                button.clicked.connect(self.zoom_out_action)
            elif i == 2:
                button.clicked.connect(self.eraser_action)
            elif i == 3:
                button.clicked.connect(self.previous_slide_action)
            elif i == 4:
                button.clicked.connect(self.next_slide_action)
            
        # Load the image
        image_path = "frontend_qt\icons\slidemodel-presentations.png"  
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
        icon_path = "frontend_qt/icons/user.png"  # Replace with the actual path to your icon image
        icon = QPixmap(icon_path)

        # Add a label to the top-left corner of the main window
        label = QLabel(self)
        label.setGeometry(60, 50, 200, 60)
        label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label.setStyleSheet("color: white; font-size: 20px; font-weight: bold ; border: 1px solid #F8C40D; padding: 2px;")
        label.setText(f'<img src="{icon.toImage()}" width="30" height="30"> Eren Jaeger')

    def zoom_in_action(self):
                # Define the action to be performed when the zoom in button is clicked
                print("Zoom In Action")

    def zoom_out_action(self):
        # Define the action to be performed when the zoom out button is clicked
        print("Zoom Out Action")

    def eraser_action(self):
        # Define the action to be performed when the eraser button is clicked
        print("Eraser Action")

    def previous_slide_action(self):
        # Define the action to be performed when the previous slide button is clicked
        print("Previous Slide Action")

    def next_slide_action(self):
        # Define the action to be performed when the next slide button is clicked
        print("Next Slide Action")      

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
