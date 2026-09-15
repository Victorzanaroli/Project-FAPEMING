# Roteiro de Aula — Aula 03 (Trilha Mobile)

## Tomada de Decisão: if, elif, else no Smartphone + Lançamento do Mini-Projeto de Intervalo

**Duração total:** 180 minutos (3h00) — **Horário:** 15h00 às 18h00
**Público-alvo:** Estudantes do Ensino Médio
**Pré-requisitos:** Variáveis, tipos de dados, `input()`, `print()`, Pydroid 3 instalado


---

## Bloco 1: Aquecimento — Tomando Decisões no Celular (10 min)

**Objetivo:** Demonstrar como o aplicativo toma caminhos diferentes com `if` e `else`.

```python
chuva = input("Está chovendo hoje? (sim/não): ")
if chuva == "sim":
    print("☂️ Leve seu guarda-chuva!")
else:
    print("😎 Use óculos de sol!")
```

---

## Bloco 2: Aula Expositiva — Estruturas Condicionais no Mobile (25 min)

### Conteúdo Teórico:
- `if`, `elif`, `else`
- Operadores de comparação: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Operadores lógicos: `and`, `or`, `not`

> **Atenção:** `=` guarda o valor na variável. `==` compara se duas coisas são iguais!

---

## Bloco 3: Engenharia Reversa — Escape Room (20 min)

Examinar as opções do jogo no Pydroid 3 (`if escolha == "1": ... elif escolha == "2": ...`).

---

## Bloco 4: Prática com IA — Sistema de Decisão Escolar/Gamer (45 min)

Criar um programa com `if/elif/else` que valida média escolar ou nível de jogador e roda no Pydroid 3.

---

## Bloco 5: Desafio "Plot Twist" (20 min)

Alteração manual no código sem usar a IA, testando a independência do aluno.

## Resumo da Duração (15h00 às 18h00)

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | Aquecimento: Tomando Decisões no Celular | 15 min | 15h00 – 15h15 |
| 2 | Aula Expositiva: Estruturas Condicionais no Mobile | 30 min | 15h15 – 15h45 |
| 3 | Engenharia Reversa: Escape Room no Celular | 25 min | 15h45 – 16h10 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h10 – 16h25** |
| 4 | Prática com IA: Sistema de Decisão Escolar/Gamer | 50 min | 16h25 – 17h15 |
| 5 | Desafio "Plot Twist" no Pydroid 3 | 25 min | 17h15 – 17h40 |
| 6 | Lançamento do Mini-Projeto de Intervalo + Encerramento | 20 min | 17h40 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |

---


## Material Didático Complementar

### ⚡ Quiz de Aquecimento (Para o início da Aula 04)

#### ❓ Pergunta 1: Verdadeiro ou Falso?
Em Python, `=` serve para testar se duas coisas são iguais e `==` serve para guardar valores na variável.
* [ ] Verdadeiro
* [ ] Falso

#### ❓ Pergunta 2: Múltipla Escolha
Qual condição deixa entrar quem tem 18 anos ou mais E nome na lista VIP?
* A) `if idade >= 18 and lista_vip == "sim":`
* B) `if idade = 18 or lista_vip = "sim":`
* C) `if idade > 18 or dançou == True:`
* D) `if idade + lista == 100:`

#### ❓ Pergunta 3: Encontre o Erro! 🔍
```python
nota = 80
if nota = 70
    print("Aprovado!")
```
**Quais os 2 erros na linha do `if`?**

---

#### 🔑 Gabarito Comentado (Para o Tutor)
1. **FALSO!** ❌ `=` atribui, `==` compara.
2. **Alternativa A!** 🎯 Usa `and` e `>=`.
3. **Erros:** Usou `=` em vez de `==` e faltou os dois pontos `:` no final do `if`.

---

### 🏠 Micro-Missão do Intervalo de 1 Mês (Para a volta na Aula 04 no Pydroid 3)

