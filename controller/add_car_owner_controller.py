from view.car_owner_view import Car_Owner
from model.add_car_owner_model import Carowner_model


class Car_owner_contrl():

    def __init__(self):
        self.view = Car_Owner()
        self.model = Carowner_model(self.view)

        self.view.pushButton.clicked.connect(self.add_owner)
        self.view.exec_()

    def add_owner(self):
        self.model.write_car_owner(self.view.get_input())

class Car_Owner_Change_Control():
    def __init__(self):
        self.view = Car_Owner()
        self.model = Carowner_model(self.view)
        self.view.setWindowTitle('修改已有信息')
        self.view.pushButton.clicked.connect(self.change_info)
        self.view.exec_()

    def change_info(self):
        self.model.change_car_info(self.view.get_input())