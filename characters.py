import pygame


class fighter:
    def __init__(self):
        self.pos_code = 1
        self.idle = pygame.image.load("img/knight_idle.png").convert_alpha()
        self.health = 120
        self.speed = 4
        self.alive = True
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
        self.alive = True
    def get_pos_code(self):
        return self.pos_code
    def get_speed(self):
        return self.speed


class wizard:
    def __init__(self):
        self.pos_code = 3
        self.idle = pygame.image.load("img/wizard_idle.png").convert_alpha()
        self.health = 100
        self.speed = 3
        self.alive = True
    def get_pos_code(self):
        return self.pos_code
    def get_speed(self):
        return self.speed


class healer:
    def __init__(self):
        self.pos_code = 4
        self.idle = pygame.image.load("img/healer_idle.png").convert_alpha()
        self.health = 60
        self.speed = 5
        self.alive = True
    def get_pos_code(self):
        return self.pos_code
    def get_speed(self):
        return self.speed