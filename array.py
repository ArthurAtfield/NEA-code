import pygame
from characters import*
class position:
    def __init__(self):
        self.pos = [{1 , 0 , 0 , 0 , 0 , 0 , 0 , 0} ,
                    {2 , 0 , 0 , 0 , 0 , 0 , 0 , 9} ,
                    {3 , 0 , 0 , 0 , 0 , 0 , 0 , 0} ,
                    {4 , 0 , 0 , 0 , 0 , 0 , 0 , 0}]

    def move(self, old_pos, new_pos, char):
        if (new_pos[0] - old_pos[0]) + (new_pos[1] - old_pos[1]) > char.get_speed():
            return False
        if self.pos[new_pos] != 0:
            return False
        else:
            self.pos[old_pos] = 0
            self.pos[new_pos] = char.get_pos_code()
