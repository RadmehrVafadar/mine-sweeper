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

# Game state management
game_state = "playing"  # "playing", "game_over", "won"
font_large = pygame.font.SysFont("Arial", 48)
font_medium = pygame.font.SysFont("Arial", 32)
game_over_time = 0



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

def check_win_condition():
    """Check if all non-bomb cells are revealed"""
    for row in mine_matrix:
        for cell in row:
            if not cell.is_bomb and not cell.display_number:
                return False
    return True

def reveal_all_bombs():
    """Reveal all bombs when game is over"""
    for row in mine_matrix:
        for cell in row:
            if cell.is_bomb:
                cell.current_image = cell.image_bomb
                cell.clicked = True

def draw_game_status(screen):
    """Draw game over or win message"""
    if game_state == "game_over":
        text = font_large.render("GAME OVER!", True, (255, 0, 0))
        restart_text = font_medium.render("Press R to Restart", True, (255, 255, 255))
    elif game_state == "won":
        text = font_large.render("YOU WON!", True, (0, 255, 0))
        restart_text = font_medium.render("Press R to Restart", True, (255, 255, 255))
    else:
        return
    
    # Draw semi-transparent overlay
    overlay = pygame.Surface((window_width, window_height))
    overlay.set_alpha(128)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))
    
    # Draw text
    text_rect = text.get_rect(center=(window_width // 2, window_height // 2 - 50))
    restart_rect = restart_text.get_rect(center=(window_width // 2, window_height // 2 + 50))
    
    screen.blit(text, text_rect)
    screen.blit(restart_text, restart_rect)

def reset_game():
    """Reset the game to initial state"""
    global game_state, mine_matrix, game_over_time
    
    game_state = "playing"
    game_over_time = 0
    
    # Reset all cells
    for row in mine_matrix:
        for cell in row:
            cell.clicked = False
            cell.display_number = False
            cell.is_land_flagged = False
            cell.current_image = cell.image_normal
            cell.text = ''
    
    # Clear all bombs
    for row in mine_matrix:
        for cell in row:
            cell.is_bomb = False
    
    # Plant bombs again
    i = 0
    while i < number_ofBombs:
        x = randint(0, board_width - 1)
        y = randint(0, board_height - 1)
        
        selected_cell = mine_matrix[y][x]
        
        if not selected_cell.get_bomb():
            selected_cell.set_bomb()
            i += 1
    
    # Recalculate bomb counts
    for y in range(board_height):
        for x in range(board_width):
            cell = mine_matrix[y][x]
            bomb_count = 0
            
            for r_offset in range(-1, 2):
                for c_offset in range(-1, 2):
                    if r_offset == 0 and c_offset == 0:
                        continue
                    
                    neighbor_row = y + r_offset
                    neighbor_col = x + c_offset
                    
                    if 0 <= neighbor_row < board_height and 0 <= neighbor_col < board_width:
                        if mine_matrix[neighbor_row][neighbor_col].get_bomb():
                            bomb_count += 1
            
            if not cell.get_bomb():
                if bomb_count > 0:
                    cell.set_text(bomb_count)



# checks the number of bombs place around each cell in 3x3 area and assigns the result to the cell
for y in range(board_height):
    for x in range(board_width):
        cell = mine_matrix[y][x]
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
        
        if not cell.get_bomb():
            if bomb_count > 0:
                cell.set_text(bomb_count)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle restart key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_state != "playing":
                reset_game()

        # Only handle game events if game is still playing
        if game_state == "playing":
            # check event changes
            toolButton.handle_event(event)
            current_tool_is_bomb = toolButton.get_is_tool_bomb()
            
            for y in range(board_height):
                for x in range(board_width):
                    mine = mine_matrix[y][x]
                    result = mine.handle_event(event, current_tool_is_bomb, mine_matrix, y, x, board_height, board_width)
                    
                    # Check for game over
                    if result == "game_over":
                        game_state = "game_over"
                        game_over_time = pygame.time.get_ticks()
                        reveal_all_bombs()
                        break
                    
                    # Check for win condition after each move
                    elif result == "continue" and check_win_condition():
                        game_state = "won"
                        break
                
                if game_state != "playing":
                    break


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    # display the button elements in the screen
    toolButton.draw(screen)

    for row in mine_matrix:
        for mine in row:
            mine.draw(screen)
    
    # Draw game status overlay if game is over or won
    draw_game_status(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
