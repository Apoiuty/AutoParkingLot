import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from camera.camera_sim import CameraSimulator
from controller import home_controller, society_controller
from model.login_model import LoginModel
from view.login_view import LoginView


class LoginController():
    def __init__(self):
        self.view = LoginView()
        self.model = LoginModel()
        self.view.setupUi(self.view)
        self.view.btn_login.clicked.connect(lambda: self.click_btn_login())
        self.view.show()  # 控制器创建视图
        self.new_view = None

    # 登录控制
    def click_btn_login(self):

        input_username = self.view.get_input_username()  # 获取视图login_view信息
        input_password = self.view.get_input_password()
        env_home = self.view.is_env_home_selected()
        env_society = self.view.is_env_society_selected()
        if input_username == '' or input_password == '':  # 输入判空
            self.view.show_input_lack_tips()  # 改变视图显示
        elif env_home == False and env_society == False:  # 环境选择判空
            self.view.show_env_tips()
        elif len(input_username) > 25 or len(input_password) > 25:
            self.view.show_input_so_long_tips()
        else:  # 向模型login_model发出信号
            flag = self.model.try_to_login(input_username, input_password)
            if flag == True:
                self.view.show_login_ok_tips()
                # time.sleep(1)
                self.open_working_windows(env_home)
                self.view.close()
            else:
                self.view.show_input_error_tips()

    # 控制新的视图出现
    def open_working_windows(self, env_home):
        if env_home == True:
            self.new_view = CameraSimulator(home_controller.HomeController(self.view.get_input_username()))  # 新控制器负责创建新视图
        else:
            self.new_view = CameraSimulator(society_controller.SocietyController(self.view.get_input_username()))


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainwindow = LoginController()
    exit_code = app.exec_()
    sys.exit(exit_code)
