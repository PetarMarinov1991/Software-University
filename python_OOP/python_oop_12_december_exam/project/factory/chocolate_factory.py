from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name, capacity):
        Factory.__init__(self, name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type, quantity):
        if ingredient_type in ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]:
            if ChocolateFactory.can_add(self, quantity):
                if ingredient_type not in self.ingredients:
                    self.ingredients.update({ingredient_type: 0})
                self.ingredients[ingredient_type] += quantity
            else:
                raise ValueError('Not enough space in factory')
        else:
            raise ValueError(f'Ingredient of type {ingredient_type} not allowed in ChocolateFactory')

    def remove_ingredient(self, ingredient_type, quantity):
        if ingredient_type in self.ingredients:
            if quantity <= self.ingredients[ingredient_type]:
                self.ingredients[ingredient_type] -= quantity
            else:
                raise ValueError('Ingredient quantity cannot be less than zero')
        else:
            raise KeyError('No such product in the factory')

    def add_recipe(self, recipe_name, recipe):
        if recipe_name not in self.recipes:
            self.recipes.update({recipe_name: recipe})
        else:
            self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name):
        if recipe_name in self.recipes:
            if recipe_name not in self.products:
                self.products.update({recipe_name: 0})
            self.products[recipe_name] += 1
            for recipe in self.recipes[recipe_name]:
                self.recipes.pop(recipe)
        else:
            raise TypeError('No such recipe')
