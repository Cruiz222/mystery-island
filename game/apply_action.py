from game.available_actions import available_actions

def apply_action(player, action):
    action = action.strip().lower()

    movement = action.startswith("go to ")
    if movement and player.get("energy", 0) <= 0:
        return {
            "success": False,
            "message": f"{action} failed, you have exhausted your energy",
            "current_location": player.get("location", "Beach"),
            "remaining_energy": player.get("energy", 0)
        }

    legal_action = available_actions(player)

    if action not in legal_action:
        return {
            "success": False,
            "message": f"{action} not supported",
            "current_location": player.get("location"),
            "remaining_energy": player.get("energy")
        }


    if not movement:
        return {
            "success": True,
            "message": f"action executed {action}",
            "current_location": player.get("location", "Beach"),
            "remaining_energy": player.get("energy", 0)
        }    

    destinations = {
            "go to jungle": "Jungle",
            "go to beach": "Beach",
            "go to cave": "Cave",
            "go to old bridge": "Old Bridge",
            "go to lighthouse": "Lighthouse",
        }

    destinations = action.replace("go to ", "").title()    

    player['location'] = destinations
    player['energy'] -= 1

    return {
        "success": True,
        "message": f"succefully moved to {destinations}",
        "current_location": player.get("location"),
        "remaining_energy": player.get("energy")
    }