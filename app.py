import sys
from PyQt5.QtWidgets import QApplication
from contact_app import ContactApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactApp()
    window.show()
    sys.exit(app.exec_())