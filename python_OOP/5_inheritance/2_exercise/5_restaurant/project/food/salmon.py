from project.food.main_dish import MainDish


class Salmon(MainDish):
    SALMON_GRAMS = 22

    def __init__(self, name: str, price: float):
        MainDish.__init__(self, name, price, Salmon.SALMON_GRAMS)
