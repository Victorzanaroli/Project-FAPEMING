# 🔁 Roteiro de Aula — Aula 03 (Trilha Mobile)

## Tratamento de Erros (`try/except`) + Repetição (`while`, `for`) + Lançamento dos Projetos do Intervalo

**Data:** 30 de setembro de 2026 (quarta-feira) — **Horário:** 15h00 às 18h00
**Duração total:** 180 minutos (3h00)
**Público-alvo:** Estudantes do Ensino Médio
**Pré-requisitos da aula anterior:** Variáveis, tipos de dados (`str`, `int`, `float`), `print()`, `input()`, `if/elif/else`, VS Code

> **🔑 Legenda do Roteiro:**
> - `[SLIDE]` → Projetar no telão (conceito visual/teórico)
> - `[IDE]` → Abrir o VS Code e digitar ao vivo (alunos copiam junto)
> - `[❓ ENGAJAMENTO]` → Jogar a pergunta para a turma, aguardar respostas
> - `[⏱️]` → Marcação de tempo estimado para o bloco

---

## 📅 Grade de Horários

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | **⚡ Quiz de Aquecimento** — Revisão da Aula 02 | 15 min | 15h00 – 15h15 |
| 2 | Aula Expositiva: `try/except` — Blindando o Código | 30 min | 15h15 – 15h45 |
| 3 | Aula Expositiva: Laços `while` e `for` | 25 min | 15h45 – 16h10 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h10 – 16h25** |
| 4 | Prática com IA: Missões de Loop + try/except no VS Code | 50 min | 16h25 – 17h15 |
| 5 | Lançamento Oficial dos Projetos do Intervalo (1 Mês) | 30 min | 17h15 – 17h45 |
| 6 | Encerramento, Tarefa e Preparação para o Hiato | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |

---

## ⚡ Bloco 1: Quiz de Aquecimento — Revisão da Aula 02 (15 min)

> **Objetivo:** Ativar o conhecimento da aula anterior de forma dinâmica e identificar dúvidas antes de avançar para o novo conteúdo.

`[SLIDE]` — Projete as perguntas no telão uma a uma. Deixe a turma responder em voz alta antes de revelar o gabarito.

---

### ❓ Pergunta 1: Verdadeiro ou Falso?
> *"O `input()` sempre retorna um número quando o usuário digita um dígito, então posso somar dois `input()` direto sem converter."*
- [ ] Verdadeiro
- [ ] Falso

**🔑 Gabarito:** **FALSO!** ❌ O `input()` SEMPRE retorna `str` (texto). `"5" + "3"` = `"53"` e não `8`. Por isso precisamos do `int()` ou `float()`.

---

### ❓ Pergunta 2: Múltipla Escolha
O código abaixo vai gerar qual resultado na tela?
```python
nota = int(input("Sua nota: "))
if nota >= 7:
    print("✅ Aprovado!")
elif nota >= 5:
    print("📋 Recuperação")
else:
    print("❌ Reprovado")
```
Se o aluno digitar `5`, o programa imprime:
- A) `✅ Aprovado!`
- B) `📋 Recuperação`
- C) `❌ Reprovado`
- D) Não imprime nada

**🔑 Gabarito:** **Alternativa B!** 🎯 `5 >= 7` é falso, então vai para `elif nota >= 5` que é **verdadeiro**.

---

### ❓ Pergunta 3: Encontre o Erro! 🔍
```python
idade = input("Quantos anos você tem? ")
if idade >= 18:
    print("Você é maior de idade!")
```
**Qual é o problema e como corrigir?**

**🔑 Gabarito:** O `input()` retorna texto (`str`) e não dá para comparar texto com número. Corrigir com `idade = int(input("Quantos anos você tem? "))`.

---

`[❓ ENGAJAMENTO]` — Rodada rápida:
> **"Me fala em UMA palavra o que vocês mais gostaram da Aula 2!"**

---

## 🛡️ Bloco 2: Aula Expositiva — `try/except`: Blindando o Código Contra Erros (30 min)

> **Objetivo:** Ensinar o tratamento de exceções com `try/except` para criar programas robustos que não "quebram" quando o usuário digita algo inesperado.

