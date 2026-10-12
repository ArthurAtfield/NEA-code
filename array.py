import pygame
class position:
    def __init__(self):
        self.pos = [{0 , 0 , 0 , 0 , 0 , 0 , 0 , 0} ,
                    {0 , 0 , 0 , 0 , 0 , 0 , 0 , 0} ,
                    {0 , 0 , 0 , 0 , 0 , 0 , 0 , 0} ,
                    {0 , 0 , 0 , 0 , 0 , 0 , 0 , 0}]

    def move(self, old_pos, new_pos, char):
        self.pos[old_pos] = 0
        self.pos[new_pos] = char.indentifier
