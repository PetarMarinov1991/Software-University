from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

    def can_drive(self, air_conditioning, distance):
        fuel_spend = air_conditioning + distance * self.fuel_consumption
        if fuel_spend <= self.fuel_quantity:
            self.fuel_quantity -= fuel_spend


class Car(Vehicle):
    def drive(self, distance):
        air_conditioning = distance * 0.9
        Car.can_drive(self, air_conditioning, distance)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def drive(self, distance):
        air_conditioning = distance * 1.6
        Truck.can_drive(self, air_conditioning, distance)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95
