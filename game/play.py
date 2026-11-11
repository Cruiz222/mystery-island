
from .new_game import new_game
from .available_actions import available_actions
from .apply_action import apply_action


def play_game():
    while True:
        print("\n=== MYSTERY ISLAND: THE LOST LIGHTHOUSE ===")
        print("Find the rope, collect the lantern, and light the beacon.")
        print("You have 6 energy points. Choose your actions wisely.\n")

        name = input("Enter your name: ").strip()
        if not name:
            name = "Explorer"

        player = new_game(name)

        while not player["game_over"]:
            print("\n" + "=" * 40)
            print(f"Explorer: {player['name']}")
            print(f"Location: {player['location']}")
            print(f"Energy: {player['energy']}")
            print(f"Inventory: {player['inventory']}")

            if player["energy"] <= 0:
                player["game_over"] = True
                player["game_won"] = False
                print("\nYou have run out of energy. Game over!")
                break

            actions = available_actions(player)

            print("\nAvailable actions:")
            for index, action in enumerate(actions, start=1):
                print(f"{index}. {action}")

            choice = input("\nChoose an action: ").strip()

            if choice.isdigit():
                index = int(choice) - 1

                if 0 <= index < len(actions):
                    choice = actions[index]
                else:
                    print("Invalid menu selection.")
                    continue

            result = apply_action(player, choice)
            print(f"\n{result['message']}")

            if (
                player["location"] == "Lighthouse"
                and "lantern" in player["inventory"]
                and not player["game_over"]
            ):
                player["game_won"] = True
                player["game_over"] = True
                print("\nYOU WIN! You successfully lit the lighthouse beacon!")
                break

            if player["game_over"]:
                break

        if not player["game_won"]:
            print("\nGame ended. Better luck next time!")

        replay = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        if replay in ("yes", "y"):
            play_game()
            break

        elif replay in ("no", "n"):
            print("Thank you for trying.. Goodbye") 
            return

        else:
            print("Invalid input... input no or yes")       
