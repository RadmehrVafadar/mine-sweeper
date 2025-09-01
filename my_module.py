import pygame

class Button:
    def __init__(self, x, y, width, height, text='', text_color=(255,255,255)):
        self.rect = pygame.Rect(x, y, width, height)
        
        # store all states
        self.image_normal = pygame.image.load('./source/Land.png').convert_alpha()
        self.image_hover = pygame.image.load('./source/land_bright.png').convert_alpha()
        self.image_flag = pygame.image.load('./source/land_with_flag.png').convert_alpha()
        self.image_bomb = pygame.image.load('./source/land_with_bomb-V2.png').convert_alpha()
        self.image_empty = pygame.image.load('./source/land_empty-V2.png').convert_alpha()

        # start with normal image
        self.current_image = self.image_normal


        # initialise box text
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.SysFont("Arial", 20)

        # keep track of whether it’s clicked
        self.clicked = False

        # is bomb or not
        self.is_bomb = False
        self.display_number = False # by default we will not display numbers and only do so when clicked
        self.is_land_flagged = False

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        
        if self.display_number:
            self.current_image = self.image_empty

        # update hover state
        if self.rect.collidepoint(mouse_pos) and not self.clicked and not self.display_number:
           self.current_image = self.image_hover

        elif not self.clicked and not self.display_number:
            self.current_image = self.image_normal

        screen.blit(self.current_image, (self.rect.x, self.rect.y))


        if self.display_number:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)


    def handle_event(self, event, is_tool_bomb=True, mine_matrix=None, row=None, col=None, board_height=None, board_width=None):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if is_tool_bomb and not self.is_land_flagged:
                    if self.is_bomb:
                        self.current_image = self.image_bomb
                        self.clicked = True
                        return "game_over"  # Return game over state
                    else:
                        # Check if this cell should trigger flood fill
                        if mine_matrix is not None and row is not None and col is not None:
                            if not self.text or self.text == '':
                                # This is an empty cell, trigger flood fill
                                self.flood_fill(mine_matrix, row, col, board_height, board_width)
                            else:
                                # This cell has a number, just reveal it
                                self.display_number = True
                                self.clicked = True
                        else:
                            # Fallback to original behavior
                            self.display_number = True
                            self.clicked = True
                        return "continue"  # Game continues
                else:
                    if self.is_land_flagged and not is_tool_bomb:
                        self.current_image = self.image_normal
                        self.is_land_flagged = False
                        self.clicked = True
                    else:
                        self.current_image = self.image_flag
                        self.is_land_flagged = True
                        self.clicked = True
                    return "continue"
        return "no_action"

    # getter functions
    def get_bomb(self):
        return self.is_bomb


    # setter functions
    def set_bomb(self):
        self.is_bomb = True

    def set_text(self, text):
        self.text = str(text)

        match text:
            case 1:
                self.text_color = (0, 128, 225) # Light Blue
            case 2:
                self.text_color = "Green"
            case 3:
                self.text_color = "Red"
            case 4:
                self.text_color = (0,0,153) # Dark blue
            case 5:
                self.text_color = (225, 0, 225) # Hot Pink
            case 6:
                self.text_color = "Orange"
            case 7:
                self.text_color = "Yellow"
            case _:
                self.text_color = (204, 0, 204) # Dark Pink

    def reveal_cell(self):
        """Reveals this cell by setting display_number to True"""
        if not self.is_land_flagged and not self.clicked:
            self.display_number = True
            self.clicked = True
            return True
        return False

    def flood_fill(self, mine_matrix, row, col, board_height, board_width):
        """Flood fill algorithm to reveal adjacent empty cells"""
        # Check bounds
        if row < 0 or row >= board_height or col < 0 or col >= board_width:
            return
        
        current_cell = mine_matrix[row][col]
        
        # Don't reveal if it's a bomb, flagged, or already revealed
        if current_cell.is_bomb or current_cell.is_land_flagged or current_cell.display_number:
            return
        
        # Reveal this cell
        current_cell.reveal_cell()
        
        # If this cell has a number (adjacent bombs), don't continue flood fill
        if current_cell.text and current_cell.text != '':
            return
        
        # Recursively reveal all 8 adjacent cells
        for r_offset in range(-1, 2):
            for c_offset in range(-1, 2):
                if r_offset == 0 and c_offset == 0:
                    continue
                
                new_row = row + r_offset
                new_col = col + c_offset
                self.flood_fill(mine_matrix, new_row, new_col, board_height, board_width)

# ----------------------------------------------------------------
# ----------------------------------------------------------------


        # Creating a new module because duplicating all methods is stupid
class ToggleButton:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

        self.is_tool_bomb = True # True = Bomb ; False = Flag
    
        # initialise sprites
        self.image_flag = pygame.image.load('./source/land_with_flag.png').convert_alpha()
        self.image_bomb = pygame.image.load('./source/land_with_bomb-V2.png').convert_alpha()


        # Start with bomb image
        self.current_image = self.image_bomb

    def draw(self, screen):
        screen.blit(self.current_image, (self.rect.x, self.rect.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # change here
            if self.rect.collidepoint(event.pos):
                if self.current_image == self.image_bomb:
                    self.current_image = self.image_flag
                    self.is_tool_bomb = False
                else:
                    self.current_image = self.image_bomb
                    self.is_tool_bomb = True
                return True
        return False


    # getter functions
    def get_is_tool_bomb(self):
        return self.is_tool_bomb

