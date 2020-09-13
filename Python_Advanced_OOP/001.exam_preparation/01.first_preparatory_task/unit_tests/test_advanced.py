from project.player.advanced import Advanced
import unittest


class TestsAdvancedPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Advanced("Peter")

    def test_init_should_create_player_attributes(self):
        self.assertEqual(self.player.username, "Peter")
        self.assertEqual(self.player.health, 250)
        self.assertEqual(self.player.card_repository.__class__.__name__, "CardRepository")

    def test_set_username_empty_string_should_raise_error(self):
        with self.assertRaises(ValueError) as cm:
            self.player.username = ""
        self.assertEqual(str(cm.exception), "Player's username cannot be an empty string.")

    def test_set_health_less_than_zero_should_raise_error(self):
        with self.assertRaises(ValueError) as cm:
            self.player.health = -1
        self.assertEqual(str(cm.exception), "Player's health bonus cannot be less than zero.")

    def test_take_damage_less_than_zero_should_raise_error(self):
        with self.assertRaises(ValueError) as cm:
            self.player.take_damage(-1)
        self.assertEqual(str(cm.exception), "Damage points cannot be less than zero")

    def test_take_damage_should_decrease_player_health(self):
        self.player.take_damage(50)
        actual = self.player.health
        expected = 200
        self.assertEqual(actual, expected)

    def test_is_dead_should_return_true(self):
        self.player.health = 0
        self.assertTrue(self.player.is_dead)

    def test_is_dead_should_return_false(self):
        self.assertFalse(self.player.is_dead)


if __name__ == "__main__":
    unittest.main()
