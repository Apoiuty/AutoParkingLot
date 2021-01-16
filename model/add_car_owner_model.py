from db.operation import DatabaseVisitor


class Carowner_model():

    def __init__(self, observer):
        self.db = DatabaseVisitor()
        self.observer = observer

    def write_car_owner(self, items):
        """
        写入数据库中新增车主的信息
        :param items: 车主信息元组
        :return:
        """

        sql = "insert into HomeCar (Hcar,Hcarport,Howner,\
        Hownerhouse,Hownerphone,Hownerkind) values " \
              "('{0}','{1}','{2}','{3}','{4}','{5}')".format(*items)

        self.db.update(sql)
