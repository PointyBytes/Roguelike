import json


def load_config(filename):
    with open(filename, "r") as file:
        return json.load(file)


# Load configurations
monsters = load_config("data/monsters.json")
items = load_config("data/items.json")

# These are the files that will be used in the game.
background_image_file = "data/menu_background.png"
game_tiles = "data/Alloy_curses_12x12.png"
