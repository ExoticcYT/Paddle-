import pygame
pygame.init()
from paddle import Paddle
from ball import Ball

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paddle")
clock = pygame.time.Clock()
FPS = 60

paddle_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()
paddle = Paddle(paddle_group)
paddle.draw(screen, "blue")
paddle_group.add(paddle)
ball = Ball(ball_group)
ball.draw(screen, "green")
ball_group.add(ball)

game_loop = True
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
    screen.fill("black")
    paddle.move(event)
    paddle.draw(screen, "blue")
    ball.draw(screen, "green")
    paddle_group.update(event)
    ball_group.update(event)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()