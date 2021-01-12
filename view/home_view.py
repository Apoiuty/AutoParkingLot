import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication

from view.pure_ui.home_ui import Ui_home


class HomeView(QMainWindow, Ui_home):
    def __init__(self):
        super(HomeView, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 创建 Application 实例 app
    window = HomeView()
    window.show()  # 显示窗口
    sys.exit(app.exec_())
