import pygame
WIDTH = 800
HEIGHT = 600

class Ball(pygame.sprite.Sprite):
    def __init__(self, ball_group):
        super().__init__()
        self.rect = pygame.Rect(WIDTH//2, HEIGHT-75, 15, 15)
        self.speed_x = 8
        self.speed_y = 8
        self.ball_group = ball_group

    def update(self, event):
        self.rect.centery -= self.speed_y
        self.rect.centerx -= self.speed_x
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >=  HEIGHT:
            self.speed_y *= -1
    
    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)
    