import pygame
import random
import os
from time import time
from menu import exibir_menu, criar_menu

# Inicializar o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo Espacial")

# Definição de cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (128, 128, 128)

# Caminho da pasta "assets"
assets_dir = os.path.join(os.path.dirname(__file__), "assets")

# Carregar imagens
imagem_nave = pygame.image.load(os.path.join(assets_dir, "nave.png"))
imagem_nave_acesa = pygame.image.load(os.path.join(assets_dir, "nave_acesa.png"))
imagem_meteoro = pygame.image.load(os.path.join(assets_dir, "meteoro.png"))
imagem_laser = pygame.image.load(os.path.join(assets_dir, "laser.png"))
imagem_bola_fogo = pygame.image.load(os.path.join(assets_dir, "bola_fogo.png"))
imagem_escudo = pygame.image.load(os.path.join(assets_dir, "escudo.png"))

# Redimensionar imagens
imagem_nave = pygame.transform.scale(imagem_nave, (50, 40))
imagem_nave_acesa = pygame.transform.scale(imagem_nave_acesa, (50, 40))
imagem_meteoro = pygame.transform.scale(imagem_meteoro, (50, 50))
imagem_laser = pygame.transform.scale(imagem_laser, (5, 10))
imagem_bola_fogo = pygame.transform.scale(imagem_bola_fogo, (40, 40))
imagem_escudo = pygame.transform.scale(imagem_escudo, (60, 60))

# Carregar fundo do jogo
fundo_jogo = pygame.image.load(os.path.join(assets_dir, "jogo.png"))
fundo_jogo = pygame.transform.scale(fundo_jogo, (largura, altura))

# Classe para habilidades
class Habilidade:
    def __init__(self, nome, custo, duracao, recarga, imagem):
        self.nome = nome
        self.custo = custo
        self.duracao = duracao
        self.recarga = recarga
        self.imagem = imagem
        self.ativa = False
        self.ultimo_uso = -recarga  # Permite usar no início do jogo

    def pode_usar(self, pontuacao):
        return (
            not self.ativa
            and pontuacao >= self.custo
            and time() - self.ultimo_uso >= self.recarga
        )

# Função principal
def main():
    menu_opcoes = criar_menu()
    while True:
        escolha = exibir_menu(menu_opcoes)
        if escolha == "Sair":
            pygame.quit()
            break
        iniciar_jogo(escolha)

# Configurações do jogo com base no nível escolhido
def iniciar_jogo(nivel):
    if nivel == "Fácil":
        velocidade_meteoro = 2
        vidas = 5
    elif nivel == "Médio":
        velocidade_meteoro = 4
        vidas = 3
    elif nivel == "Difícil":
        velocidade_meteoro = 6
        vidas = 1
    else:
        print(f"Nível inválido: {nivel}. Saindo.")
        pygame.quit()
        return

    executar_jogo(velocidade_meteoro, vidas)

