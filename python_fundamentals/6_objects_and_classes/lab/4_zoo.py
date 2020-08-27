class Animal:
    def __init__(self, name):
        self.name = name


class Species:
    MAMMALS = 'mammal'
    FISH = 'fish'
    BIRDS = 'bird'

    @staticmethod
    def get_plural_name(name):
        if name == Species.MAMMALS:
            return 'Mammals'
        if name == Species.FISH:
            return 'Fishes'
        if name == Species.BIRDS:
            return 'Birds'


class Zoo:
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def get_total_animals(self):
        return len(self.mammals) + len(self.fishes) + len(self.birds)

    def add_animal(self, species, name):
        if species == Species.MAMMALS:
            self.mammals.append(name)
        elif species == Species.FISH:
            self.fishes.append(name)
        elif species == Species.BIRDS:
            self.birds.append(name)

    def get_info(self, species):
        animals = ''
        if species == Species.MAMMALS:
            animals = self.mammals
        elif species == Species.FISH:
            animals = self.fishes
        elif species == Species.BIRDS:
            animals = self.birds
        species_name_plural = Species.get_plural_name(species)
        return (
            f'{species_name_plural} in {self.name}: {", ".join([animal.name for animal in animals])}\n'
            f'Total animals: {self.get_total_animals()}'
        )


zoo_name = input()
animals_count = int(input())

zoo = Zoo(zoo_name)

for _ in range(animals_count):
    species, animal_name = input().split(' ', maxsplit=1)
    animal = Animal(animal_name)
    zoo.add_animal(species, animal)

print(zoo.get_info(input()))
