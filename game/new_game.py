
def new_game(name):
    return {
        "name": name.strip(),
        "location": "Beach",
        "energy": 6,
        "inventory": [],
        "game_over": False,
        "game_won": False
    }
