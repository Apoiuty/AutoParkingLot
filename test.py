# uname = "worker02"
# upassword = "111111"
# urank = "5"
# uphone = "1523681523"
#
# sql = "insert into User(Uname,Upassword,Urank,Uphone) values(\"%s\",\"%s\",\"%s\",\"%s\")"%(uname,upassword,urank,uphone)
# print(sql)
from model.add_admin_model import AddAdminModel

# import sqlite3
# conn = sqlite3.connect('Database.db')
# print("Opened database successfully")
# uname = "worker11"
# upassword = "111111"
# urank = "5"
# uphone = "1523681523"
# sql = "insert into User(Uname,Upassword,Urank,Uphone) values(\"%s\",\"%s\",\"%s\",\"%s\")"%(uname,upassword,urank,uphone)
# sql = "delete from  User where Uname = \"%s\""%(uname)
# print(sql)
# print(conn.execute(sql))
# print(conn.commit())
# conn.close()

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super(MyWindow, self).__init__(parent)

        self.setWindowTitle('QMessageBox例子')
        self.resize(300,100)

        self.mybutton=QPushButton(self)
        self.mybutton.move(5,5)
        self.mybutton.setText('点击消息弹出消息框')
        self.mybutton.clicked.connect(self.msg)
    def msg(self):
        #弹出消息对话框
        reply = QMessageBox.information(self, '标题','消息对话框正文',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        reply1 = QMessageBox.question(self, "标题", "提问框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        print(reply1)
        reply2 = QMessageBox.warning(self, "标题", "警告框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        reply3 = QMessageBox.critical(self, "标题", "严重错误对话框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        reply4 = QMessageBox.about(self, "标题", "关于对话框消息正文")


if __name__ == '__main__':
    app=QApplication(sys.argv)
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_())