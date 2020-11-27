import unittest


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Petar', 5000, 100)
        self.worker_2 = Worker('Ivan', 1000, -1)

    def test_worker_correct_init(self):
        self.assertEqual(self.worker.name, 'Petar')
        self.assertEqual(self.worker.salary, 5000)
        self.assertEqual(self.worker.energy, 100)
        self.assertEqual(self.worker.money, 0)

    def test_if_worker_energy_incremented_after_rest_method_called(self):
        self.assertEqual(self.worker.energy, 100)
        self.worker.rest()
        self.assertEqual(self.worker.energy, 101)

    def test_if_error_raised_if_worker_tries_to_work_with_energy_less_then_or_eq_zero(self):
        with self.assertRaises(Exception):
            self.worker_2.work()
        self.worker_2.rest()
        with self.assertRaises(Exception):
            self.worker_2.work()

    def test_if_worker_gets_salary_after_work_method_called(self):
        self.assertEqual(self.worker.money, 0)
        self.worker.work()
        self.assertEqual(self.worker.money, 5000)

    def test_if_worker_energy_decreased_after_work_method_called(self):
        self.assertEqual(self.worker.energy, 100)
        self.worker.work()
        self.assertEqual(self.worker.energy, 99)

    def test_get_info_method(self):
        result = self.worker.get_info()
        self.assertEqual(result, 'Petar has saved 0 money.')


if __name__ == "__main__":
    unittest.main()
