# Roteiro de Aula — Aula 06

## Modularização e Funções

**Duração total:** 150 minutos (2h30)
**Público-alvo:** Estudantes do Ensino Médio sem conhecimento prévio em programação
**Pré-requisitos da aula anterior:** Variáveis, tipos, `if/elif/else`, `while`, `for`, listas

---

## Bloco 1: Aquecimento — A Receita de Bolo (10 min)

**Objetivo:** Mostrar que funções são "receitas" reutilizáveis.

### Ações do Tutor:
- Analogia no quadro:
  > *"Imaginem que vocês precisam fazer 3 bolos para uma festa. Vocês escrevem a receita 3 vezes? Não! Vocês escrevem a receita UMA VEZ e seguem ela 3 vezes. Em programação, isso se chama FUNÇÃO."*
- Escrever no quadro:
  ```python
  # A "receita" (função)
  def fazer_bolo(sabor):
      print(f"Misturando ingredientes do bolo de {sabor}...")
      print(f"Assando o bolo de {sabor} por 40 minutos...")
      print(f"🎂 Bolo de {sabor} pronto!")
  
  # Usando a receita 3 vezes
  fazer_bolo("chocolate")
  fazer_bolo("morango")
  fazer_bolo("cenoura")
  ```
- Rodar ao vivo — mostrar que o mesmo bloco de código é executado 3 vezes com sabores diferentes.

---

## Bloco 2: Aula Expositiva — def, Parâmetros e return (25 min)

**Objetivo:** Formalizar a criação de funções, passagem de parâmetros e retorno de valores.

### Conteúdo Teórico:

#### Criando uma Função
```python
def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo ao curso!")

# Chamando a função
saudacao("Ana")     # Olá, Ana! Bem-vindo ao curso!
saudacao("Bruno")   # Olá, Bruno! Bem-vindo ao curso!
```

#### Parâmetros — Os "Ingredientes" da Receita
```python
# Função com 2 parâmetros
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media  # Devolve o resultado

# Usando a função
resultado = calcular_media(85, 92)
print(f"Sua média é: {resultado}")  # 88.5
```

#### `return` — A Resposta da Função
> *"`print()` mostra na tela. `return` devolve o valor para quem chamou."*

```python
# COM return: a função "devolve" o resultado
def somar(a, b):
    return a + b

total = somar(10, 20)  # total = 30
print(total)

# SEM return: a função só executa, não devolve nada
def mostrar_soma(a, b):
    print(a + b)  # Mostra 30, mas não devolve

total = mostrar_soma(10, 20)  # total = None (vazio!)
```

#### Escopo — O que acontece dentro, fica dentro
```python
def minha_funcao():
    segredo = "sou local"  # Só existe DENTRO da função

minha_funcao()
# print(segredo)  # ERRO! A variável "segredo" não existe fora
```

#### Por que Modularizar?
| Sem funções (repetitivo) | Com funções (organizado) |
|---|---|
| Código copiado e colado 5 vezes | Código escrito 1 vez e chamado 5 vezes |
| Se achar um bug, precisa corrigir em 5 lugares | Se achar um bug, corrige em 1 lugar só |
| Difícil de ler e entender | Cada função tem um nome que explica o que faz |

---

## Bloco 3: Engenharia Reversa — EscapeRoom.py (20 min)

**Objetivo:** Identificar funções no código real e visualizar como modularizar.

### Ações do Tutor:
- Abrir `EscapeRoom.py` no projetor.
- Focar nas funções existentes:

| O que procurar | Onde está | Conceito |
|---|---|---|
| *"Quais funções existem neste código?"* | `limpar_tela()` (linha 4) e `jogar_escape_room()` (linha 8) | `def` + funções auxiliares |
| *"O que a `limpar_tela()` faz?"* | Limpa o terminal a cada transição de sala | Função utilitária reutilizável |
| *"Cada sala poderia ser uma função separada?"* | Sim! Ex: `def sala()`, `def cozinha()`, `def quarto()` | Modularização por responsabilidade |

### Exercício coletivo no projetor:
- Mostrar como a Sala (linhas 20–44) poderia virar uma função:
  ```python
  def jogar_sala():
      achou = False
      while not achou:
          limpar_tela()
          print("🛋️ VOCÊ ESTÁ NA SALA")
          # ... (mesmo código de dentro)
      return True  # Retorna que encontrou a pista
  ```
- Perguntar: *"Qual a vantagem disso?"* → Se quiser mudar a Sala, mexe só nessa função. Se quiser adicionar uma sala nova, é só criar outra função.

---

## Bloco 4: Prática com IA — Multi-Calculadora Modular (45 min)

