import pygame

class Player:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load("assets/nave.png")
        self.image = pygame.transform.scale(self.image, (50, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.speed = 5
        self.lives = 3

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < pygame.display.get_surface().get_width():
            self.rect.x += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def is_colliding(self, fireballs):
        for fireball in fireballs:
            if self.rect.colliderect(fireball.rect):
                self.lives -= 1
                fireballs.remove(fireball)
                return True
        return False

