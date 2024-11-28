
import pygame

class Projectile:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/laser.png")
        self.image = pygame.transform.scale(self.image, (5, 10))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 7

    def move(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def is_off_screen(self):
        return self.rect.bottom < 0
