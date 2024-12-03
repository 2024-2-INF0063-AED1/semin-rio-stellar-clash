# *Stellar Clash*: Um Jogo de Batalha Espacial com Estruturas de Dados Avançadas

**Autores:** 
- **ANDREIA ELIAS CORRÊA  /  202302523**
- **JOAO VITOR DE PINA ADORNO DE PAIVA /  202302556** 
- **MARIA CLARA DUTRA COSTA / 202302568**

**Resumo:**  

Este trabalho apresenta o desenvolvimento de um jogo de batalha espacial, Stellar Clash, que utiliza estruturas de dados avançadas, como listas, filas, árvores e grafos. O projeto integra teoria e prática de algoritmos para criar um sistema interativo, com foco em desempenho e modularidade. O jogo inicia com uma tela de menu onde o jogador escolhe a dificuldade. No ambiente espacial, o jogador controla uma nave, enfrentando meteoros e bolas de fogo, acumulando pontos para desbloquear habilidades como maior velocidade, dano aprimorado e tiros especiais. As fases, conectadas por um grafo, apresentam desafios progressivamente mais complexos. 

**Palavras-chave:** Jogos, filas, grafos, árvore,Pygame.

---

# **Seção I: Introdução**

## **Problema**  
O problema abordado neste seminário envolve a **exploração de algoritmos e técnicas** para desenvolver um sistema eficiente de manipulação de dados em jogos ou aplicativos interativos. O foco está na análise de estruturas de dados e algoritmos para otimizar o desempenho e a experiência do usuário, especialmente em contextos onde múltiplas interações e processos precisam ser gerenciados de maneira eficiente e ordenada. Este problema se aplica a jogos, sistemas de inteligência artificial e plataformas que envolvem grandes volumes de dados.

## **Dataset**  

Os dados explorados neste seminário consistem em **dados sintéticos de jogos**, que incluem informações sobre o comportamento de personagens, trajetórias, interações e ações em um ambiente virtual. Estes dados serão utilizados para avaliar como os algoritmos se comportam em diferentes situações e quais estruturas de dados são mais eficientes em termos de tempo e espaço.

## **Métodos**

-Serão revisados os seguintes métodos:

- **Python e Pygame**: Linguagem de programação e biblioteca principal para desenvolvimento e manipulação gráfica. 
- **Algoritmos de Busca (BFS, DFS)**: Utilizados para explorar grafos e árvores, essenciais para determinar caminhos e decisões no jogo.
- **Algoritmos de Ordenação**: Técnicas de ordenação para melhorar a eficiência de diversas operações no jogo, como filas de tarefas ou controle de inventário.
- **Algoritmos de Programação Dinâmica**: Técnicas utilizadas para resolver problemas complexos de otimização em jogos, como caminhos mínimos ou alocação de recursos.  

## **Avaliação**  
A avaliação incluirá:

   1. Desempenho da biblioteca **Pygame** na renderização e manipulação de elementos em tempo real. 
   2. Eficiência da **fila** no gerenciamento de elementos dinâmicos.  
   3. A clareza e navegabilidade do **menu hierárquico baseado em árvores**.  
   4. Transições coerentes e desafiadoras geradas pelo **grafo de fases**.

---

# **Seção II: Fundamentos Teóricos**

## **Interação do Jogador e Controles**

Antes de iniciar, o jogador escolhe a dificuldade no **Menu**:  
- **Setas para cima/baixo** (`↑` / `↓`)*: Navegam entre os níveis de dificuldade.  
- **Botão Enter (`Enter`)**: Confirma a escolha da dificuldade (**Fácil**, **Médio** ou **Difícil**).  

Durante o jogo, um conjunto de teclas garante o controle da nave e o uso de habilidades, proporcionando uma experiência dinâmica e interativa:  

