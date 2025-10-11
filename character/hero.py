from character import Character


class Hero(Character):
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
        self.specialization = specialization
        self.inventory = inventory

    def attack(self) -> int:
        pass

    def move(self) -> int:
        pass

    def die(self):
        pass

    def is_alive(self) -> bool:
        pass
