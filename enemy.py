import pygame

class Enemy:
    def __init__(self):
        self.pos_code = 9
        self.idle = pygame.transform.flip(pygame.image.load("img/beast_idle.png").convert_alpha(), True, False)
        self.health = 500
        self.speed = 3
        self.alive = True
    def get_pos_code(self):
        return self.pos_code
    def get_speed(self):
        return self.speed