### ⏱️ [0–5 min] A Dor do Código Sem Proteção

`[IDE]` — Mostre o erro na prática:
```python
# Código SEM proteção: quebrará se o usuário digitar "abc"
numero = int(input("Digite um número: "))
print(f"O dobro é: {numero * 2}")
```

Rode o código e digite `"abc"` propositalmente. Mostre o erro `ValueError` na tela.

`[❓ ENGAJAMENTO]`
> **"O que aconteceu? Esse erro feio apareceria para os usuários do nosso app. Como evitar?"**

---

### ⏱️ [5–20 min] A Blindagem: `try/except`

`[SLIDE]` — Projete a estrutura:

```
try:            → "Tente fazer isso..."
    [código]
except:         → "Se der erro, faça isso em vez de travar!"
    [tratamento]
```

`[IDE]` — Evoluindo em 3 passos:

#### Passo 1: `try/except` básico
```python
# bloco_try_basico.py
try:
    numero = int(input("Digite um número: "))
    print(f"O dobro é: {numero * 2}")
except:
    print("⚠️ Isso não é um número válido! Tente de novo.")
```

#### Passo 2: `try/except` com erro específico
```python
# bloco_try_especifico.py
try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 100 / numero
    print(f"100 dividido por {numero} = {resultado}")
except ValueError:
    print("❌ Erro: você digitou texto onde esperava um número!")
except ZeroDivisionError:
    print("❌ Erro: não é possível dividir por zero!")
```

**Roteiro de fala:**
- *"O `try` é a 'zona de risco' — o código que pode falhar fica aqui."*
- *"O `except` é o 'plano B' — o que fazer quando o erro acontecer."*
- *"Podemos ter vários `except` para tratar tipos diferentes de erro, igualzinho ao `elif`!"*

#### Passo 3: `try/except` com `else` e `finally`
```python
# bloco_try_completo.py
try:
    idade = int(input("Qual é a sua idade? "))
except ValueError:
    print("❌ Digite apenas números!")
else:
    # Roda SÓ se não houve erro
    print(f"✅ Idade registrada: {idade} anos.")
finally:
    # Roda SEMPRE, com ou sem erro
    print("--- Verificação concluída. ---")
```

`[❓ ENGAJAMENTO]`
> **"Por que o bloco `finally` roda sempre? Onde isso seria útil em um app real?"**
> *(Ex: fechar uma conexão com banco de dados, independentemente de erro)*

---

### ⏱️ [20–30 min] `try/except` dentro de `while` — A Combinação Poderosa

`[IDE]` — O padrão mais usado no mercado:
```python
# validacao_robusta.py
while True:
    try:
        nota = float(input("Digite sua nota (0 a 10): "))
        if 0 <= nota <= 10:
            break  # Sai do loop se a nota for válida
        else:
            print("⚠️ A nota deve ser entre 0 e 10!")
    except ValueError:
        print("❌ Isso não é um número! Tente novamente.")

print(f"✅ Nota registrada com sucesso: {nota}")
```

**Roteiro de fala:**
- *"Esse é o padrão 'repita até o usuário acertar'. O `while True` mantém o loop rodando, o `break` só deixa sair se tudo estiver certo."*
- *"Todo app profissional usa esse padrão — Instagram, iFood, qualquer sistema de login."*

---

## 🔁 Bloco 3: Aula Expositiva — Laços `while` e `for` (25 min)

> **Objetivo:** Formalizar os laços de repetição `while` e `for`, contadores, acumuladores e a função `range()`.

### ⏱️ [0–10 min] O Laço `while` — Enquanto a Condição For Verdadeira

`[IDE]` — Criar `loops_while.py`:

```python
# 1. while básico com contador
energia = 100
while energia > 0:
    print(f"⚡ Jogando no celular... Energia atual: {energia}")
    energia -= 20  # Reduz energia a cada rodada

print("🪫 Sua energia acabou! Game Over.")

# 2. Menu de opções infinito com while True e break
print("\n--- MENU DO APP ---")
while True:
    opcao = input("1-Jogar | 2-Instruções | 3-Sair: ")
    if opcao == "1":
        print("🎮 Iniciando o jogo...")
    elif opcao == "2":
        print("📖 Instruções: sobreviva o máximo possível!")
    elif opcao == "3":
        print("👋 Saindo do app... Até mais!")
        break  # Interrompe o laço
    else:
        print("⚠️ Opção inválida! Escolha 1, 2 ou 3.")
```

