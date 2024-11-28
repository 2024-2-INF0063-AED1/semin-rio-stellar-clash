import random
import pygame
import sys
from player import Player
from projectile import Projectile
from meteor import Meteor
from fireball import Fireball
from collections import deque

# Inicializar o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo Espacial")

# Definição de cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Fonte para exibir o placar e vidas
font = pygame.font.Font(None, 36)

def game_loop():
    clock = pygame.time.Clock()
    player = Player(WIDTH, HEIGHT)
    projectiles = []
    meteors = [Meteor(WIDTH) for _ in range(5)]
    fireballs = deque()
    score = 0

    while True:
        screen.fill((0, 0, 0))

        # Evento de fechamento do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Movimentação da nave
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Disparar projéteis
        if keys[pygame.K_SPACE]:
            projectiles.append(Projectile(player.rect.centerx, player.rect.top))

        # Atualizar e desenhar projéteis
        for projectile in projectiles[:]:
            projectile.move()
            if projectile.is_off_screen():
                projectiles.remove(projectile)
            else:
                projectile.draw(screen)

        # Atualizar e desenhar meteoros
        for meteor in meteors:
            meteor.move()
            if meteor.rect.top > HEIGHT:
                meteor.reset(WIDTH)
            meteor.draw(screen)

        # Atualizar e desenhar bolas de fogo
        if random.randint(1, 120) == 1:
            fireballs.append(Fireball(WIDTH))
        for fireball in list(fireballs):
            fireball.move()
            if fireball.is_off_screen(HEIGHT):
                fireballs.remove(fireball)
            fireball.draw(screen)

        # Verificar colisões
        for meteor in meteors[:]:
            for projectile in projectiles[:]:
                if meteor.is_colliding(projectile):
                    if meteor in meteors:
                        meteors.remove(meteor)
                    if projectile in projectiles:
                        projectiles.remove(projectile)
                    score += 10
                    meteors.append(Meteor(WIDTH))

        # Verificar colisões com bolas de fogo
        if player.is_colliding(fireballs):
            if player.lives == 0:
                pygame.quit()
                sys.exit()

        # Desenhar a nave
        player.draw(screen)

        # Exibir a pontuação e vidas
        score_text = font.render(f"Pontos: {score}", True, WHITE)
        lives_text = font.render(f"Vidas: {player.lives}", True, RED)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))

        # Atualizar a tela
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    game_loop()
