from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtCore
from view.society_ui import Ui_society
import sys

class SocietyView(QMainWindow,Ui_society):
    def __init__(self):
        super(SocietyView, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 创建 Application 实例 app
    window = SocietyView()
    window.show()                 # 显示窗口
    sys.exit(app.exec_())