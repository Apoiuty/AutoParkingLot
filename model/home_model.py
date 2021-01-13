import configparser
from datetime import datetime

from cnn.identifier import identify_car_plate
from db.operation import DatabaseVisitor


class HomeModel():
    def __init__(self, observer):
        self.db = DatabaseVisitor()
        self.observer = observer
        self.config = configparser.ConfigParser()
        # 写成相对路径读取配置文件

    # 自动模式先识别再update_data,进入此流程
    def identify_result(self, path, flag):
        result = identify_car_plate(path)
        self.update_data(result, flag)

    # 手动模式无需再识别，直接update_data,进入此流程
    def update_data(self, car, flag):  # 对应的数据库一部分
        checked = self.check_carplate(car)  # 更新前先判断车牌是否符合规范
        if checked == False:  # 尤其是手动模式输入不合格车牌，更新状态，并通知视图改变显示
            self.observer.msgbox_to_check_handmode_input()
            return
        dbvisitor = DatabaseVisitor()
        rate = float(self.get_rate())
        fee = 0
        if flag == 0:  # 车辆进入的数据库更新
            sql = "insert into SocietyCurrent (\"Scar\",\"Srate\") values (\"%s\",\"%f\")" % (car, rate)
            re = dbvisitor.update(sql)
        else:  # 车离开的更新，此处涉及计费等操作，因此可能需要多次数据库操作，还需要考虑那种意外

            # 没有意外的情况
            sql = "SELECT * FROM SocietyCurrent WHERE Scar = '%s'" % (car)
            re = dbvisitor.find_all(sql)
            item_to_rite = re[0]
            in_time = item_to_rite[1]
            in_time = datetime.strptime(in_time, "%Y-%m-%d %H:%M:%S")
            now_time = datetime.now()
            sec = (now_time - in_time).seconds
            fee = sec / 3600 * float(item_to_rite[2]) * 1000
            # todo:把这里1000删了
            now_time = str(now_time)[:-7]
            sql_update = "insert into SocietyHistory (\"Scar\",\"Sin\",\"Sout\",\"Sfee\",\"Srate\") " \
                         "values (\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\")".format(
                car, str(in_time), now_time, round(fee, 2), float(item_to_rite[2]))
            item_to_del = "delete from SocietyCurrent where Scar='{0}'".format(car)
            dbvisitor.update(item_to_del)
            dbvisitor.update(sql_update)
        # 改变最终视图
        self.notify_observer_result_condition(car, flag, round(fee, 2))  # 输入合格，通知视图观察者识别状态改变,flag=0为进入

    def check_carplate(self, carplate):  # 检查传入车牌合法性
        PLATE_CHARS_PROVINCE = ["京", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑",
                                "苏", "浙", "皖", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤",
                                "桂", "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁",
                                "新", "警", "军", "甲", "W"]
        # 这些是合法的字符
        PLATE_CHARS_LETTER = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H",
                              "J",
                              "K", "L", "M", "N", "P",
                              "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        # 首先检查长度
        if len(carplate) != 7:
            return False
        # #检查车牌首字符,考虑到特种车辆（虽然可能不会停进来）,放到后面一并检查
        # if carplate[0] not in PLATE_CHARS_PROVINCE :
        #     return False
        # 检查车牌字符是否在合法字符集中
        for i in range(0, 7):
            if carplate[i] not in PLATE_CHARS_LETTER and carplate[i] not in PLATE_CHARS_PROVINCE:
                return False
        return True

    def notify_observer_result_condition(self, result_msg, flag, fee):
        if flag == 0:  # 车辆进入识别
            self.observer.show_in_car(result_msg)
            self.observer.show_in_time()
        else:
            self.observer.show_out_car(result_msg)
            self.observer.show_out_time()
            self.observer.show_out_fee(fee)

    def get_rate(self):  # 获得当前费率
        self.config.read('../config.ini', encoding='utf-8')
        rate = self.config['sys']['society_rate']
        return rate
