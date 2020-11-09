class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__worker_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals):
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
            return 'Not enough budget'
        return 'Not enough space for animal'

    def hire_worker(self, worker):
        if self.__worker_capacity > len(self.workers):
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        worker = [w for w in self.workers if w.name == worker_name]
        if worker:
            self.workers.remove(worker[0])
            return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        workers_salaries = sum([s.salary for s in self.workers])
        if self.__budget >= workers_salaries:
            self.__budget -= workers_salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        animal_needs = sum([a.get_needs() for a in self.animals])
        if self.__budget >= animal_needs:
            self.__budget -= animal_needs
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, profit):
        self.__budget += profit

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        lions_repr = '\n'.join([l.__repr__() for l in lions])
        tigers = [t for t in self.animals if t.__class__.__name__ == 'Tiger']
        tigers_repr = '\n'.join([t.__repr__() for t in tigers])
        cheetah = [c for c in self.animals if c.__class__.__name__ == 'Cheetah']
        cheetah_repr = '\n'.join([c.__repr__() for c in cheetah])
        return f'You have {len(self.animals)} animals\n' \
               f'----- {len(lions)} Lions:\n' \
               f'{lions_repr}\n' \
               f'----- {len(tigers)} Tigers:\n' \
               f'{tigers_repr}\n' \
               f'----- {len(cheetah)} Cheetahs:\n' \
               f'{cheetah_repr}'

    def workers_status(self):
        keepers = [k for k in self.workers if k.__class__.__name__ == 'Keeper']
        keepers_repr = '\n'.join([k.__repr__() for k in keepers])
        caretakers = [c for c in self.workers if c.__class__.__name__ == 'Caretaker']
        caretakers_repr = '\n'.join([c.__repr__() for c in caretakers])
        vets = [v for v in self.workers if v.__class__.__name__ == 'Vet']
        vets_repr = '\n'.join([v.__repr__() for v in vets])
        return f'You have {len(self.workers)} workers\n' \
               f'----- {len(keepers)} Keepers:\n' \
               f'{keepers_repr}\n' \
               f'----- {len(caretakers)} Caretakers:\n' \
               f'{caretakers_repr}\n' \
               f'----- {len(vets)} Vets:\n' \
               f'{vets_repr}'