`[❓ ENGAJAMENTO]`
> **"O que aconteceria se a gente esquecesse o `energia -= 20`? E o `break`?"**
> *(Loop infinito — travar o programa!)*

---

### ⏱️ [10–20 min] O Laço `for` — Para Cada Item em uma Sequência

`[IDE]` — Criar `loops_for.py`:

```python
# 1. for com range() — repetição contada
print("🚀 Contagem regressiva:")
for i in range(5, 0, -1):
    print(i)
print("💥 DECOLAR!")

# 2. for percorrendo uma lista
jogadores = ["Ana", "Bruno", "Carla", "Diego"]
print("\n🏆 Ranking:")
for posicao, nome in enumerate(jogadores, start=1):
    print(f"{posicao}º lugar: {nome}")

# 3. for acumulador — somando pontuações
pontuacoes = [150, 230, 80, 310, 195]
total = 0
for ponto in pontuacoes:
    total += ponto
print(f"\nTotal de pontos do time: {total}")
```

**Roteiro de fala:**
- *"`range(5, 0, -1)` significa: começa no 5, vai até 0 (exclusive), de -1 em -1."*
- *"`enumerate()` dá o índice e o valor ao mesmo tempo — não precisa mais de contador manual!"*

---

### ⏱️ [20–25 min] `while` vs `for` — Quando Usar Cada Um?

`[SLIDE]` — Projete a tabela:

| Laço | Quando usar | Exemplo no dia a dia |
|------|-------------|---------------------|
| `while` | Quando não sei quantas vezes vai repetir | Menu de app, validação de login, jogo rodando "infinito" |
| `for` | Quando sei exatamente quantas vezes ou tenho uma lista | Processar todos os itens de uma lista, contar de 1 a 10 |

---

## ☕ Intervalo — 15 minutos (16h10 – 16h25)

Antes de liberar, projete no telão:
```
☕ INTERVALO!
Quando voltar: você vai colocar tudo junto — try/except + while + for — numa missão prática com IA.
Deixe o VS Code aberto. 🎮
```

---

## 🟠 Bloco 4: Prática com IA — Missões de Loop + try/except (50 min)

> **Objetivo:** Os alunos usam a IA para gerar e personalizar scripts que combinam `try/except`, `while` e `for` no VS Code.

### ⏱️ [0–5 min] Instrução do Bloco

`[SLIDE]` — Projete:
```
🤖 REGRA DE OURO:
1. Copie o prompt → cole na IA → rode no VS Code.
2. DEU ERRO? Copie o erro → cole na IA → peça correção.
3. Seja o DETETIVE: identifique onde está o try/except, o while e o for no código.
```

---

### ⏱️ [5–50 min] Escolha sua Missão!

#### 🎰 MISSÃO A — "O Caixa Eletrônico Blindado" *(para quem curte apps financeiros)*

**Prompt para copiar na IA:**
```
Atue como professor de Python para iniciantes.
Crie um programa de Caixa Eletrônico simples no terminal do VS Code.
Regras:
1. O programa deve ter um saldo inicial de R$ 500,00.
2. Use um laço while True com menu: 1-Ver Saldo | 2-Sacar | 3-Depositar | 4-Sair.
3. Use try/except ValueError para tratar entradas não numéricas no saque e depósito.
4. Não permita sacar mais do que o saldo disponível (use if para isso).
5. Máximo 30 linhas, sem bibliotecas externas, comentários em português.
```

**Desafio extra:** Peça à IA para adicionar um histórico de transações usando uma lista com `append()`.

---

#### 🎮 MISSÃO B — "O Quiz Implacável" *(para quem curte jogos de perguntas)*

