import pygame


class fighter:
    def __init__(self):
        self.pos_code = 1
        self.idle = pygame.image.load("img/knight_idle.png").convert_alpha()
        self.health = 120
        self.speed = 4
    def get_pos_code(self):
        return self.pos_code
    def get_speed(self):
        return self.speed
    
class ranger:
    def __init__(self):
        self.pos_code = 2
        self.idle = pygame.image.load("img/ranger_idle.png").convert_alpha()
        self.health = 80
        self.speed = 4
    def get_pos_code(self):
        return self.pos_code
    def get_speed(self):
        return self.speed


