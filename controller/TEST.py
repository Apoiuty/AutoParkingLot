from db.operation import DatabaseVisitor

# ndbvisitor = DatabaseVisitor()
# #sql = "SELECT * FROM User "
# sql="SELECT Upassword FROM User WHERE Uname = 'worker01'"
# db_password = ndbvisitor.find_one(sql)
# print(db_password)

from PyQt5 import QtCore
from view.ui_login import Ui_login
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
import time
from db.operation import DatabaseVisitor

class ControllerLogin():
    def __init__(self):
        self.view=Ui_login()
        self.model=None
        self.view.setupUi(self.view)
        self.view.btn_login.clicked.connect(lambda:self.click_btn_login())
        self.view.show()

    #登录控制逻辑
    def click_btn_login(self):
        dbvisitor=DatabaseVisitor()
        username=self.view.input_username.text()
        password=self.view.input_password.text()
        if username=='' or password=='':#判空
            self.view.label_tips.setText('请输入用户名和密码')
        elif self.view.radiobtn_house.isChecked()==False and self.view.radiobtn_social.isChecked()==False:
            self.view.label_tips.setText('请选择工作环境')
        else:
            sql="SELECT Upassword FROM User WHERE Uname = '%s'" % (username)
            re=dbvisitor.find_one(sql)
            db_password=re[0]
            if db_password==False:
                self.view.label_tips.setText('此管理员用户不存在')
            else:
                if password==db_password:
                    self.view.label_tips.setText('登录成功')
                    time.sleep(1)
                    self.view.close()#关闭登录界面
                    #self.open_working_window()#打开对应模式的工作界面
                else:
                    self.view.label_tips.setText('密码错误')

    #打开对应模式工作窗口
    def open_working_window(self):
        if self.view.radiobtn_social.isChecked()==True:
            pass
        else:
            pass

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    ui = ControllerLogin()
    #ui.show()
    sys.exit(app.exec_())