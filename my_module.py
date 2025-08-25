import pygame

class Button:
    def __init__(self, x, y, width, height, is_bomb):
        self.rect = pygame.Rect(x, y, width, height)
        
        # store all states
        self.image_normal = pygame.image.load('./source/Land.png').convert_alpha()
        self.image_hover = pygame.image.load('./source/land_bright.png').convert_alpha()
        self.image_flag = pygame.image.load('./source/land_with_flag.png').convert_alpha()
        self.image_bomb = pygame.image.load('./source/land_with_bomb.png').convert_alpha()

        # start with normal image
        self.current_image = self.image_normal


        # keep track of whether it’s clicked
        self.clicked = False

        # is bomb or not
        self.is_bomb = is_bomb

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
                self.current_image = self.image_flag
                self.clicked = True
                return True
        return False

    def tool_button(self, event):
        self.current_image = self.image_bomb

