import pygame

pygame.init()

pygame.display.set_mode((600, 400))
pygame.display.set_caption("First game")

clock = pygame.time.Clock()
FPS = 60

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False
    clock.tick(FPS)