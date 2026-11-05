from game.available_actions import available_actions
from game.collect_item import collect_item

def apply_action(player, action):
    action = action.strip().lower()

    movement = action.startswith("go to ")
    is_collection = action.startswith("collect ")

    legal_action = available_actions(player)
    if action not in legal_action:
        return {
            "success": False,
            "message": f"{action} not supported",
            "current_location": player.get("location"),
            "remaining_energy": player.get("energy")
        }

    if (is_collection or movement) and player.get("energy", 0) <= 0:
        return {
            "success": False,
            "message": f"{action} failed, you have exhausted your energy",
            "current_location": player.get("location", "Beach"),
            "remaining_energy": player.get("energy", 0)
        }    

    if is_collection:
        item_name = action.replace("collect ", "").strip()

        result = collect_item(player, item_name)

        if result.get("success"):
            player["energy"] -= 1  
            return {
                "success": True,
                "message": f"{item_name} successfully collected",
                "current_location": player.get("location"),
                "inventory": player.get("inventory"),
                "remaining_energy": player.get("energy")
            }   
        else:
            return {
                "success": False,
                "message": result.get("message", "collection failed"),
                "current_location": player.get("location"),
                "remaining_energy": player.get("energy"),
                "inventory": player.get("inventory")
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

    destination = destinations[action]
    player['location'] = destination
    player['energy'] -= 1

    return {
        "success": True,
        "message": f"succefully moved to {destination}",
        "current_location": player.get("location"),
        "remaining_energy": player.get("energy")
    }
