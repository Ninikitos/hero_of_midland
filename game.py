from settings import *
from character.hero import Hero

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Hero of Midland")
        self.clock = pygame.time.Clock()
        self.running = True

        # sprite groups
        self.hero_sprite_group = pygame.sprite.Group()

        self.hero = Hero(name='Aldin', description='Cool guy',
                         strength = 2,
                         intellect = 3,
                         agility = 3,
                         hp = 100,
                         mana = 100,
                         movement_speed = 1.2,
                         position = (400, 300),
                         sprite = pygame.image.load("assets/monsters/dragon.png").convert_alpha(),
                         groups = hero_sprite_group
                         )

    def run(self):
        while self.running:
            # delta time
            dt: float = pygame.time.get_ticks()

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            self.hero_sprite_group.update(dt)

            # draw
            self.hero_sprite_group.draw(self.screen)
            pygame.display.update()
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