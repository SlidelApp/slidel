from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget, QFileDialog)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(676, 694)
        MainWindow.setStyleSheet(u"")

        def uploadFiles(self):
            fileDialog = QFileDialog()
            fileDialog.setFileMode(QFileDialog.ExistingFiles)
            if fileDialog.exec():
                fileNames = fileDialog.selectedFiles()

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.UiMainIcon = QLabel(self.centralwidget)
        self.UiMainIcon.setObjectName(u"UiMainIcon")
        self.UiMainIcon.setGeometry(QRect(0, 10, 61, 41))
        self.UiMainIcon.setStyleSheet("image: url(GUI/smile.svg);")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(380, 10, 281, 51))
        self.widget.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(246, 211, 45);")
        self.UiMainIcon_2 = QLabel(self.widget)
        self.UiMainIcon_2.setObjectName(u"UiMainIcon_2")
        self.UiMainIcon_2.setGeometry(QRect(0, 10, 61, 41))
        self.UiMainIcon_2.setStyleSheet(u"image: url(GUI/account.png);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 10, 211, 31))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 18pt \"Noto Sans\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 50, 311, 61))
        self.label_2.setStyleSheet(u"font: 700 23pt \"Noto Sans\";\n"
"color: rgb(255, 255, 255);\n"
"padding:10px;")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 150, 241, 181))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 100, 311, 61))
        self.label_3.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 700 17pt \"Noto Sans\";\n"
"padding:10px;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 340, 311, 61))
        self.label_4.setStyleSheet(u"font: 700 17pt \"Noto Sans\";\n"
"padding:10px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 390, 241, 201))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 15pt \"Noto Sans\";\n"
"color:rgb(0, 0, 0);")

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(390, 100, 311, 61))
        self.label_5.setStyleSheet(u"font: 700 17pt \"Noto Sans\";\n"
"padding:10px;\n"
"color:rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(410, 150, 241, 181))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 15pt \"Noto Sans\";\n"
"color:rgb(0, 0, 0);")
        self.pushButton_2.clicked.connect(uploadFiles)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(390, 340, 311, 61))
        self.label_6.setStyleSheet(u"font: 700 17pt \"Noto Sans\";\n"
"padding:10px;\n"
"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.UiMainIcon.setText("")
        self.UiMainIcon_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"John Doe ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Your Files", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Last Used File", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Blank Canvas", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"+ Use Blank Canvas", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"+ Open File", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Recent Files", None))
        # retranslateUi


if __name__ == "__main__":
    app = QApplication([])

    # Create the QMainWindow instance
    mainWindow = QMainWindow()
    
    # Create the Ui_MainWindow instance
    ui = Ui_MainWindow()
    
    # Setup the UI on the main window
    ui.setupUi(mainWindow)
    
    # Show the main window
    mainWindow.show()

    app.exec()
