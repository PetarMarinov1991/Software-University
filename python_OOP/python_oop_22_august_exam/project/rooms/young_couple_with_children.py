from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        Room.__init__(self, family_name, budget=None, members_count=2, children=children, expenses=None)
        self.appliances = [TV(), Fridge(), Laptop()]
        self.budget = salary_one + salary_two
        self.room_cost = 30
        self.members_count += len(children)
        self.child_cost = sum([c.cost for c in children])
        self.expenses = sum([a.get_monthly_expense() * self.members_count for a in self.appliances]) + self.child_cost
