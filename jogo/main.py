import pygame
import random
import os
from time import time
from menu import exibir_menu, criar_menu
import networkx as nx
import matplotlib.pyplot as plt

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
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

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
        intervalo_bola_fogo = 2.5
    elif nivel == "Médio":
        velocidade_meteoro = 4
        vidas = 3
        intervalo_bola_fogo = 1.5 
    elif nivel == "Difícil":
        velocidade_meteoro = 6
        vidas = 1
        intervalo_bola_fogo = 0.8
    else:
        print(f"Nível inválido: {nivel}. Saindo.")
        pygame.quit()
        return

    executar_jogo(velocidade_meteoro, vidas, intervalo_bola_fogo)

#Tela de vitoria
def tela_ganhou():
    tela.blit(fundo_jogo, (0, 0))
    fonte_ganhou = pygame.font.Font(None, 72)
    texto_ganhou = fonte_ganhou.render("You win!", True, VERDE)
    texto_continuar = pygame.font.Font(None, 36).render(
        "Pressione qualquer tecla para voltar ao menu.", True, CINZA
    )

    # Centralizar os textos na tela
    tela.blit(
        texto_ganhou,
        (largura // 2 - texto_ganhou.get_width() // 2, altura // 2 - texto_ganhou.get_height() // 2),
    )
    tela.blit(
        texto_continuar,
        (
            largura // 2 - texto_continuar.get_width() // 2,
            altura // 2 + texto_ganhou.get_height(),
        ),
    )
    pygame.display.flip()

    # Esperar o jogador pressionar uma tecla
    aguardando = True
    while aguardando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                aguardando = False
    #Voltando a tela inicial
    main()

def tela_perdeu():
    tela.blit(fundo_jogo, (0, 0))
    fonte_perdeu = pygame.font.Font(None, 72)
    texto_perdeu = fonte_perdeu.render("Game Over", True, VERMELHO)
    texto_continuar = pygame.font.Font(None, 36).render(
        "Pressione qualquer tecla para voltar ao menu.", True, CINZA
    )

    # Centralizar os textos na tela
    tela.blit(
        texto_perdeu,
        (largura // 2 - texto_perdeu.get_width() // 2, altura // 2 - texto_perdeu.get_height() // 2),
    )
    tela.blit(
        texto_continuar,
        (
            largura // 2 - texto_continuar.get_width() // 2,
            altura // 2 + texto_perdeu.get_height(),
        ),
    )
    pygame.display.flip()

    # Esperar o jogador pressionar uma tecla
    aguardando = True
    while aguardando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                aguardando = False
    #Voltando a tela inicial
    main()

# Código principal do jogo
def executar_jogo(velocidade_meteoro, vidas,intervalo_bola_fogo):
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
    
    # Criar um grafo direcionado para representar a progressão entre fases
    grafo_fases = nx.DiGraph()

    # Adicionando nós   
    grafo_fases.add_node("1")
    grafo_fases.add_node("2")
    grafo_fases.add_node("3")

    # Adicionar arestas (conexões entre fases)
    grafo_fases.add_edge("1", "2")
    grafo_fases.add_edge("1", "3")
    grafo_fases.add_edge("2", "3")

    #Fase incial
    fase_atual = "1"

    # Função para avançar para a próxima fase
    def avancar_fase(fase_atual):
        proximas = list(grafo_fases.successors(fase_atual))
        return proximas[0] if proximas else fase_atual

    # Exibir a fase na tela
    def exibir_fase(tela, fase_atual, largura):
        texto_fase = fonte.render(f"Fase: {fase_atual}", True, (255, 255, 255))
        # Calcular a posição para centralizar o texto no topo da tela
        texto_largura = texto_fase.get_width()
        pos_x = (largura - texto_largura) // 2  
        tela.blit(texto_fase, (pos_x, 10))  

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
        if time() - tempo_ultima_bola_fogo > intervalo_bola_fogo:
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
                        tela_perdeu()
                        return

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

        # Avançar de fase ao atingir uma pontuação de 100 (exemplo)
        if pontuacao >= 500 and fase_atual == "1":
            fase_atual = avancar_fase(fase_atual)
        elif pontuacao >= 1000 and fase_atual == "2":
            fase_atual = avancar_fase(fase_atual)
        elif pontuacao >= 1500 and fase_atual == "3":
            tela_ganhou()
        
        #Exibir fase no canto superior no centro
        exibir_fase(tela, fase_atual, largura)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
