from game.ai import HostileEnemy, RangedEnemy
import game.consumable, game.equippable
from game.equipment import Equipment
from game.fighter import Fighter
from game.inventory import Inventory
from game.level import Level
from game.entity import Actor, Item


# The player
player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=1, base_power=2),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

# Monsters
orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)
troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)
rat = Actor(
    char="r",
    color=(107, 122, 109),
    name="Rat",
    ai_cls=RangedEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=2, base_defense=0, base_power=2),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=5),
)
walking_cadaver = Actor(
    char="c",
    color=(238, 122, 109),
    name="Walking Cadaver",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=50, base_defense=0, base_power=5),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=150),
)

# Scrolls & Consumables
confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=game.consumable.ConfusionConsumable(number_of_turns=10),
)
fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=game.consumable.FireballDamageConsumable(damage=12, radius=3),
)
health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=game.consumable.HealingConsumable(amount=4),
)
large_health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Large Health Potion",
    consumable=game.consumable.HealingConsumable(amount=8),
)
lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=game.consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

# Weapons & Armor
dagger = Item(
    char="/", color=(0, 191, 255), name="Dagger", equippable=game.equippable.Dagger()
)
sword = Item(
    char="/", color=(0, 191, 255), name="Sword", equippable=game.equippable.Sword()
)

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=game.equippable.LeatherArmor(),
)
chain_mail = Item(
    char="[",
    color=(139, 69, 19),
    name="Chain Mail",
    equippable=game.equippable.ChainMail(),
)
plate_mail = Item(
    char="[",
    color=(139, 69, 19),
    name="Plate Mail",
    equippable=game.equippable.PlateMail(),
)
