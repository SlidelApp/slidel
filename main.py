from PySide6.QtWidgets import QApplication
from ui.settings_ui import SettingsUI

if __name__ == "__main__":
    app = QApplication([])
    window = SettingsUI()
    window.show()
    app.exec()
