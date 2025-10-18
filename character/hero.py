from character import Character


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
                 sprite: str):
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
        """
        Initialize a monster with basic stats and visuals.

        Args:
            name (str): Character's name.
            description (str): Short bio or role info.
            specialization (str): Hero specialization warrior, wizard etc.
            inventory (list): Items that will be looted from monsters.
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
        self.specialization = specialization
        self.inventory = inventory

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
