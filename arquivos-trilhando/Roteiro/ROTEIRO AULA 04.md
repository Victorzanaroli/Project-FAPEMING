# Roteiro de Aula — Aula 04

## Repetição e Automação: while, for

**Duração total:** 180 minutos (3h00) — **Horário:** 15h00 às 18h00
**Público-alvo:** Estudantes do Ensino Médio sem conhecimento prévio em programação
**Pré-requisitos da aula anterior:** Variáveis, tipos, `input()`, `if/elif/else`, operadores


---

## Bloco 1: Boas-Vindas, Apresentação dos Mini-Projetos do Intervalo e Aquecimento (20 min)

**Objetivo:** Celebrar o retorno após o intervalo de 1 mês, apresentar os Mini-Projetos (Tamagotchi Escolar, A Jornada do Herói ou Quiz Buzzfeed) desenvolvidos pelos alunos no hiato e conectar com a necessidade de automação e repetição.

### Ações do Tutor:
- **Acolhimento e Reagrupamento (5 min):** Recepcionar os alunos na volta das 4 semanas de intervalo, resgatando a empolgação com o código.
- **Mini-Feira dos Projetos do Mês (10 min):**
  - Cada aluno ou dupla projeta seu código no computador (ou mostra na tela do celular) e executa o seu projeto escolhido (Tamagotchi Escolar, A Jornada do Herói ou Quiz Buzzfeed) para a turma ou para a dupla ao lado.
  - O tutor faz elogios rápidos com destaque para o uso criativo de `input()`, variáveis e `if/elif/else`.
- **Conexão com a Repetição (5 min):**
  > *"Vocês criaram jogos e testes incríveis! Mas repararam que para jogar de novo a gente precisa dar 'play' de novo? E se a gente quisesse que o Tamagotchi ou a batalha ficasse rodando sozinha até o jogador perder ou passar de fase? Hoje vocês vão aprender o maior superpoder dos computadores: fazer a mesma coisa repetidas vezes sem errar!"*

- Analogia no quadro:
  > *"Imaginem que o professor precisa fazer a chamada de 40 alunos. Ele pega a lista e, PARA CADA nome, pergunta: 'Presente?'. Isso é um laço de repetição — o computador faz isso em milissegundos."*
- Traduzir para Python:
  ```python
  alunos = ["Ana", "Bruno", "Carla"]
  for aluno in alunos:
      print(f"{aluno}, presente?")
  ```


---

## Bloco 2: Aula Expositiva — while e for (25 min)

**Objetivo:** Formalizar os dois tipos de laço, contadores, acumuladores e comandos de controle.

### Conteúdo Teórico:

#### O Laço `while` (Enquanto)
> *"Repita ENQUANTO a condição for verdadeira."*

```python
# Conta de 1 até 5
contador = 1
while contador <= 5:
    print(f"Número: {contador}")
    contador += 1  # Sem isso, laço infinito!

print("Fim da contagem!")
```

> **Perigo!** Se esquecer de atualizar o contador (`contador += 1`), o programa roda para sempre. Isso se chama **laço infinito** — e é o erro mais clássico de programação.

#### O Laço `for` (Para cada)
> *"Repita PARA CADA item na coleção."*

```python
# Para cada número de 1 até 5
for numero in range(1, 6):
    print(f"Número: {numero}")
```

#### `range()` — O Gerador de Sequências
| Chamada | Gera | Uso típico |
|---------|------|-----------|
| `range(5)` | 0, 1, 2, 3, 4 | Repetir 5 vezes |
| `range(1, 6)` | 1, 2, 3, 4, 5 | Contar de 1 a 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 | Números pares |

#### Comandos de Controle
| Comando | O que faz |
|---------|----------|
| `break` | Sai do laço imediatamente |
| `continue` | Pula para a próxima volta |

```python
# Exemplo com break
while True:
    senha = input("Digite a senha: ")
    if senha == "1234":
        print("Acesso liberado!")
        break  # Sai do laço
    else:
        print("Senha errada! Tente de novo.")
```

#### Contadores e Acumuladores
```python
# Acumulador: soma todos os números de 1 a 10
soma = 0
for numero in range(1, 11):
    soma += numero  # soma = soma + numero
print(f"A soma total é: {soma}")  # 55
```

