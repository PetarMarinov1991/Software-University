from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one, pension_two):
        Room.__init__(self, family_name, budget=None, members_count=2, children=None, expenses=None)
        self.room_cost = 15
        self.budget = pension_one + pension_two
        self.appliances = [TV(), Fridge(), Stove()]
        self.expenses = sum([a.get_monthly_expense() * self.members_count for a in self.appliances])
