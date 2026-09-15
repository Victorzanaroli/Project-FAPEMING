# Roteiro de Aula — Aula 04

## Retorno do Intervalo: Feira dos Projetos + Listas e Coleções de Dados

**Duração total:** 180 minutos (3h00) — **Horário:** 15h00 às 18h00
**Público-alvo:** Estudantes do Ensino Médio sem conhecimento prévio em programação
**Pré-requisitos da aula anterior:** Variáveis, `input()`, `if/elif/else`, `while/for` (conceitos das Aulas 1–3)

---

## Bloco 1: Boas-Vindas e Apresentação dos Projetos do Mês (45 min)

**Objetivo:** Celebrar o retorno após o intervalo de 1 mês, apresentar os Mini-Projetos (Tamagotchi Escolar, A Jornada do Herói ou Quiz Buzzfeed) desenvolvidos pelos alunos no hiato e conectar com a necessidade de armazenar múltiplos dados em estruturas de listas.

### Ações do Tutor:
- **Acolhimento e Reagrupamento (10 min):** Recepcionar os alunos na volta das 4 semanas de intervalo, resgatando a empolgação com o código.
- **Mini-Feira dos Projetos do Mês (30 min):**
  - Cada aluno ou dupla projeta seu código no computador e executa o projeto escolhido (Tamagotchi Escolar, A Jornada do Herói ou Quiz Buzzfeed) para a turma ou para a dupla ao lado.
  - O tutor faz elogios com destaque para a aplicação da lógica aprendida (Variáveis, Input, `if/else`, `while`).
- **Conexão com Listas (5 min):**
  > *"Vocês criaram sistemas incríveis! Mas se no Tamagotchi a gente quisesse guardar um histórico de tudo que o bichinho comeu? Ou se no RPG a gente quisesse guardar 10 itens no inventário? Criar 10 variáveis diferentes daria muito trabalho. Hoje vocês vão aprender a usar LISTAS — uma única caixinha que guarda milhares de coisas!"*

---

## Bloco 2: Aula Expositiva — Estrutura de Dados: Listas (30 min)

**Objetivo:** Ensinar o conceito de listas (`list`), índices, adição de elementos (`append`), tamanho (`len`) e percurso com `for`.

### Conteúdo Teórico:

#### 1. Criando e Acessando Listas
```python
# Uma lista guarda múltiplos valores em uma única variável
mochila = ["Espada", "Escudo", "Poção de Vida"]

# Acessando itens pelo índice (começa no 0!)
print(mochila[0])  # Espada
print(mochila[1])  # Escudo
```

#### 2. Adicionando Itens com `append()`
```python
mochila.append("Chave Mágica")  # Adiciona ao final da lista
print(f"Sua mochila agora tem: {len(mochila)} itens!")
```

#### 3. Percorrendo a Lista com `for`
```python
print("🎒 ITENS NA SUA MOCHILA:")
for item in mochila:
    print(f"- {item}")
```

---

## Resumo da Duração (15h00 às 18h00)

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | Boas-Vindas e Apresentação dos Projetos do Mês | 45 min | 15h00 – 15h45 |
| 2 | Aula Expositiva: Listas (índices, append, len, for) | 30 min | 15h45 – 16h15 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h15 – 16h30** |
| 3 | Prática com IA: Inventário / Lista de Compras | 50 min | 16h30 – 17h20 |
| 4 | Caça ao Tesouro e Desafio Prático com Listas | 25 min | 17h20 – 17h45 |
| 5 | Encerramento e Backup | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |

---

## Bloco 3: Prática com IA — Inventário Inteligente ou Lista de Tarefas (50 min)

**Objetivo:** Usar a IA para construir um gerenciador de listas interativo com menu `while`.

### Prompt Modelo:
```
Crie um aplicativo em Python para terminal que gerencie uma Lista de Tarefas / Inventário.
Regras:
1. Crie uma lista vazia chamada lista_itens = [].
2. Use um laço while True com o menu: 1-Adicionar Item | 2-Ver Lista | 3-Remover Item | 4-Sair.
3. Se escolher 1: peça o nome do item com input() e adicione com append().
4. Se escolher 2: use um laço for para exibir todos os itens numerados.
```

---

## Bloco 4: Caça ao Tesouro e Desafio Prático com Listas (25 min)

Os alunos inspecionam o código, alteram mensagens e adicionam novos métodos de manipulação de listas.

---

## Bloco 5: Encerramento e Backup (15 min)

Salvar os scripts `.py` e registrar a evolução técnica dos alunos.

---

## Conceitos de Programação Absorvidos

- [x] Conceito de coleção de dados e listas em Python
- [x] Indexação (base 0) e tamanho de listas (`len`)
- [x] Método `append()` para adicionar elementos
- [x] Percurso de listas com laço `for`

---

### 🏠 Micro-Missão de Casa (Para o final desta aula)

> **Escolha UMA das duas opções abaixo para realizar no caderno ou PC (10 a 15 min):**

#### 🛒 Opção A — "A Lista de Compras do Futuro"
- **Tarefa:** Crie no Python uma lista chamada `compras = []`. Faça um laço `while` que pede ao usuário para cadastrar 3 produtos e adiciona à lista. No final, exiba os produtos em ordem numerada usando `for`.

#### 🎵 Opção B — "A Playlist dos Meus Sonhos"
- **Tarefa:** Crie uma lista com suas 4 músicas favoritas. Use o comando `input()` para perguntar ao usuário o nome de mais uma música e insira na lista com `append()`. Mostre a playlist atualizada na tela!
