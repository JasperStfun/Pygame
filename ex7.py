import pygame

pygame.init()


W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Изображения")

WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (249, 228, 176)

clock = pygame.time.Clock()
FPS = 60

car_surf = pygame.image.load("images/car.bmp").convert()
car_rect = car_surf.get_rect(center=(W//2, H//2))
car_surf.set_colorkey((255, 255, 255))

bg_surf = pygame.image.load("images/sand.jpg").convert()
finish_surf = pygame.image.load("images/finish.png").convert_alpha()

car_up = car_surf
car_down = pygame.transform.flip(car_surf, 0, 1)
car_left = pygame.transform.rotate(car_surf, 90)
car_right = pygame.transform.rotate(car_surf, -90)


bg_surf = pygame.transform.scale(bg_surf, (bg_surf.get_width()//3, bg_surf.get_height()//3))


car = car_up
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    bt = pygame.key.get_pressed()
    if bt[pygame.K_LEFT]:
        car = car_left
        car_rect.x -= speed
        if car_rect.x < 0:
            car_rect.x = 0
    elif bt[pygame.K_RIGHT]:
        car = car_right
        car_rect.x += speed
        if car_rect.x > W-car_rect.height:
            car_rect.x = W-car_rect.height
    elif bt[pygame.K_UP]:
        car = car_up
        car_rect.y -= speed
        if car_rect.y < 0:
            car_rect.y = 0
    elif bt[pygame.K_DOWN]:
        car = car_down
        car_rect.y += speed
        if car_rect.y > H-car_rect.height:
            car_rect.y = H-car_rect.height

    sc.blit(bg_surf, (0, 0))
    sc.blit(finish_surf, (0, 0))
    sc.blit(car, car_rect)

    pygame.display.update()

    clock.tick(FPS)