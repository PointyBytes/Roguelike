from game.entity import Actor
from game.fighter import Fighter
from game.equipment import Equipment
from game.inventory import Inventory
from game.level import Level
from game.ai import HostileEnemy


def create_player(x: int, y: int) -> Actor:
    player_config = {
        "char": "@",
        "color": [255, 255, 255],
        "name": "Player",
        "ai_cls": HostileEnemy,
        "equipment": Equipment(),
        "fighter": Fighter(
            hp=30, base_defense=1, base_power=2, base_dexterity=1, base_perception=1
        ),
        "inventory": Inventory(capacity=26),
        "level": Level(level_up_base=200),
    }

    return Actor(
        x=x,
        y=y,
        char=player_config["char"],
        color=tuple(player_config["color"]),
        name=player_config["name"],
        ai_cls=player_config["ai_cls"],
        equipment=player_config["equipment"],
        fighter=player_config["fighter"],
        inventory=player_config["inventory"],
        level=player_config["level"],
    )
