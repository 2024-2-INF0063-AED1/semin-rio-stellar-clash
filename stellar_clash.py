import pygame
import random
import sys
import os
from collections import deque

# Inicializar o Pygame
pygame.init()

# Definições de cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Caminho da pasta "assets"
assets_dir = os.path.join(os.path.dirname(__file__), "assets")

# Função para carregar recursos (imagens)
def carregar_imagem(nome_arquivo, largura, altura):
    imagem = pygame.image.load(os.path.join(assets_dir, nome_arquivo))
    return pygame.transform.scale(imagem, (largura, altura))

# Carregar imagens
imagem_nave = carregar_imagem("nave.png", 50, 40)
imagem_meteoro = carregar_imagem("meteoro.png", 50, 50)
imagem_laser = carregar_imagem("laser.png", 5, 10)
imagem_bola_fogo = carregar_imagem("bola_fogo.png", 40, 40)

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo Espacial")

# Fonte para exibir o placar e vidas
fonte = pygame.font.Font(None, 36)

# Classe para a nave
class Nave:
    def __init__(self):
        self.largura = 50
        self.altura = 40
        self.x = largura // 2 - self.largura // 2
        self.y = altura - self.altura - 10
        self.velocidade = 5
        self.vidas = 3

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.x < largura - self.largura:
            self.x += self.velocidade

    def desenhar(self):
        tela.blit(imagem_nave, (self.x, self.y))

# Classe para os projéteis
class Projetil:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 7

    def mover(self):
        self.y -= self.velocidade

    def desenhar(self):
        tela.blit(imagem_laser, (self.x, self.y))

# Classe para os meteoros
class Meteoro:
    def __init__(self):
        self.x = random.randint(0, largura - 50)
        self.y = random.randint(-200, -50)
        self.velocidade = 3

    def mover(self):
        self.y += self.velocidade
        if self.y > altura:
            self.reposicionar()

    def reposicionar(self):
        self.x = random.randint(0, largura - 50)
        self.y = random.randint(-200, -50)

    def desenhar(self):
        tela.blit(imagem_meteoro, (self.x, self.y))

# Classe para as bolas de fogo
class BolaFogo:
    def __init__(self):
        self.x = random.randint(0, largura - 40)
        self.y = -40
        self.velocidade = 5

    def mover(self):
        self.y += self.velocidade

    def desenhar(self):
        tela.blit(imagem_bola_fogo, (self.x, self.y))

# Função para gerenciar o placar
def desenhar_placar(pontuacao, vidas):
    texto_pontuacao = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
    texto_vidas = fonte.render(f"Vidas: {vidas}", True, VERMELHO)
    tela.blit(texto_pontuacao, (10, 10))
    tela.blit(texto_vidas, (10, 50))

# Função principal do jogo
def main():
    # Inicializar objetos
    nave = Nave()
    projeteis = []
    meteoros = [Meteoro() for _ in range(5)]
    bolas_fogo = deque()
    tempo_bola_fogo = 0
    pontuacao = 0

    # Controle do jogo
    clock = pygame.time.Clock()
    jogando = True

    while jogando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False

        # Movimentação da nave
        teclas = pygame.key.get_pressed()
        nave.mover(teclas)

        # Gerar projéteis
        if teclas[pygame.K_SPACE]:
            projeteis.append(Projetil(nave.x + nave.largura // 2, nave.y))

        # Atualizar projéteis
        for projetil in projeteis[:]:
            projetil.mover()
            if projetil.y < 0:
                projeteis.remove(projetil)

        # Atualizar meteoros
        for meteoro in meteoros:
            meteoro.mover()

        # Gerar novas bolas de fogo
        tempo_bola_fogo += 1
        if tempo_bola_fogo > 120:
            bolas_fogo.append(BolaFogo())
            tempo_bola_fogo = 0

        # Atualizar bolas de fogo
        for bola in bolas_fogo:
            bola.mover()
        if bolas_fogo and bolas_fogo[0].y > altura:
            bolas_fogo.popleft()

        # Colisões
        for projetil in projeteis[:]:
            for meteoro in meteoros[:]:
                if meteoro.x < projetil.x < meteoro.x + 50 and meteoro.y < projetil.y < meteoro.y + 50:
                    projeteis.remove(projetil)
                    meteoros.remove(meteoro)
                    pontuacao += 10
                    meteoros.append(Meteoro())

        for bola in list(bolas_fogo):
            if nave.x < bola.x < nave.x + nave.largura and nave.y < bola.y < nave.y + nave.altura:
                nave.vidas -= 1
                bolas_fogo.remove(bola)
                if nave.vidas == 0:
                    jogando = False

        # Desenhar
        tela.fill(PRETO)
        nave.desenhar()
        for projetil in projeteis:
            projetil.desenhar()
        for meteoro in meteoros:
            meteoro.desenhar()
        for bola in bolas_fogo:
            bola.desenhar()
        desenhar_placar(pontuacao, nave.vidas)

        # Atualizar tela
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

