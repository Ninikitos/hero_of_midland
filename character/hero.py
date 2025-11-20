import pygame
from math import sqrt
from .character import Character


class Hero(Character):
    """Playable hero character."""

    def __init__(self,
                 name: str,
                 description: str,
                 specialization: str,
                 inventory: list,
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
            groups
        )
        """
        Initialize a hero with basic stats and visuals.

        Args:
            name (str): Hero's name.
            description (str): Short bio or role info.
            specialization (str): Hero specialization warrior, wizard etc.
            inventory (list): Items that will be looted from monsters.
            rank (int): Hero rank to calculate if hero can fight it.
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
        self.specialization = specialization
        self.inventory = inventory
        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect(center=self.position)
        self.target = None

    def move(self, target_x: float, target_y: float):
        """Set the coordinates of the target to move towards."""
        self.target = (float(target_x), float(target_y))

    def update(self, dt: float):
        """Smoothly move toward the target based on speed and dt."""
        if self.target is None:
            return

        # where we want to go
        tx, ty = self.target

        # where we are now
        x, y = self.position

        # calculate distance to a target
        dx = tx - x
        dy = ty - y

        # TODO: temp solution to test hero movement. I need to find
        # a way to move a hero on a two-dimensional grid.
        dist = sqrt(dx**2 + dy**2)

        # direction normalized
        dir_x = dx / dist
        dir_y = dy / dist

        step = self.movement_speed * dt

        # avoid overshoot (snap)
        if step >= dist:
            self.position = [tx, ty]
            self.target = None
        else:
            self.position[0] += dir_x * step
            self.position[1] += dir_y * step

        self.rect.center = (round(self.position[0]), round(self.position[1]))

    def attack(self) -> int:
        """Perform an attack and return damage dealt."""
        pass

    def die(self):
        """Handle death logic (animation, cleanup, etc.)."""
        pass

    def is_alive(self) -> bool:
        """Return True if character still has HP."""
        pass
