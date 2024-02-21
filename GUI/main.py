from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QWidget,
    QFileDialog,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(676, 694)
        MainWindow.setStyleSheet("")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.UiMainIcon = QLabel(self.centralwidget)
        self.UiMainIcon.setObjectName("UiMainIcon")
        self.UiMainIcon.setGeometry(QRect(0, 10, 61, 41))
        self.UiMainIcon.setStyleSheet("image: url(GUI/smile.svg);")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(390, 20, 281, 51))
        self.widget.setStyleSheet(
            "border-radius:20px;\n" "background-color: rgb(246, 211, 45);"
        )

        def uploadFiles(self):
            fileDialog = QFileDialog()
            fileDialog.setFileMode(QFileDialog.ExistingFiles)
            if fileDialog.exec():
                fileNames = fileDialog.selectedFiles()

        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(60, 0, 201, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n" 'font: 700 18pt "Noto Sans";')

        self.accBtn = QPushButton(self.widget)
        self.accBtn.setObjectName("accBtn")
        self.accBtn.setGeometry(QRect(10, 0, 51, 43))
        self.accBtn.setStyleSheet("image: url(GUI/account.png);")

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(0, 50, 311, 61))
        self.label_2.setStyleSheet(
            'font: 700 23pt "Noto Sans";\n'
            "color: rgb(255, 255, 255);\n"
            "padding:10px;"
        )
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(0, 100, 311, 61))
        self.label_3.setStyleSheet(
            "color:rgb(255, 255, 255);\n"
            'font: 700 17pt "Noto Sans";\n'
            "padding:10px;"
        )
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(0, 340, 311, 61))
        self.label_4.setStyleSheet(
            'font: 700 17pt "Noto Sans";\n'
            "padding:10px;\n"
            "color: rgb(255, 255, 255);"
        )

        self.blankCanvasBtn = QPushButton(self.centralwidget)
        self.blankCanvasBtn.setObjectName("blankCanvasBtn")
        self.blankCanvasBtn.setGeometry(QRect(20, 390, 241, 201))
        self.blankCanvasBtn.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 15pt "Noto Sans";\n'
            "color:rgb(0, 0, 0);"
        )

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(390, 100, 311, 61))
        self.label_5.setStyleSheet(
            'font: 700 17pt "Noto Sans";\n'
            "padding:10px;\n"
            "color:rgb(255, 255, 255);"
        )

        self.openFileBtn = QPushButton(self.centralwidget)
        self.openFileBtn.setObjectName("openFileBtn")
        self.openFileBtn.setGeometry(QRect(410, 150, 241, 181))
        self.openFileBtn.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 15pt "Noto Sans";\n'
            "color:rgb(0, 0, 0);"
        )
        self.openFileBtn.clicked.connect(uploadFiles)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(390, 340, 311, 61))
        self.label_6.setStyleSheet(
            'font: 700 17pt "Noto Sans";\n'
            "padding:10px;\n"
            "color: rgb(255, 255, 255);"
        )
        self.lastUsedBtn = QPushButton(self.centralwidget)
        self.lastUsedBtn.setObjectName("lastUsedBtn")
        self.lastUsedBtn.setGeometry(QRect(20, 150, 241, 201))
        self.lastUsedBtn.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            'font: 700 15pt "Noto Sans";\n'
            "color:rgb(0, 0, 0);"
        )
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.UiMainIcon.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", "John Doe ", None))
        self.accBtn.setText("")
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "Your Files", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "Last Used File", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", "Blank Canvas", None)
        )
        self.blankCanvasBtn.setText(
            QCoreApplication.translate("MainWindow", "+ Use Blank Canvas", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", "Open File", None)
        )
        self.openFileBtn.setText(
            QCoreApplication.translate("MainWindow", "+ Use Blank Canvas", None)
        )
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", "Recent Files", None)
        )
        self.lastUsedBtn.setText("")

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
