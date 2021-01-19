from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import QtCore
from view.pure_ui.add_admin_ui import Ui_add_admin
import sys

class AddAdminView(QMainWindow,Ui_add_admin):
    def __init__(self):
        super(AddAdminView, self).__init__()
        self.setFixedSize(333, 364)
        self.setupUi(self)

    def mes(self,message,mode):
        if(mode == "information"):
            reply = QMessageBox.information(self, 'Message', message, QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            return reply
        if(mode == "question"):
            reply = QMessageBox.question(self, 'Message', message, QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.No)
            return reply
        if (mode == "warning"):
            reply = QMessageBox.warning(self, 'Message', message, QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            return reply
        if(mode == "critical"):
            reply = QMessageBox.critical(self, 'Message', message, QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.No)
            return reply
    def get_input_username(self):
        re=self.uname.text()
        return re

    def get_input_password(self):
        re=self.upassword.text()
        return re
    def get_input_doublepassword(self):
        re = self.doubleupassword.text()
        return re
    def get_input_urank(self):
        re = self.urank.text()
        return re

    def get_input_uphone(self):
        re = self.uphone.text()
        return re


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 创建 Application 实例 app
    window = AddAdminView()
    window.show()                 # 显示窗口
    sys.exit(app.exec_())