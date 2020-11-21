from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name, salary_one, salary_two):
        Room.__init__(self, family_name, budget=None, members_count=2, children=None, expenses=None)
        self.room_cost = 20
        self.budget = salary_one + salary_two
        self.appliances = [TV(), Fridge(), Laptop()]
        self.expenses = sum([a.get_monthly_expense() * self.members_count for a in self.appliances])
