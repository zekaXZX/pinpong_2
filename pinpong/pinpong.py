from pygame import *
from random import randint

font.init()
font1 = font.Font(None, 36)
font2 = font.Font(None, 80)

win_width = 800
win_height = 600
window = display.set_mode((win_width, win_height))
display.set_caption("Ля пін понг")
clock = time.Clock()

img_racket = 'platform.png'
img_back = 'background.jpg'
img_ball = 'ball-removebg-preview.png'

WIN = font2.render("YOU WIN ", 2, (255, 255, 255))
LOSE = font2.render("YOU LOSE ", 2, (255, 235, 255))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


class Ball(GameSprite):
    def update(self):
        global ball_speed_x, ball_speed_y
        self.rect.x += ball_speed_x
        self.rect.y += ball_speed_y

        if self.rect.y <= 0 or self.rect.y >= win_height - self.rect.height:
            ball_speed_y = -ball_speed_y


racket = Player2(img_racket, 10, 200, 25, 100, 10)
racket2 = Player1(img_racket, 775, 200, 25, 100, 10)
ball = Ball(img_ball, randint(50,350), randint(50,200), 50, 50, 10)
background = transform.scale(image.load(img_back), (win_width, win_height))

finish = False
game = True

ball_speed_x = 5
ball_speed_y = 5
score = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        text_win = font1.render("Рахунок: " + str(score), 1, (255, 255, 255))
        window.blit(text_win, (10, 10))
        racket.update()
        racket.reset()
        racket2.update()
        racket2.reset()
        ball.reset()
        ball.update()
        if ball.rect.x <= 0 or ball.rect.x >= win_width - ball.rect.width:
            window.blit(LOSE, (260, 200))
            finish = True
        if ball.rect.colliderect(racket.rect) or ball.rect.colliderect(racket2.rect):
            ball_speed_y = randint(-8, 8)
            ball_speed_x = -ball_speed_x
            score += 1
        if score == 20:
            window.blit(WIN, (260, 200))
            finish = True
    display.update()
    clock.tick(30)