**Prompt para copiar na IA:**
```
Atue como um apresentador animado de quiz.
Crie um programa Python para rodar no terminal do VS Code com as regras:
1. Crie uma lista com 5 perguntas de cultura geral, cada uma com 4 alternativas (A, B, C, D).
2. Use um laço for para percorrer as perguntas.
3. Use try/except para tratar respostas inválidas (não A, B, C ou D): repita a pergunta até resposta válida com while.
4. Ao final, exiba a pontuação e uma classificação com if/elif/else.
5. Máximo 35 linhas, sem bibliotecas externas, comentários em português.
```

**Desafio extra:** Peça à IA para embaralhar a ordem das perguntas usando `random.shuffle()`.

---

#### 🌡️ MISSÃO C — "O Assistente de Saúde" *(para quem curte apps úteis)*

**Prompt para copiar na IA:**
```
Atue como desenvolvedor sênior de apps Python para saúde.
Crie um assistente de saúde pessoal no terminal do VS Code com as regras:
1. Use um laço for para pedir ao usuário que registre 5 medições de frequência cardíaca (bpm).
2. Use try/except ValueError para rejeitar entradas não numéricas e repetir a pergunta.
3. Calcule e exiba: média, valor máximo e valor mínimo dos batimentos.
4. Use if/elif/else para dar um diagnóstico: "Bradicardia" (<60), "Normal" (60-100), "Taquicardia" (>100).
5. Máximo 30 linhas, sem bibliotecas externas, comentários em português.
```

**Desafio extra:** Peça à IA para plotar um gráfico simples em ASCII com os valores registrados.

---

### 🎯 Perguntas Pedagógicas do Monitor (circular pela sala)

Quando o código estiver rodando, o monitor se aproxima:

`[❓ ENGAJAMENTO]` → *"Me aponta onde está o `try/except` no seu código. O que acontece se o usuário digitar 'abc' aí?"*

`[❓ ENGAJAMENTO]` → *"Me mostra o `while` ou `for`. Qual é a condição de saída do laço?"*

`[❓ ENGAJAMENTO]` → *"Se eu tirar o `break`, o que acontece?"*

---

## 🚀 Bloco 5: Lançamento Oficial dos Projetos do Intervalo de 1 Mês (30 min)

> **Objetivo:** Apresentar os 3 projetos que os alunos irão desenvolver no smartphone (Pydroid 3) durante o hiato de outubro. Com `try/except`, `while`, `for`, variáveis, `input` e `if/else`, eles têm toda a base necessária!

> **Orientação ao Tutor:** Apresente **exclusivamente as 3 opções abaixo** para que cada aluno escolha a sua favorita:

### 👾 Opção 1 — "Tamagotchi Escolar" (Foco em `while` + máquina de estados)
- **A Ideia:** Um "Bichinho Virtual" equilibrando Estudo, Sono e Diversão.
- **A Lógica:**
  - Variáveis: `energia = 100`, `conhecimento = 0`, `estresse = 0`.
  - Laço `while` que roda enquanto `energia > 0` e `estresse < 100`.
  - Menu: `1-Estudar`, `2-Dormir`, `3-Jogar Celular`.
  - `try/except` para tratar opções inválidas.
  - Vitória se `conhecimento >= 100`. Derrota se `energia <= 0` ou `estresse >= 100`.

### ⚔️ Opção 2 — "A Jornada do Herói" (Mini RPG Textual)
- **A Ideia:** Aventura em texto por salas de uma masmorra ou escola misteriosa.
- **A Lógica:**
  - Variável `vida = 100` e `inventario = []`.
  - Navegação com `while` e `if/elif/else` para caminhos.
  - `try/except` para capturar entradas inválidas no menu.
  - Laço `for` para exibir o inventário.

### 📊 Opção 3 — "O Teste de Personalidade Buzzfeed" (Quiz de Perfil)
- **A Ideia:** Quiz que descobre "Qual personagem de filme você é?".
- **A Lógica:**
  - Variáveis acumuladoras para cada perfil.
  - Laço `for` para percorrer as perguntas.
  - `try/except` + `while` para validar respostas (A, B ou C).
  - `if/elif/else` para revelar o personagem vencedor.

