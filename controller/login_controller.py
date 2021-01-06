from PyQt5 import QtCore
from view.login_view import LoginView
from model.login_model import LoginModel
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import time
from db.operation import DatabaseVisitor


class LoginController():
    def __init__(self):
        self.view = LoginView()
        self.model = LoginModel()
        self.view.setupUi(self.view)
        self.view.btn_login.clicked.connect(lambda: self.click_btn_login())
        self.view.show()  # 控制器创建视图

    # 登录动作
    def click_btn_login(self):
        # 获取视图login_view信息
        input_username = self.view.line_input_username.text()
        input_password = self.view.line_input_password.text()
        env_society = self.view.radiobtn_society.isChecked()
        env_home = self.view.radiobtn_home.isChecked()
        if input_username == '' or input_password == '':  # 判空
            self.view.label_tips.setText('请输入用户名和密码')#改变视图显示
        elif env_home==False and env_society==False:
            self.view.label_tips.setText('请选择工作环境')
        else:# 向模型login_model发出信号
            flag=self.model.try_to_login(input_username, input_password)
            if flag==True:
                self.view.label_tips.setText("登陆成功")
                #time.sleep(1)
                self.view.close()
            else:
                self.view.label_tips.setText("用户名或密码错误")
                #self.open_working_windows(env_society,env_home)
    # def open_working_windows(self,env_society,env_home):
    #     if env_home:
    #         model=HomeModel()
    #             new_working_windows=HomeController(model)






if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainwindow = LoginController()
    sys.exit(app.exec_())
# from PyQt5 import QtCore
#
# from view.ui_login import Ui_login
# from PyQt5.QtWidgets import QApplication,QMainWindow
# import sys
# import time
# from db.operation import DatabaseVisitor
#
# class LoginController(QMainWindow,Ui_login):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         Ui_login.__init__(self)
#         self.setupUi(self)
#         self.btn_login.clicked.connect(lambda:self.click_btn_login())
#
#     #登录控制逻辑
#     def click_btn_login(self):
#         dbvisitor=DatabaseVisitor()
#         username=self.input_username.text()
#         password=self.input_password.text()
#         if username=='' or password=='':#判空
#             self.label_tips.setText('请输入用户名和密码')
#         elif self.radiobtn_house.isChecked()==False and self.radiobtn_social.isChecked()==False:
#             self.label_tips.setText('请选择工作环境')
#         else:
#             sql="SELECT Upassword FROM User WHERE Uname = '%s'" % (username)
#             re=dbvisitor.find_one(sql)
#             db_password=re[0]
#             print(db_password)
#             print(password)
#             if db_password==False:
#                 self.label_tips.setText('此管理员用户不存在')
#             else:
#                 if password==db_password:
#                     self.label_tips.setText('登录成功')
#                     time.sleep(1)
#                     self.close()#关闭登录界面
#                     self.open_working_window()#打开对应模式的工作界面
#                 else:
#                     self.label_tips.setText('密码错误')
#
#     #打开对应模式工作窗口
#     def open_working_window(self):
#         if self.radiobtn_social.isChecked()==True:
#             pass
#         else:
#             pass
#
# if __name__ == '__main__':
#     QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
#     app = QApplication(sys.argv)
#     ui = LoginControl()
#     ui.show()
#     sys.exit(app.exec_())