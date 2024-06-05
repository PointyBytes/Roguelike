from game.entity import Actor
from game.ai import PassivePlayer
from game.fighter import Fighter
from game.inventory import Inventory
from game.equipment import Equipment
from game.level import Level


def create_player(x: int, y: int, config: dict) -> Actor:
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
        ai_cls=PassivePlayer,
        equipment=equipment,
        fighter=fighter,
        inventory=inventory,
        level=level,
    )