#### 🚀 Mini-Projeto de Intervalo: Escolha 1 das 3 Opções de Jogos/Chatbots

Como a turma terá 1 mês de intervalo antes da Aula 04, os alunos deverão escolher **UM** dos 3 projetos autorais abaixo para desenvolver no celular (Pydroid 3) ou no computador. No início da Aula 04, faremos uma **Mini-Feira de Projetos Mobile (15-20 min)** onde cada aluno/dupla mostrará seu programa rodando no smartphone!

---

#### 🎮 Opção 1: "Tamagotchi Escolar" (Foco em Máquina de Estados com `while` Infinito)
- **A Ideia:** Um Bichinho Virtual (ou o próprio aluno como personagem) que precisa equilibrar Estudo, Sono e Diversão no Pydroid 3.
- **Lógica Principal:**
  - Variáveis inteiras iniciais: `energia = 100`, `conhecimento = 0`, `estresse = 0`.
  - Laço `while` que roda enquanto `energia > 0 and estresse < 100 and conhecimento < 100`.
- **Menu Básico:** Exibe opções: `1-Estudar`, `2-Dormir`, `3-Jogar celular`.
  - *Se 1 (Estudar):* `conhecimento += 10`, `energia -= 20`, `estresse += 10`.
  - *Se 2 (Dormir):* `energia += 50`, `estresse -= 10`.
  - *Se 3 (Jogar):* `estresse -= 30`, `energia -= 10`.
  - O laço repete mostrando o status atualizado do personagem no terminal do celular.
- **Missão Extra (Para o Mês):** 
  - Vitória se `conhecimento >= 100` -> `print("🎉 Parabéns! Você passou de ano com sucesso!")`.
  - Derrota se `energia <= 0` -> `print("💀 Você desmaiou de cansaço!")`.
  - Derrota se `estresse >= 100` -> `print("🤯 Você surtou de estresse!")`.
  - *Desafio IA:* Usar o Gemini no celular para ajudar a balancear os números (`+10`, `-20`)!

---

#### ⚔️ Opção 2: "A Jornada do Herói" (Mini RPG Textual em Salas Encadeadas)
- **A Ideia:** Um jogo de aventura onde o jogador avança de sala em sala e precisa tomar decisões no Pydroid 3 que gastam sua vida.
- **Lógica Principal:**
  - Variável inicial `vida = 100`. Estrutura linear de salas.
  - Entra na Sala 1, lê o texto, faz uma escolha com `input()`. Se a escolha for ruim, `vida = vida - 40`.
  - Usar `if vida > 0:` para permitir avançar para as salas seguintes.
- **Missão Extra (Para o Mês):** 
  - Criar o "Chefão Final" na última sala com `vida_chefe = 50`.
  - Usar um laço `while vida_chefe > 0 and vida > 0:` onde o jogador ataca (`vida_chefe -= 15`) e toma dano (`vida -= 10`) a cada rodada até um dos dois zerar a vida!

---

#### 🧩 Opção 3: "O Teste de Personalidade Buzzfeed" (Foco em Condicionais `if/elif/else`)
- **A Ideia:** Um quiz interativo no celular com 3 a 5 perguntas (*"Qual herói da Marvel você é?"* ou *"Qual profissão combina com você?"*).
- **Lógica Principal:**
  - Variáveis separadas de pontuação para cada perfil (ex: `pontos_aranha = 0`, `pontos_thor = 0`).
  - Perguntas com `print()` e capturas com `input()` (`A`, `B` ou `C`).
  - Estruturas `if` somam pontos na variável correspondente.
- **Missão Extra (Para o Mês):**
  - Criar um grande bloco `if/elif/else` no final para declarar automaticamente o perfil campeão.
  - Tratar erros de digitação: se o usuário digitar uma opção inválida (ex: `"X"`), usar um `else:` avisando *"Resposta inválida! Você perdeu os pontos desta rodada"*.
