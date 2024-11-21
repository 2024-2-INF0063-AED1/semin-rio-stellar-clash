# Stellar Clash: Um Jogo de Batalha Espacial com Estruturas de Dados Avançadas

**Autores:** [ANDREIA ELIAS CORRÊA  /  202302523], [JOAO VITOR DE PINA ADORNO DE PAIVA /  202302556],  [MARIA CLARA DUTRA COSTA / 202302568]
**Resumo:**  
Este trabalho apresenta o desenvolvimento de um jogo de batalha espacial, *Stellar Clash*, temos o objetivo de utilizar conceitos de estruturas de dados avançados, como filas, árvores, grafos e ponteiros. O projeto visa integrar teoria e prática no uso de algoritmos e estruturas de dados no desenvolvimento de um sistema interativo, com foco em desempenho e modularidade. O jogo inclui elementos como organização de ondas de inimigos (filas), mapeamento de campos de batalha (grafos) e gestão de habilidades (árvores).

**Palavras-chave:** Jogos, estruturas de dados, filas, grafos, árvores, C.

---

## Seção I: Introdução

### Problema
Desenvolver um sistema que integre conceitos avançados de estruturas de dados em um projeto prático, de forma a demonstrar o impacto dessas técnicas na organização e desempenho de sistemas interativos. O contexto do problema é o desenvolvimento de um jogo de batalha espacial, onde a gestão de inimigos, movimentação em campo e evolução de habilidades exigem estruturas otimizadas e escaláveis.

Este problema tem aplicação prática no ensino de algoritmos, desenvolvimento de jogos e sistemas embarcados. Além disso, a abordagem ajuda estudantes a consolidar o conhecimento teórico adquirido em sala de aula.

### Revisão de Literatura
Para fundamentar o projeto, foram analisados os seguintes materiais:

1. **Cormen et al. (2009): "Introduction to Algorithms"**  
   Referência essencial para o entendimento de estruturas de dados e algoritmos. Ofereceu base teórica para o uso de filas, árvores e grafos no contexto computacional.

2. **Livro: "Game Programming Patterns" (Robert Nystrom)**  
   Explora padrões de design aplicados ao desenvolvimento de jogos, auxiliando na organização modular do código e na implementação de funcionalidades de combate e habilidades.

3. **Artigo: "Aplicações de Estruturas de Dados no Desenvolvimento de Jogos" (Revista Brasileira de Computação, 2022)**  
   O artigo descreve como filas e grafos são usados em jogos modernos, principalmente em jogos de estratégia e combate. Inspirou a modelagem do campo de batalha como grafo.

### Dataset
Embora o projeto envolva dados gerados dinamicamente, foram definidos alguns parâmetros fixos:

- **Atributos das naves:** Vida, dano e velocidade configurados no início do jogo.  
- **Campo de batalha:** Representado como um grafo fixo, usando matriz de adjacência.  
- **Ondas de inimigos:** Geradas aleatoriamente, seguindo padrões pré-estabelecidos.  

### Métodos
O projeto utiliza C para manipulação de memória e ponteiros. Métodos aplicados incluem:

- **Filas:** Organização da ordem de chegada dos inimigos.  
- **Árvores:** Estruturação e evolução de habilidades do jogador.  
- **Grafos:** Representação do mapa do campo de batalha.  
- **Ponteiros:** Gerenciamento dinâmico dos objetos do jogo.  

### Avaliação
Critérios utilizados para avaliação:

- **Funcionalidade:** O jogo funciona conforme o esperado?  
- **Desempenho:** Tempos de resposta adequados em diferentes situações.  
- **Modularidade:** Código organizado para futuras extensões.  
- **Feedback de usuários:** Testes com jogadores para avaliar usabilidade.

---

## Seção III: Metodologia

A metodologia foi organizada em quatro etapas principais:

### Etapa 1: Planejamento
1. Escolha do tema: "Jogo de Batalha de Naves".  
2. Definição das estruturas de dados:  
   - **Fila:** Gerenciar inimigos.  
   - **Grafo:** Representar o campo de batalha.  
   - **Árvore:** Gerenciar habilidades.  
   - **Ponteiros:** Gerenciar dinamicamente objetos.  
3. Criação do roteiro de desenvolvimento e prazos.

### Etapa 2: Implementação
1. Desenvolvimento das classes principais:  
   - **Classe Nave:** Representa atributos das naves.  
   - **Gerenciador de inimigos:** Baseado em filas.  
   - **Grafo:** Para os caminhos no campo de batalha.  
   - **Árvore:** Para habilidades do jogador.  
2. Integração das estruturas de dados:  
   - Filas controlam a ordem de chegada dos inimigos.  
   - Grafos para movimentação das naves.  
   - Árvore para melhorias de habilidades.  
3. Implementação do loop do jogo:  
   - Gerencia ataques, movimentação e upgrades.

### Etapa 3: Testes
1. **Testes unitários:**  
   - Inserção e remoção na fila.  
   - Navegação no grafo.  
   - Atualização de habilidades na árvore.  
2. **Testes de desempenho:**  
   - Tempo de resposta ao adicionar inimigos.  
   - Consumo de memória com diferentes tamanhos de campo.  
3. **Testes com usuários:**  
   - Feedback sobre dificuldade e mecânicas do jogo.

### Etapa 4: Documentação e Revisão
1. Produção do relatório técnico em Markdown.  
2. Criação de slides para apresentação.  
3. Submissão para revisão entre pares no GitHub.

---

