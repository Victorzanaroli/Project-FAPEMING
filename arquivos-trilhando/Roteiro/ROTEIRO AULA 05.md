# Roteiro de Aula — Aula 05

## Organização de Dados: Listas

**Duração total:** 150 minutos (2h30)
**Público-alvo:** Estudantes do Ensino Médio sem conhecimento prévio em programação
**Pré-requisitos da aula anterior:** Variáveis, `if/elif/else`, `while`, `for`, `range()`

---

## Bloco 1: Aquecimento — A Lista de Compras (10 min)

**Objetivo:** Mostrar que listas são a forma mais natural de organizar dados.

### Ações do Tutor:
- Analogia no quadro:
  > *"Imaginem sua lista de compras do mercado: ela tem vários itens, vocês podem adicionar, riscar, ver quantos faltam e reorganizar. Em Python, a gente faz EXATAMENTE isso com listas."*
- Escrever no quadro:
  ```python
  # A lista de compras
  compras = ["arroz", "feijão", "leite", "café"]
  
  # Adicionar um item
  compras.append("pão")
  
  # Quantos itens tenho?
  print(len(compras))  # 5
  
  # Ver o primeiro item
  print(compras[0])  # arroz
  ```
- Rodar ao vivo no terminal.

---

## Bloco 2: Aula Expositiva — Listas e suas Operações (25 min)

**Objetivo:** Formalizar a criação, acesso, modificação e iteração em listas.

### Conteúdo Teórico:

#### Criando Listas
```python
# Lista de textos
nomes = ["Ana", "Bruno", "Carla"]

# Lista de números
notas = [85, 92, 78, 65, 90]

# Lista vazia (para ir preenchendo depois)
inventario = []
```

#### Acessando Itens (Indexação)
> **Regra fundamental:** Em Python, a contagem começa do ZERO!

```python
frutas = ["maçã", "banana", "uva", "manga"]
#          [0]      [1]      [2]    [3]

print(frutas[0])   # maçã (primeiro)
print(frutas[2])   # uva (terceiro)
print(frutas[-1])  # manga (último)
```

#### Métodos Essenciais
| Método | O que faz | Exemplo |
|--------|----------|---------|
| `.append(item)` | Adiciona no final | `lista.append("novo")` |
| `.remove(item)` | Remove a primeira ocorrência | `lista.remove("velho")` |
| `.pop()` | Remove e retorna o último | `ultimo = lista.pop()` |
| `len(lista)` | Conta quantos itens | `total = len(lista)` |
| `item in lista` | Verifica se existe | `if "arroz" in compras:` |

#### Percorrendo uma Lista com `for`
```python
alunos = ["Ana", "Bruno", "Carla"]

for aluno in alunos:
    print(f"Chamando: {aluno}")
```

#### Listas dentro de Listas (Matrizes)
```python
# Uma grade 3x3 (tipo jogo da velha)
tabuleiro = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", " ", "O"]
]

# Acessar a posição (linha 1, coluna 2)
print(tabuleiro[1][2])  # "O"
```

### Ações do Tutor:
- Digitar cada exemplo ao vivo.
- Provocar um `IndexError` de propósito: `frutas[10]` → mostrar o erro e explicar.
- Perguntar: *"Se a lista tem 4 itens, qual é o índice do último?"* → 3 (porque começa do 0).

---

## Bloco 3: Engenharia Reversa — BatalhaNaval.py (20 min)

**Objetivo:** Mostrar que o jogo que eles já jogaram é, na essência, uma **lista de listas** (matriz).

### Ações do Tutor:
- Abrir `BatalhaNaval.py` no projetor.
- Focar nas linhas 10–17:

```python
# O tabuleiro é uma LISTA DE LISTAS (matriz 5x5)
tabuleiro = [
    [agua, agua, agua, agua, agua],  # linha 0
    [agua, agua, agua, agua, agua],  # linha 1
    [agua, agua, agua, agua, agua],  # linha 2
    [agua, agua, agua, agua, agua],  # linha 3
    [agua, agua, agua, agua, agua]   # linha 4
]
```

| O que procurar | Onde está | Conceito |
|---|---|---|
| *"Onde está a matriz do jogo?"* | Linhas 11–17: `tabuleiro = [...]` | Lista de listas |
| *"Onde os alvos são guardados?"* | Linha 20: `alvos = []` → `alvos.append(...)` | Lista vazia + append |
| *"Como ele verifica se acertou?"* | Linha 78: `if (linha_tiro, coluna_tiro) in alvos:` | `in` (verificação) |
| *"Como o mapa é impresso?"* | Linha 48–49: `for i, linha in enumerate(tabuleiro):` | `for` + lista |

