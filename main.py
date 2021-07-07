from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication
from src.analysisTool import Tool
from sys import argv

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(argv)
    nst = Tool()
    nst.show()
    exit(app.exec_())
