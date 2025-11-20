from settings import *
from character.hero import Hero
from character.monster import Monster

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Hero of Midland")
        self.clock = pygame.time.Clock()
        self.running = True

        # sprite groups to manage sprites lifecycle
        self.hero_sprite_group = pygame.sprite.Group()
        self.monster_sprite_group = pygame.sprite.Group()

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
            position=[100, 50],
            sprite='assets/monsters/dragon.png',
            groups=self.hero_sprite_group
        )

        self.regular_monster = Monster(
            name='Goblin',
            description='Regular goblin',
            rank=1,
            strength=1,
            intellect=1,
            agility=1,
            hp=100,
            mana=0,
            movement_speed=100,
            position=[400, 900],
            sprite='assets/monsters/goblin.png',
            groups=self.monster_sprite_group
        )

        # each sprite needs to have a group, for manipulation purpose
        self.hero_sprite_group.add(self.hero)
        self.monster_sprite_group.add(self.regular_monster)

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

            # draw sprites on a screen by group
            self.hero_sprite_group.draw(self.screen)
            self.monster_sprite_group.draw(self.screen)
            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
# # create a surface object, image is drawn on it.
# imp = pygame.image.load("assets/monsters/dragon.png").convert()
# dragon = pygame.transform.scale(imp, (200, 200))
# # Using blit to copy content from one surface to other
# screen.blit(dragon, (0, 0))
#
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
