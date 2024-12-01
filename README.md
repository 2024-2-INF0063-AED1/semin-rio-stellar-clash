# Stellar Clash: Um Jogo de Batalha Espacial com Estruturas de Dados Avançadas

**Autores:** 
- **ANDREIA ELIAS CORRÊA  /  202302523**
- **JOAO VITOR DE PINA ADORNO DE PAIVA /  202302556** 
- **MARIA CLARA DUTRA COSTA / 202302568**

**Resumo:**  
Este trabalho apresenta o desenvolvimento de um jogo de batalha espacial, *Stellar Clash*, temos o objetivo de utilizar conceitos de estruturas de dados avançados, como Listas, filas, árvores e grafos. O projeto visa integrar teoria e prática no uso de algoritmos e estruturas de dados no desenvolvimento de um sistema interativo, com foco em desempenho e modularidade.
O jogo consiste em um ambiente espacial onde o jogador controla uma nave, enfrentando meteoros e desviando de bolas de fogo enquanto tenta acumular pontos. Esses pontos podem ser usados para desbloquear habilidades , como aumento de velocidade, dano aprimorado e tiros especiais. As fases são interconectadas por um grafo, representando desafios progressivos que aumentam em complexidade.  


**Palavras-chave:** Jogos, estruturas de dados, filas, grafos, árvores,Python,Pygame.

---


# **Seção I: Introdução**

## **Problema**  
Jogos que oferecem desafios progressivos e sistemas de evolução do jogador têm alto potencial de engajamento. No entanto, a criação de mecânicas que combinem progressão, complexidade adaptativa e decisões estratégicas exige ferramentas eficazes e flexíveis. Este projeto apresenta um jogo espacial desenvolvido em Python, utilizando a biblioteca Pygame para a criação de elementos interativos, integrando filas e árvores, e ampliando a complexidade com grafos para a estruturação de fases e conexões.  

## **Dataset**  
Os dados são gerados proceduralmente dentro do jogo:  
- **Filas:** Gerenciam dinamicamente elementos como bolas de fogo, adicionadas com base em eventos temporais.  
- **Árvores:** Estruturam o menu principal do jogo, organizando as opções em uma hierarquia clara e interativa. Cada nó da árvore representa uma opção de menu, como iniciar o jogo em diferentes dificuldades ou sair.
- **Grafos:** Representam as conexões entre fases, onde cada nó corresponde a uma fase, e as arestas indicam caminhos possíveis.  

## **Métodos**  
1. **Python e Pygame:**  
   - Linguagem de programação e biblioteca principal para desenvolvimento e manipulação gráfica.  
2. **Filas (deque):**  
   - Gerencia elementos dinâmicos, como bolas de fogo.  
3. **Árvores:**  
   -  Implementam o menu do jogo, organizando opções como seleção de dificuldade e comandos para iniciar ou sair do jogo.
4. **Grafos:**  
   - Estruturam as fases, utilizando algoritmos como Busca em Largura (BFS).  

## **Avaliação**  
A avaliação incluirá:  
1. Desempenho da biblioteca Pygame na renderização e manipulação de elementos em tempo real.  
2. Eficiência da fila no gerenciamento de elementos dinâmicos.  
3. A clareza e navegabilidade do menu hierárquico baseado em árvores.
4. Transições coerentes e desafiadoras geradas pelo grafo de fases.  

---

# **Seção II: Fundamentos Teóricos**

## **Interação do Jogador e Controles**

O jogo utiliza um conjunto de teclas para controlar a nave e acessar habilidades, garantindo uma experiência dinâmica e interativa. Abaixo, as funções de cada tecla:  

- **Setas Esquerda e Direita (`←` / `→`)**: Controlam o movimento horizontal da nave, permitindo ao jogador desviar de obstáculos e alinhar disparos.  
- **Espaço (`Space`)**: Dispara projéteis laser para destruir meteoros e ganhar pontos.  
- **Tecla `V`**: Ativa a habilidade de **velocidade melhorada**, aumentando temporariamente a agilidade da nave. Disponível ao acumular 100 pontos.  
- **Tecla `E`**: Ativa o **escudo protetor**, tornando a nave invulnerável a ataques por 15 segundos. Requer 500 pontos para ativação.  

Esses controles foram projetados para oferecer uma jogabilidade intuitiva e adaptável ao ritmo de progresso do jogador.  

## **Mecânicas do Jogo**

### **Filas**  
A estrutura de **fila** (`deque`) é empregada para gerenciar as bolas de fogo, que representam ameaças dinâmicas no jogo. Essa escolha permite uma execução eficiente e ordenada das ações relacionadas a essas entidades.  
- **Funcionamento**:  
  1. As bolas de fogo são adicionadas à fila em intervalos regulares (120 quadros).  
  2. Movem-se continuamente para baixo, representando seu deslocamento em direção à nave.  
  3. Quando saem da tela, são removidas do início da fila, mantendo a estrutura atualizada e economizando memória.  

Essa abordagem simula o comportamento natural de um fluxo de inimigos, com inserção e remoção otimizadas.  

### **Árvores**  
Árvores são estruturas hierárquicas utilizadas para organizar e representar estrutura o menu principal do jogo, permitindo uma navegação clara e interativa entre as opções. Essa estrutura foi implementada por meio da classe NoHabilidade, que organiza cada opção como um nó na hierarquia do menu.

#### *Funcionamento:*
- O nó raiz representa a entrada principal do menu (Iniciar Jogo).
- Cada nó filho é uma opção de menu, como "Fácil", "Médio", "Difícil" ou "Sair".
- O jogador utiliza as teclas direcionais para navegar entre as opções e a tecla "Enter" para selecionar.

  Essa abordagem oferece flexibilidade para expandir ou reorganizar as opções do menu de forma modular.

