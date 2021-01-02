from PyQt5 import QtCore

from view.ui_login import Ui_login
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
import time
from db.operation import DatabaseVisitor

class LoginControl(QMainWindow,Ui_login):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_login.__init__(self)
        self.setupUi(self)
        self.btn_login.clicked.connect(lambda:self.click_btn_login())

    #登录控制逻辑
    def click_btn_login(self):
        dbvisitor=DatabaseVisitor()
        username=self.input_username.text()
        password=self.input_password.text()
        if username=='' or password=='':#判空
            self.label_tips.setText('请输入用户名和密码')
        elif self.radiobtn_house.isChecked()==False and self.radiobtn_social.isChecked()==False:
            self.label_tips.setText('请选择工作模式')
        else:
            sql="SELECT Upassword FROM User WHERE Uname = '%s'" % (username)
            re=dbvisitor.find_one(sql)
            db_password=re[0]
            print(db_password)
            print(password)
            if db_password==False:
                self.label_tips.setText('此管理员用户不存在')
            else:
                if password==db_password:
                    self.label_tips.setText('登录成功')
                    #print('登录成功')
                    #self.open_working_window()#打开对应模式的工作界面
                    #time.sleep(1)
                    #self.close()#关闭登录界面
                else:
                    self.label_tips.setText('密码错误')

    #打开对应模式工作窗口
    def open_working_window(self):
        if self.radiobtn_social.isChecked()==True:
            pass
            #打开社会停车场工作界面
        else:
            pass

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    ui = LoginControl()
    ui.show()
    sys.exit(app.exec_())