import pygame
WIDTH = 800
HEIGHT = 600

class Paddle(pygame.sprite.Sprite):
    def __init__(self, paddle_group):
        super().__init__()
        self.rect = pygame.Rect(WIDTH//2, HEIGHT-50, 100, 15)
        self.velocity = 15
        self.width = WIDTH
        self.paddle_group = paddle_group

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.rect.left>0:
                self.rect.x -= self.velocity
            if event.key == pygame.K_RIGHT and self.rect.right<self.width:
                self.rect.x += self.velocity

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)
