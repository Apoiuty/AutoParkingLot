import configparser
from datetime import datetime

from db.operation import DatabaseVisitor
from model.society_model import SocietyModel


class HomeModel(SocietyModel):
    def __init__(self, observer):
        self.db = DatabaseVisitor()
        self.observer = observer
        self.config = configparser.ConfigParser()
        # 写成相对路径读取配置文件

    # 手动模式无需再识别，直接update_data,进入此流程
    def update_data(self, car, flag):  # 对应的数据库一部分
        checked = self.check_carplate(car)  # 更新前先判断车牌是否符合规范
        if checked == False:  # 尤其是手动模式输入不合格车牌，更新状态，并通知视图改变显示
            self.observer.msgbox_to_check_handmode_input()
            return
        dbvisitor = DatabaseVisitor()
        fee = 0
        if flag == 0:  # 车辆进入的数据库更新
            sql = "insert into HomeHistory (\"Hcar\",\"Hflag\",\"Hin\") values (\"%s\",\"%f\",\"%s\")" % (
                car, 1, str(datetime.now())[:-7])
            re = dbvisitor.update(sql)
        else:
            # 没有意外的情况
            sql = "SELECT * FROM HomeHistory WHERE Hcar = '%s' and Hflag = '1'" % (car)
            re = dbvisitor.find_all(sql)
            if not re:
                return
            item_to_rite = max(re, key=lambda s: s[0])
            in_time = item_to_rite[-2]
            in_time = datetime.strptime(in_time, "%Y-%m-%d %H:%M:%S")
            now_time = datetime.now()
            now_time = str(now_time)[:-7]
            sql_update = "update HomeHistory set Hcar=\"{0}\",Hin=\"{1}\",Hout=\"{2}\",Hflag=\"{3}\"  \
                          where Hno='{4}'".format(
                car, str(in_time), now_time, 0, item_to_rite[0])
            dbvisitor.update(sql_update)
        # 改变最终视图
        self.notify_observer_result_condition(car, flag, -1)  # 输入合格，通知视图观察者识别状态改变,flag=0为进入
