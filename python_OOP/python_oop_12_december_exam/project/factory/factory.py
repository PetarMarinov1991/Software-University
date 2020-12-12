from abc import ABC, abstractmethod


class Factory(ABC):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    @abstractmethod
    def add_ingredient(self, ingredient_type, quantity):
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient_type, quantity):
        pass

    def can_add(self, value):
        return value <= self._capacity
