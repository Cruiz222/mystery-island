
import unittest
from unittest.mock import patch
from game.play import play_game


class TestPlayGame(unittest.TestCase):

    
    @patch("builtins.input", side_effect=[
    "Ada",
    "go to jungle",
    "go to cave",
    "go to jungle",
    "go to beach",
    "go to jungle",
    "go to beach",
    "no"
    ])
    def test_player_loses_when_energy_runs_out(self, mock_input):
        with patch("builtins.print") as mock_print:
            play_game()

        printed_messages = [
            str(call) for call in mock_print.call_args_list
        ]

        self.assertTrue(
            any(
                "run out of energy" in message
                for message in printed_messages
            )
        )

    @patch("builtins.input", side_effect=[
        "Ada",
        "quit",
        "yes",
        "John",
        "quit",
        "no"
    ])
    def test_player_can_replay_game(self, mock_input):
        with patch("builtins.print") as mock_print:
            play_game()

        printed_messages = [
            str(call) for call in mock_print.call_args_list
        ]

        game_titles = [
            message for message in printed_messages
            if "MYSTERY ISLAND" in message
        ]

        self.assertEqual(len(game_titles), 2)

    @patch("builtins.input", side_effect=[
        "Ada",
        "quit",
        "no"
    ])
    def test_declining_replay_exits_game(self, mock_input):
        with patch("builtins.print"):
            play_game()

        self.assertEqual(mock_input.call_count, 3)


if __name__ == "__main__":
    unittest.main()
