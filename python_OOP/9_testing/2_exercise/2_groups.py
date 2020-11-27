import unittest


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

    def __str__(self):
        return f'Group {self.name} with members {", ".join([str(p) for p in self.people])}'


class TestPerson(unittest.TestCase):
    def setUp(self):
        Person.id_counter = 0
        self.person_1 = Person('Valeri', 'Bojinov')

    def test_custom_repr(self):
        result = repr(self.person_1)
        self.assertIn('Valeri', result)
        self.assertNotIn('Nikoleta', result)
        self.assertEqual(result, 'Person 0: Valeri Bojinov')

    def test_custom_str(self):
        result = str(self.person_1)
        self.assertIn('Bojinov', result)
        self.assertNotIn('Person', result)
        self.assertEqual(result, 'Valeri Bojinov')

    def test_auto_incremented_id(self):
        current_id = Person.id_counter
        person_2 = Person('2', '2')
        self.assertEqual(current_id, 1)
        self.assertEqual(person_2.id, 1)
        self.assertEqual(Person.id_counter, 2)

    def test_custom_add(self):
        person_2 = Person('Niki', 'Mihaylov')
        person_3 = self.person_1 + person_2
        self.assertEqual(person_3.name, 'Valeri')
        self.assertEqual(person_3.surname, 'Mihaylov')

    def test_set_attributes(self):
        self.assertEqual(self.person_1.name, 'Valeri')
        self.assertEqual(self.person_1.surname, 'Bojinov')


class TestGroup(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person('Valeri', 'Bojinov')
        self.person_2 = Person('Niki', 'Mihaylov')
        self.group = Group('A grupa', [self.person_1, self.person_2])

    def test_custom_len(self):
        self.assertEqual(len(self.group), 2)

    def test_custom_add(self):
        person_3 = Person('Nikoleta', 'Lozanova')
        group_2 = Group('sex', [person_3])
        group_3 = self.group + group_2
        self.assertEqual(len(group_3), 3)

    def test_custom_get_item(self):
        result = self.group[1]
        self.assertIn('Niki', result)
        self.assertEqual(result, 'Person 1: Niki Mihaylov')

    def test_custom_get_item_invalid_idx(self):
        with self.assertRaises(IndexError):
            result = self.group[2]

    def test_custom_repr(self):
        result = repr(self.group)
        self.assertIn('Group', result)
        self.assertIn('Valeri', result)
        self.assertIn('Niki', result)
        self.assertNotIn('Nikoleta', result)
        self.assertEqual(result, f'Group A grupa with members Valeri Bojinov, Niki Mihaylov')

    def test_custom_str(self):
        result = str(self.group)
        self.assertIn('Group', result)
        self.assertIn('Valeri', result)
        self.assertIn('Niki', result)
        self.assertNotIn('Nikoleta', result)
        self.assertEqual(result, f'Group A grupa with members Valeri Bojinov, Niki Mihaylov')

    def test_set_attributes(self):
        self.assertEqual(self.group.name, 'A grupa')
        self.assertEqual(len(self.group.people), 2)


if __name__ == "__main__":
    unittest.main()
