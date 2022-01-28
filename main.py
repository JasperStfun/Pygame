import pygame

from random import randint
from ball import Ball

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)

pygame.mixer.music.load('sounds/bird.mp3')
pygame.mixer.music.play(-1)

s_catch = pygame.mixer.Sound('sounds/catch.ogg')

W = 1000
H = 570

f = pygame.font.SysFont(None, 30)

sc = pygame.display.set_mode((W, H))
bg = pygame.image.load('images/back1.jpg').convert()
score = pygame.image.load('images/score_fon.png').convert_alpha()
telega = pygame.image.load('images/telega.png').convert_alpha()
t_rect = telega.get_rect(centerx=W//2, bottom=H-5)


WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (249, 228, 176)
BLACK = (0, 0, 0)


clock = pygame.time.Clock()
FPS = 60
game_score = 0


balls_data = ({'path': 'ball_bear.png', 'score': 100},
              {'path': 'ball_fox.png', 'score': 150},
              {'path': 'ball_panda.png', 'score': 200})
balls_surf = [pygame.image.load('images/'+data['path']).convert_alpha() for data in balls_data]
balls = pygame.sprite.Group()


def createBall(group):
    indx = randint(0, len(balls_surf)-1)
    x = randint(20, W-20)
    speed = randint(1, 4)

    return Ball(x, speed, balls_surf[indx], balls_data[indx]['score'], group)

createBall(balls)

speed = 10


def collideBalls():
    global game_score
    for ball in balls:
        if t_rect.collidepoint(ball.rect.center):
            s_catch.play()
            game_score += ball.score
            ball.kill()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        t_rect.x -= speed
        if t_rect.x < 0:
            t_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        t_rect.x += speed
        if t_rect.x > W-t_rect.width:
            t_rect.x = W-t_rect.width

    collideBalls()

    sc.blit(bg, (0, 0))
    balls.draw(sc)
    sc.blit(score, (0, 0))
    sc_text = f.render(str(game_score), 1, (94, 138, 14))
    sc.blit(sc_text, (20, 10))
    sc.blit(telega, t_rect)
    pygame.display.update()

    clock.tick(FPS)

    balls.update(H)