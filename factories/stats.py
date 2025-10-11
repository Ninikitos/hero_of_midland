from abc import ABC, abstractmethod


# Products
class Stat(ABC):
    """Abstract base class for all hero stats: strength, intelligence and agility.
   Attributes:
       stat_title (str): Display name of the stat.
       stat_value (int): Current value of the stat.

   Methods:
       increase_stat(hero, value): Increase stat for a hero by fixed amount.
       apply_multiplier(hero, multiplier): Multiply hero's stat by a given factor.
       description() -> str: Returns a human-readable description of the stat.
   """

    def __init__(self, stat_title: str, stat_value: int):
        """Initialize stat with title and starting value."""
        self.stat_title = stat_title
        self.stat_value = stat_value

    def __str__(self):
        """Return pretty string representation using description."""
        return self.description()

    @abstractmethod
    def increase_stat(self, hero, value: int):
        """Increase stat for a hero by value."""
        pass

    @abstractmethod
    def apply_multiplier(self, hero, multiplier: float):
        """Multiply stat value for a hero by multiplier."""
        pass

    def description(self):
        """Return description of stat and itэs value."""
        return f"Stat name: {self.stat_title}. Stat value: {self.stat_value}"


# Concrete products
class Strength(Stat):
    """Concrete Strength stat that increases hero's attack power."""

    def __init__(self):
        super().__init__(stat_title="Strength", stat_value=1)

    def increase_stat(self, hero, value: int):
        """Increase hero's strength by given value and update stat_value."""
        hero.strength += value
        self.stat_value += value

    def apply_multiplier(self, hero, multiplier: float):
        """Apply multiplier to hero's strength and update stat_value."""
        hero.strength = int(hero.strength * multiplier)
        self.stat_value = hero.strength


class Intellect(Stat):
    """Concrete Intellect stat that increases hero's magical attack."""

    def __init__(self):
        super().__init__(stat_title='Intellect', stat_value=1)

    def increase_stat(self, hero, value: int):
        """Increase hero's Intellect by given value and update stat_value."""
        hero.intellect += value
        self.stat_value += value

    def apply_multiplier(self, hero, multiplier: float):
        """Apply multiplier to hero's Intellect and update stat_value."""
        hero.intellect = int(hero.intellect * multiplier)
        self.stat_value = hero.itellect


class Agility(Stat):
    """Concrete Agility stat that increases hero's chance to dodge attack."""

    def __init__(self):
        super().__init__(stat_title='Agility', stat_value=1)

    def increase_stat(self, hero, value: int):
        """Increase hero's agility by given value and update stat_value."""
        hero.agility += value
        self.stat_value += value

    def apply_multiplier(self, hero, multiplier: float):
        """Apply multiplier to hero's agility and update stat_value."""
        hero.agility = int(hero.agility * multiplier)
        self.stat_value = hero.agility


# Concrete factory (Creator)
class StatFactory(ABC):
    """Abstract factory interface to create Stat.

    Methods:
        create_stat() -> Stat: Abstract method that returns a Stat instance.
    """

    @abstractmethod
    def create_stat(self) -> Stat:
        """Create and return a new Stat instance."""
        pass


# Concrete factories (Creators)
class StrengthFactory(StatFactory):
    """Factory for creating Strength stats."""

    def create_stat(self) -> Stat:
        """Return a new instance of Strength stat."""
        return Strength()


class IntellectFactory(StatFactory):
    """Factory for creating Intellect stats."""

    def create_stat(self) -> Stat:
        """Return a new instance of Intellect stat."""
        return Intellect()


class AgilityFactory(StatFactory):
    """Factory for creating Agility stats."""

    def create_stat(self) -> Stat:
        """Return a new instance of Agility stat."""
        return Agility()
