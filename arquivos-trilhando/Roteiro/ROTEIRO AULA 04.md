# Roteiro de Aula — Aula 04

## Repetição e Automação: while, for

**Duração total:** 150 minutos (2h30)
**Público-alvo:** Estudantes do Ensino Médio sem conhecimento prévio em programação
**Pré-requisitos da aula anterior:** Variáveis, tipos, `input()`, `if/elif/else`, operadores

---

## Bloco 1: Aquecimento — O Poder da Repetição (10 min)

**Objetivo:** Mostrar que o grande poder dos computadores é fazer a mesma coisa milhões de vezes sem errar nem cansar.

### Ações do Tutor:
- Analogia no quadro:
  > *"Imaginem que o professor precisa chamar a chamada de 40 alunos. Ele pega a lista e, PARA CADA nome, pergunta: 'Presente?'. Isso é um laço de repetição — o computador faz isso em milissegundos."*
- Escrever no quadro o pseudocódigo:
  ```
  PARA CADA aluno na lista_de_chamada:
      Perguntar: "Aluno X, presente?"
      Anotar a resposta
  ```
- Traduzir para Python:
  ```python
  alunos = ["Ana", "Bruno", "Carla"]
  for aluno in alunos:
      print(f"{aluno}, presente?")
  ```
- Rodar ao vivo e mostrar as 3 linhas impressas automaticamente.

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

## Resumo da Duração

| Bloco | Atividade | Duração |
|-------|-----------|---------|
| 1 | Aquecimento: O poder da repetição | 10 min |
| 2 | Aula Expositiva: while, for, range, break | 25 min |
| 3 | Engenharia Reversa: BatalhaNaval.py | 20 min |
| 4 | Prática com IA: Jogo de Adivinhação | 45 min |
| 5 | Depuração com IA: Laço Infinito | 15 min |
| 6 | Encerramento e Backup | 10 min |
| **Total** | | **125 min** |

> **Margem:** 25 minutos para imprevistos técnicos.

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
