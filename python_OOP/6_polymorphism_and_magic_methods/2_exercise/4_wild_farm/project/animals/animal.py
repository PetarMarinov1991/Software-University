from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass


class Bird(Animal):
    @abstractmethod
    def __init__(self, name: str, weight: float,  wing_size: float):
        Animal.__init__(self, name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Mammal(Animal):
    @abstractmethod
    def __init__(self, name: str, weight: float, living_region: str):
        Animal.__init__(self, name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'