- **Setas Esquerda e Direita (`←` / `→`)**: Movem a nave horizontalmente, permitindo desviar de obstáculos e alinhar disparos.  
- **Espaço (`Space`)**: Dispara projéteis laser para destruir meteoros e acumular pontos.  
- **Tecla `V`**: Ativa a habilidade de **velocidade melhorada**, aumentando temporariamente a agilidade da nave. *(Disponível ao acumular 100 pontos)*.  
- **Tecla `E`**: Ativa o **escudo protetor**, tornando a nave invulnerável a ataques por 15 segundos. *(Requer 500 pontos para ativação)*.  

Esses controles foram desenvolvidos para oferecer uma jogabilidade intuitiva, adaptável ao ritmo de progressão do jogador e alinhada aos desafios apresentados em cada nível.

## Mecânicas do Jogo

### Mecanismos Fundamentais

| **Mecanismo**   | **Descrição** | **Funcionamento** | **Exemplo no Jogo** |
|:----------------:|:-------------:|:-----------------:|:-------------------:|
| **Listas**      | Estruturas sequenciais de dados, onde os elementos podem ser acessados por índice. Útil para representar projéteis, inimigos ou qualquer entidade que precise ser manipulada de forma ordenada. | - Elementos podem ser acessados por índice, facilitando o controle de várias entidades ao mesmo tempo. <br> - Facilita a manipulação e atualização dinâmica de dados. | Controle da fila de ataques programados por turno, onde os inimigos ou projéteis são gerenciados e processados sequencialmente. |
| **Filas (Deque)** | Gerenciam **bolas de fogo**, que são ameaças dinâmicas no jogo. A fila permite ações ordenadas e eficientes. | - Bolas de fogo adicionadas à fila a cada 120 quadros. <br> - Movem-se continuamente para baixo, simulando ameaça em direção à nave. <br> - Remoção automática do início da fila ao sair da tela, economizando memória. | Controle das bolas de fogo como ameaças que avançam em direção à nave do jogador. |
| **Árvores**  | Representam a hierarquia do **menu principal**, facilitando a navegação interativa. Implementadas pela classe `NoHabilidade`, organizam as opções como uma árvore. | - **Nó raiz**: "Iniciar Jogo" representa a entrada principal do menu. <br> - **Nós filhos**: Opções como "Fácil", "Médio", "Difícil" ou "Sair". <br> - **Navegação**: Teclas direcionais para navegar e "Enter" para selecionar opções. | Organização das opções no menu do jogo de forma hierárquica, permitindo a navegação eficiente. |
| **Grafos**   | Gerenciam as **transições de fase** com base na **pontuação** do jogador, permitindo uma progressão dinâmica e desafiante entre as fases. | - **Conexões**: O grafo modela as transições entre as fases, que são acionadas pela pontuação do jogador. <br> - **Flexibilidade**: Permite uma progressão baseada em metas de pontuação, com diferentes caminhos de evolução. | Definição de transições de fase e caminhos para o progresso do jogador com base em pontuação. |
> *Essa arquitetura utiliza estruturas clássicas de dados para criar um jogo dinâmico e interativo.*

### **Aplicações do Grafo:**

| **Nó**         | **Descrição**                                                                 |
|----------------|-----------------------------------------------------------------------------|
|  Fase 1        | Fase inicial do jogo, onde o jogador começa sua jornada.                    |
|  Fase 2        | Fase intermediária que é alcançada quando o jogador atinge 500 pontos.       |
|  Fase 3        | Fase final, que é acessada após o jogador atingir 1000 pontos.                |
|  Vitória       | Tela de vitória quando o jogador alcança 1500 pontos.                        |
  
- Cada fase é associada a um **nó** no grafo, e as **arestas** entre eles determinam quando o jogador pode avançar para a próxima fase. O sistema de pontuação é o critério que desbloqueia o próximo nó (fase) do grafo, permitindo uma progressão de jogo organizada e crescente.

## Técnicas e Algoritmos Utilizados

### **Técnicas de Game Design**

