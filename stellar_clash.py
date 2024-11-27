import pygame
import random
import sys
import os  # Importar a biblioteca para manipulação de caminhos
from collections import deque  # Para usar a fila

# Inicializar o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo Espacial")

# Definição de cores (apenas para o texto e fundo)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Caminho da pasta "assets"
assets_dir = os.path.join(os.path.dirname(__file__), "assets")

# Carregar imagens
imagem_nave = pygame.image.load(os.path.join(assets_dir, "nave.png"))
imagem_meteoro = pygame.image.load(os.path.join(assets_dir, "meteoro.png"))
imagem_laser = pygame.image.load(os.path.join(assets_dir, "laser.png"))
imagem_bola_fogo = pygame.image.load(os.path.join(assets_dir, "bola_fogo.png"))  # Nova imagem

# Redimensionar imagens, se necessário
imagem_nave = pygame.transform.scale(imagem_nave, (50, 40))  # Ajuste para o tamanho da nave
imagem_meteoro = pygame.transform.scale(imagem_meteoro, (50, 50))  # Ajuste para o tamanho do meteoro
imagem_laser = pygame.transform.scale(imagem_laser, (5, 10))  # Ajuste para o tamanho do laser
imagem_bola_fogo = pygame.transform.scale(imagem_bola_fogo, (40, 40))  # Ajuste para o tamanho da bola de fogo

# Configurações da nave
nave_largura, nave_altura = 50, 40
nave_x = largura // 2 - nave_largura // 2
nave_y = altura - nave_altura - 10
velocidade_nave = 5
vidas = 3  # Adicionando vidas da nave

# Configuração dos projéteis
projeteis = []

# Configuração dos meteoros
meteoros = []
for _ in range(5):
    x = random.randint(0, largura - 50)
    y = random.randint(-200, -50)
    meteoros.append([x, y])

# Configuração da bola de fogo
bola_fogo = deque()  # Fila para gerenciar as posições da bola de fogo
tempo_bola_fogo = 0  # Controlar o tempo para gerar novas bolas de fogo

# Velocidade dos meteoros, projéteis e bola de fogo
velocidade_meteoro = 3
velocidade_projetil = 7
velocidade_bola_fogo = 5

# Pontuação
pontuacao = 0

# Fonte para exibir o placar e vidas
fonte = pygame.font.Font(None, 36)

# Loop principal do jogo
clock = pygame.time.Clock()
jogando = True

while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False

    # Movimentação da nave
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and nave_x > 0:
        nave_x -= velocidade_nave
    if teclas[pygame.K_RIGHT] and nave_x < largura - nave_largura:
        nave_x += velocidade_nave
    if teclas[pygame.K_SPACE]:
        # Adicionar um projétil
        projeteis.append([nave_x + nave_largura // 2, nave_y])

    # Atualizar posição dos projéteis
    for projetil in projeteis[:]:
        projetil[1] -= velocidade_projetil
        if projetil[1] < 0:
            projeteis.remove(projetil)

    # Atualizar posição dos meteoros
    for meteoro in meteoros:
        meteoro[1] += velocidade_meteoro
        if meteoro[1] > altura:
            # Reposicionar o meteoro
            meteoro[0] = random.randint(0, largura - 50)
            meteoro[1] = random.randint(-200, -50)

    # Gerar novas bolas de fogo em intervalos
    tempo_bola_fogo += 1
    if tempo_bola_fogo > 120:  # A cada 2 segundos (aproximadamente)
        x = random.randint(0, largura - 40)
        bola_fogo.append([x, -40])  # Adiciona a posição inicial da bola de fogo
        tempo_bola_fogo = 0

    # Atualizar posição das bolas de fogo
    for bola in bola_fogo:
        bola[1] += velocidade_bola_fogo
    if bola_fogo and bola_fogo[0][1] > altura:
        bola_fogo.popleft()  # Remove a bola que saiu da tela

    # Colisões entre projéteis e meteoros
    for projetil in projeteis[:]:
        for meteoro in meteoros[:]:
            if (
                meteoro[0] < projetil[0] < meteoro[0] + 50
                and meteoro[1] < projetil[1] < meteoro[1] + 50
            ):
                projeteis.remove(projetil)
                meteoros.remove(meteoro)
                pontuacao += 10
                # Adicionar um novo meteoro
                x = random.randint(0, largura - 50)
                y = random.randint(-200, -50)
                meteoros.append([x, y])

    # Colisão entre a nave e as bolas de fogo
    for bola in list(bola_fogo):
        if (
            nave_x < bola[0] < nave_x + nave_largura
            and nave_y < bola[1] < nave_y + nave_altura
        ):
            vidas -= 1
            bola_fogo.remove(bola)  # Remove a bola que colidiu
            if vidas == 0:
                jogando = False  # Fim do jogo

    # Desenhar o fundo
    tela.fill(PRETO)

    # Desenhar a nave
    tela.blit(imagem_nave, (nave_x, nave_y))

    # Desenhar os projéteis
    for projetil in projeteis:
        tela.blit(imagem_laser, (projetil[0], projetil[1]))

    # Desenhar os meteoros
    for meteoro in meteoros:
        tela.blit(imagem_meteoro, (meteoro[0], meteoro[1]))

    # Desenhar as bolas de fogo
    for bola in bola_fogo:
        tela.blit(imagem_bola_fogo, (bola[0], bola[1]))

    # Exibir a pontuação e vidas
    texto_pontuacao = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
    texto_vidas = fonte.render(f"Vidas: {vidas}", True, VERMELHO)
    tela.blit(texto_pontuacao, (10, 10))
    tela.blit(texto_vidas, (10, 50))

    # Atualizar a tela
    pygame.display.flip()

    # Controlar o FPS
    clock.tick(60)

pygame.quit()
sys.exit()