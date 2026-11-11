
from .available_actions import available_actions
from .collect_item import collect_item


def apply_action(player, action):
    action = action.strip().lower()

    movement = action.startswith("go to ")
    is_collection = action.startswith("collect ")

    # Validate the action first.
    legal_actions = available_actions(player)

    if action not in legal_actions:
        return {
            "success": False,
            "message": f"{action} is not available here.",
            "current_location": player["location"],
            "remaining_energy": player["energy"],
            "inventory": player["inventory"]
        }

    # Energy validation.
    if (movement or is_collection) and player["energy"] <= 0:
        return {
            "success": False,
            "message": "You have exhausted your energy.",
            "current_location": player["location"],
            "remaining_energy": player["energy"],
            "inventory": player["inventory"]
        }

    # Item collection.
    if is_collection:
        item = action.replace("collect ", "", 1)
        result = collect_item(player, item)

        if result["success"]:
            player["energy"] -= 1

        result["remaining_energy"] = player["energy"]
        return result

    # Inventory inspection.
    if action == "check inventory":
        return {
            "success": True,
            "message": f"Your inventory: {player['inventory']}",
            "current_location": player["location"],
            "remaining_energy": player["energy"],
            "inventory": player["inventory"]
        }

    # Quit game.
    if action == "quit":
        player["game_over"] = True
        player["game_won"] = False

        return {
            "success": True,
            "message": "You abandoned the island adventure.",
            "current_location": player["location"],
            "remaining_energy": player["energy"],
            "inventory": player["inventory"]
        }

    # Movement destinations.
    destinations = {
        "go to jungle": "Jungle",
        "go to beach": "Beach",
        "go to cave": "Cave",
        "go to old bridge": "Old Bridge",
        "go to lighthouse": "Lighthouse"
    }

    destination = destinations[action]

    # Bridge requirement.
    if (
        player["location"] == "Cave"
        and destination == "Old Bridge"
        and "rope" not in player["inventory"]
    ):
        return {
            "success": False,
            "message": "You need a rope to cross the Old Bridge.",
            "current_location": player["location"],
            "remaining_energy": player["energy"],
            "inventory": player["inventory"]
        }

    player["location"] = destination
    player["energy"] -= 1

    # Energy exhaustion.
    if player["energy"] == 0:
        player["game_over"] = True
        player["game_won"] = False

    return {
        "success": True,
        "message": f"Successfully moved to {destination}.",
        "current_location": player["location"],
        "remaining_energy": player["energy"],
        "inventory": player["inventory"]
    }
