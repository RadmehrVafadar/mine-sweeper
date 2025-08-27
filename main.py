# Example file showing a circle moving on screen
import pygame
from random import randint
from my_module import Button
from my_module import ToggleButton

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
toolButton = ToggleButton(650, 650, 32, 32)
# mine board setup
board_width = 16
board_height = 16

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



# checks the number of bombs place around each cell in 3x3 area and assigns the result to the cell
for y in range(board_height):
    for x in range(board_width):
        cell = mine_matrix[y][x]
        if not cell.get_bomb():
            bomb_count = 0

        for r_offset in range(-1, 2):
            for c_offset in range(-1, 2):

                if r_offset == 0 and c_offset == 0:
                    continue


                neighbor_row = y + r_offset
                neighbor_col = x  + c_offset


                if 0 <= neighbor_row < board_height and 0 <= neighbor_col < board_width:
                    if mine_matrix[neighbor_row][neighbor_col].get_bomb():
                        bomb_count += 1
        if bomb_count > 0:
            cell.set_text(bomb_count)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check event changes
        toolButton.handle_event(event)
        current_tool_is_bomb = toolButton.get_is_tool_bomb()
        for row in mine_matrix:
            for mine in row:
                mine.handle_event(event, current_tool_is_bomb)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    # display the button elements in the screen
    toolButton.draw(screen)

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
