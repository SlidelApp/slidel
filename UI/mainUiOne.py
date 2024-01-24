from PySide6.QtWidgets import QApplication, QWidget
from launchConfig import MyWidget
import sys

# app = QApplication(sys.argv)
# window = QWidget()
# window.show()
# app.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())