- **Loop de Jogo:**  
  Controle do fluxo contínuo das ações principais, como:
  - Movimentação da nave.
  - Geração de meteoros e bolas de fogo.
  - Verificação de colisões e cálculo de pontuações.

- **Eventos Dinâmicos:**  
  - **Geração Aleatória:** Meteoros e bolas de fogo aparecem em posições diferentes a cada ciclo, com dificuldade ajustada conforme o progresso do jogador.
  - **Habilidades Especiais:** Ativação de escudo e "nave acesa" baseada na pontuação acumulada.
 
### **Algoritmos Relevantes**

- **Detecção de Colisão:**  
  Implementação de lógica para identificar sobreposição de objetos por meio de coordenadas bidimensionais.

- **Geração Aleatória:**  
  Posicionamento inicial e dinâmica de surgimento de meteoros e bolas de fogo, regulados por uma frequência crescente com o avanço dos níveis.

- **Progressão por Grafos:**  
  Estrutura de grafos para modelar a sequência de fases, permitindo flexibilidade na definição de rotas e objetivos.

- **Controle de Recursos:**  
  Uso de timers e condições para ativar habilidades especiais, limitadas por pontuação.

### **Benchmarks**

- **Comparação de Desempenho:**  
  Avaliação frente a outros projetos educativos similares, observando mecânicas, gráficos e interatividade.

- **Testes de Escalabilidade:**  
  Simulações com aumento progressivo de meteoros, bolas de fogo e fases, medindo desempenho técnico do jogo.


---

# **Seção III: Metodologia**  

  ![image](https://github.com/user-attachments/assets/945b0733-002d-414f-8f04-ac60c46c6d01)

  > *Diagrama de fluxo do jogo **Stellar Clash***
  
---

# **Seção IV: Resultados e Conclusões**

## **Resultados**  
- **Jogabilidade**: Foi implementado um sistema funcional que permite ao jogador acumular pontos, desbloquear habilidades e interagir com inimigos. As filas foram eficazes para gerenciar os elementos temporais, e a árvore para fazer a dinamica de menu o que proporcionou progressão estratégica ao jogo.  
- **Desempenho Técnico**: O jogo manteve um desempenho fluido em testes, com frame rates consistentes e resposta rápida aos comandos do jogador.  
- **Estrutura de Grafos**: Ainda em desenvolvimento, o uso de grafos promete oferecer uma progressão rica em diversidade de caminhos e desafios, expandindo a rejogabilidade.  

## **Conclusões**  
![Video das funcionalidades do jogo](https://github.com/user-attachments/assets/51869970-ae32-466d-8089-61d7ad8d6768)
 > *Interface do jogo*

O projeto demonstrou que é possível combinar algoritmos básicos e intermediários em Python para criar uma experiência de jogo envolvente. As principais lições aprendidas incluem:  
1. **Integração de Algoritmos**: O uso de filas, árvores e grafos mostrou-se eficiente na construção de mecânicas robustas.  
2. **Utilização do Pygame**: A biblioteca simplificou a implementação de gráficos e eventos, mas requer cuidados para manter a otimização.  
3. **Desafios Técnicos**: A criação de um grafo eficiente para fases destacou a importância de planejamento e estruturação de dados.

---

# **Seção V: video demonstrativo**

![spaceclash-ezgif com-video-to-gif-converter (1)](https://github.com/user-attachments/assets/294d240f-71c3-4553-adc1-930d43282c65)
 > *Esse video mosta como o jogo funciona ao todo ( `menu` , `habilidades` , `game over` , `Fases` , `vitória` )*

---

## **Referências**

- Space Shooter Game Using Python : https://codewithcurious.com/projects/space-shooter-game-using-python/

- Pygame Tutorial - Python Game Development Course: https://www.youtube.com/watch?v=FfWpgLFMI7w

- Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2014). Data Structures and Algorithms in Python. Wiley.

---
