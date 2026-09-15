# Roteiro de Aula — Aula 02

## Desmontando o Código: Variáveis, Tipos de Dados e Input

**Duração total:** 180 minutos (3h00) — **Horário:** 15h00 às 18h00
**Público-alvo:** Estudantes do Ensino Médio sem conhecimento prévio em programação
**Pré-requisitos da aula anterior:** Contato inicial com IA, conceito de prompt bom/ruim, `print()`


---

## Bloco 1: Abertura e Recapitulação (10 min)

**Objetivo:** Resgatar a memória da Aula 1, fixar os conceitos de prompt e `print()`.

### Ações do Tutor:
- Receber os alunos e verificar se todos estão logados nos computadores.
- Perguntar à turma: *"Quem lembra o que é um prompt? E o que o comando `print()` faz?"*
- Projetar na tela o código do Pac-Man da Aula 1 e pedir que alguém aponte onde está um `print()`.
- Conectar com o objetivo da aula: *"Vocês sabem mostrar texto na tela. Agora vamos entender como o computador guarda informações e como ele ouve o que vocês digitam."*

---

## Bloco 2: Aula Expositiva-Dialogada — Variáveis, Tipos e Input (30 min)

**Objetivo:** Ensinar os três pilares fundamentais: variáveis, tipos de dados e entrada do usuário.

### Conteúdo Teórico:

#### O que é uma Variável?
Analogia para o quadro/projetor:
> *"Uma variável é uma caixa com etiqueta. Você escolhe o nome da etiqueta e coloca algo dentro. O computador guarda e lembra quando você pedir."*

```python
# A caixa "nome" guarda o texto "Maria"
nome = "Maria"

# A caixa "idade" guarda o número 16
idade = 16

# A caixa "altura" guarda o número com vírgula 1.65
altura = 1.65
```

#### Os Três Tipos Básicos
| Tipo | O que guarda | Exemplo | Como reconhecer |
|------|-------------|---------|-----------------|
| `str` (string) | Texto | `"Olá mundo"` | Tem aspas ao redor |
| `int` (inteiro) | Número inteiro | `42` | Número sem ponto |
| `float` (flutuante) | Número com decimal | `3.14` | Número com ponto |

#### O Comando `input()` — A Pergunta do Computador
```python
# O computador pergunta e ESPERA a resposta
nome = input("Qual é o seu nome? ")
print("Olá, " + nome + "! Bem-vindo ao curso!")
```

> **Regra importante:** O `input()` sempre devolve texto (`str`). Para usar como número, precisa converter:
```python
idade_texto = input("Qual sua idade? ")
idade = int(idade_texto)  # Converte texto para número inteiro
```

### Ações do Tutor:
- Escrever os exemplos no quadro ou projetor.
- Executar ao vivo no terminal: digitar `nome = input("Seu nome: ")` e mostrar que o computador para e espera.
- Fazer a pergunta: *"Se eu digitar 16 no input, o computador entende como o número 16 ou como o texto '16'?"* (Resposta: texto! Precisa converter.)

---

## Bloco 3: Engenharia Reversa Guiada — Pac-Man.py (20 min)

**Objetivo:** Aplicar os conceitos recém-aprendidos inspecionando código real dos jogos da Aula 1.

### Ações do Tutor:
- Abrir o arquivo `Pac-Man.py` no projetor.
- Guiar a turma nesta "caça ao tesouro":

| O que procurar | Onde está no código | Conceito reforçado |
|---|---|---|
| *"Onde está o nome do personagem?"* | Linha 6: `pacman = "C"` | Variável do tipo `str` |
| *"Onde está a pontuação inicial?"* | Linha 25: `pontos = 0` | Variável do tipo `int` |
| *"Onde o computador ouve o jogador?"* | Linha 47: `jogada = input(...)` | `input()` |
| *"Se eu mudar o `'C'` para `'😎'`, o que acontece?"* | O Pac-Man muda de visual | Atribuição de variável |