### **Grafos no Jogo**  
Os grafos serão adicionados no futuro para implementar funcionalidades mais complexas, como rotas de meteoros e padrões de movimento de inimigos.

#### **Por que usar grafos?**
- **Representação de conexões:** Grafos são ideais para modelar relações entre diferentes pontos ou entidades, como rotas de meteoros ou conexões entre fases do jogo.
- **Flexibilidade:** Permite criar padrões de movimentação variados e interativos.

Os **grafos** serão utilizados para representar o progresso entre fases ou desafios, com cada nó simbolizando um evento ou fase e as arestas conectando essas etapas.  
- **Aplicação**:  
  - Nó inicial: Fase introdutória com meteoros simples.  
  - Nós intermediários: Desafios mais complexos, como múltiplas bolas de fogo ou meteoros em maior velocidade.  
  - Nó final: Fase culminante com chefes ou padrões complexos de obstáculos.  

Essa abordagem permite uma progressão não linear, oferecendo ao jogador diferentes trajetórias e experiências ao longo do jogo.  

---

# **Seção III: Metodologia**  

## **Linguagem e Ferramentas**  
O projeto é desenvolvido em Python, escolhida por sua simplicidade e vasta biblioteca de suporte, sendo o **Pygame** a ferramenta principal para renderização gráfica e manipulação de eventos. Essa combinação permite o desenvolvimento ágil de mecânicas de jogo e animações.  

## **Passo a Passo do Desenvolvimento**  

1. **Planejamento e Estruturação:**  
   - Escolha do Python e Pygame para garantir flexibilidade na implementação.  
   - Estruturas de dados específicas:  
     - **Filas (deque):** Gerenciar elementos como bolas de fogo, otimizando adição e remoção. 
     - **Árvores:** Árvore hierárquica para organizar o menu principal.  
     - **Grafos:** Conectar fases e aumentar a complexidade adaptativa.  

2. **Desenvolvimento com Pygame:**
   -Criar a interface gráfica do menu, renderizando opções como "Fácil", "Médio", "Difícil" e "Sair".
   - Criar uma interface gráfica fluida, renderizando a nave, projéteis, meteoros e bolas de fogo.  
   - Lógica de colisão e eventos temporais para movimentação e geração de novos elementos.  
   - Integração do sistema de habilidades com um menu interativo, acessado por atalhos no teclado.  

4. **Modelagem com Estruturas de Dados:**  
 No código apresentado, diversas estruturas de dados foram utilizadas para diferentes funcionalidades, aproveitando suas características específicas para atender às necessidades do jogo.

5. **Teste e Ajuste:**  
   - Medir o desempenho do Pygame em diferentes resoluções e taxas de quadros.  
   - Avaliar a fluidez da fila na manipulação de elementos dinâmicos.  
   - Testar o equilíbrio da progressão no sistema de Menu.  
   - Garantir que o grafo de fases ofereça desafios crescentes e caminhos coerentes.  


---
![image](https://github.com/user-attachments/assets/7452331b-8b5b-448a-87ff-be2b512720d3)

---
# **Seção IV: Resultados e Conclusões**

## **Resultados**  
- **Jogabilidade**: Foi implementado um sistema funcional que permite ao jogador acumular pontos, desbloquear habilidades e interagir com inimigos. As filas foram eficazes para gerenciar os elementos temporais, e a árvore para fazer a dinamica de menu o que proporcionou progressão estratégica ao jogo.  
- **Desempenho Técnico**: O jogo manteve um desempenho fluido em testes, com frame rates consistentes e resposta rápida aos comandos do jogador.  
- **Estrutura de Grafos**: Ainda em desenvolvimento, o uso de grafos promete oferecer uma progressão rica em diversidade de caminhos e desafios, expandindo a rejogabilidade.  

## **Conclusões**  
O projeto demonstrou que é possível combinar algoritmos básicos e intermediários em Python para criar uma experiência de jogo envolvente. As principais lições aprendidas incluem:  
1. **Integração de Algoritmos**: O uso de filas, árvores e grafos mostrou-se eficiente na construção de mecânicas robustas.  
2. **Utilização do Pygame**: A biblioteca simplificou a implementação de gráficos e eventos, mas requer cuidados para manter a otimização.  
3. **Desafios Técnicos**: A criação de um grafo eficiente para fases destacou a importância de planejamento e estruturação de dados.

![image](https://github.com/user-attachments/assets/3993e3bd-ba22-4468-8378-4f20d5707354)
 

![WhatsApp Image 2024-11-30 at 00 18 53](https://github.com/user-attachments/assets/7aa6caf7-c207-4b4d-9643-cf43a4b85712)
ii
---

# **Seção V: video demonstrativo**

...



---
### **Requisitos para rodar o jogo**

Certifique-se de atender aos seguintes requisitos antes de executar o jogo:

1. **Versão do Python**: Python 3.8 ou superior.
2. **Dependências**:
   - Instale as dependências necessárias usando o comando:

   ```bash
   pip install pygame
   ````

### **Como inicializa?**

Para rodar o jogo, use o seguinte comando no terminal, a partir do diretório onde o arquivo está salvo:

  ```bash
python main.py
````

---

## **Referências**

Space Shooter Game Using Python : [https://codewithcurious.com/projects/space-shooter-game-using-python/]

Pygame Tutorial for Beginners - Python Game Development Course: [https://www.youtube.com/watch?v=FfWpgLFMI7w]

Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2014). Data Structures and Algorithms in Python. Wiley.

---

## **Apêndices**

(colocar os codigos mais importantes aqui)...

---

