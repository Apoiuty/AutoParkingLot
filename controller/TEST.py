import sys,math
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyComboBox(QComboBox) :
    def __init__(self):
        super(MyComboBox,self).__init__()
        self.setAcceptDrops(True)  # A控件可以接受其他拖拽过来的内容
    def dragEnterEvent(self,e):
        print(e)
        if e.mimeData().hasText():  # 拖拽过来如果是文本就接受
            e.accept()
        else:
            e.ignore()

    def dropEvent(self,e):
        self.addItem(e.mimeData().text())  # 这里的addItem是针对QComboBox

class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo,self).__init__()
        formLayout = QFormLayout()
        formLayout.addRow(QLabel("请将左边的文本拖拽到右边的下拉列表中"))
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)  # 让QLineEdit控件可拖动

        combo = MyComboBox()
        formLayout.addRow(lineEdit,combo)
        self.setLayout(formLayout)
        self.setWindowTitle('拖拽案例')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrapDropDemo()
    main.show()
    sys.exit(app.exec_())
import os, sys
# 可供图片拖拽Label控件
# class DropLabel(QLabel):
#     # 1、继承QLabel
#     # 2、设置自定义信号函数pyqtSignal在使用时默认传递两个参数
#     def __init__(self, *args, **kwargs):
#         QLabel.__init__(self, *args, **kwargs)
#         self.setAcceptDrops(True)
#         self.dropDown = pyqtSignal(object, str)
#
#     def dragEnterEvent(self, event):
#         if event.mimeData().hasText():
#             event.acceptProposedAction()
#
#     def dropEvent(self, event):
#         # 一定要使用super，因为程序先看子类方法再去看父类方法,子类方法覆盖了
#         # 父类方法,会到导致dropEvent()的其他方法无法使用
#         # event:事件对象
#         super(DropLabel, self).dropEvent(event)
#         image = event.mimeData().text()
#         #image_path = re.sub('^file:///', '', image)
#         # 图片是放在DropLabel对象内，并不是Qlabel对象
#         # 3、槽函数，对应 pyqtSignal 信号，这里返回 DropLabel 对象和图片的路径
#         self.dropDown.emit(self, image)
#         event.acceptProposedAction()
#
# class View(QWidget):
#     def _setup(self):
#         # 创建重写的QLabel
#         self._createLabel()
#         self.banner1.dropDown.connect(self.ondropDown())
#
#
#     def _createLabel(self):
#         self.banner1 = DropLabel(self.Widget32)
#         self.banner1.setObjectName("banner1")
#         self.verticalLayout_47.addWidget(self.banner1)
#
#
#     def ondropDown(self, _label, _path):
#         if _path.endswith('.png'):
#             pixmap = QPixmap(_path)
#             _label.setScaledContents(True)  # 自适应大小
#             _label.setPixmap(pixmap)

# # ndbvisitor = DatabaseVisitor()
# # #sql = "SELECT * FROM User "
# # sql="SELECT Upassword FROM User WHERE Uname = 'worker01'"
# # db_password = ndbvisitor.find_one(sql)
# # print(db_password)
# # from PyQt5.QtWidgets import QMainWindow
# #
# # class Ui_login(QMainWindow):
#
# from PyQt5 import QtCore
# from view.login_view import LoginView
# from model.login_model import LoginModel
# from PyQt5.QtWidgets import QApplication, QMainWindow
# import sys
# import time
# from db.operation import DatabaseVisitor
#
#
# class ControllerLogin():
#     def __init__(self, model):
#         self.view = LoginView()
#         self.model = model  # LoginModel()这里model作为参数传入
#         self.view.setupUi(self.view)
#         self.view.btn_login.clicked.connect(lambda: self.click_btn_login())
#         self.view.show()  # 控制器创建视图
#
#     # 登录动作
#     def click_btn_login(self):
#         # 获取login_view信息
#         input_username = self.view.line_input_username.text()
#         input_password = self.view.line_input_password.text()
#         env_society = self.view.radiobtn_society.isChecked()
#         env_home = self.view.radiobtn_home.isChecked()
#         # 向模型发出控制信号
#         self.model.try_to_login(input_username, input_password, env_society, env_home)
#
#
# if __name__ == '__main__':
#     QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
#     app = QApplication(sys.argv)
#     model=LoginModel()
#     mainwindow = ControllerLogin(model)
#     sys.exit(app.exec_())
#
# # from PyQt5 import QtCore
# # login逻辑重构前代码，备份
# # from view.ui_login import Ui_login
# # from PyQt5.QtWidgets import QApplication,QMainWindow
# # import sys
# # import time
# # from db.operation import DatabaseVisitor
# #
# # class LoginController(QMainWindow,Ui_login):
# #     def __init__(self):
# #         QMainWindow.__init__(self)
# #         Ui_login.__init__(self)
# #         self.setupUi(self)
# #         self.btn_login.clicked.connect(lambda:self.click_btn_login())
# #
# #     #登录控制逻辑
# #     def click_btn_login(self):
# #         dbvisitor=DatabaseVisitor()
# #         username=self.input_username.text()
# #         password=self.input_password.text()
# #         if username=='' or password=='':#判空
# #             self.label_tips.setText('请输入用户名和密码')
# #         elif self.radiobtn_house.isChecked()==False and self.radiobtn_social.isChecked()==False:
# #             self.label_tips.setText('请选择工作环境')
# #         else:
# #             sql="SELECT Upassword FROM User WHERE Uname = '%s'" % (username)
# #             re=dbvisitor.find_one(sql)
# #             db_password=re[0]
# #             print(db_password)
# #             print(password)
# #             if db_password==False:
# #                 self.label_tips.setText('此管理员用户不存在')
# #             else:
# #                 if password==db_password:
# #                     self.label_tips.setText('登录成功')
# #                     time.sleep(1)
# #                     self.close()#关闭登录界面
# #                     self.open_working_window()#打开对应模式的工作界面
# #                 else:
# #                     self.label_tips.setText('密码错误')
# #
# #     #打开对应模式工作窗口
# #     def open_working_window(self):
# #         if self.radiobtn_social.isChecked()==True:
# #             pass
# #         else:
# #             pass
# #
# # if __name__ == '__main__':
# #     QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
# #     app = QApplication(sys.argv)
# #     ui = LoginControl()
# #     ui.show()
# #     sys.exit(app.exec_())
