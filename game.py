import pygame, sys
from object import*
from settings import*
class Game:
    def __init__(self):

        self.width = 1000
        self.backgroundImg = pygame.image.load("img/start screen.png")
        self.button = button(200, 125, (20, 20), white)

    
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
            screen.blit(self.backgroundImg, (0,0))




            pygame.display.flip()


            clock.tick(60)

        pygame.quit()
