class DamageCalculator:
    """Singleton class for calculating different types of damage."""

    def __new__(cls):
        """Create or return the existing instance of the DamageCalculator class."""
        if not hasattr(cls, 'instance'):
            cls.instance = super(DamageCalculator, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        """Initialize DamageCalculator class with default multipliers."""
        self.hero_multiplier = 1.0
        self.regular_monster_multiplier = 0.8
        self.boss_monster_multiplier = 1.5

    def calculate_damage(self, attacker: Character, target: Character) -> int:
        """
        Calculate damage based on attacker type and stats.

        Args:
            attacker (Character): The entity performing the attack (Hero, Monster or BossMonster).
            target (Character): The entity receiving the attack.

        Returns:
            int: The amount of damage dealt to the target.
        """
        base_attack = getattr(attacker, 'attack', 10)
        agility = getattr(target, 'agility', 0)

        # Determine multiplier by attacker type
        if attacker.__class__.__name__ == "Hero":
            multiplier = self.hero_multiplier
        elif attacker.__class__.__name__ == "Monster":
            multiplier = self.regular_monster_multiplier
        elif attacker.__class__.__name__ == "BossMonster":
            multiplier = self.boss_monster_multiplier
        else:
            multiplier = 1.0

        # Basic formula for damage calculation
        damage = int((base_attack * multiplier) - (agility * 0.5))
        return damage

    def set_multipliers(self, hero: float = None, regular: float = None, boss: float = None):
        """
        Update damage multipliers for different attacker types.

        Args:
            hero (float): Multiplier for hero attacks.
            regular (float): Multiplier for regular monsters.
            boss (float): Multiplier for boss monsters.
        """
        if hero is not None:
            self.hero_multiplier = hero
        if regular is not None:
            self.regular_monster_multiplier = regular
        if boss is not None:
            self.boss_monster_multiplier = boss
