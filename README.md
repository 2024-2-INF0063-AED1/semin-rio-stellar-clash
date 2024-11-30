# Stellar Clash: Um Jogo de Batalha Espacial com Estruturas de Dados Avançadas

**Autores:** 
- **ANDREIA ELIAS CORRÊA  /  202302523**
- **JOAO VITOR DE PINA ADORNO DE PAIVA /  202302556** 
- **MARIA CLARA DUTRA COSTA / 202302568**

**Resumo:**  
Este trabalho apresenta o desenvolvimento de um jogo de batalha espacial, *Stellar Clash*, temos o objetivo de utilizar conceitos de estruturas de dados avançados, como filas, árvores, grafos e ponteiros. O projeto visa integrar teoria e prática no uso de algoritmos e estruturas de dados no desenvolvimento de um sistema interativo, com foco em desempenho e modularidade.
O jogo consiste em um ambiente espacial onde o jogador controla uma nave, enfrentando meteoros e desviando de bolas de fogo enquanto tenta acumular pontos. Esses pontos podem ser usados para desbloquear habilidades em uma árvore evolutiva, como aumento de velocidade, dano aprimorado e tiros especiais. As fases são interconectadas por um grafo, representando desafios progressivos que aumentam em complexidade.  


**Palavras-chave:** Jogos, estruturas de dados, filas, grafos, árvores,Python,Pygame.

---


# **Seção I: Introdução**

## **Problema**  
Jogos que oferecem desafios progressivos e sistemas de evolução do jogador têm alto potencial de engajamento. No entanto, a criação de mecânicas que combinem progressão, complexidade adaptativa e decisões estratégicas exige ferramentas eficazes e flexíveis. Este projeto apresenta um jogo espacial desenvolvido em Python, utilizando a biblioteca Pygame para a criação de elementos interativos, integrando filas e árvores de habilidades, e ampliando a complexidade com grafos para a estruturação de fases e conexões.  

## **Dataset**  
Os dados são gerados proceduralmente dentro do jogo:  
- **Filas:** Gerenciam dinamicamente elementos como bolas de fogo, adicionadas com base em eventos temporais.  
- **Árvores:** Estruturam o sistema de habilidades, onde habilidades dependem de pré-requisitos.  
- **Grafos:** Representam as conexões entre fases, onde cada nó corresponde a uma fase, e as arestas indicam caminhos possíveis.  

## **Métodos**  
1. **Python e Pygame:**  
   - Linguagem de programação e biblioteca principal para desenvolvimento e manipulação gráfica.  
2. **Filas (deque):**  
   - Gerencia elementos dinâmicos, como bolas de fogo.  
3. **Árvores:**  
   - Representam o sistema de habilidades desbloqueáveis.  
4. **Grafos:**  
   - Estruturam as fases, utilizando algoritmos como Busca em Largura (BFS).  

## **Avaliação**  
A avaliação incluirá:  
1. Desempenho da biblioteca Pygame na renderização e manipulação de elementos em tempo real.  
2. Eficiência da fila no gerenciamento de elementos dinâmicos.  
3. Progresso do jogador na árvore de habilidades.  
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

### **Árvore de Habilidades**  
O sistema de habilidades utiliza uma estrutura de **árvore**, onde cada habilidade está conectada a outras que precisam ser desbloqueadas antes. Isso permite uma progressão lógica e estratégica para melhorar a nave.  
- **Estrutura Planejada**:  
  - **Raiz**: A habilidade de **velocidade melhorada** é o ponto de partida.  
  - **Nível 1**: Habilidades defensivas, como o **escudo protetor**.  
  - **Nível 2**: Habilidades ofensivas avançadas, como **disparos duplos** ou **taxa de disparo aumentada**.  

Cada habilidade exige pontos acumulados, recompensando o desempenho do jogador e promovendo decisões estratégicas.  

### **Grafos no Jogo**  
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
     - **Árvores:** Sistema de habilidades com lógica de desbloqueio progressivo.  
     - **Grafos:** Conectar fases e aumentar a complexidade adaptativa.  

2. **Desenvolvimento com Pygame:**  
   - Criar uma interface gráfica fluida, renderizando a nave, projéteis, meteoros e bolas de fogo.  
   - Lógica de colisão e eventos temporais para movimentação e geração de novos elementos.  
   - Integração do sistema de habilidades com um menu interativo, acessado por atalhos no teclado.  

3. **Modelagem com Estruturas de Dados:**  
   - **Filas:**  
     - Gerenciar dinamicamente a posição e número de bolas de fogo no jogo.  
   - **Árvores:**  
     - Sistema hierárquico onde habilidades dependem de pontos acumulados e pré-requisitos.  
   - **Grafos:**  
     - Definir nós como fases e arestas como conexões possíveis, utilizando algoritmos de busca para determinar transições.  

4. **Teste e Ajuste:**  
   - Medir o desempenho do Pygame em diferentes resoluções e taxas de quadros.  
   - Avaliar a fluidez da fila na manipulação de elementos dinâmicos.  
   - Testar o equilíbrio da progressão no sistema de habilidades.  
   - Garantir que o grafo de fases ofereça desafios crescentes e caminhos coerentes.  

## **Visualização da Metodologia**  
- Gráficos demonstrando como o Pygame gerencia eventos e renderização em tempo real.  
- Fluxogramas para ilustrar o funcionamento da fila e da árvore de habilidades.  
- Representação de um grafo típico das fases, com nós e arestas destacando conexões possíveis.  


---
![image](https://github.com/user-attachments/assets/7452331b-8b5b-448a-87ff-be2b512720d3)


