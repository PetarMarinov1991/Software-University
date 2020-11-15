class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return self.name + ' ' + other.surname

    def __repr__(self):
        return self.name + ' ' + self.surname


class Group:
    def __init__(self, name: str, people: [Person]):
        self.name = name
        self.people = people

    def __add__(self, other):
        return self.people + other.people

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        return f'Group {self.name} with members {", ".join([str(p) for p in self.people])}'
