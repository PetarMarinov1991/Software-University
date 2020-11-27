class Person:
    id_counter = 0

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.id = Person.id_counter
        Person.id_counter += 1

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self):
        return f'Person {self.id}: {self.name} {self.surname}'

    def __str__(self):
        return self.name + ' ' + self.surname


class Group:
    def __init__(self, name: str, people: [Person]):
        self.name = name
        self.people = people

    def __add__(self, other):
        return Group(self.name, self.people + other.people)

    def __len__(self):
        return len(self.people)

    def __getitem__(self, item):
        return self.people[item].__repr__()

    def __repr__(self):
        return f'Group {self.name} with members {", ".join([str(p) for p in self.people])}'
