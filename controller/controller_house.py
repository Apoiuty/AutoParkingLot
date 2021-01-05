from PyQt5 import QtCore

from view.ui_house import Ui_house
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
import time
from db.operation import DatabaseVisitor
class HouseControl(QMainWindow,Ui_house):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_house.__init__(self)
        self.setupUi(self)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    widget = QMainWindow()
    ui = Ui_house()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())