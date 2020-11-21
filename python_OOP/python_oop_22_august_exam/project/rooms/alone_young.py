from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name, salary):
        Room.__init__(self, family_name, budget=salary, members_count=1, children=None, expenses=None)
        self.room_cost = 10
        self.appliances = [TV()]
        self.expenses = sum([a.get_monthly_expense() * self.members_count for a in self.appliances])
