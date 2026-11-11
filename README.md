# Mystery Island: The Lost Lighthouse

A simple text-based adventure game built with Python. Explore a mysterious island, collect essential items, manage your energy, cross dangerous terrain, and reach the lighthouse to restore its beacon.

## Features

- Interactive text-based gameplay.
- Five explorable locations.
- Energy management system.
- Inventory management.
- Item collection with location restrictions.
- Movement restrictions based on collected items.
- Win and lose conditions.
- Input validation and replay functionality.
- Automated unit tests using Python's built-in `unittest` framework.

## Game Objective

Your mission is to reach the Lighthouse and light its beacon.

To complete your mission, you must:

1. Explore the island.
2. Find and collect the rope.
3. Find and collect the lantern.
4. Use the rope to cross the Old Bridge.
5. Reach the Lighthouse with the lantern.

**Be careful:** You have only 6 energy points. Movement and successful item collection consume energy, so plan your actions wisely.

## Locations

| Location | Available Actions |
|---|---|
| Beach | Travel to Jungle |
| Jungle | Travel to Beach or Cave; collect rope |
| Cave | Travel to Jungle or Old Bridge; collect lantern |
| Old Bridge | Travel to Cave or Lighthouse |
| Lighthouse | Travel back to Old Bridge |

## Requirements

- Python 3.10 or later (if supported by the Python version used to run the project).
- No third-party Python packages are required.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Cruiz222/mystery-island.git
```

### 2. Enter the project directory

```bash
cd mystery-island
```

### 3. Run the game

```bash
python3 main.py
```

## Running Tests

The project uses Python's built-in `unittest` framework.

Run the complete test suite:

```bash
python3 -m unittest discover -s tests -v
```

The tests cover game initialization, available actions, movement rules, energy management, inventory operations, bridge restrictions, and gameplay behaviour.

## Project Structure

```text
mystery-island/
│
├── game/
│   ├── __init__.py
│   ├── new_game.py
│   ├── available_actions.py
│   ├── collect_item.py
│   ├── apply_action.py
│   └── play.py
│
├── tests/
│   ├── test_new_game.py
│   └── test_play.py
│
├── main.py
└── README.md
```

## Technologies

- Python
- unittest
- Git and GitHub

## Author

**Cruiz222**

