from db.operation import DatabaseVisitor


class Log_Model():
    """
    日志的控制器，与数据库交互
    """

    def __init__(self, observer):
        self.db = DatabaseVisitor()
        self.observer = observer
        self.db_index = {'home': 'HomeHistory', 'society': 'SocietyHistory'}

    def get_log_data_plate(self, index, circu):
        """
        以车牌信息查询表
        :param circu:
        :param index: 车牌信息
        :return:
        """
        index = index.strip()
        if circu == 'society':
            sql = "SELECT * FROM " + self.db_index[circu] + " WHERE Scar = '%s'" % (index)
        else:
            sql = "SELECT * FROM " + self.db_index[circu] + " WHERE Hcar = '%s'" % (index)
        re = self.db.find_all(sql)
        re += self.db.find_all(sql)
        re = list(set(re))
        self.observer.set_tabel(re, circu)

    def get_log_data_time(self, data, circu):
        """
        以一个时间段查询车辆信息
        :param circu:
        :param data: 时间区间,以逗号间隔
        :return:
        """
        data = data.strip()
        data = data.split(',')
        data_begin = data[0].strip()
        data_end = data[1].strip()
        # 查询语句
        if circu == 'society':
            sql_begin = "SELECT * FROM " + self.db_index[circu] + " WHERE Sout between '{0}' and '{1}'".format(
                data_begin,
                data_end)
            sql_end = "SELECT * FROM " + self.db_index[circu] + " WHERE Sin between '{0}' and '{1}'".format(data_begin,
                                                                                                            data_end)
        else:
            sql_begin = "SELECT * FROM " + self.db_index[circu] + " WHERE Hout between '{0}' and '{1}'".format(
                data_begin,
                data_end)
            sql_end = "SELECT * FROM " + self.db_index[circu] + " WHERE Hin between '{0}' and '{1}'".format(data_begin,
                                                                                                            data_end)

        re = self.db.find_all(sql_end)
        re += self.db.find_all(sql_begin)
        re = list(set(re))
        self.observer.set_tabel(re, circu)

    def get_log_data_owner(self, index):
        sql = "SELECT * FROM HomeCar WHERE Howner = '{0}' ".format(index)
        re = self.db.find_all(sql)
        re = list(set(re))
        self.observer.set_tabel(re, 'home_owner')
