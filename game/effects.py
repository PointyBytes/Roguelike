from __future__ import annotations
from typing import TYPE_CHECKING
from game.engine import MessageLog

if TYPE_CHECKING:
    from game.entity import Actor


# TODO: See to it that all of the code below starts to work
class GameEffect:
    """Base class for all effects. Describes a persistent effect on an Entity."""

    def __init__(self, name: str, duration: int = -1, damage_per_turn: int = 0):
        self.message_log = MessageLog()
        self.entety = Actor()
        self.duration = duration
        self.damage_per_turn = damage_per_turn
        self.name = name

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

    def tick(self, entity: Actor, num_ticks: int = 1):
        self.on_tick(entety, num_ticks)
        if self.duration > 0:
            self.duration = max(self.duration - num_ticks, 0)

    def on_apply(self, entity: Actor):
        """Execute actions when the effect is applied."""
        # Example: add a message to the log
        self.message_log.add_message(f"{entity.name} is affected by {self.name}.")
        raise NotImplementedError()

    def on_remove(self, entity: Actor):
        """Execute actions when the effect is removed."""
        # Example: add a message to the log
        self.message_log.add_message(
            f"{entity.name} is no longer affected by {self.name}."
        )
        raise NotImplementedError()

    def on_merge(self, effect: GameEffect):
        """Effects refresh duration on merge by default."""
        self.duration = max(self.duration, effect.duration)

    @property
    def expired(self) -> bool:
        return self.duration == 0


class HealingEffect(GameEffect):
    def __init__(self, duration: int, potency: int, entety: Actor):
        super().__init__("Healing", duration, potency)

    def on_apply(self, entity: Actor):
        self.message_log.add_message(entety, "<entity> is healing!")

    def on_tick(self, entity: Actor, num_ticks: int):
        amount = self.potency * num_ticks
        entity.components[comps.Combatant].heal(amount)
        self.message_log.add_message(entity, f"<entity> heals {amount} damage!")

    def on_remove(self, entity: Actor):
        self.message_log.add_message(entity, "<entity> is no longer healing.")


class PoisonEffect(GameEffect):
    def __init__(self, duration: int, potency: int):
        super().__init__("Poison", duration, potency)

    def on_apply(self, entity: Actor):
        self.message_log.add_message(entity, "<entity> is poisoned!")

    def on_tick(self, entity: Actor, num_ticks: int):
        amount = self.potency * num_ticks
        entity.components[comps.Combatant].damage(amount)
        self.message_log.add_message(
            entity, f"<entity> takes {amount} damage from poison!"
        )

    def on_remove(self, entity: Actor):
        self.message_log.add_message(entity, "<entity> is no longer poisoned.")


class BleedEffect(GameEffect):
    """Describes damage over time caused by bleeding."""

    def __init__(self, duration: int, potency: int):
        super().__init__("Bleed", duration, potency)

    def on_apply(self, entity: Actor):
        self.message_log.add_message(entity, "<entity> is bleeding!")

    def on_tick(self, entity: Actor, num_ticks: int):
        dmg = self.potency * num_ticks
        entity.components[comps.Combatant].damage(1)
        self.message_log.add_message(entity, f"<entity> bleeds for {dmg} damage!")

    def on_merge(self, effect: GameEffect):
        """Bleed is nasty, stacking potency AND refreshing duration."""
        self.potency += effect.potency
        super().on_merge(effect)

    def on_remove(self, entity: Actor):
        self.message_log.add_message(entity, "<entity> is no longer bleeding.")


class BurningEffect(GameEffect):
    def __init__(self, duration: int, potency: int):
        super().__init__("Burning", duration, potency)

    def on_apply(self, entity: Actor):
        self.message_log.add_message(entity, "<entity> is burning!")

    def on_tick(self, entity: Actor, num_ticks: int):
        entity.components[comps.comps.Combatant].damage(self.potency)
        self.message_log.add_message(
            entity, f"<entity> burns for {self.potency} damage!"
        )

    def on_merge(self, effect: GameEffect):
        # Burn stacks duration
        self.duration += effect.duration

    def on_remove(self, entity: Actor):
        self.message_log.add_message(entity, "<entity>'s flames burn out.")


class StunnedEffect(GameEffect):
    def __init__(self, duration):
        super().__init__("Stunned", duration, 0)

    def on_apply(self, entity: Actor):
        self.message_log.add_message(entity, "<entity> is stunned!")

    def on_remove(self, entity: Actor):
        self.message_log.add_message(entity, "<entity> is no longer stunned.")
