
import pygame
import sys
from src.game import Game

def main():
    # Inicializa o Pygame
    pygame.init()

    # Cria a janela do jogo e configurações
    largura, altura = 800, 600
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Jogo Espacial")

    # Cria a instância do jogo
    jogo = Game(largura, altura, tela)

    # Loop principal do jogo
    while jogo.jogando:
        jogo.processar_eventos()
        jogo.atualizar()
        jogo.desenhar()
        jogo.controlar_fps()

    # Finaliza o Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
