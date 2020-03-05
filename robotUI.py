import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = None

def main():
    app = QApplication(sys.argv)
    main_window = UI()
    main_window.initUI()
    sys.exit(app.exec_())

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        
    def initUI(self):
        # File bar menu

        # Central widget

        # Widgets within central widget

        # Buttons?

        # Add to layouts

        # Finalize geometry
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Worker Scheduler')
        self.show()

main()
    