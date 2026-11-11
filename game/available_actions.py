
def available_actions(player):
    valid_locations = [
        "Beach",
        "Jungle",
        "Cave",
        "Old Bridge",
        "Lighthouse"
    ]

    current_location = player.get("location", "Beach")

    if current_location not in valid_locations:
        raise ValueError("Invalid location")

    actions = ["check inventory", "quit"]

    if current_location == "Beach":
        actions.append("go to jungle")

    elif current_location == "Jungle":
        actions.extend([
            "go to beach",
            "go to cave",
            "collect rope"
        ])

    elif current_location == "Cave":
        actions.extend([
            "go to jungle",
            "go to old bridge",
            "collect lantern"
        ])

    elif current_location == "Old Bridge":
        actions.extend([
            "go to cave",
            "go to lighthouse"
        ])

    elif current_location == "Lighthouse":
        actions.append("go to old bridge")

    return actions
