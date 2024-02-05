from PySide6.QtWidgets import QApplication


def load_stylesheet(filename):
    with open(filename, "r") as file:
        return file.read()



