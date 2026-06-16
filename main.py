import pygame
pygame.init()
from paddle import Paddle

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paddle")
clock = pygame.time.Clock()
FPS = 60

paddle = Paddle(WIDTH, HEIGHT)
paddle.draw(screen, "blue")

game_loop = True
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
    screen.fill("black")
    paddle.move(event)
    paddle.draw(screen, "blue")
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()