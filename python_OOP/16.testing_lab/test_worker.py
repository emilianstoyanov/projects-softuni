from unittest import TestCase


class TestWorker(TestCase):
    def test_workerInit_whenCorrectNameSalaryAndEnergy_shouldBeInitializer(self):
        """
        Test if the worker is initialized with correct name, salary and energy
        """
        name = "Worker name"
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)
        self.assertEqual(name, worker.name)
        self.assertEqual(salary, worker.salary)
        self.assertEqual(energy, worker.energy)
        self.assertEqual(0, worker.money)



