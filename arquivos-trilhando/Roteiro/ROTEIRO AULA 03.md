# Roteiro de Aula — Aula 03

## Repetição, Automação (while, for) + Lançamento dos Projetos do Mês

**Duração total:** 180 minutos (3h00) — **Horário:** 15h00 às 18h00
**Público-alvo:** Estudantes do Ensino Médio sem conhecimento prévio em programação
**Pré-requisitos da aula anterior:** Variáveis, tipos de dados (`str`, `int`, `float`), `print()`, `input()`, `if/elif/else`

---

## Bloco 1: Aquecimento — Repetição no Dia a Dia e o Superpoder do Loop (15 min)

**Objetivo:** Mostrar como os laços de repetição evitam código duplicado e permitem jogos contínuos.

### Ações do Tutor:
- Escrever no quadro a analogia:
  > *"Imaginem um jogo onde, a cada segundo, você precisa mandar o personagem andar. Sem repetição, teríamos que escrever 1000 linhas de código! Com a repetição (`while` ou `for`), escrevemos 2 linhas que rodam para sempre!"*
- Mostrar no terminal:
  ```python
  # Repetição automática
  contador = 1
  while contador <= 5:
      print(f"🔄 Rodada número {contador}")
      contador += 1
  ```
- Conectar: *"Hoje vocês aprendem o último ingrediente essencial da lógica de programação. Com Variáveis, Input, If/Else e Repetição, vocês podem criar QUALQUER jogo!"*

---

## Bloco 2: Aula Expositiva — Laços while e for (30 min)

**Objetivo:** Formalizar os laços `while` (enquanto) e `for` (para cada), contadores, acumuladores e prevenção de laço infinito.

### Conteúdo Teórico:

#### 1. O Laço `while` (Enquanto)
```python
energia = 100
while energia > 0:
    print(f"⚡ Jogando... Energia atual: {energia}")
    energia -= 20  # Reduz energia a cada rodada

print("🪫 Sua energia acabou! Game Over.")
```

#### 2. O Laço `for` com `range()` (Repetição Contada)
```python
print("🚀 Contagem regressiva:")
for i in range(5, 0, -1):
    print(i)
print("💥 DECOLAR!")
```

#### 3. Menu de Opções Infinito com `while True` e `break`
```python
while True:
    opcao = input("1-Jogar | 2-Instruções | 3-Sair: ")
    if opcao == "3":
        print("Saindo do jogo... Até mais!")
        break  # Interrompe o laço
```

---

## Bloco 3: Engenharia Reversa Guiada — Jogo da Adivinhação com Vidas (25 min)

**Objetivo:** Identificar `while`, contadores de vidas e `if/else` trabalhando em conjunto num código real.

---

## Resumo da Duração (15h00 às 18h00)

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | Aquecimento: Repetição no dia a dia e superpoder do loop | 15 min | 15h00 – 15h15 |
| 2 | Aula Expositiva: Laços while e for (contadores e menus) | 30 min | 15h15 – 15h45 |
| 3 | Engenharia Reversa: Jogo da Adivinhação com Vidas | 25 min | 15h45 – 16h10 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h10 – 16h25** |
| 4 | Prática com IA: Praticando Loops e Menus em Python | 30 min | 16h25 – 16h55 |
| 5 | Lançamento Oficial dos Mini-Projetos do Intervalo (1 Mês) | 50 min | 16h55 – 17h45 |
| 6 | Encerramento e Preparação para o Hiato de 1 Mês | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |

---

## Bloco 4: Prática com IA — Praticando Loops e Menus em Python (30 min)

Os alunos testam a criação de menus interativos e sistemas de repetição no computador.

---

## Bloco 5: Lançamento Oficial dos Mini-Projetos do Intervalo (1 Mês) (50 min)

**Objetivo:** Apresentar os 3 projetos desafiadores que os alunos irão desenvolver durante o hiato de 4 semanas. Como já aprenderam variáveis, `input`, `if/else` e `while`, eles têm a base completa necessária!

> **Orientação ao Tutor:** Apresente **exclusivamente as 3 opções abaixo** para que a turma escolha a sua favorita:

### 👾 Opção 1 — "Tamagotchi Escolar" (Foco em Máquina de Estados e `while` infinito)
- **A Ideia:** Um "Bichinho Virtual" (ou o próprio aluno) equilibrando Estudo, Sono e Diversão.
- **A Lógica:** 
  - Variáveis: `energia = 100`, `conhecimento = 0`, `estresse = 0`.
  - Laço `while` que roda enquanto `energia > 0` e `estresse < 100`.
  - Menu principal: `1-Estudar`, `2-Dormir`, `3-Jogar Celular`.
  - Se Estudar: `conhecimento += 10`, `energia -= 20`, `estresse += 10`.
  - Se Dormir: `energia += 50`, `estresse -= 10`.
  - Vitória se `conhecimento >= 100`. Derrota se `energia <= 0` ("Desmaiou de cansaço") ou `estresse >= 100` ("Surtou").

### ⚔️ Opção 2 — "A Jornada do Herói" (Mini RPG Textual em Salas)
- **A Ideia:** Um jogo de aventura em texto por salas de uma masmorra ou escola misteriosa.
- **A Lógica:**
  - Variável `vida = 100` e `inventario = []`.
  - Estrutura de navegação com `while` e `if/elif/else` para escolher caminhos (ex: Sala do Trono, Biblioteca, Masmorra).
  - Testes de combate com monstros usando `while` até a vida do monstro ou do jogador zerar.

### 📊 Opção 3 — "O Teste de Personalidade Buzzfeed" (Quiz de Perfil com Pontuação)
- **A Ideia:** Um quiz que descobre "Qual personagem de filme/série você é?" ou "Qual sua profissão do futuro?".
- **A Lógica:**
  - Variáveis acumuladoras para cada perfil (ex: `pontos_dev`, `pontos_gamer`, `pontos_artista`).
  - Perguntas com opções A, B, C que somam pontos em cada perfil usando `if/elif/else`.
  - Laço `while` para validar entradas incorretas (se o usuário digitar algo diferente de A, B ou C, o loop repete a pergunta).
  - No final, o programa compara as pontuações e revela o vencedor.

---

## Bloco 6: Encerramento e Preparação para o Hiato de 1 Mês (15 min)

Cada aluno escolhe qual dos 3 projetos vai desenvolver durante o mês, salva seus códigos e tira dúvidas finais com a equipe.

---

## Conceitos de Programação Absorvidos

- [x] Estrutura de repetição `while` e prevenção de laço infinito
- [x] Estrutura `for` e função `range()`
- [x] Menu infinito com `while True` e `break`
- [x] Integração completa de lógica: Variáveis + `input` + `if/elif/else` + `while`

---

### 🏠 Tarefa do Intervalo (1 Mês de Hiato)

> **Escolha UMA das 3 opções detalhadas acima (Tamagotchi Escolar, A Jornada do Herói ou Teste Buzzfeed) para desenvolver e aprimorar durante o mês de intervalo. Você irá apresentar o seu projeto na Aula 04!**
