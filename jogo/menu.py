import pygame
import os

# Inicializar o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Menu - Escolha o Nível")

# Cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
CINZA = (128, 128, 128)

# Carregar fundo do menu
menu_bg = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "menu.png"))
menu_bg = pygame.transform.scale(menu_bg, (largura, altura))

# Fonte
font_titulo = pygame.font.Font(None, 72)
font_opcao = pygame.font.Font(None, 48)

class NoHabilidade:
    def __init__(self, nome, filhos=None):
        if filhos is None:
            filhos = []
        self.nome = nome
        self.filhos = filhos

def criar_menu():
    # Criar a árvore de opções
    raiz = NoHabilidade("Iniciar Jogo", [
        NoHabilidade("Fácil"),
        NoHabilidade("Médio"),
        NoHabilidade("Difícil"),
        NoHabilidade("Sair")
    ])
    return raiz

def exibir_menu(menu_raiz):
    """Exibe o menu e retorna a escolha do usuário"""
    opcoes = [filho.nome for filho in menu_raiz.filhos]
    selecionado = 0
    jogando = True
    
    while jogando:
        # Definir o fundo da tela
        tela.blit(menu_bg, (0, 0))
        
        # Exibir o título "Menu"
        titulo = font_titulo.render("Menu", True, BRANCO)
        tela.blit(titulo, (largura // 2 - titulo.get_width() // 2, 50))

        # Calcular a posição vertical para as opções
        espacamento_vertical = 70
        altura_total_opcoes = len(opcoes) * espacamento_vertical
        inicio_vertical = (altura - altura_total_opcoes) // 2  # Para centralizar verticalmente
        inicio_vertical += 40  

        # Exibir as opções de menu (centradas e com caixas)
        for i, opcao in enumerate(opcoes):
            cor_fonte = BRANCO if i != selecionado else VERMELHO
            texto = font_opcao.render(opcao, True, cor_fonte)
            # Desenhar caixa em volta da opção
            largura_texto = texto.get_width() + 20
            altura_texto = texto.get_height() + 10
            pygame.draw.rect(tela, CINZA, (largura // 2 - largura_texto // 2, inicio_vertical + i * espacamento_vertical, largura_texto, altura_texto))
            # Exibir o texto da opção dentro da caixa
            tela.blit(texto, (largura // 2 - texto.get_width() // 2, inicio_vertical + i * espacamento_vertical + 5))

        pygame.display.update()

        # Eventos de controle do menu
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    selecionado = (selecionado + 1) % len(opcoes)
                elif evento.key == pygame.K_UP:
                    selecionado = (selecionado - 1) % len(opcoes)
                elif evento.key == pygame.K_RETURN:
                    return opcoes[selecionado]

    pygame.quit()
    return "Sair"
