# Example file showing a circle moving on screen
import pygame
from my_module import Button

# pygame setup
pygame.font.init()
pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
running = True
dt = 0

board_width = 16
board_height = 16

mine_matrix = [[Button(40*i,40*j, 30,30, "") for j in range(board_width)] for i in range(board_height)]

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")
    for row in mine_matrix:
        for mine in row:
            mine.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
