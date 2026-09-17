import pygame, sys
from object import*
from settings import*
class Game:
    def __init__(self):

        self.width = 1024
        self.backgroundImg = pygame.image.load("img/start screen.png")
        self.button = button(300, 100, (362, 384), white)
        

    
    def run(self):
        pygame.init()

        WIDTH, HEIGHT = 1024, 768
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("My Pygame Window")

        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((30, 30, 30))
            screen.blit(pygame.transform.scale(self.backgroundImg,(1024,768)), (0,0))
            





            pygame.display.flip()


            clock.tick(60)

        pygame.quit()
    #while run:
        #mouse_pos = pygame.mouse.get_pos()