### Ações do Tutor:
- Digitar cada exemplo ao vivo no terminal.
- Provocar um laço infinito de propósito (esquecer o `+= 1`) e mostrar como usar `Ctrl + C` para interromper.
- Perguntar: *"Qual a diferença entre `while` e `for`?"* → `while` repete enquanto uma condição for verdadeira; `for` repete para cada item de uma sequência.

---

## Bloco 3: Engenharia Reversa — BatalhaNaval.py (20 min)

**Objetivo:** Encontrar os laços `while` e `for` dentro do jogo que os alunos já jogaram na Aula 1.

### Ações do Tutor:
- Abrir o arquivo `BatalhaNaval.py` no projetor.
- Guiar a turma:

| O que procurar | Onde está no código | Conceito reforçado |
|---|---|---|
| *"Onde o jogo fica rodando até acabar?"* | Linha 31: `while tentativas > 0 and acertos < 3:` | `while` com duas condições |
| *"Onde os navios são sorteados sem repetir posição?"* | Linha 21: `while len(alvos) < 3:` | `while` com condição de parada |
| *"Onde o mapa é desenhado linha por linha?"* | Linha 48: `for i, linha in enumerate(tabuleiro):` | `for` iterando sobre lista |
| *"E se eu mudar `tentativas = 8` para `tentativas = 3`?"* | Linha 27: O jogo fica muito mais difícil | Valor inicial do contador |

### Demonstração ao vivo:
- Mudar `tentativas = 8` para `tentativas = 20` e rodar — mostrar como uma variável controla a dificuldade.
- Mudar a quantidade de alvos de 3 para 5 e perguntar: *"O que precisa mudar junto?"* (o tabuleiro pode ficar apertado).

---

## Bloco 4: Prática com IA — Jogo de Adivinhação com Tentativas (45 min)

**Objetivo:** Criar um jogo que usa `while` para repetir e `if/else` para decidir.

### Instrução para os alunos:
> *"O computador vai pensar em um número de 1 a 100 e vocês têm 7 tentativas para adivinhar. A cada palpite, ele diz se o número é MAIOR ou MENOR."*

### Prompt Modelo:
```
Crie um jogo de adivinhação em Python para terminal.
Regras:
1. O computador sorteia um número aleatório de 1 a 100 usando a biblioteca random.
2. O jogador tem 7 tentativas para adivinhar.
3. A cada tentativa, mostre se o palpite foi MAIOR ou MENOR que o número secreto.
4. Se acertar, mostre "Parabéns! Você acertou em X tentativas!" e encerre.
5. Se gastar as 7 tentativas, mostre "Game Over! O número era Y."
6. Use while para o laço de tentativas e if/else para as comparações.
7. Adicione comentários explicativos em português.
8. Use apenas as bibliotecas random e nada mais.
```

### Ações do Tutor:
- Circular verificando se os alunos entendem o papel do `while` no jogo.
- Perguntar: *"Se eu mudar de 7 para 3 tentativas, fica mais fácil ou mais difícil?"*

---

## Bloco 5: Depuração com IA — O Laço Infinito (15 min)

**Objetivo:** Ensinar a técnica de depuração usando IA e reforçar o conceito de laço infinito.

### Dinâmica:
- O tutor projeta na tela um código **propositalmente errado** com laço infinito:
  ```python
  # CÓDIGO COM BUG
  numero = 1
  while numero <= 10:
      print(numero)
      # Ops! Esqueceu de incrementar!
  ```
- Rodar e mostrar a tela travando (Ctrl+C para parar).
- Pedir que os alunos usem o prompt de depuração no Gemini:
  ```
  Meu código Python está em loop infinito. O programa fica repetindo o número 1 sem parar.
  Aqui está o código:
  [COLAR O CÓDIGO]
  Explique o problema em 2 frases e me dê o código corrigido.
  ```
- Discutir a resposta da IA: *"Vocês viram? O erro era a falta do `numero += 1`. O computador ficou preso porque a condição NUNCA ficou falsa."*

---

## Bloco 6: Encerramento e Backup (10 min)

**Objetivo:** Salvar o progresso e preparar a próxima aula.

### Ações do Tutor:
- Verificar quais alunos completaram o jogo de adivinhação.
- Orientar o salvamento e exportação de logs.
- Frase de fechamento:
  > *"Hoje vocês aprenderam o verdadeiro superpoder dos computadores: a repetição. Na próxima aula, vamos aprender a organizar dados em LISTAS — como uma prateleira de inventário de RPG onde você pode adicionar, remover e procurar itens!"*

---

