def available_actions(player):
    Valid_locations = [
        "Beach", "Cave",
        "Jungle", "Old Bridge",
        "Lighthouse"
    ]

    current_location = player.get("location", "Beach")

    if current_location not in Valid_locations:
        raise ValueError("invalid location")

    actions = ["check inventory", "quit"]

    if current_location == "Beach":
        actions.insert(0, "go to jungle")

    elif current_location == "Jungle":
        actions.insert(0, "go to beach")
        actions.insert(1, "go to cave")

    elif current_location == "Cave":
        actions.insert(0, "go to jungle")
        actions.insert(1, "go to old bridge")

    elif current_location == "Old Bridge":
        actions.insert(0, "go to cave")
        actions.insert(1, "go to lighthouse")

    elif current_location == "Lighthouse":
        actions.insert(0, "go to old bridge")


    return actions    
