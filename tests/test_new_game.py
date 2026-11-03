import unittest

from game.new_game import new_game
from game.available_actions import Available_actions

class New_game(unittest.TestCase):
    def test_new_game_starts_correct_state(self):
        player = {
            "name": "Ada",
            "location": "Beach",
            "energy": 5,
            "inventory": [],
            "game_over": False,
            "game_won": False
        }

        result = new_game("Ada")

        self.assertEqual(player["name"], "Ada")
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)
        self.assertEqual(player["inventory"], [])
        self.assertEqual(player["game_over"], False)
        self.assertEqual(player["game_won"], False)


    def test_new_game_creates_independent_inventory(self):
        player_one = {
            "name": "Ada",
            "energy": 5,
            "inventory": []
        }

        player_two = {
            "name": "John",
            "energy": 5,
            "inventory": []
        }

        player_one["inventory"].append("rope")

        self.assertEqual(player_one["inventory"], "rope")
        self.assertEqual(player_two["inventory"], [])


class Available_actions(unittest.TestCase):
    def test_beach_returns_correct_actions(self):
        player = {
            "name": "John",
            "location": "Beach",
            "energy": 5
        }
        result = Available_actions(player)

        self.assertIn("go to jungle", result)
        self.assertIn("check inventory", result)
        self.assertIn("quit", result)
        self.assertNotIn("go to cave", result)


    def test_lighthouse_returns_correct_state(self):
        player = {
            "name": "John",
            "location": "Lighthouse",
            "energy": 5
        }

        result = Available_actions(player)

        self.assertIn("go to old bridge", result)
        self.assertIn("check inventory", result)
        self.assertIn("quit", result)
        self.assertNotIn("go to jungle", result)


    def test_available_actions_does_not_change_player(self):
        player = {
            "name": "John",
            "location": "Beach",
            "energy": 5,
            "inventory": []
        }    

        copy = player.copy()

        result = Available_actions(player)

        self.assertEqual(player, copy)
        self.assertEqual(player["energy"], 5)
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player("inventory"), [])

          

if __name__ = "__main__":
    unittest.main()