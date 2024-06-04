from copy import deepcopy
import json
import globals
from game.entity import Actor, Item
from game.ai import HostileEnemy, SkittishEnemy
import game.consumable, game.equippable
from game.equipment import Equipment
from game.fighter import Fighter
from game.inventory import Inventory
from game.level import Level
from game.player import create_player


def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


monsters = load_data("data/monsters.json")
items = load_data("data/items.json")
player_data = load_data("data/player.json")


def create_actor(config, x, y):
    ai_cls = globals()[config["ai_cls"]]
    fighter = Fighter(**config["fighter"])
    inventory = Inventory(**config["inventory"])
    equipment = Equipment()
    level = Level(**config["level"])

    return Actor(
        x=x,
        y=y,
        char=config["char"],
        color=tuple(config["color"]),
        name=config["name"],
        ai_cls=ai_cls,
        equipment=equipment,
        fighter=fighter,
        inventory=inventory,
        level=level,
    )


def create_item(config, x, y):
    if "consumable" in config:
        consumable_type = getattr(game.consumable, config["consumable"]["type"])
        consumable = consumable_type(
            **{k: v for k, v in config["consumable"].items() if k != "type"}
        )
        return Item(
            x=x,
            y=y,
            char=config["char"],
            color=tuple(config["color"]),
            name=config["name"],
            consumable=consumable,
        )
    elif "equippable" in config:
        equippable_type = getattr(game.equippable, config["equippable"]["type"])
        equippable = equippable_type()
        return Item(
            x=x,
            y=y,
            char=config["char"],
            color=tuple(config["color"]),
            name=config["name"],
            equippable=equippable,
        )
    else:
        return Item(
            x=x,
            y=y,
            char=config["char"],
            color=tuple(config["color"]),
            name=config["name"],
        )


def spawn_monster(monster_name, x, y):
    monster_config = monsters[monster_name]
    return create_actor(monster_config, x, y)


def spawn_item(item_name, x, y):
    item_config = items[item_name]
    return create_item(item_config, x, y)


def spawn_player(x, y):
    return create_player(x, y)
