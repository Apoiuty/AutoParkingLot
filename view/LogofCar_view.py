from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QHeaderView

from view.pure_ui.LogofCar_ui import Ui_LogByCarName


class carnameLog(QDialog, Ui_LogByCarName):
    """
    日志查询类
    """

    def __init__(self):
        """
        窗体初始化
        :param dialog: 对话框
        """
        QDialog.__init__(self)
        self.setupUi(self)

    def set_tabel(self, items):
        """
        设置table view的显示查询信息
        :param items:查询到的列表
        :return:
        """
        items = [i[1:-1] for i in items]
        row = len(items)
        col = 4

        model = QStandardItemModel(row, col)
        model.setHorizontalHeaderLabels(['车牌', '进入时间', '离去时间', '收费'])

        for i in range(row):
            for j in range(col):
                item = QStandardItem(str(items[i][j]))
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                model.setItem(i, j, item)

        self.TableOfCarLog.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.TableOfCarLog.setModel(model)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = carnameLog()
    ui.show()
    sys.exit(app.exec_())
