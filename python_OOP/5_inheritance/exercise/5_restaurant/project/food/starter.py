from project.food.food import Food


class Starter(Food):
    def __init__(self, name: str, price: float, grams: float, calories: float):
        Food.__init__(self, name, price, grams, calories)

    @property
    def calories(self):
        return self._calories