# Código principal do jogo
def executar_jogo(velocidade_meteoro, vidas):
    nave_largura, nave_altura = 50, 40
    nave_x = largura // 2 - nave_largura // 2
    nave_y = altura - nave_altura - 10
    velocidade_nave = 5

    # Configuração dos projéteis
    projeteis = []

    # Configuração dos meteoros
    meteoros = [[random.randint(0, largura - 50), random.randint(-200, -50)] for _ in range(5)]

    # Configuração da bola de fogo
    bolas_fogo = []
    tempo_ultima_bola_fogo = time()

    # Velocidade dos objetos
    velocidade_projetil = 5
    velocidade_bola_fogo = 5

    # Pontuação
    pontuacao = 0

    # Habilidades
    nave_acesa = Habilidade("Nave Acesa", 100, 10, 15, imagem_nave_acesa)
    escudo = Habilidade("Escudo", 500, 15, 15, imagem_escudo)

    # Fonte para exibir a pontuação
    fonte = pygame.font.Font(None, 36)

    # Loop principal do jogo
    clock = pygame.time.Clock()
    jogando = True

    while jogando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False

        teclas = pygame.key.get_pressed()

        # Movimentação da nave
        if teclas[pygame.K_LEFT] and nave_x > 0:
            nave_x -= velocidade_nave
        if teclas[pygame.K_RIGHT] and nave_x < largura - nave_largura:
            nave_x += velocidade_nave
        if teclas[pygame.K_SPACE]:
            projeteis.append([nave_x + nave_largura // 2, nave_y])

        # Ativar habilidade Nave Acesa
        if teclas[pygame.K_v]:
            if nave_acesa.pode_usar(pontuacao):
                nave_acesa.ativa = True
                velocidade_nave += 3
                pontuacao -= nave_acesa.custo
                nave_acesa.ultimo_uso = time()

        # Ativar habilidade Escudo
        if teclas[pygame.K_e]:
            if escudo.pode_usar(pontuacao):
                escudo.ativa = True
                pontuacao -= escudo.custo
                escudo.ultimo_uso = time()

        # Desativar habilidades após o tempo de duração
        if nave_acesa.ativa and time() - nave_acesa.ultimo_uso >= nave_acesa.duracao:
            nave_acesa.ativa = False
            velocidade_nave -= 3

        if escudo.ativa and time() - escudo.ultimo_uso >= escudo.duracao:
            escudo.ativa = False

        # Atualizar posição dos projéteis
        for projetil in projeteis[:]:
            projetil[1] -= velocidade_projetil
            if projetil[1] < 0:
                projeteis.remove(projetil)

        # Atualizar posição dos meteoros
        for meteoro in meteoros:
            meteoro[1] += velocidade_meteoro
            if meteoro[1] > altura:
                meteoro[0] = random.randint(0, largura - 50)
                meteoro[1] = random.randint(-200, -50)

        # Colisão entre projéteis e meteoros
        for projetil in projeteis[:]:
            for meteoro in meteoros[:]:
                if (
                    meteoro[0] < projetil[0] < meteoro[0] + 50
                    and meteoro[1] < projetil[1] < meteoro[1] + 50
                ):
                    projeteis.remove(projetil)
                    meteoros.remove(meteoro)
                    pontuacao += 10
                    meteoros.append([random.randint(0, largura - 50), random.randint(-200, -50)])
                    break

        # Gerar novas bolas de fogo
        if time() - tempo_ultima_bola_fogo > 2:  # Uma bola a cada 2 segundos
            bolas_fogo.append([random.randint(0, largura - 40), -40])
            tempo_ultima_bola_fogo = time()

        # Atualizar posição das bolas de fogo
        for bola in bolas_fogo[:]:
            bola[1] += velocidade_bola_fogo
            if bola[1] > altura:
                bolas_fogo.remove(bola)

        # Colisão entre a nave e as bolas de fogo
        for bola in bolas_fogo[:]:
            if (
                nave_x < bola[0] < nave_x + nave_largura
                and nave_y < bola[1] < nave_y + nave_altura
            ):
                bolas_fogo.remove(bola)
                if not escudo.ativa:
                    vidas -= 1
                    if vidas == 0:
                        jogando = False

        # Desenhar o fundo
        tela.blit(fundo_jogo, (0, 0))

        # Desenhar a nave
        tela.blit(imagem_nave_acesa if nave_acesa.ativa else imagem_nave, (nave_x, nave_y))

        # Desenhar o escudo acima da nave (se ativo)
        if escudo.ativa:
            tela.blit(imagem_escudo, (nave_x - 5, nave_y - 10))

        # Desenhar as vidas no canto superior direito
        for i in range(vidas):
            tela.blit(imagem_nave, (largura - (i + 1) * 60, 10))

        # Exibir pontuação no canto superior esquerdo
        texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
        tela.blit(texto_pontuacao, (10, 10))

        # Exibir habilidades disponíveis
        pygame.draw.rect(tela, CINZA, (10, 50, 150, 60))  # Caixa cinza para habilidades
        if nave_acesa.pode_usar(pontuacao):
            tela.blit(nave_acesa.imagem, (15, 55))
        if escudo.pode_usar(pontuacao):
            tela.blit(escudo.imagem, (80, 55))

        # Exibir projéteis
        for projetil in projeteis:
            tela.blit(imagem_laser, (projetil[0], projetil[1]))

        # Exibir meteoros
        for meteoro in meteoros:
            tela.blit(imagem_meteoro, (meteoro[0], meteoro[1]))

        # Exibir bolas de fogo
        for bola in bolas_fogo:
            tela.blit(imagem_bola_fogo, (bola[0], bola[1]))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