## Resumo da Duração (15h00 às 18h00)

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | Boas-Vindas, Apresentação dos Projetos & Aquecimento | 25 min | 15h00 – 15h25 |
| 2 | Aula Expositiva: while, for, range, break | 30 min | 15h25 – 15h55 |
| 3 | Engenharia Reversa: BatalhaNaval.py | 25 min | 15h55 – 16h20 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h20 – 16h35** |
| 4 | Prática com IA: Jogo de Adivinhação | 55 min | 16h35 – 17h30 |
| 5 | Depuração com IA: Laço Infinito | 15 min | 17h30 – 17h45 |
| 6 | Encerramento e Backup | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |


---

## Conceitos de Programação Absorvidos

- [x] Laço `while` (enquanto)
- [x] Laço `for` (para cada)
- [x] `range()` (gerador de sequências)
- [x] Contadores e acumuladores (`+= 1`, `+= numero`)
- [x] `break` e `continue`
- [x] Depuração de laço infinito

## Recursos Utilizados da Pasta do Projeto

- `Jogos/BatalhaNaval.py` — Material de Engenharia Reversa
- Formulário Google de coleta de chats
- Script de captura de logs (.jsonl)

## Vínculo com a Pesquisa

- **Artigo 1:** Nesta aula marca-se o fim da **Fase 1 do Crossover**. Considerar aplicar uma mini-avaliação intermediária (5 questões rápidas de raciocínio algorítmico + NASA-TLX) nos últimos 20 minutos como pós-teste T1.
- **Artigo 2:** Os logs de depuração do Bloco 5 alimentam o Índice de Iteração de Depuração (DII).

---

## Material Didático Complementar

### ⚡ Quiz de Aquecimento (Para o início da Aula 05)

#### ❓ Pergunta 1: Verdadeiro ou Falso?
Se você esquecer de atualizar o contador dentro de um laço `while` (por exemplo, esquecer de colocar `contador += 1`), o programa entra em um "laço infinito" e trava a tela repetindo para sempre.
* [ ] Verdadeiro
* [ ] Falso

#### ❓ Pergunta 2: Múltipla Escolha
O que a instrução `range(1, 4)` gera quando usada dentro de um laço `for` em Python?
* A) Os números `1`, `2` e `3` (para antes do 4).
* B) Os números `1`, `2`, `3` e `4`.
* C) Uma pizza de 4 queijos com borda recheada.
* D) Apenas o número `4`.

#### ❓ Pergunta 3: Encontre o Erro! 🔍
Um aluno tentou fazer uma contagem regressiva de 1 até 5 no terminal, mas a tela travou mostrando o número 1 sem parar:
```python
numero = 1
while numero <= 5:
    print(f"Número: {numero}")
    # Ops! Esqueceu algo aqui!
```
**O que está faltando dentro do laço `while` para o programa funcionar corretamente?**

---

#### 🔑 Gabarito Comentado (Para o Tutor)
1. **VERDADEIRO!** ✅ Sem alterar a variável testada, a condição do `while` permanece verdadeira eternamente, criando o famoso laço infinito.
2. **Alternativa A!** 🎯 O `range(inicio, fim)` vai do número inicial até o número anterior ao limite final (`1, 2, 3`). A opção C é absurdamente saborosa, mas incorreta!
3. **Faltou incrementar o contador com `numero += 1`!** 🛑 Sem essa linha, o valor da variável `numero` nunca muda, travando o programa. 
   * *Correção:* Adicionar `numero += 1` no final do bloco do `while`.

---

### 🏠 Micro-Missão de Casa (Para o final desta aula)

> **Escolha UMA das duas opções abaixo para realizar (10 a 15 min):**

#### 🤖 Opção A — "O Robô da Chamada Escolar / Treino"
- **Tarefa:** Escreva no caderno (ou PC) uma estrutura de repetição com `for` ou `while` que simula um robô chamando a lista de 4 colegas da sua fileira na sala ou contando 5 repetições de um exercício físico.
- **Exemplo:** `for aluno in ["Ana", "Bruno", "Carla", "Diego"]:` mostrar `print(aluno + ", presente?")`.

#### 🚀 Opção B — "Contador Regressivo de Lançamento"
- **Tarefa:** Escreva no caderno (ou PC) um programa em Python usando o laço `while` ou `for` com `range(10, 0, -1)` que faz a contagem regressiva de 10 até 1 e no final exibe `print("🚀 LANÇAMENTO DO FOGUETE REALIZADO COM SUCESSO!")`.


