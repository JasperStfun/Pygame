import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Surface")

WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60

surf = pygame.Surface((W, 200))
bita = pygame.Surface((50, 10))

surf.fill(BLUE)
bita.fill(RED)

bx, by = 0, 150
x, y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surf.fill(BLUE)
    surf.blit(bita, (bx, by))
    if bx < W:
        bx += 5
    else:
        bx = 0
    
    if y < H:
        y += 1
    else:
        y = 0

    sc.fill(WHITE)
    sc.blit(surf, (x, y))
    pygame.display.update()

    clock.tick(FPS)