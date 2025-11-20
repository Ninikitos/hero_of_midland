import pygame
from .character import Character


class Monster(Character):
    """General Monster class that will fight Hero."""
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
                 sprite: str,
                 groups: list):
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
            sprite,
            groups)
        """
        Initialize a monster with basic stats and visuals.

        Args:
            name (str): Character's name.
            description (str): Short bio or role info.
            rank (int): Monster rank to calculate if hero can fight it.
            strength (int): Physical power.
            intellect (int): Magical power.
            agility (int): Attack speed or chance to dodge.
            hp (int): Health points.
            mana (int): Magic points.
            movement_speed (float): Units moved per turn.
            position: [x, y] coordinates on the map.
            sprite (str): Sprite image path.
        """
        self.rank = rank
        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect(center=self.position)

    def drop_loot(self) -> str:
        """Drop a piece of equipment."""
        pass

    def attack(self) -> int:
        """Perform an attack and return damage dealt."""
        pass

    def move(self, movement_speed: float, position: list) -> int:
        """Move Monster based on movement speed."""
        pass

    def die(self):
        """Handle death logic (animation, cleanup, etc.)."""
        pass

    def is_alive(self) -> bool:
        """Return True if monster still has HP."""
        pass