---

## 🔴 Bloco 6: Encerramento, Tarefa e Preparação para o Hiato (15 min)

### Resumo do Que Foi Aprendido

`[SLIDE]` — Projete no telão:
```
🎯 O QUE VOCÊS DOMINARAM HOJE:

✅ try/except    → O código NUNCA mais vai "quebrar feio"
✅ while         → O computador REPETE enquanto precisar
✅ for           → O computador PERCORRE listas e sequências
✅ break         → Sair do loop quando a condição for atingida
✅ range()       → Gerar sequências numéricas

🚀 PRÓXIMA AULA (novembro): Vocês voltam com o projeto pronto!
```

**Frase de fechamento:**
> *"Hoje vocês aprenderam o que separa um código amador de um código profissional: robustez. Um app que quebra quando o usuário erra não serve. Com try/except, o código aguenta! Guardem o projeto no celular — nos vemos em novembro com o projeto pronto!"*

---

## ✅ Conceitos de Programação Absorvidos

- [x] Tratamento de exceções com `try/except` no VS Code
- [x] Captura de erros específicos (`ValueError`, `ZeroDivisionError`)
- [x] Blocos `else` e `finally` no tratamento de erros
- [x] Estrutura de repetição `while` e prevenção de laço infinito
- [x] Estrutura `for` com `range()`, `enumerate()` e listas
- [x] Menu interativo com `while True` e `break`
- [x] Combinação `try/except` + `while` para validação de entradas

---

## 🔑 Gabarito de Respostas — Para o Tutor

| Pergunta de Engajamento | Resposta Esperada |
|------------------------|-------------------|
| Por que o `input()` não devolve número direto? | Porque `input()` sempre retorna `str`. Precisamos converter com `int()` ou `float()` |
| O que é `ValueError`? | Erro que ocorre quando tentamos converter texto que não é número (ex: `int("abc")`) |
| Quando usar `while` vs `for`? | `while` quando não se sabe quantas repetições; `for` quando se sabe ou tem uma lista |
| O que o `break` faz? | Interrompe imediatamente o laço em que está |
| O que o `finally` faz? | Executa sempre, independentemente de ter ocorrido erro ou não |

---

### 🏠 Tarefa de Casa — Projeto Integrado (Conteúdo das Aulas 1, 2 e 3)

> **Entrega na Aula 04 (novembro). Cada aluno deve escolher UMA das três opções e desenvolver no Pydroid 3 do celular durante o mês de outubro.**

---

#### 👾 Opção 1 — Tamagotchi Escolar
Requisitos obrigatórios:
- [ ] Usa variáveis para `energia`, `conhecimento` e `estresse`
- [ ] Possui menu com `while True` + `try/except` para entradas inválidas
- [ ] Laço que roda enquanto as condições de jogo são atendidas
- [ ] Ao menos uma condicional `if/elif/else` para verificar vitória/derrota
- [ ] Mensagens amigáveis com `f-string`

#### ⚔️ Opção 2 — A Jornada do Herói (Mini RPG)
Requisitos obrigatórios:
- [ ] Navegação por pelo menos 3 "salas" com `while` e `if/elif/else`
- [ ] Inventário como lista com `append()` e exibido com `for`
- [ ] `try/except` tratando entradas inválidas do menu
- [ ] Variável de vida que decresce em combates (usando `while`)
- [ ] Mensagens dramáticas e imersivas com `f-string`

#### 📊 Opção 3 — Teste de Personalidade Buzzfeed
Requisitos obrigatórios:
- [ ] Mínimo de 5 perguntas percorridas com laço `for`
- [ ] Validação de resposta (A, B ou C) com `while` + `try/except`
- [ ] Pontuação acumulada para cada perfil com variáveis
- [ ] Resultado final revelado com `if/elif/else`
- [ ] Pelo menos uma mensagem especial por perfil com `f-string`

> **💡 Dica do Tutor:** Oriente os alunos a usarem a IA no celular para ajudar a criar e corrigir o código, mas que entendam cada linha. Na Aula 04, o tutor fará uma "auditoria viva" perguntando sobre partes específicas do código!
