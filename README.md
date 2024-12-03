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

   Neste seminário, abordamos o desenvolvimento de um sistema eficiente para manipulação de dados em jogos ou aplicativos interativos, com o objetivo de otimizar o desempenho e melhorar a experiência do usuário. O problema se aplica a contextos como jogos, inteligência artificial e plataformas que lidam com grandes volumes de dados, onde a eficiência e a organização são essenciais.
   
   Para investigar o problema, utilizamos duas principais estruturas de dados. A **árvore do menu** representa uma hierarquia de opções e subopções, funcionando como um meio de navegação para o usuário. Já o **grafo das fases** é utilizado para representar as diferentes fases do jogo, onde os **nós** são as fases e as **arestas** indicam as transições entre elas. Essas duas estruturas são fundamentais para a dinâmica do jogo, incluindo a pontuação e as configurações de dificuldade que ajustam variáveis como a velocidade dos meteoros e o número de vidas.
   
   A implementação será feita utilizando **Python** e a biblioteca **Pygame** para o desenvolvimento gráfico. Para explorar as estruturas de dados, aplicaremos algoritmos como **BFS (Busca em Largura)** e **DFS (Busca em Profundidade)**, que são essenciais para navegar e tomar decisões dentro do grafo e da árvore. Além disso, utilizaremos **algoritmos de ordenação** e **programação dinâmica** para otimizar o gerenciamento de recursos e encontrar soluções para problemas complexos, como caminhos mínimos ou alocação de recursos no jogo.
   
   A avaliação do sistema será feita com base em quatro critérios principais: o desempenho da renderização de elementos em tempo real usando **Pygame**, a eficiência da **fila** no gerenciamento de elementos dinâmicos, a clareza e navegabilidade do **menu hierárquico** e a coerência das transições no **grafo das fases**. Ao final, esperamos demonstrar como o uso eficiente de algoritmos e estruturas de dados pode melhorar a experiência do usuário e a performance do sistema.

---

# **Seção II: Fundamentos Teóricos**

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
 > **Interface do jogo** |
> ***Menu:** ⬆️⬇️: mover nas dificuldades*
> ***Jogo:** ➡️⬅️: mover a nave | `E`: escudo(500 pts) | `V`: velocidade(100 pts)*

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
