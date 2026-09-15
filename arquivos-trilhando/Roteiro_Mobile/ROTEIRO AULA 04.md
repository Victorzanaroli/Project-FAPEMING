# Roteiro de Aula — Aula 04 (Trilha Mobile)

## Repetição e Automação: while, for & Apresentação dos Chatbots Mobile

**Duração total:** 180 minutos (3h00) — **Horário:** 15h00 às 18h00
**Público-alvo:** Estudantes do Ensino Médio
**Pré-requisitos:** Variáveis, `input()`, `if/elif/else`, Mini-Projeto do Intervalo criado no Pydroid 3


---

## Bloco 1: Retorno do Intervalo & Mini-Feira de Projetos Mobile (20 min)

**Objetivo:** Celebrar o retorno após o intervalo de 1 mês e apresentar os Mini-Projetos (Tamagotchi Escolar, A Jornada do Herói ou Quiz Buzzfeed) criados pelos alunos no Pydroid 3 do celular.

### Ações do Tutor:
- **Acolhimento (5 min):** Boas-vindas de volta após as 4 semanas!
- **Mini-Feira dos Projetos Mobile (10 min):** Alunos abrem o projeto escolhido (Tamagotchi Escolar, A Jornada do Herói ou Quiz Buzzfeed) no Pydroid 3 do celular (ou PC) e executam para a turma.
- **Conexão com Repetição (5 min):** 
  > *"Para o seu jogo ou Tamagotchi não fechar sozinho depois de uma ação, precisamos que ele fique REPETINDO. Hoje vamos aprender o poder do while e do for no celular!"*


---

## Bloco 2: Aula Expositiva — while, for e o Botão Stop no Celular (25 min)

### Conteúdo Teórico:
- Laço `while` (enquanto a condição for verdadeira).
- Laço `for` + `range(inicio, fim)`.
- Contadores (`contador += 1`).

### 📱 Dica Crucial para Smartphone:
- **O Laço Infinito no Pydroid 3:** Se o aluno esquecer o `contador += 1`, a tela do celular vai piscar sem parar.
- **Como resolver no celular:** Ensinar a apertar o **botão quadrado vermelho (STOP)** no canto da tela do Pydroid 3 para interromper a execução com segurança!

### 🏠 Micro-Missão de Casa (Para o final desta aula)

> **Escolha UMA das duas opções abaixo para realizar no Pydroid 3 / Caderno (10 a 15 min):**

#### 🤖 Opção A — "O Robô da Chamada Escolar no Celular"
- **Tarefa:** Escreva no Pydroid 3 uma estrutura `for` que percorre uma lista de 4 colegas da sua turma e imprime o nome de cada um com a mensagem *"presente no app!"*.

#### 🚀 Opção B — "Contador Regressivo de Lançamento"
- **Tarefa:** Crie no Pydroid 3 do celular uma contagem regressiva de 10 até 1 usando o laço `while` ou `for` com `range(10, 0, -1)` e mostre no final `print("🚀 FOGUETE LANÇADO DO CELULAR COM SUCESSO!")`.

---

## Bloco 3: Engenharia Reversa — Batalha Naval no Celular (20 min)

Inspecionar o `while tentativas > 0:` no script da Batalha Naval rodando no Pydroid 3.

---

## Bloco 4: Prática com IA — Jogo de Adivinhação no Celular (45 min)

Criar o Jogo de Adivinhação de Números (1 a 100) com 7 tentativas usando `while` e `random` no Pydroid 3.

---

## Bloco 5: Depuração com IA — Resolvendo o Loop Infinito (15 min)

Projetar um código com loop infinito e usar o Gemini para depurar e corrigir.

---

## Resumo da Duração (15h00 às 18h00)

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | Boas-Vindas, Feira dos Projetos & Aquecimento | 25 min | 15h00 – 15h25 |
| 2 | Aula Expositiva: while, for e Botão Stop no Celular | 30 min | 15h25 – 15h55 |
| 3 | Engenharia Reversa: Batalha Naval no Celular | 25 min | 15h55 – 16h20 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h20 – 16h35** |
| 4 | Prática com IA: Jogo de Adivinhação no Celular | 55 min | 16h35 – 17h30 |
| 5 | Depuração com IA: Resolvendo Loop Infinito | 15 min | 17h30 – 17h45 |
| 6 | Encerramento e Backup | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |

---


## Material Didático Complementar

### ⚡ Quiz de Aquecimento (Para o início da Aula 05)

#### ❓ Pergunta 1: Verdadeiro ou Falso?
Se você esquecer o `contador += 1` no `while`, o programa entra em loop infinito e no Pydroid 3 você deve apertar o botão vermelho de STOP para parar.
* [ ] Verdadeiro
* [ ] Falso

#### ❓ Pergunta 2: Múltipla Escolha
O que o `range(1, 4)` gera no laço `for`?
* A) Os números 1, 2 e 3.
* B) Os números 1, 2, 3 e 4.
* C) Uma coxinha de frango.
* D) O número 4.

#### ❓ Pergunta 3: Encontre o Erro! 🔍
```python
numero = 1
while numero <= 5:
    print(numero)
```
**O que está faltando para não travar o celular?**

---

#### 🔑 Gabarito Comentado (Para o Tutor)
1. **VERDADEIRO!** ✅ O botão vermelho Interrompe o loop infinito no Pydroid 3.
2. **Alternativa A!** 🎯 Gera 1, 2 e 3.
3. **Faltou o incremento `numero += 1`!** 🛑
