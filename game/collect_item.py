def collect_item(player, item):
    location = player.get("location")

    ITEM_LOCATIONS = {
        "rope": "Jungle",
        "lantern": "Cave"
    }


    item = item.strip().lower()
    if item not in ITEM_LOCATIONS or ITEM_LOCATIONS[item] != location:
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
