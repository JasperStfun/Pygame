import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Клавиатура")

WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60


x = W // 2
y = H // 2

speed = 5

flleeft = flright = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flleeft = True
            elif event.key == pygame.K_RIGHT:
                flright = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                flleeft = flright = False
    
    if flleeft:
        x -= speed
    elif flright:
        x += speed

    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
    pygame.display.update()

    clock.tick(FPS)