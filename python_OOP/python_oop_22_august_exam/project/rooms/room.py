class Room:
    def __init__(self, family_name, budget, members_count, children=None, expenses=None):
        if children is None:
            children = []
        self.room_cost = None
        self.children = children
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self._expenses = expenses

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')
        self._expenses = value

    def calculate_expenses(self):
        return self._expenses + self.room_cost
