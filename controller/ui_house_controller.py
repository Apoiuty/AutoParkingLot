from PyQt5 import QtCore

from view.ui_house import Ui_house
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
import time
from db.operation import DatabaseVisitor

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    widget = QMainWindow()
    ui = Ui_house()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())