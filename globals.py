import json

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

player_atk = (224, 224, 224)
enemy_atk = (255, 192, 192)
needs_target = (63, 255, 255)
status_effect_applied = (63, 255, 63)
descend = (159, 63, 255)

player_die = (255, 48, 48)
enemy_die = (255, 160, 48)

invalid = (255, 255, 0)
impossible = (128, 128, 128)
error = (255, 64, 64)

welcome_text = (32, 160, 255)
health_recovered = (0, 255, 0)

hp_bar_text = white
hp_bar_filled = (0, 96, 0)
hp_bar_empty = (64, 16, 16)

exp_bar_text = white
exp_bar_filled = (32, 32, 144)
exp_bar_empty = (16, 16, 64)

menu_title = (255, 255, 63)
menu_text = white


# These are the files that will be used in the game.
background_image_file = "data/menu_background.png"
game_tiles = "data/Alloy_curses_12x12.png"


def load_config(filename):
    with open(filename, "r") as file:
        return json.load(file)


# Load configurations
monsters = load_config("data/monsters.json")
items = load_config("data/items.json")
