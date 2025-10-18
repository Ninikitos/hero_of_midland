from character import Character

class BossMonster(Character):
    """Represents a powerful boss-type monster.

    Attributes:
        rank (int): Boss difficulty level or tier.
    """

    def __init__(self,
                 name: str,
                 description: str,
                 rank: int,
                 strength: int,
                 intellect: int,
                 agility: int,
                 hp: int,
                 mana: int,
                 movement_speed: float,
                 position: list,
                 sprite: str):
        """
        Initialize a boss monster with rank and base stats.

        Args:
            name: Monster's name.
            description: Short info about the boss.
            rank: Difficulty or tier level.
            strength: Physical power value.
            intellect: Magical power value.
            agility: Dexterity and speed value.
            hp: Health points.
            mana: Magic points.
            movement_speed: Units moved per turn.
            position: [x, y] coordinates on the map.
            sprite: Path or ID of boss image.
        """
        super().__init__(
            name,
            description,
            strength,
            intellect,
            agility,
            hp,
            mana,
            movement_speed,
            position,
            sprite)
        self.rank = rank

    def drop_loot(self) -> str:
        """Return loot dropped after the boss dies."""
        pass

    def attack(self) -> int:
        """Perform a boss-specific attack and return damage dealt."""
        pass

    def move(self, movement_speed: float, position: list) -> int:
        """Move the boss character based on movement speed and position."""
        pass

    def die(self):
        """Handle boss death sequence and cleanup."""
        pass

    def is_alive(self) -> bool:
        """Return True if the boss still has HP left."""
        pass
