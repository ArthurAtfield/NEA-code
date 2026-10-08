import pygame, sys
from object import*
from settings import*
class Game:
    def __init__(self):
        self.width = 1024
        self.backgroundImg = pygame.image.load("img/start screen.png")
        self.start_rect = pygame.Rect(330, 120, 670, 380)
        self.show_hitbox = True
        self.start_game = False
   
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
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_rect.collidepoint(event.pos):
                        play = main_game()
                        play.run()
                        running = False
            if self.show_hitbox:
                pygame.draw.rect(screen, (255, 0, 0), self.start_rect, 2)


            screen.fill((30, 30, 30))
            screen.blit(pygame.transform.scale(self.backgroundImg,(1024,768)), (0,0))
            





            pygame.display.flip()


            clock.tick(60)

        pygame.quit()

class main_game:
    def __init__(self):
        self.width = 1024
        self.NEA_background = pygame.image.load("img/back_game.png")
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
                    pygame.quit()
                    sys.exit()
            screen.fill((30, 30, 30))
            screen.blit(pygame.transform.scale(self.NEA_background,(1024,768)), (0,0))                
            pygame.display.flip()               
            clock.tick(60)