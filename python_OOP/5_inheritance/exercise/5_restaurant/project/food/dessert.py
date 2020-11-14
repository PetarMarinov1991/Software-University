from project.food.food import Food


class Dessert(Food):
    def __init__(self, name: str, price: float, grams: float, calories: float):
        Food.__init__(self, name, price, grams)
        self._calories = calories

    @property
    def calories(self):
        return self._calories
