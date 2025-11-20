import pygame


class Character(pygame.sprite.Sprite):
    """Base class for hero and all monsters."""

    def __init__(self,
                 name: str,
                 description: str,
                 strength: int,
                 intellect: int,
                 agility: int,
                 hp: int,
                 mana: int,
                 movement_speed: float,
                 position: list | tuple,
                 image: str,
                 groups: list,
                 ):
        """
        Initialize a character with basic stats and visuals.

        Args:
            name (str): Character's name.
            description (str): Short bio or role info.
            strength (int): Physical power.
            intellect (int): Magical power.
            agility (int): Attack speed or chance to dodge.
            hp (int): Health points.
            mana (int): Magic points.
            movement_speed (float): Units moved per turn.
            position: (x, y) coordinates on the map.
            image (str): Sprite image path.
            groups (list): Sprite group on the map.
        """
        super().__init__(*groups)

        self.name = name
        self.description = description
        self.strength = strength
        self.intellect = intellect
        self.agility = agility
        self.hp = hp
        self.mana = mana
        self.movement_speed = movement_speed
        self.position = position
        self.image = image

    def attack(self) -> int:
        """Perform an attack and return damage dealt."""
        pass

    def move(self, movement_speed: float, position: list) -> int:
        """Move the character based on movement speed."""
        pass

    def die(self):
        """Handle death logic (animation, cleanup, etc.)."""
        pass

    def is_alive(self) -> bool:
        """Return True if character still has HP."""
        pass

    def collect_loot(self, monster) -> list:
        """Collect items dropped from monster."""
        pass
