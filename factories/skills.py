from abc import ABC, abstractmethod


# Products
class Skill(ABC):
    """Abstract base class for all skills.

    Attributes:
        skill_title (str): Display name of the skill.
        skill_mana_cost (int): Amount of mana required to use the skill.

    Methods:
        cast(attacker, target): Abstract method for applying skill effects.
        description() -> str: Returns a human-readable description of the skill.
    """

    def __init__(self, skill_title: str, skill_mana_cost: int):
        """Initialize a new skill with title and mana cost."""
        self.skill_title = skill_title
        self.skill_mana_cost = skill_mana_cost

    def __str__(self):
        """Return string representation using the skill description."""
        super().__str__()
        return self.description()

    @abstractmethod
    def cast(self, attacker, target):
        """Apply the skill effect from attacker to target."""
        pass

    def description(self) -> str:
        """Return the skill name and mana cost as a string."""
        return f'Skill: {self.skill_title}. Mana cost: {self.skill_mana_cost}'


# Concrete products
class PowerStrike(Skill):
    """Warrior specific skill that deals 3x attack damage."""

    def __init__(self):
        """Initialize Power Strike with predefined title and mana cost."""
        super().__init__(skill_title='Power Strike', skill_mana_cost=5)

    def cast(self, attacker, target):
        """Deal 3x attack damage from attacker to target."""
        damage = attacker.attack * 3
        target.hp -= damage
        print(f'{attacker.name} strikes {target.name} for {damage} dmg!')


class Fireball(Skill):
    """Wizard specific skill that deals 3x attack damage."""

    def __init__(self):
        """Initialize Fireball with predefined title and mana cost."""
        super().__init__(skill_title='Fireball', skill_mana_cost=15)

    def cast(self, attacker, target):
        """Deal 3x attack damage from attacker to target."""
        damage = attacker.intelligence * 3
        target.hp -= damage
        print(f"{attacker.name} casts Fireball on {target.name} for {damage} dmg!")


class MultiStrike(Skill):
    """Archer specific skill that deals 2x attack damage."""

    def __init__(self):
        """Initialize Multi Strike with predefined title and mana cost."""
        super().__init__(skill_title='Multi Strike', skill_mana_cost=10)

    def cast(self, attacker, target):
        """Deal 2x attack damage from attacker to target."""
        damage = attacker.attack * 2
        target.hp -= damage
        print(f"{attacker.name} strikes {target.name} for {damage} dmg!")


# Factory (Creator)
class SkillFactory(ABC):
    """Abstract factory interface for creating skills.

    Methods:
        create_skill() -> Skill: Abstract method that return a Skill instance.
    """

    @abstractmethod
    def create_skill(self) -> Skill:
        """Create and return a new Skill instance."""
        pass


# Concrete factories (Creators)
class WarriorSkillFactory(SkillFactory):
    """Factory for creating Warrior skills."""

    def create_skill(self) -> Skill:
        """Return a new instance of PowerStrike."""
        return PowerStrike()


class WizardSkillFactory(SkillFactory):
    """Factory for creating Wizard skills."""

    def create_skill(self) -> Skill:
        """Return a new instance of Fireball."""
        return Fireball()


class ArcherSkillFactory(SkillFactory):
    """Factory for creating Archer skills."""

    def create_skill(self) -> Skill:
        """Return a new instance of MultiStrike."""
        return MultiStrike()
