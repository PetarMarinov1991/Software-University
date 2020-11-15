from project.product import Product


class Beverage(Product):
    def __init__(self, name: str, price: float, milliliters: float):
        Product.__init__(self, name, price)
        self._milliliters = milliliters

    @property
    def milliliters(self):
        return self._milliliters
