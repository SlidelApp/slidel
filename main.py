from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QApplication
from ui.settings_ui import SettingsUI
from djangoapp.myapp.accounts.views import create_account  # Add this import

if __name__ == "__main__":
    app = QApplication([])
    window = SettingsUI(create_account)  
    window.show()
    app.exec()
