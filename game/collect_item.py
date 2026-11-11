
def collect_item(player, item):
    item_locations = {
        "rope": "Jungle",
        "lantern": "Cave"
    }

    item = item.strip().lower()
    location = player["location"]
    inventory = player["inventory"]

    if item not in item_locations:
        return {
            "success": False,
            "message": f"Unknown item: {item}",
            "current_location": location,
            "inventory": inventory
        }

    if item_locations[item] != location:
        return {
            "success": False,
            "message": f"You cannot collect {item} here.",
            "current_location": location,
            "inventory": inventory
        }

    if item in inventory:
        return {
            "success": False,
            "message": f"You already have {item}.",
            "current_location": location,
            "inventory": inventory
        }

    inventory.append(item)

    return {
        "success": True,
        "message": f"You collected {item}.",
        "current_location": location,
        "inventory": inventory
    }
