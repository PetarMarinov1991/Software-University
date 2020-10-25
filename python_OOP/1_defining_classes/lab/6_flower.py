class Flower:
    def __init__(self, name, water_requirements, is_happy=False):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = is_happy

    def water(self, quantity):
        if self.water_requirements <= quantity:
            self.is_happy = True

    def happy_or_not(self):
        if self.is_happy:
            return f'happy'
        return f'not happy'

    def status(self):
        return f'{self.name} is {Flower.happy_or_not(self)}'
