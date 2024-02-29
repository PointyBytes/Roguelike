from __future__ import annotations
from typing import TYPE_CHECKING
from game.message_log import MessageLog

if TYPE_CHECKING:
    from game.entity import Actor


class GameEffect:
    """Base class for all effects. Describes a persistent effect on an Entity."""

    def __init__(self, name: str, duration: int = -1, damage_per_turn: int = 0):
        self.duration = duration
        self.damage_per_turn = damage_per_turn
        self.name = name

    def on_tick(self, entity: Actor, num_ticks: int):
        raise NotImplementedError()

    def on_apply(self, entity: Actor, message_log: MessageLog):
        """Execute actions when the effect is applied."""
        # Example: add a message to the log
        message_log.add_message(f"{e.name} is affected by {self.name}.")
        raise NotImplementedError()

    def on_remove(self, entity: Actor, message_log: MessageLog):
        """Execute actions when the effect is removed."""
        # Example: add a message to the log
        message_log.add_message(f"{e.name} is no longer affected by {self.name}.")
        raise NotImplementedError()

    def on_merge(self, effect: GameEffect):
        """Effects refresh duration on merge by default."""
        self.duration = max(self.duration, effect.duration)

    @property
    def expired(self) -> bool:
        return self.duration == 0


class HealingEffect(GameEffect):
    """Effect representing healing/regeneration."""

    def __init__(self, amount: int):
        self.amount = amount

    def apply(self, entity: Actor) -> None:
        entity.fighter.heal(self.amount)


class PoisonEffect(GameEffect):
    """Effect representing poisoning."""

    def __init__(self, damage_per_turn: int, duration: int):
        self.damage_per_turn = damage_per_turn
        self.duration = duration

    def apply(self, entity: Actor) -> None:
        entity.take_damage(self.damage_per_turn)
        self.duration -= 1


class BleedEffect(GameEffect):
    """Describes damage over time caused by bleeding."""

    def __init__(self, damage_per_turn: int, duration: int):
        self.damage_per_turn = damage_per_turn
        self.duration = duration

    def apply(self, entity: Actor) -> None:
        entity.take_damage(self.damage_per_turn)
        self.duration -= 1


class BurningEffect(GameEffect):
    def __init__(self, duration: int, potency: int):
        super().__init__("Burning", duration, potency)


class StunnedEffect(GameEffect):
    def __init__(self, duration):
        super().__init__("Stunned", duration, 0)


# Old code to be merged with the code above. Note that there is a different coding style to the one above.
class GameEffect:
    """Describes a persistent effect on an Entity."""

    def tick(self, entity: Actor, num_ticks: int = 1):
        self.on_tick(e, num_ticks)
        if self.duration > 0:
            self.duration = max(self.duration - num_ticks, 0)

    def __str__(self) -> str:
        addendum = ""
        has_duration = self.duration > 0
        has_potency = self.potency > 0

        if has_duration and has_potency:
            addendum = f" {self.potency}({self.duration} t)"
        elif has_duration:
            addendum = f"({self.duration} t)"
        elif has_potency:
            addendum = f" {self.potency}"

        return f"{self.name}{addendum}"


class BleedEffect(GameEffect):
    """Describes damage over time caused by bleeding."""

    def __init__(self, duration: int, potency: int):
        super().__init__("Bleed", duration, potency)

    def on_apply(self, entity: Actor):
        add_msg_about(entity, "<entity> is bleeding!")

    def on_tick(self, entity: Actor, num_ticks: int):
        dmg = self.potency * num_ticks
        entity.components[comps.Combatant].damage(1)
        add_msg_about(entity, f"<entity> bleeds for {dmg} damage!")

    def on_merge(self, eff: GameEffect):
        """Bleed is nasty, stacking potency AND refreshing duration."""
        self.potency += eff.potency
        super().on_merge(eff)

    def on_remove(self, entity: Actor):
        add_msg_about(entity, "<entity> is no longer bleeding.")


class HealingEffect(GameEffect):
    def __init__(self, duration: int, potency: int):
        super().__init__("Healing", duration, potency)

    def on_apply(self, entity: Actor):
        add_msg_about(e, "<entity> is healing!")

    def on_tick(self, entity: Actor, num_ticks: int):
        amt = self.potency * num_ticks
        entity.components[comps.Combatant].heal(amt)
        add_msg_about(entity, f"<entity> heals {amt} damage!")

    def on_remove(self, entity: Actor):
        add_msg_about(entity, "<entity> is no longer healing.")


class PoisonEffect(GameEffect):
    def __init__(self, duration: int, potency: int):
        super().__init__("Poison", duration, potency)

    def on_apply(self, entity: Actor):
        add_msg_about(entity, "<entity> is poisoned!")

    def on_tick(self, entity: Actor, num_ticks: int):
        amt = self.potency * num_ticks
        entity.components[comps.Combatant].damage(amt)
        add_msg_about(entity, f"<entity> takes {amt} damage from poison!")

    def on_remove(self, entity: Actor):
        add_msg_about(entity, "<entity> is no longer poisoned.")


class LightningEffect(GameEffect):
    def __init__(self, potency: int):
        super().__init__("Lightning", 0, potency)

    def on_apply(self, entity: Actor):
        low = max(0, self.potency - 3)
        high = self.potency + 3
        dmg = cbt.gauss_roll(low, high)
        entity.components[comps.Combatant].damage(dmg)
        add_msg_about(entity, f"<entity> is struck by lightning for {dmg} damage!")


class BurningEffect(GameEffect):
    def __init__(self, duration: int, potency: int):
        super().__init__("Burning", duration, potency)

    def on_apply(self, entity: Actor):
        add_msg_about(entity, "<entity> is burning!")

    def on_tick(self, entity: Actor, num_ticks: int):
        entity.components[comps.comps.Combatant].damage(self.potency)
        add_msg_about(entity, f"<entity> burns for {self.potency} damage!")

    def on_merge(self, eff: GameEffect):
        # Burn stacks duration
        self.duration += eff.duration

    def on_remove(self, entity: Actor):
        add_msg_about(entity, "<entity>'s flames burn out.")


class StunnedEffect(GameEffect):
    def __init__(self, duration):
        super().__init__("Stunned", duration, 0)

    def on_apply(self, entity: Actor):
        add_msg_about(entity, "<entity> is stunned!")

    def on_remove(self, entity: Actor):
        add_msg_about(entity, "<entity> is no longer stunned.")
