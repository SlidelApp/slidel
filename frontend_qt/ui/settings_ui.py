from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PySide6.QtGui import QFont
import os

class SettingsUI(QWidget):
    def __init__(self):
        super(SettingsUI, self).__init__()

        self.displayed_name = "John Doe"
        self.username = "johndoe"
        self.password = "pass1234"

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Settings")
        self.setGeometry(100, 100, 400, 300)

        heading_label = QLabel("My Profile")
        heading_label.setFont(QFont("Arial", 18, QFont.Bold))

        displayed_name_label = QLabel("Display Name")
        self.displayed_name_edit = QLineEdit(self.displayed_name)
        edit_displayed_name_button = QPushButton("Edit")
        edit_displayed_name_button.clicked.connect(self.toggle_displayed_name_edit_mode)

        username_label = QLabel("Username")
        self.username_edit = QLineEdit(self.username)
        edit_username_button = QPushButton("Edit")
        edit_username_button.clicked.connect(self.toggle_username_edit_mode)

        password_label = QLabel("Password")
        self.password_edit = QLineEdit(self.password)
        self.password_edit.setEchoMode(QLineEdit.Password) 
        edit_password_button = QPushButton("Edit")
        edit_password_button.clicked.connect(self.toggle_password_edit_mode)

        home_button = QPushButton("Home")
        home_button.clicked.connect(self.go_to_home_page)

        delete_button = QPushButton("Delete Account")
        delete_button.clicked.connect(self.delete_account)

        layout = QVBoxLayout()

        layout.addWidget(heading_label)

        layout.addWidget(displayed_name_label)
        layout.addWidget(self.displayed_name_edit)
        layout.addWidget(edit_displayed_name_button)

        layout.addWidget(username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(edit_username_button)

        layout.addWidget(password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(edit_password_button)

        layout.addWidget(home_button)
        layout.addWidget(delete_button)

        self.setLayout(layout)

        self.load_styles()

    def load_styles(self):
        style_file = os.path.join(os.path.dirname(__file__), 'styles.qss')
        try:
            with open(style_file, "r") as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error: Could not find the style sheet file: {style_file}")

    def toggle_displayed_name_edit_mode(self):
        if self.displayed_name_edit.isEnabled():
            self.displayed_name = self.displayed_name_edit.text()
        self.displayed_name_edit.setEnabled(not self.displayed_name_edit.isEnabled())

    def toggle_username_edit_mode(self):
        if self.username_edit.isEnabled():
            self.username = self.username_edit.text()
        self.username_edit.setEnabled(not self.username_edit.isEnabled())

    def toggle_password_edit_mode(self):
        if self.password_edit.isEnabled():
            self.password = self.password_edit.text()
        self.password_edit.setEnabled(not self.password_edit.isEnabled())

    def go_to_home_page(self):
        print("Going to Home Page")  

    def delete_account(self):
        result = QMessageBox.question(self, "Confirmation", "Are you sure you want to delete your account?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            print("Account Deleted") 
        else:
            QMessageBox.information(self, "Deletion Cancelled", "Your account has not been deleted.")
