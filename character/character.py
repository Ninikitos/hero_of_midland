class Character():
    name: str
    description: str
    strength: int
    intellect: int
    agility: int
    hp: int
    mana: int
    movement_speed: float
    position: list
    sprite: str

    def __init__(self,
                 name: str,
                 description: str,
                 strength: int,
                 intellect: int,
                 agility: int,
                 hp: int,
                 mana: int,
                 movement_speed: float,
                 position: list,
                 sprite: str
                 ):
        self.name = name
        self.description = description
        self.strength = strength
        self.intellect = intellect
        self.agility = agility
        self.hp = hp
        self.mana = mana
        self.movement_speed = movement_speed
        self.position = position
        self.sprite = sprite

    def attack(self) -> int:
        pass

    def move(self) -> int:
        pass

    def die(self):
        pass

    def is_alive(self) -> bool:
        pass
