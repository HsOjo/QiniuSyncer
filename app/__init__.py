from PyQt5.QtWidgets import QApplication
from sys import argv

from .controller.main import MainWindow
class Application:
    def __init__(self):
        self.qt = QApplication(argv)
        self.main = MainWindow()

    def run(self):
        self.main.show()
        return self.qt.exec_()
