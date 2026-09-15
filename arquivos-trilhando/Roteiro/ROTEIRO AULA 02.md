# Roteiro de Aula — Aula 02

## Variáveis, Tipos de Dados e Tomada de Decisão (if, elif, else)

**Duração total:** 180 minutos (3h00) — **Horário:** 15h00 às 18h00
**Público-alvo:** Estudantes do Ensino Médio sem conhecimento prévio em programação
**Pré-requisitos da aula anterior:** Contato inicial com IA, conceito de prompt bom/ruim, `print()`, `input()` e variáveis básicas

---

## Bloco 1: Abertura e Recapitulação (15 min)

**Objetivo:** Resgatar a memória da Aula 1, fixar os conceitos de `print()`, `input()` e variáveis iniciados na aula anterior.

### Ações do Tutor:
- Receber os alunos e verificar se todos estão logados nos computadores.
- Perguntar à turma: *"Quem lembra para que serve o `print()`? E o `input()`? O que é uma variável?"*
- Projetar no quadro o exemplo:
  ```python
  nome = input("Qual é o seu nome? ")
  print(f"Olá, {nome}! Hoje vamos ensinar o computador a tomar decisões!")
  ```
- Conectar com o objetivo da aula: *"Hoje vamos entender os tipos de dados que o computador guarda e aprender a dar inteligência ao programa com `if`, `elif` e `else`!"*

---

## Bloco 2: Aula Expositiva — Variáveis, Tipos e Tomada de Decisão (30 min)

**Objetivo:** Ensinar os tipos de dados (`str`, `int`, `float`), conversão com `int()` e a estrutura condicional completa (`if`, `elif`, `else`).

### Conteúdo Teórico:

#### 1. Tipos de Dados e Conversão
| Tipo | O que guarda | Exemplo | Como converter |
|------|-------------|---------|----------------|
| `str` (string) | Texto | `"Ana"` | Padrão do `input()` |
| `int` (inteiro) | Número inteiro | `16` | `int(input())` |
| `float` (flutuante) | Número decimal | `1.75` | `float(input())` |

```python
idade = int(input("Digite sua idade: "))  # Converte texto para número inteiro
```

#### 2. Tomada de Decisão (`if / elif / else`)
```python
nota = int(input("Digite sua nota (0 a 100): "))

if nota >= 70:
    print("✅ Aprovado com sucesso!")
elif nota >= 40:
    print("⚠️ Recuperação! Precisa estudar mais.")
else:
    print("❌ Reprovado.")
```

#### 3. Operadores de Comparação e Lógicos
- **Comparação:** `==` (igual), `!=` (diferente), `>` (maior), `<` (menor), `>=` (maior ou igual), `<=` (menor ou igual).
- **Lógicos:** `and` (E - ambas verdadeiras), `or` (OU - pelo menos uma verdadeira).

---

## Bloco 3: Engenharia Reversa Guiada — Decisões no Pac-Man e Escape Room (25 min)

**Objetivo:** Identificar como o `if/else` controla o fluxo dos jogos reais.

### Ações do Tutor:
- Abrir o código do `EscapeRoom.py` ou `Pac-Man.py` no projetor.
- Mostrar onde o `if` decide o que acontece quando o jogador faz uma escolha:
  ```python
  escolha = input("Você quer abrir a porta 1 ou porta 2? ")
  if escolha == "1":
      print("🚪 Você encontrou uma chave sagrada!")
  else:
      print("🐉 Um dragão apareceu!")
  ```

---

## Resumo da Duração (15h00 às 18h00)

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | Abertura e Recapitulação (print, input, variáveis) | 15 min | 15h00 – 15h15 |
| 2 | Aula Expositiva: Tipos de Dados e Condicionais (if/elif/else) | 30 min | 15h15 – 15h45 |
| 3 | Engenharia Reversa Guiada (Decisões em Jogos) | 25 min | 15h45 – 16h10 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h10 – 16h25** |
| 4 | Prática com IA: Sistema Inteligente de Decisões / Quiz | 55 min | 16h25 – 17h20 |
| 5 | Prompting Condicional e Testes de Estresse | 25 min | 17h20 – 17h45 |
| 6 | Encerramento e Backup | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |

---

## Bloco 4: Prática com IA — Quiz e Sistema de Decisão com IA (55 min)

**Objetivo:** Criar um programa interativo que faz perguntas, testa respostas com `if/elif/else` e acumula pontos.

### Prompt Modelo para os Alunos:
```
Atue como um professor de Python. Crie um programa de Quiz com 4 perguntas em Python.
Regras:
1. Peça o nome do jogador com input().
2. Crie uma variável pontos = 0.
3. Para cada pergunta, use se/senão (if/else) para verificar a resposta.
4. Se acertar, some 1 ponto e mostre mensagem de parabéns.
5. No final, use if/elif/else para dar um troféu baseado nos pontos.
```

---

## Bloco 5: Prompting Condicional e Testes de Estresse (25 min)

Os alunos testam variações de respostas e aprendem a tratar o `else` para respostas inválidas.

---

## Bloco 6: Encerramento e Backup (15 min)

Salvar o código `.py` e exportar os logs do dia.

---

## Conceitos de Programação Absorvidos

- [x] Variáveis e conversão de tipos (`str`, `int`, `float`)
- [x] Leitura de dados com `input()`
- [x] Condicionais (`if`, `elif`, `else`)
- [x] Operadores relacionais (`==`, `!=`, `>`, `<`) e lógicos (`and`, `or`)

---

### 🏠 Micro-Missão de Casa (Para o final desta aula)

> **Escolha UMA das duas opções abaixo para realizar no caderno ou PC (10 a 15 min):**

#### 🎮 Opção A — "O Classificador de Gamer / Estudante"
- **Tarefa:** Crie no Python (ou no caderno) um script que pede a idade do usuário e sua quantidade de horas de jogo por dia. Use `if/elif/else` para classificar o perfil em "Gamer Casual", "Pro Player" ou "Foco nos Estudos!".

#### 🌦️ Opção B — "O Assistente de Vestuário Inteligente"
- **Tarefa:** Crie um programa que pede a temperatura atual (`int(input())`) e se está chovendo (`sim/não`). Use `if/elif/else` com `and/or` para recomendar o look ideal (ex: "Jaqueta e Guarda-chuva", "Camiseta e Óculos de Sol").
