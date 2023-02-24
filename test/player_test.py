# Unit testing for player.py

import unittest
from app.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        testId = "123ADF"
        testName = "Terry"
        human = Player(testId, testName)

    def test_player_name(self):
        self.assertIsEqual(self.id, "123ADF")

    def test_player_uid(self):
        self.assertIsEqual(self.name, "Terry")
