from PyQt5 import QtCore
from view.delete_admin_view  import DeleteAdminView
from model.delete_admin_model import DeleteAdminModel

from PyQt5.QtWidgets import QApplication,QMessageBox

import sys

class DeleteAdminController():
    def __init__(self):
        self.view = DeleteAdminView()
        self.model = DeleteAdminModel()
        self.view.setupUi(self.view)
        #绑定函数
        self.view.cut.clicked.connect(lambda: self.click_delete())
        self.view.show()  # 控制器创建视图
        self.new_view=None

    # 登录控制
    def click_delete(self):

        input_username = self.view.get_input_username()  # 获取视图login_view信息
        if(input_username == ""):
            self.view.mes(message="未输入账号",mode="information")
        else:
            if(QMessageBox.Yes == self.view.mes(message="要删除%s的账户吗？" % (input_username), mode="information")):
                flag = self.model.try_to_delete(input_username)
                if flag:
                    self.view.mes(message="删除成功",mode="information")
                else:
                    self.view.mes(message="不存在该用户,删除失败,请重新输入", mode="information")
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainwindow = DeleteAdminController()
    sys.exit(app.exec_())
    # exit_code=app.exec_()
    # sys.exit(exit_code)

