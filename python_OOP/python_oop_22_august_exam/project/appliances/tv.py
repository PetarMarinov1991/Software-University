from project.appliances.appliance import Appliance


class TV(Appliance):
    def __init__(self):
        Appliance.__init__(self, 1.5)