**Objetivo:** Criar um programa que usa múltiplas funções para resolver problemas diferentes.

### Prompt Modelo:
```
Crie uma Multi-Calculadora em Python para terminal com as seguintes funcionalidades,
cada uma em uma FUNÇÃO SEPARADA:

1. calcular_imc(peso, altura) → calcula o IMC e retorna a classificação
   (Abaixo do peso, Normal, Sobrepeso, Obeso)
2. converter_temperatura(valor, unidade) → converte Celsius para Fahrenheit
   e vice-versa
3. calcular_media_escolar(nota1, nota2, nota3) → calcula a média e retorna
   se está Aprovado (>=70) ou Reprovado

Regras:
- Crie um MENU principal usando while True que pergunta qual calculadora usar.
- Cada função deve ter parâmetros e usar return para devolver o resultado.
- O menu principal chama a função escolhida e mostra o resultado.
- Adicione comentários em português explicando cada função.
- Use apenas print(), input() e operações matemáticas básicas.
```

### Ações do Tutor:
- Após o código funcionar, pedir ao aluno que **adicione uma 4ª função manualmente** (ex: `calcular_desconto(preco, percentual)`) — sem pedir para a IA.
- Verificar se o aluno sabe:
  1. Onde criar a função (`def` antes do menu principal)
  2. Como chamar no menu (adicionar uma opção 4)
  3. O que colocar no `return`

---

## Bloco 5: Prompt Arquitetural — Refatoração com IA (15 min)

**Objetivo:** Usar a IA para transformar código monolítico em código modular.

### Dinâmica:
- O tutor projeta um código bagunçado (tudo num bloco só, sem funções):
  ```python
  # Código MONOLÍTICO (tudo junto e misturado)
  print("=== CALCULADORA ===")
  opcao = input("1-IMC 2-Temperatura: ")
  if opcao == "1":
      peso = float(input("Peso: "))
      altura = float(input("Altura: "))
      imc = peso / (altura ** 2)
      if imc < 18.5:
          print("Abaixo do peso")
      elif imc < 25:
          print("Normal")
      else:
          print("Sobrepeso")
  elif opcao == "2":
      # ... mais código misturado
  ```
- Pedir que os alunos usem o **Prompt Arquitetural**:
  ```
  Refatore este código Python dividindo-o em funções separadas.
  Cada funcionalidade deve ter sua própria função com def, parâmetros e return.
  Mantenha o menu principal chamando cada função.
  ```
- Comparar as duas versões lado a lado: *"Qual é mais fácil de ler? Qual é mais fácil de dar manutenção?"*

---

## Bloco 6: Encerramento e Backup (10 min)

### Ações do Tutor:
- Verificar conclusão das atividades.
- Exportar logs e salvar códigos.
- Frase de fechamento:
  > *"Vocês agora dominam os fundamentos completos do Python: variáveis, decisões, repetições, listas e funções. Na próxima aula, vamos SAIR DO TERMINAL PRETO e criar interfaces visuais bonitas com o Flet — botões, cores, layouts! E vamos definir os projetos finais que vocês vão apresentar na última aula."*

---

## Resumo da Duração

| Bloco | Atividade | Duração |
|-------|-----------|---------|
| 1 | Aquecimento: A receita de bolo | 10 min |
| 2 | Aula Expositiva: def, parâmetros, return, escopo | 25 min |
| 3 | Engenharia Reversa: EscapeRoom.py (funções) | 20 min |
| 4 | Prática com IA: Multi-Calculadora Modular | 45 min |
| 5 | Prompt Arquitetural: Refatoração | 15 min |
| 6 | Encerramento e Backup | 10 min |
| **Total** | | **125 min** |

> **Margem:** 25 minutos para imprevistos.

---

## Conceitos de Programação Absorvidos

- [x] Definição de funções: `def nome(parametros):`
- [x] Parâmetros e argumentos
- [x] `return` vs `print()` dentro de funções
- [x] Escopo de variáveis (local vs global)
- [x] Refatoração de código monolítico para modular
- [x] Uso de IA para reorganizar código

## Recursos Utilizados da Pasta do Projeto

- `Jogos/EscapeRoom.py` — Material de Engenharia Reversa (foco em funções)
- Formulário Google de coleta de chats

## Marco Pedagógico

> **Ao final da Aula 6, o aluno domina os fundamentos completos de Python necessários para construir o projeto final:**
> `print` → `input` → variáveis → `if/elif/else` → `while/for` → listas → funções.
>
> As Aulas 7 e 8 aplicam esses fundamentos em um contexto de interface gráfica (Flet) e integração com IA.
