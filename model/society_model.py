from db.operation import DatabaseVisitor
from cnn.identifier import identify_car_plate
class SocietyModel():
    def __init__(self):
        self.db=DatabaseVisitor()
        self.observer=[]

    def identify_result(self,path):
        return identify_car_plate(path)

    #下面是数据库相关操作






