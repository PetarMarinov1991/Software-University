from project.appliances.appliance import Appliance


class Stove(Appliance):
    def __init__(self):
        Appliance.__init__(self, 0.7)
