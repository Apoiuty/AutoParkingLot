from PyQt5 import QtCore, QtWidgets
from view.LogofCar_view import carnameLog
from model.log_model import Log_Model
from controller import home_controller, society_controller
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp
import sys


class LogController():
    """
    日志控制器
    """

    def __init__(self, mode):
        """
         控制器初始化
        :param mode: 是车牌查询还是日期查询
        """
        self.mode = mode
        self.view = carnameLog()
        self.model = Log_Model()
        self.view.CarNameConfirm.clicked.connect(self.get_log_data)
        self.view.show()

    def get_log_data(self):
        """
        获取输入的信息并查询记录
        :return:
        """
        Query_item = self.view.CarNameInput.text()
        # 获取输入信息并查询项目
        if self.mode == 'plate':
            re = self.model.get_log_data_plate(Query_item)
        else:
            re = self.model.get_log_data_time(Query_item)

        if re:
            # 输出查询到的车辆信息
            self.view.set_tabel(re)
        else:
            # todo:没有查询到弹出无记录
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    test = LogController('time')
    sys.exit(app.exec_())
