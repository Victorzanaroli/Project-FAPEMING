# Roteiro de Aula — Aula 02 (Trilha Mobile)

## Desmontando o Código: Variáveis, Tipos de Dados e Input no Smartphone

**Duração total:** 180 minutos (3h00) — **Horário:** 15h00 às 18h00
**Público-alvo:** Estudantes do Ensino Médio
**Pré-requisitos da aula anterior:** `print()`, prompts com IA, aplicativo Pydroid 3 instalado


---

## Bloco 1: Abertura e Recapitulação (10 min)

**Objetivo:** Resgatar a memória da Aula 1 e reforçar o uso do Pydroid 3 no celular.

### Ações do Tutor:
- Verificar se todos estão com o Pydroid 3 aberto no celular ou o ambiente aberto no PC.
- Recapitular o `print()` e a estrutura de prompts.
- Projetar o objetivo do dia: aprender a guardar informações em caixas (variáveis) e fazer o celular perguntar coisas com o `input()`.

---

## Bloco 2: Aula Expositiva — Variáveis, Tipos e Input no Mobile (30 min)

**Objetivo:** Ensinar variáveis (`str`, `int`, `float`) e entrada do usuário.

### Conteúdo Teórico:
- **Variável:** Uma caixa com etiqueta no celular.
```python
nick = "ShadowPlayer"  # str (texto)
nivel = 10             # int (inteiro)
velocidade = 7.5       # float (decimal)
```
- **O Comando `input()`:** Faz o celular abrir a caixa de diálogo/teclado para o jogador digitar.
```python
nome = input("Digite seu nickname: ")
print("Bem-vindo ao jogo, " + nome + "!")
```
- **Conversão com `int()`:**
```python
idade_texto = input("Sua idade: ")
idade = int(idade_texto)  # Converte texto para número inteiro
```

---

## Bloco 3: Engenharia Reversa — Pac-Man no Celular (20 min)

**Objetivo:** Inspecionar o código do Pac-Man no Pydroid 3 e localizar variáveis e `input()`.

### Ações do Tutor:
- Abrir o script `Pac-Man.py` no celular/projetor.
- Pedir que os alunos encontrem a linha do `pacman = "C"`, a pontuação `pontos = 0` e o `input()`.
- Alterar o `pacman` para um emoji (ex: `"😎"`) e rodar no Pydroid 3.

---

## Bloco 4: Prática com IA — Quiz Interativo Personalizado (40 min)

**Objetivo:** Gerar um Quiz no Gemini e rodar no Pydroid 3 do celular.

### Prompt Modelo:
```
Crie um quiz de 5 perguntas sobre [FUTEBOL / ANIME / GAMES] em Python para rodar no terminal do Pydroid 3 no celular.
Regras:
1. Use apenas print() e input().
2. Crie a variável "pontos = 0".
3. Se acertar, some 1 ponto e diga "Acertou!".
4. No final, exiba o total de pontos.
```

---

## Bloco 5: Caça ao Tesouro no Código (20 min)

**Objetivo:** Tutor passa nas mesas/celulares conferindo se os alunos sabem apontar as variáveis e o `input()`.

---

## Resumo da Duração (15h00 às 18h00)

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | Abertura e Recapitulação | 15 min | 15h00 – 15h15 |
| 2 | Aula Expositiva: Variáveis, Tipos e Input no Mobile | 35 min | 15h15 – 15h50 |
| 3 | Engenharia Reversa: Pac-Man no Celular | 25 min | 15h50 – 16h15 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h15 – 16h30** |
| 4 | Prática com IA: Quiz Personalizado | 50 min | 16h30 – 17h20 |
| 5 | Caça ao Tesouro no Código | 25 min | 17h20 – 17h45 |
| 6 | Encerramento e Backup | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |

---


## Material Didático Complementar

### 🏠 Micro-Missão de Casa (Para o final desta aula)

> **Escolha UMA das duas opções abaixo para realizar no Pydroid 3 / Caderno (10 a 15 min):**

#### 👾 Opção A — "Ficha de Status do Gamer/Social Media"
- **Tarefa:** Crie no Pydroid 3 do celular (ou caderno) 3 caixas de variáveis com seus respectivos tipos para o seu personagem de jogo:
  1. `str` (Texto) -> ex: `nick = "ShadowNinja"`
  2. `int` (Número inteiro) -> ex: `nivel = 25`
  3. `float` (Número decimal) -> ex: `velocidade = 8.5`
- **Desafio:** Escreva a linha com `input()` perguntando quantas moedas de ouro o jogador tem e mostre tudo com `print()`.

#### 🐶 Opção B — "Calculadora de Idade Canina/Felina"
- **Tarefa:** Crie no Pydroid 3 um mini aplicativo que calcula a idade do seu pet em anos humanos:
  1. Peça a idade do pet com `input("Idade do pet: ")` e converta com `int()`.
  2. Multiplique por `7` e guarde na variável `idade_humana`.
  3. Execute no botão Play (▶) e veja o resultado na tela do celular!

### ⚡ Quiz de Aquecimento (Para o início da Aula 03)

#### ❓ Pergunta 1: Verdadeiro ou Falso?
O comando `input()` no Pydroid 3 sempre lê o que o usuário digita como um Texto (`str`), mesmo se ele digitar o número `18`.
* [ ] Verdadeiro
* [ ] Falso

#### ❓ Pergunta 2: Múltipla Escolha
Como perguntar a idade do jogador no celular e converter para número inteiro?
* A) `idade = int(input("Sua idade: "))`
* B) `idade = "18 anos de pura ousadia"`
* C) `idade = input("idade") + 10`
* D) `idade = int("dezoito")`

#### ❓ Pergunta 3: Encontre o Erro! 🔍
```python
idade = input("Quantos anos você tem? ")
proximo_ano = idade + 1
print(proximo_ano)
```
**Qual é o erro nesse código e como corrigir?**

---

#### 🔑 Gabarito Comentado (Para o Tutor)
1. **VERDADEIRO!** ✅ `input()` sempre devolve `str`.
2. **Alternativa A!** 🎯 `int()` converte a resposta do `input()` para número.
3. **Faltou usar `int()`!** 🛑 O correto é `idade = int(input("..."))`.
