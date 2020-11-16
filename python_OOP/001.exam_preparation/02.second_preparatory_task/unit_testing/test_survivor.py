import unittest

from project.survivor import Survivor


class TestSurvivor(unittest.TestCase):
    def test_set_attr(self):
        s = Survivor("test", 10)
        self.assertEqual(s.name, "test")
        self.assertEqual(s.age, 10)
        self.assertEqual(s.needs, 100)
        self.assertEqual(s.health, 100)

    def test_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            Survivor("", 10)
        self.assertEqual(str(ex.exception), "Name not valid!")

    def test_age_raises(self):
        with self.assertRaises(ValueError) as ex:
            Survivor("test", -10)
        self.assertEqual(str(ex.exception), "Age not valid!")

    def test_health_raises(self):
        s = Survivor("test", 10)
        with self.assertRaises(ValueError) as ex:
            s.health = -10
        self.assertEqual(str(ex.exception), "Health not valid!")

    def test_health_can_not_be_more_than_100(self):
        s = Survivor("test", 10)
        s.health += 20
        self.assertEqual(s.health, 100)

    def test_needs_raises(self):
        s = Survivor("test", 10)
        with self.assertRaises(ValueError) as ex:
            s.needs = -10
        self.assertEqual(str(ex.exception), "Needs not valid!")

    def test_needs_can_not_be_more_than_100(self):
        s = Survivor("test", 10)
        s.needs += 20
        self.assertEqual(s.needs, 100)

    def test_needs_sustain_true(self):
        s = Survivor("test", 10)
        s.needs -= 10
        self.assertEqual(s.needs_sustenance, True)

    def test_needs_sustain_false(self):
        s = Survivor("test", 10)
        s.needs += 10
        self.assertEqual(s.needs_sustenance, False)

    def test_health_sustenance_true(self):
        s = Survivor("test", 10)
        s.health -= 10
        self.assertEqual(s.needs_healing, True)

    def test_health_sustenance_false(self):
        s = Survivor("test", 10)
        s.health += 10
        self.assertEqual(s.needs_healing, False)


if __name__ == "__main__":
    unittest.main()