- Executar o Pac-Man ao vivo, mudar o caractere do `pacman` para um emoji e rodar novamente — reação imediata.

### Perguntas de fixação:
1. *"A variável `pontos` é `int`, `str` ou `float`?"* → `int`
2. *"E se eu escrever `pontos = "zero"` em vez de `pontos = 0`, o que aconteceria?"* → Erro quando tentar somar `+ 10`
3. *"O `input()` sempre devolve o quê?"* → Texto (`str`)

---

## Bloco 4: Prática com IA — Quiz Interativo Personalizado (40 min)

**Objetivo:** Cada aluno usa o Gemini para gerar um quiz sobre um tema que ele gosta, aplicando `print()`, `input()`, variáveis e contagem de pontos.

### Instrução para os alunos:
> *"Escolham um tema que vocês adoram: futebol, música, anime, séries, games, ciência... Vocês vão pedir para a IA criar um quiz de 5 perguntas sobre esse tema."*

### Prompt Modelo (projetar no quadro):
```
Crie um quiz de 5 perguntas sobre [TEMA DO ALUNO] em Python para rodar no terminal.
Regras:
1. Use apenas print() e input().
2. Crie uma variável chamada "pontos" que começa em 0.
3. Se o jogador acertar a resposta, some 1 ponto e mostre "Acertou!".
4. Se errar, mostre "Errou! A resposta certa era [X]".
5. No final, mostre quantos acertou de 5 com uma mensagem personalizada.
6. Adicione comentários em português explicando cada parte do código.
```

### Ações do Tutor:
- Circular pelo laboratório ajudando alunos que travaram na redação do prompt.
- Validar se o script de captura de logs está ativo nos terminais.
- Se algum código der erro, orientar o aluno a usar o **prompt de depuração**:
  ```
  Meu código Python deu este erro: [COLAR O ERRO]. Explique o que fiz de errado em 2 frases e me dê o código corrigido.
  ```

---

## Bloco 5: Caça ao Tesouro no Código (20 min)

**Objetivo:** Garantir que o aluno não apenas gerou o quiz, mas compreende a estrutura.

### Dinâmica:
O tutor passa em cada mesa e faz **3 perguntas obrigatórias**:

1. *"Me mostra no código onde está a variável que conta os pontos."*
2. *"Muda o texto da pergunta 3 para algo engraçado e roda de novo."*
3. *"Qual o tipo da variável `pontos`? E da variável que guarda a resposta do `input()`?"*

### Desafio extra (para quem terminar cedo):
> *"Peça para a IA adicionar uma mensagem diferente no final dependendo da pontuação: se acertou 5/5 → 'Gênio!', se acertou 3-4 → 'Mandou bem!', se acertou 0-2 → 'Estude mais!'."*

(Isso introduz **sutilmente** o conceito de `if/elif/else` que será formalizado na Aula 3.)

---

## Bloco 6: Encerramento e Backup (10 min)

**Objetivo:** Salvar o progresso, exportar os logs de IA e preparar a próxima aula.

### Ações do Tutor:
- Verificar quais alunos conseguiram rodar o quiz com sucesso.
- Orientar o salvamento dos arquivos `.py` gerados.
- Garantir a exportação do arquivo `.jsonl` com os logs do dia.
- Pedir que compartilhem o chat com a IA via formulário Google.
- Frase de fechamento:
  > *"Hoje vocês entenderam que o computador guarda informações em caixas chamadas variáveis e que ele ouve vocês através do input(). Na próxima aula, vamos ensinar o computador a TOMAR DECISÕES — como um semáforo que decide se abre ou fecha!"*

---

## Resumo da Duração (15h00 às 18h00)

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | Abertura e Recapitulação | 15 min | 15h00 – 15h15 |
| 2 | Aula Expositiva: Variáveis, Tipos, Input | 35 min | 15h15 – 15h50 |
| 3 | Engenharia Reversa: Pac-Man.py | 25 min | 15h50 – 16h15 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h15 – 16h30** |
| 4 | Prática com IA: Quiz Personalizado | 50 min | 16h30 – 17h20 |
| 5 | Caça ao Tesouro no Código | 25 min | 17h20 – 17h45 |
| 6 | Encerramento e Backup | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |


