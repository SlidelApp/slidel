import fileSelectorLayout as fsw
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

app = QApplication([])
screen_resolution = app.primaryScreen().size()


window = fsw.FileSelectorWindow(screen_resolution.width(), screen_resolution.height())
window.show()
app.exec()


        

    

    
