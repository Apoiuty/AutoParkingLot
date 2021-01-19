from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import QtCore
from view.pure_ui.add_admin_ui import Ui_add_admin
import sys
from view.pure_ui.delete_admin_ui import Ui_delete_admin

class DeleteAdminView(QMainWindow,Ui_delete_admin):
    def __init__(self):
        super(DeleteAdminView, self).__init__()
        self.setFixedSize(400,168)
        self.setupUi(self)

    def mes(self, message, mode):
        if (mode == "information"):
            reply = QMessageBox.information(self, 'Message', message, QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.No)
            return reply
        if (mode == "question"):
            reply = QMessageBox.question(self, 'Message', message, QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            return reply
        if (mode == "warning"):
            reply = QMessageBox.warning(self, 'Message', message, QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.No)
            return reply
        if (mode == "critical"):
            reply = QMessageBox.critical(self, 'Message', message, QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            return reply
    def get_input_username(self):
        re=self.lineEdit.text()
        return re


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 创建 Application 实例 app
    window = DeleteAdminView()
    window.show()                 # 显示窗口
    sys.exit(app.exec_())