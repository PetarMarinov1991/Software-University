from project.factory.factory import Factory


class PaintFactory(Factory):
    def __init__(self, name, capacity):
        Factory.__init__(self, name, capacity)

    def add_ingredient(self, ingredient_type, quantity):
        if ingredient_type in ["white", "yellow", "blue", "green", "red"]:
            if PaintFactory.can_add(self, quantity):
                if ingredient_type not in self.ingredients:
                    self.ingredients.update({ingredient_type: 0})
                self.ingredients[ingredient_type] += quantity
                self.capacity -= quantity
            else:
                raise ValueError('Not enough space in factory')
        else:
            raise TypeError(f'Ingredient of type {ingredient_type} not allowed in PaintFactory')

    def remove_ingredient(self, ingredient_type, quantity):
        if ingredient_type in self.ingredients:
            if quantity <= self.ingredients[ingredient_type]:
                self.ingredients[ingredient_type] -= quantity
                self.capacity += quantity
            else:
                raise ValueError('Ingredient quantity cannot be less than zero')
        else:
            raise KeyError('No such ingredient in the factory')
    
    @property
    def products(self):
        return self.ingredients
    
    @products.setter
    def products(self, value):
        self.ingredients = value
