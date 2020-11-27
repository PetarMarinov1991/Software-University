import unittest


class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class CatTest(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('Garfield')

    def test_cat_size_increased_after_eating(self):
        self.assertEqual(self.cat.size, 0)
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        self.assertEqual(self.cat.fed, False)
        self.cat.eat()
        self.assertEqual(self.cat.fed, True)

    def test_cat_cant_eat_if_already_fed_raises_error(self):
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_cant_sleep_if_not_fed_raises_error(self):
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertEqual(self.cat.sleepy, False)


if __name__ == "__main__":
    unittest.main()
