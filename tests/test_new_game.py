import copy
import unittest
from game.new_game import new_game
from game.available_actions import available_actions
from game.apply_action import apply_action
from game.collect_item import collect_item

class TestNewGame(unittest.TestCase):
    def test_new_game_starts_correct_state(self):

        result = new_game("Ada")

        self.assertEqual(result["name"], "Ada")
        self.assertEqual(result["location"], "Beach")
        self.assertEqual(result["energy"], 6)
        self.assertEqual(result["inventory"], [])
        self.assertEqual(result["game_over"], False)
        self.assertEqual(result["game_won"], False)




    def test_new_game_creates_independent_inventory(self):
        
        player_one = new_game("Ada")
        player_two = new_game("John")

        player_one["inventory"].append("rope")

        self.assertEqual(player_one["inventory"], ["rope"])
        self.assertEqual(player_two["inventory"], [])


class TestAvailableActions(unittest.TestCase):
    def test_beach_returns_correct_actions(self):
        player = {
            "name": "John",
            "location": "Beach",
            "energy": 6
        }
        result = available_actions(player)

        self.assertIn("go to jungle", result)
        self.assertIn("check inventory", result)
        self.assertIn("quit", result)
        self.assertNotIn("go to cave", result)


    def test_lighthouse_returns_correct_state(self):
        player = {
            "name": "John",
            "location": "Lighthouse",
            "energy": 6
        }

        result = available_actions(player)

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

        player_copy = copy.deepcopy(player)

        result = available_actions(player)

        self.assertEqual(player, player_copy)
        self.assertEqual(player["energy"], 5)
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["inventory"], [])



class TestApplyAction(unittest.TestCase):
    def test_legal_move_produces_the_right_state(self):
        player = {
            "name": "Ada",
            "location": "Beach",
            "energy": 6,
            "game_over": False,
            "game_won": False,
            "inventory": []
        }  

        result = apply_action(player, "go to jungle")

        self.assertTrue(result["success"])
        self.assertEqual(result["current_location"], "Jungle")
        self.assertEqual(result["remaining_energy"], 5)
        self.assertEqual(player["location"], "Jungle")
        self.assertEqual(player["energy"], 5)


    def test_illegal_move_does_not_change_player_state(self):
        player = {
            "name": "Ada",
            "location": "Beach",
            "energy": 6,
            "game_over": False,
            "game_won": False,
            "inventory": []
        }

        result = apply_action(player, "go to Cave") 
        
        self.assertFalse(result["success"])
        self.assertEqual(result["remaining_energy"], 6)
        self.assertEqual(result["current_location"], "Beach")
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 6)


    def test_move_with_zero_energy_does_not_change_state(self):
        player = {
            "name": "Ada",
            "location": "Beach",
            "energy": 0,
            "inventory": [],
            "game_over": False,
            "game_won": False
        }

        result = apply_action(player, "go to jungle")

        self.assertFalse(result["success"])
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 0)


    def test_reaching_lighthouse_with_zero_energy_does_not_end_game(self):
        player = {
            "name": "Ada",
            "location": "Old Bridge",
            "energy": 1,
            "inventory": ["rope", "lantern"],
            "game_over": False,
            "game_won": False
        }

        result = apply_action(player, "go to lighthouse")

        self.assertTrue(result["success"])
        self.assertEqual(player["location"], "Lighthouse")
        self.assertEqual(player["energy"], 0)
        self.assertFalse(player["game_over"])
        self.assertFalse(player["game_won"])


    def test_crossing_bridge_with_rope_is_successful(self):
        player = {
            "name": "Ada",
            "location": "Cave",
            "energy": 4,
            "inventory": ["rope"],
            "game_over": False,
            "game_won": False
        }

        result = apply_action(player, "go to old bridge")

        self.assertTrue(result["success"])
        self.assertEqual(player["location"], "Old Bridge")
        self.assertEqual(player["energy"], 3)


    def test_quitting_game_sets_game_over(self):
        player = {
            "name": "Ada",
            "location": "Beach",
            "energy": 6,
            "inventory": [],
            "game_over": False,
            "game_won": False
        }

        result = apply_action(player, "quit")

        self.assertTrue(result["success"])
        self.assertTrue(player["game_over"])
        self.assertFalse(player["game_won"])
        self.assertEqual(player["energy"], 6)


    def test_player_can_complete_the_full_winning_route(self):
        player = new_game("Ada")

        winning_actions = [
            "go to jungle",
            "collect rope",
            "go to cave",
            "collect lantern",
            "go to old bridge",
            "go to lighthouse"
        ]

        for action in winning_actions:
            result = apply_action(player, action)
            self.assertTrue(result["success"], result["message"])

        self.assertEqual(player["location"], "Lighthouse")
        self.assertEqual(player["inventory"], ["rope", "lantern"])
        self.assertEqual(player["energy"], 0)
        self.assertFalse(player["game_over"])


    def test_crossing_bridge_without_rope_is_rejected(self):
        player = new_game("Ada")
        player["location"] = "Old Bridge"

        result = apply_action(player, "go to lighthouse")

        self.assertFalse(result["success"])
        self.assertEqual(player["location"], "Old Bridge")                



class TestCollectItem(unittest.TestCase):
    def test_collecting_item_at_right_location_is_successful(self):
        player = {
            "name": "Ada",
            "location": "Cave",
            "inventory": [],
            "energy": 6,
            "game_over": False,
            "game_won": False
        }

        result = collect_item(player, "lantern")

        self.assertTrue(result["success"])
        self.assertEqual(result["current_location"], "Cave")
        self.assertEqual(result["inventory"], ["lantern"])
        self.assertEqual(player["inventory"], ["lantern"])
        self.assertEqual(player["location"], "Cave")       
          

    def test_collecting_item_at_wrong_location_is_rejected(self):
        player = {
            "name": "Ada",
            "location": "Cave",
            "inventory": [],
            "energy": 6,
            "game_over": False,
            "game_won": False
        }

        result = collect_item(player, "rope")

        self.assertFalse(result["success"])
        self.assertEqual(result["current_location"], "Cave")
        self.assertEqual(player["inventory"], [])
        self.assertEqual(player["location"], "Cave")


    def test_collecting_same_item_twice_is_rejected(self):
        player = {
            "name": "Ada",
            "location": "Jungle",
            "inventory": ["rope"],
            "energy": 6,
            "game_over": False,
            "game_won": False
        }

        result = collect_item(player, "rope")

        self.assertFalse(result["success"])
        self.assertEqual(result["inventory"], ["rope"])
        self.assertEqual(player["inventory"], ["rope"])


    def test_successful_collection_adds_to_inventory_and_reduce_energy(self):
        player = {
            "name": "Ada",
            "location": "Jungle",
            "inventory": [],
            "energy": 6,
            "game_over": False,
            "game_won": False
        }

        result = apply_action(player, "collect rope")

        self.assertTrue(result["success"])
        self.assertEqual(result["current_location"], "Jungle")
        self.assertEqual(result["remaining_energy"], 5)
        self.assertEqual(player["inventory"], ["rope"])
        self.assertEqual(player["energy"], 5)



    def test_failed_collection_does_not_update_inventory_nor_reduce_energy(self):
        player = {
            "name": "Ada",
            "location": "Jungle",
            "inventory": [],
            "energy": 6,
            "game_over": False,
            "game_won": False
        }    

        result = collect_item(player, "lantern")

        self.assertFalse(result["success"])
        self.assertEqual(result["inventory"], [])
        self.assertEqual(player["inventory"], [])
        self.assertEqual(player["energy"], 6)

 

if __name__ == "__main__":
    unittest.main()