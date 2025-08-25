# Example file showing a circle moving on screen
import pygame
from random import randint
from my_module import Button


# pygame setup
window_width = 700
window_height = 700

pygame.font.init()
pygame.display.set_caption("Mines")
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
running = True
dt = 0



# Tool selection button
tool_switch = Button(650, 650, 32, 32)
# mine board setup
board_width = 16
board_height = 16

is_bomb = True # Needs to be random with a certain number of bombs (e.)
mine_matrix = [[Button(40*i,40*j, 32,32) for j in range(board_width)] for i in range(board_height)]
# example:
# [
#   [0, 0, 0]
#   [0, 0, 0]
#   [0, 0, 0]
# ]

# plant select number of bumbs randomly
number_ofBombs = 40
i = 0
while i < number_ofBombs:
    x = randint(0, board_width - 1)
    y = randint(0, board_height - 1)

    selected_cell = mine_matrix[y][x]

    if not selected_cell.get_bomb():
        selected_cell.set_bomb()
        i += 1

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")


    tool_switch.draw(screen)
    tool_switch.tool_button(event)



    # display the button elements in the screen
    for row in mine_matrix:
        for mine in row:
            mine.draw(screen)
            mine.handle_event(event)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
