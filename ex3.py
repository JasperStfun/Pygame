import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Мышь")

WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60

sp = None

sc.fill(WHITE)
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        pos = pygame.mouse.get_pos()

        if sp is None:
            sp = pos

        width = pos[0] - sp[0]
        heigth = pos[1] - sp[1]

        sc.fill(WHITE)
        pygame.draw.rect(sc, RED, (sp[0], sp[1], width, heigth))
        pygame.display.update()
    else:
        sp = None
            

    clock.tick(FPS)    