### Desafio relâmpago:
> *"Mudem o tabuleiro para 6×6 em vez de 5×5. O que mais precisa mudar?"* (A validação de coordenadas na linha 65 e a criação dos alvos na linha 22–23.)

---

## Bloco 4: Prática com IA — Gerenciador de Tarefas OU Inventário de RPG (45 min)

**Objetivo:** Criar um programa que usa listas para organizar dados de forma prática.

### O aluno escolhe UM dos dois temas:

#### Opção A — Gerenciador de Tarefas (To-Do List)
```
Crie um gerenciador de tarefas em Python para terminal.
Funcionalidades:
1. Menu com opções: Adicionar tarefa, Listar tarefas, Marcar como concluída, Remover tarefa, Sair.
2. Use uma lista para guardar as tarefas.
3. Ao listar, mostre cada tarefa com um número na frente (1, 2, 3...).
4. Para marcar como concluída, adicione [✅] na frente do texto.
5. Use while True para manter o menu rodando até o usuário digitar "Sair".
6. Adicione comentários em português explicando o uso de cada método de lista.
```

#### Opção B — Inventário de RPG
```
Crie um sistema de inventário de RPG em Python para terminal.
Funcionalidades:
1. O jogador começa com uma mochila vazia (lista).
2. Menu: Adicionar item, Ver inventário, Usar item (remove da mochila), Verificar se tem item, Sair.
3. Limite de 5 itens na mochila. Se tentar adicionar acima de 5, mostre "Mochila cheia!".
4. Ao ver o inventário, mostre cada item com emoji (ex: "⚔️ Espada", "🧪 Poção").
5. Use while e for. Adicione comentários em português.
```

### Ações do Tutor:
- Circular verificando se os alunos entendem `.append()`, `.remove()`, `len()`.
- Perguntar: *"Como você sabe se a mochila está cheia?"* → `if len(inventario) >= 5:`

---

## Bloco 5: Desafio Extra — Ordenação e Prioridade (15 min)

**Objetivo:** Introduzir a ideia de dados estruturados e manipulação avançada de listas.

### Para quem terminou cedo:
> *"Peça para a IA adicionar uma funcionalidade de PRIORIDADE: cada tarefa tem Alta, Média ou Baixa prioridade. Ao listar, mostre primeiro as de prioridade Alta."*

- Isso introduz **sutilmente** conceitos de dicionários ou listas de tuplas (preparação para a Aula 6).
- O tutor pode mostrar no projetor uma solução simples usando `.sort()`.

---

## Bloco 6: Encerramento e Backup (10 min)

### Ações do Tutor:
- Verificar conclusão das atividades.
- Exportar logs e salvar códigos.
- Frase de fechamento:
  > *"Vocês aprenderam a organizar dados em listas, como uma estante de biblioteca. Na próxima aula, vamos aprender a criar FUNÇÕES — rotinas reutilizáveis que evitam copiar e colar o mesmo código várias vezes!"*

---

## Resumo da Duração

| Bloco | Atividade | Duração |
|-------|-----------|---------|
| 1 | Aquecimento: A lista de compras | 10 min |
| 2 | Aula Expositiva: Listas e operações | 25 min |
| 3 | Engenharia Reversa: BatalhaNaval.py (matriz) | 20 min |
| 4 | Prática com IA: To-Do List ou Inventário RPG | 45 min |
| 5 | Desafio Extra: Ordenação e prioridade | 15 min |
| 6 | Encerramento e Backup | 10 min |
| **Total** | | **125 min** |

> **Margem:** 25 minutos para imprevistos.

---

## Conceitos de Programação Absorvidos

- [x] Listas: criação, indexação (começa do 0!)
- [x] Métodos: `.append()`, `.remove()`, `.pop()`, `len()`
- [x] Verificação: `item in lista`
- [x] Iteração: `for item in lista:`
- [x] Listas aninhadas (matrizes)
- [x] `IndexError` e tratamento

## Recursos Utilizados da Pasta do Projeto

- `Jogos/BatalhaNaval.py` — Material de Engenharia Reversa (foco na matriz)
- Formulário Google de coleta de chats

## Vínculo com a Pesquisa

- **Artigo 1 (Crossover):** A partir desta aula, os grupos **invertem** as condições (quem usava IA agora faz sem, e vice-versa). O tutor deve anotar qual grupo é A e qual é B.
- **Artigo 2:** A complexidade dos artefatos (To-Do List / Inventário) será analisada via rubrica de maturidade de código.
