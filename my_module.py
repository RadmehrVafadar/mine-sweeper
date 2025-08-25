import pygame

class Button:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        
        # store all states
        self.image_normal = pygame.image.load('./source/Land.png').convert_alpha()
        self.image_hover = pygame.image.load('./source/land_bright.png').convert_alpha()
        self.image_flag = pygame.image.load('./source/land_with_flag.png').convert_alpha()
        self.image_bomb = pygame.image.load('./source/land_with_bomb-V2.png').convert_alpha()

        # start with normal image
        self.current_image = self.image_normal


        # keep track of whether it’s clicked
        self.clicked = False

        # is bomb or not
        self.is_bomb = False
        self.toggled = False

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        # update hover state
        if self.rect.collidepoint(mouse_pos) and not self.clicked:
           self.current_image = self.image_hover
        elif not self.clicked:
            self.current_image = self.image_normal

        # draw current image
        screen.blit(self.current_image, (self.rect.x, self.rect.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.is_bomb:
                    self.current_image = self.image_bomb
                    self.clicked = True
                else:
                    self.current_image = self.image_flag
                    self.clicked = True
                
                return True
        return False

    def tool_button(self, event):
        if event.type == pygame.MOUSEBUTTONUP:  # change here
            if self.rect.collidepoint(event.pos):
                if self.current_image == self.image_bomb:
                    self.current_image = self.image_flag
                else:
                    self.current_image = self.image_bomb
                self.clicked = True # fix this clicked update chcker please. It is conflicted with the hover 
                return True
        return False



    # getter functions
    def get_bomb(self):
        return self.is_bomb


    # setter functions
    def set_bomb(self):
        self.is_bomb = True
