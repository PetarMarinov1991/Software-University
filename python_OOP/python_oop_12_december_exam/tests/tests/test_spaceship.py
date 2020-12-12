import unittest

from project.spaceship.spaceship import Spaceship


class TestSpaceShip(unittest.TestCase):
    def setUp(self):
        self.spaceship = Spaceship('Apollo 13', 2)

    def test_init(self):
        self.assertEqual(self.spaceship.name, 'Apollo 13')
        self.assertEqual(self.spaceship.capacity, 2)
        self.assertEqual(self.spaceship.astronauts, [])

    def test_addRaisesValueError_whenShipIsFull(self):
        self.spaceship.astronauts.append('Yurii Gagarin')
        self.spaceship.astronauts.append('John Crichton')
        with self.assertRaises(ValueError) as ex:
            self.spaceship.add('Batman')
        self.assertEqual(str(ex.exception), 'Spaceship is full')

    def test_addRaisesValueError_whenAstronautAlreadyInSpaceship(self):
        self.spaceship.astronauts.append('Yurii Gagarin')
        with self.assertRaises(ValueError) as ex:
            self.spaceship.add('Yurii Gagarin')
        self.assertEqual(str(ex.exception), 'Astronaut Yurii Gagarin Exists')

    def test_add_append(self):
        self.spaceship.add('Yurii Gagarin')
        self.assertEqual(self.spaceship.astronauts, ['Yurii Gagarin'])

    def test_remove_removesAstronaut_whenAstronautIn(self):
        self.spaceship.astronauts.append('Yurii Gagarin')
        self.spaceship.astronauts.append('John Crichton')
        self.spaceship.remove('Yurii Gagarin')
        self.assertEqual(self.spaceship.astronauts, ['John Crichton'])

    def test_remove_raisesValueError_whenAstronautNotIn(self):
        with self.assertRaises(ValueError) as ex:
            self.spaceship.remove('Yurii Gagarin')
        self.assertEqual(str(ex.exception), 'Astronaut Not Found')
