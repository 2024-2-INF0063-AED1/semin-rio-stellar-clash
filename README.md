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

## Técnicas e Algoritmos Utilizados

### **Técnicas de Game Design**    
| **Categoria**         | **Descrição**                                                                                   |
|------------------------|-------------------------------------------------------------------------------------------------                                                                                       |
| **Loop de Jogo**       | Controle do fluxo contínuo das ações principais, como movimentação, geração de meteoros e bolas de fogo, verificação de colisões e cálculo de pontuações. |
| **Eventos Dinâmicos**  | - **Geração Aleatória**: Meteoros e bolas de fogo aparecem em posições diferentes, com dificuldade ajustada ao progresso. <br> - **Habilidades Especiais**: Ativação de escudo e "nave acesa" baseada na pontuação. |

### **Algoritmos Relevantes**   
| **Categoria**         | **Descrição**                                                                                   |
|------------------------|-------------------------------------------------------------------------------------------------                                                                                
| **Detecção de Colisão**| Lógica para identificar sobreposição de objetos por meio de coordenadas bidimensionais.         |
| **Geração Aleatória**  | Posicionamento inicial e surgimento dinâmico de meteoros e bolas de fogo, com frequência crescente conforme os níveis avançam. |
| **Progressão por Grafos** | Uso de grafos para modelar a sequência de fases, permitindo rotas e objetivos flexíveis.       |
| **Controle de Recursos** | Uso de timers e condições para ativar habilidades especiais, limitadas por pontuação acumulada. |

### **Benchmarks**         
| **Categoria**         | **Descrição**                                                                                   |
|------------------------|-----------------------------------------------------------------------------------------------|
| **Comparação de Desempenho** | Avaliação frente a projetos similares, analisando mecânicas, gráficos e interatividade.     |
| **Testes de Escalabilidade** | Simulações com aumento progressivo de elementos como meteoros e fases, avaliando o desempenho técnico. |

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
