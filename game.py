import pygame

class Game:
    def __init__(self):
        self.width = 1000
        self.backgroundImg = pygame.image.load("img/start screen")

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


    pygame.display.flip()


    clock.tick(60)

pygame.quit()
