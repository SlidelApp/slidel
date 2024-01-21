from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel,QVBoxLayout, QHBoxLayout
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


       # Load the icon image
        icon_path = "D:/slidel/slidel/download.png"  # Replace with the actual path to your icon image
        icon = QPixmap(icon_path)

        # Add a label to the top-left corner of the main window
        label = QLabel(self)
        label.setGeometry(60, 50, 200, 60)
        label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label.setStyleSheet("color: white; font-size: 20px; font-weight: bold ; border: 1px solid #F8C40D; padding: 2px;")
        label.setText(f'<img src="{icon.toImage()}" width="30" height="30"> Eren Jaeger')

        # Create a vertical layout for the frame
        layout = QVBoxLayout(self.side_frame)
        layout.setSpacing(40)  # Set vertical spacing between labels to 0

        # Add some empty space at the top
        layout.addSpacing(40)


        # Add five labels to the layout
        for _ in range(5):
            label = QLabel(self.side_frame)
            label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            label.setStyleSheet("background-color: #F8C40D; color: white; font-size: 16px; font-weight: bold ; border: 1px solid #F8C40D; padding: 5px; border-radius: 5px;")
            label.setFixedSize(70, 40)  # Set fixed size for each label
            layout.addWidget(label)

        # Adjust spacing between labels and frame
        layout.addStretch()

      

         # Add another label at the bottom
        bottom_label = QLabel(self.side_frame)
        bottom_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        bottom_label.setStyleSheet("background-color: #F8C40D; color: white; font-size: 16px; font-weight: bold ; border: 1px solid #F8C40D; padding: 5px; border-radius: 5px;")
        bottom_label.setFixedSize(70, 40)
        layout.addWidget(bottom_label)

          # Add some empty space at the bottom
        layout.addSpacing(40)
        




        


    


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
