import pygame, sys
from object import*
from settings import*
from characters import*
from enemy import*
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
        for i in range(4):
            for x in range(8):
                self.grid = pygame.Rect((54 + (152 * x)), (90 + (128 * i)), 152, 128)
        self.turns = [1 , 2 , 3 , 4 , 9]
        self.fighter = fighter()
        self.ranger = ranger()
        self.wizard = wizard()
        self.healer = healer()
        self.enemy = Enemy()
        self.over = pygame.image.load("img/game_over.png").convert_alpha()
        self.button_1 = pygame.image.load("img/move_1_button.png").convert_alpha()
        self.button_2 = pygame.image.load("img/move_2_button.png").convert_alpha()
        

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
                    if self.grid.collidepoint(event.pos):
                        print("Grid clicked!")
            screen.fill((30, 30, 30))
            screen.blit(pygame.transform.scale(self.NEA_background,(1024,768)), (0,0))
            screen.blit(pygame.transform.scale(fighter().idle,(152,128)), (54,90))
            screen.blit(pygame.transform.scale(ranger().idle,(152,128)), (54,218))
            screen.blit(pygame.transform.scale(wizard().idle,(152,128)), (54,346))
            screen.blit(pygame.transform.scale(healer().idle,(180,148)), (44,440))
            screen.blit(pygame.transform.scale(Enemy().idle,(180,148)), (800,200))
            screen.blit(pygame.transform.scale(self.button_1,(226,75)), (20,600))
            screen.blit(pygame.transform.scale(self.button_2,(226,75)), (266,600))
            pygame.draw.rect(screen, (255, 255, 255), self.grid, 2)    
            pygame.display.flip()               
            clock.tick(60)
            if self.fighter.alive == False and self.ranger.alive == False and self.wizard.alive == False and self.healer.alive == False:
                screen.blit(pygame.transform.scale(self.over,(800,500)), (100,75))
                pygame.display.flip()
                pygame.time.delay(3000)
                running = False
