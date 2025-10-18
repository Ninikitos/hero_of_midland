from abc import ABC, abstractmethod


# Products
class Potion(ABC):
    """Abstract base class for all potions

    Attributes:
        potion_title (str) Potion name.
        potion_value (int) Amount of point potion will give.

    Methods:
        apply(hero): Abstract method for using potion.
        description() -> str: Return a human-readable description of the potion.
    """

    def __init__(self, potion_title: str, potion_value: int):
        """Initialize a new potion with title and value."""
        self.potion_value = potion_value
        self.potion_title = potion_title

    def __str__(self):
        """Return string representation using the potion description"""
        super().__init__()
        return self.description()

    @abstractmethod
    def apply(self, target, value: int):
        """Apply potion on a target"""
        pass

    def description(self):
        """Return potion name and value it will apply."""
        print(f'Potion: {self.__repr__()}. Value {self.potion_value} was applied.')


# Concrete products
class StatPotion(Potion):
    """Potion that will increase target stats by specified potion value."""

    def __init__(self):
        """Initialize Stat Potion with predefined title and potion value"""
        super().__init__(potion_title='Stats Potion', potion_value=2)

    def apply(self, hero, value: int):
        """Increase all stats by value."""
        hero.strength += value
        hero.intellect += value
        hero.agility += value


class HealthPotion(Potion):
    """Potion that will restore target health by specified potion value."""

    def __init__(self):
        """Initialize Health potion with predefined title and potion value."""
        super().__init__(potion_title='Health Potion', potion_value=50)

    def apply(self, hero, value: int):
        """Restore hero's health by given value."""
        hero.hp += value


class ManaPotion(Potion):
    """Potion that will restore target mana by specified potion value."""

    def __init__(self):
        """Initialize Mana potion with predefined title and potion value."""
        super().__init__(potion_title='Mana Potion', potion_value=50)

    def apply(self, hero, value: int):
        """Restore hero's mana by given value."""
        hero.mana += value


# Concrete Factory
class PotionFactory(ABC):
    """Abstract factory for to create Potions.

    Methods:
        create_potion() -> Potion: Abstract method that returns a Potion instance.
    """

    @abstractmethod
    def create(self) -> Potion:
        """Create and return a new Potion instance."""
        pass


# Concrete factories (Creators)
class StatPotionFactory(PotionFactory):
    """Factory for creating potion for stats increase."""

    def create(self) -> Potion:
        """Returns a new instance of a Stats potion."""
        return StatPotion()


class HealthPotionFactory(PotionFactory):
    """Factory for creating potion to restore health."""

    def create(self) -> Potion:
        """Returns a new instance of a Health potion."""
        return HealthPotion()


class ManaPotionFactory(PotionFactory):
    """Factory for creating potion to restore mana."""

    def create(self) -> Potion:
        """Return a new instance of a Mana restore potion."""
        return ManaPotion()
