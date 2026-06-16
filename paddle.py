import pygame

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x//2, y-50, 100, 15)
        self.velocity = 15
        self.width = x

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.rect.left>0:
                self.rect.x -= self.velocity
            if event.key == pygame.K_RIGHT and self.rect.right<self.width:
                self.rect.x += self.velocity

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)
