
import pygame
import random

class Meteor:
    def __init__(self, screen_width):
        self.image = pygame.image.load("assets/meteoro.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-200, -50)
        self.speed = 3

    def move(self):
        self.rect.y += self.speed

    def reset(self, screen_width):
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-200, -50)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def is_colliding(self, projectile):
        return self.rect.colliderect(projectile.rect)
