import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((1720, 1080))
pygame.display.set_caption("Hello Pygame")

# create a surface object, image is drawn on it.
imp = pygame.image.load("../dragon.png").convert()
dragon = pygame.transform.scale(imp, (200, 200))
# Using blit to copy content from one surface to other
screen.blit(dragon, (0, 0))

# paint screen one time
pygame.display.flip()
status = True
while (status):

  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False

# Quit Pygame
pygame.quit()