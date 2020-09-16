import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def test_attributes(self):
        hard = Hardware('hard', 'test', 100, 100)
        self.assertEqual('hard', hard.name)
        self.assertEqual('test', hard.type)
        self.assertEqual(100, hard.memory)
        self.assertEqual(100, hard.capacity)
        self.assertEqual([], hard.software_components)
        self.assertListEqual([], hard.software_components)

    def test_install(self):
        hard = Hardware('h1', 'test', 100, 100)
        s1 = Software('win', 'Express', 120, 120)
        with self.assertRaises(Exception) as context:
            hard.install(s1)
        self.assertEqual(str(context.exception), 'Software cannot be installed')

    def test_uninstall(self):
        hard = Hardware('h1', 'test', 100, 100)
        s1 = Software('win', 'Express', 10, 10)
        hard.install(s1)
        hard.uninstall(s1)
        self.assertEqual([], hard.software_components)
        self.assertListEqual([], hard.software_components)


if __name__ == '__main__':
    unittest.main()
