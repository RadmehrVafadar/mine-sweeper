import pygame

class Button:
    def __init__(self, x, y, width, height, text='0', text_color=(255,255,255)):
        self.rect = pygame.Rect(x, y, width, height)
        
        # store all states
        self.image_normal = pygame.image.load('./source/Land.png').convert_alpha()
        self.image_hover = pygame.image.load('./source/land_bright.png').convert_alpha()
        self.image_flag = pygame.image.load('./source/land_with_flag.png').convert_alpha()
        self.image_bomb = pygame.image.load('./source/land_with_bomb-V2.png').convert_alpha()


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
        text_rect = (self.rect.x, self.rect.y)
        # update hover state
        if self.rect.collidepoint(mouse_pos) and not self.clicked and not self.display_number:
           self.current_image = self.image_hover

        elif not self.clicked and not self.display_number:
            self.current_image = self.image_normal

        if self.display_number:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)


            self.current_image = text_surface

        screen.blit(self.current_image, text_rect)

    def handle_event(self, event, is_tool_bomb=True):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if is_tool_bomb and not self.is_land_flagged:
                    if self.is_bomb:
                        self.current_image = self.image_bomb
                        # Add a gamer over state chacker here
                        self.clicked = True
                    else:
                        self.display_number = True
                        self.clicked = True
                else:
                    if self.is_land_flagged and not is_tool_bomb:
                        self.current_image = self.image_normal
                        self.is_land_flagged = False
                        self.clicked = True
                    else:
                        self.current_image = self.image_flag
                        self.is_land_flagged = True
                        self.clicked = True
                return True
        return False

    # getter functions
    def get_bomb(self):
        return self.is_bomb


    # setter functions
    def set_bomb(self):
        self.is_bomb = True


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

