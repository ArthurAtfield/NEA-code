import pygame

class Game:
    def __init__(self):
        self.width = 1000
        self.backgroundImg = pygame.image.load("img/start screen.png")
    #def draw(self, pic, coords):
        #screen.blit(pic, coords)

    def run(self):
        pygame.init()

        WIDTH, HEIGHT = 1024, 768
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("My Pygame Window")

        clock = pygame.time.Clock()
        running = True
        self.backgroundImg = pygame.transform.scale(self.backgroundImg, (1024, 768), Dest_surface=None)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((30, 30, 30))
            screen.blit(self.backgroundImg, (0,0))


            pygame.display.flip()


            clock.tick(60)

        pygame.quit()
