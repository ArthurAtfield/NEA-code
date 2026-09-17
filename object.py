import pygame 
from settings import*
class button(pygame.sprite.Sprite):
    def __init__(self, width, height, pos, colour):
        self.height = height
        self.width = width
        self.image = pygame.Surface((self.width , self.height))
        self.image.fill(colour)
        self.pos = pos
    def pressed(self, left_click):
        mouse_pos = pygame.mouse.get_pos()
        key = pygame.mouse.get_pressed()
        if key == left_click:
            return True
