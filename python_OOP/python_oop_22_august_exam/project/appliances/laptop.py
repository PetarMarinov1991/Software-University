from project.appliances.appliance import Appliance


class Laptop(Appliance):
    def __init__(self):
        Appliance.__init__(self, 1)
