from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit, Food


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return 'Squeak'

    def feed(self, food):
        if not isinstance(food, Vegetable) or not isinstance(food, Fruit):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 0.1 * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return 'Woof!'

    def feed(self, food):
        if not isinstance(food, Meat):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 0.4 * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return 'Meow'

    def feed(self, food):
        if not isinstance(food, Meat) or not isinstance(food, Vegetable):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 0.3 * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return 'ROAR!!!'

    def feed(self, food):
        if not isinstance(food, Meat):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += food.quantity
        self.food_eaten += food.quantity
