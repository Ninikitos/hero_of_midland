from random import randint

from settings import *
from character.hero import Hero
from character.monster import Monster

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hero of Midland")
        self.clock = pygame.time.Clock()
        self.running = True

        # sprite groups to manage sprites lifecycle
        self.hero_sprite_group = pygame.sprite.Group()
        self.monster_sprite_group = pygame.sprite.Group()

        # all regular monsters
        self.regular_monsters = []

        # all characters that will be in the game
        self.hero = Hero(
            name='Aldin',
            description='Cool guy',
            specialization='warrior',
            inventory=[],
            strength=2,
            intellect=3,
            agility=3,
            hp=100,
            mana=100,
            movement_speed=200,
            position=[HERO_X, HERO_Y],
            sprite='assets/monsters/dragon.png',
            groups=self.hero_sprite_group
        )
        for _ in range(10):
            monster = Monster(
                name='Goblin',
                description='Regular goblin',
                rank=1,
                strength=1,
                intellect=1,
                agility=1,
                hp=100,
                mana=0,
                movement_speed=100,
                position=[0, 0],
                sprite='assets/monsters/goblin.png',
                groups=[]
            )

            w = monster.image.get_width()
            h = monster.image.get_height()

            monster.position = [
                randint(w // 2, SCREEN_WIDTH - w // 2),
                randint(h // 2, SCREEN_HEIGHT - h // 2)
            ]
            monster.rect.center = monster.position

            if self._place_monsters(monster):
                self.regular_monsters.append(monster)

        # each sprite needs to have a group, for rendering purpose
        self.hero_sprite_group.add(self.hero)
        self.monster_sprite_group.add(self.regular_monsters)


    def _draw_grid(self, surface: pygame.Surface):
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(surface, (150, 150, 150), (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(surface, (150, 150, 150), (0, y), (SCREEN_WIDTH, y))

    def _place_monsters(self, monster: Monster) -> bool:
        player_cx = self.hero.rect.centerx // CELL_SIZE
        player_cy = self.hero.rect.centery // CELL_SIZE
        monster_cx = monster.rect.centerx // CELL_SIZE
        monster_cy = monster.rect.centery // CELL_SIZE

        # 2 cells away from hero
        MIN_DIST = 2

        dist_x = abs(monster_cx - player_cx)
        dist_y = abs(monster_cy - player_cy)

        # monster must be at least 2 cells away from hero
        return dist_x > MIN_DIST or dist_y > MIN_DIST

    def run(self):
        while self.running:
            # delta time
            dt: float = self.clock.tick() / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.hero.move(x, y)

            # update sprite position frame by frame
            self.hero.update(dt)

            # background color of a game field
            self.screen.fill((23, 23, 111))
            self._draw_grid(self.screen)

            # draw sprites on a screen by group
            self.hero_sprite_group.draw(self.screen)
            self.monster_sprite_group.draw(self.screen)

            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()

