
import pygame
import random
from collections import deque

class Fireball:
    def __init__(self, screen_width):
        self.image = pygame.image.load("assets/bola_fogo.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -40
        self.speed = 5

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def is_off_screen(self, screen_height):
        return self.rect.top > screen_height
