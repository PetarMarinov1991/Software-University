class EasterShop:
    def __init__(self, name, chocolate_factory, egg_factory, paint_factory, storage=None):
        if storage is None:
            storage = {}
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = storage

    def add_chocolate_ingredient(self, type, quantity):
        self.chocolate_factory.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type, quantity):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type, quantity):
        self.paint_factory.add_ingredient(type, quantity)

    def make_chocolate(self, recipe):
        self.chocolate_factory.make_chocolate(recipe)
        if recipe not in self.storage:
            self.storage.update({recipe: 0})
        self.storage[recipe] += 1

    def paint_egg(self, color, egg_type):
        if egg_type not in self.egg_factory.ingredients or color in self.chocolate_factory.ingredients:
            raise ValueError('Invalid commands')
        egg_key = f"{color} {egg_type}"
        if egg_type in self.egg_factory.products:
            if egg_key not in self.storage:
                self.storage.update({egg_key: 0})
            self.storage[egg_key] += 1
            self.egg_factory.remove_ingredient(egg_type, 1)

    def __repr__(self):
        result = ''
        result += f'Shop name: {self.name}\n'
        result += f'Shop Storage:\n'
        for key, value in self.storage.items():
            result += f'{key}: {value}\n'
        return result
