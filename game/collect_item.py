def collect_item(player, item):
    location = player.get("location")

    ITEM_LOCATION = {
        "rope": "Jungle",
        "lantern": "Cave"
    }

    item = item.lower()
    if ITEM_LOCATION != location:
        return {
            "success": False,
            "message": f"Action failed: {item} cannot be collected at this location",
            "current_location": location,
            "inventory": player.get("inventory")
        }
    
    if item in player["inventory"]:
        return {
            "success": False,
            "message": f"Action failed: {item} already exists",
            "current_location": location,
            "inventory": player.get("inventory")
        }

    player["inventory"].append(item)
    return {
        "success": True,
        "message": f"{item} successfully collected",
        "current_location": location,
        "inventory": player.get("inventory")
    }