---

## Conceitos de Programação Absorvidos

- [x] Variáveis (criação e atribuição com `=`)
- [x] Tipos de dados: `str`, `int`, `float`
- [x] Entrada do usuário: `input()`
- [x] Conversão de tipos: `int()`, `float()`
- [x] Concatenação de strings: `+`
- [x] Leitura e inspeção de código gerado por IA

## Recursos Utilizados da Pasta do Projeto

- `Jogos/Pac-Man.py` — Material de Engenharia Reversa
- Formulário Google de coleta de chats
- Script de captura de logs (.jsonl)

---

## Material Didático Complementar

### ⚡ Quiz de Aquecimento (Para o início da Aula 03)

#### ❓ Pergunta 1: Verdadeiro ou Falso?
O comando `input()` sempre lê o que o usuário digita como se fosse um Texto (`str`), mesmo se ele digitar um número inteiro como `18`.
* [ ] Verdadeiro
* [ ] Falso

#### ❓ Pergunta 2: Múltipla Escolha
Você está criando a ficha de um personagem de jogo e precisa perguntar a idade do jogador e converter para número inteiro para poder fazer contas depois. Qual linha faz isso corretamente?
* A) `idade = int(input("Qual sua idade? "))`
* B) `idade = "18 anos de pura ousadia e alegria"`
* C) `idade = input("idade") + 10`
* D) `variavel_secreta_da_nasa = int("dezoito mega bytes")`

#### ❓ Pergunta 3: Encontre o Erro! 🔍
Um aluno tentou calcular quantos anos ele terá no ano que vem, mas o código travou:
```python
idade = input("Quantos anos você tem? ")
proximo_ano = idade + 1
print(proximo_ano)
```
**Por que o Python deu erro ao tentar somar `idade + 1` e como corrigir?**

---

#### 🔑 Gabarito Comentado (Para o Tutor)
1. **VERDADEIRO!** ✅ O `input()` sempre devolve uma `str`. Se digitar `18`, o Python entende como a palavra `"18"`.
2. **Alternativa A!** 🎯 A função `int()` envolve o `input()` para converter o texto em número inteiro. A opção D dá erro porque `"dezoito"` por extenso não vira número direto.
3. **Faltou converter `idade` para inteiro com `int()`!** 🛑 O Python não consegue somar Texto (`str`) com Número (`int`). 
   * *Correção:* `idade = int(input("Quantos anos você tem? "))`

---

### 🏠 Micro-Missão de Casa (Para o final desta aula)

> **Escolha UMA das duas opções abaixo para realizar (10 a 15 min):**

#### 🎮 Opção A — "Ficha de Status do Gamer/Social Media"
- **Tarefa:** Imagine que você está criando a ficha de um personagem de jogo ou perfil de rede social. Crie no caderno (ou PC) 3 caixas de variáveis com seus tipos e valores:
  1. Variável do tipo `str` (Texto) -> ex: `nick = "ShadowNinja"`
  2. Variável do tipo `int` (Número inteiro) -> ex: `nivel = 25`
  3. Variável do tipo `float` (Número decimal) -> ex: `velocidade = 8.5`
- **Desafio:** Escreva a linha em Python perguntando a quantidade de moedas ou seguidores com `input()` e convertendo para inteiro.

#### 🐶 Opção B — "Calculadora de Idade Canina/Felina"
- **Tarefa:** Escreva no caderno (ou PC) um mini programa em Python que calcula a idade do seu pet em "anos humanos":
  1. Peça a idade do pet com `input()` e converta para `int()`.
  2. Multiplique a idade por `7` e guarde na variável `idade_humana`.
  3. Mostre o resultado com `print("Seu pet teria " + str(idade_humana) + " anos humanos!")`.


