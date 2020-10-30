class PizzaDelivery:
    ordered = False

    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if not PizzaDelivery.ordered:
            if ingredient not in self.ingredients:
                self.ingredients[ingredient] = 0
            self.ingredients[ingredient] += quantity
            self.price += ingredient_price * quantity
        return f'Pizza {self.name} already prepared and we can\'t make any changes!'

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if not PizzaDelivery.ordered:
            if ingredient not in self.ingredients:
                return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
            if self.ingredients[ingredient] < quantity:
                return f'Please check again the desired quantity of {ingredient}!'
            self.ingredients[ingredient] -= quantity
            self.price -= ingredient_price * quantity
        return f'Pizza {self.name} already prepared and we can\'t make any changes!'

    def pizza_ordered(self):
        PizzaDelivery.ordered = True
        return f'You\'ve ordered pizza {self.name} ' \
               f'prepared with {", ".join([f"{k}: {v}" for k, v in self.ingredients.items()])} ' \
               f'and the price will be {self.price}lv.'
