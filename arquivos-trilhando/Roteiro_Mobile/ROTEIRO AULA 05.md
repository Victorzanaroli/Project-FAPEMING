# Roteiro de Aula — Aula 05 (Trilha Mobile)

## Organização de Dados: Listas no Smartphone

**Duração total:** 180 minutos (3h00) — **Horário:** 15h00 às 18h00
**Público-alvo:** Estudantes do Ensino Médio
**Pré-requisitos:** Variáveis, `if/else`, `while/for`, Pydroid 3 instalado


---

## Bloco 1: Aquecimento — A Lista do Mercado/Mochila (10 min)

Conceito de lista em Python: `mochila = ["caderno", "estojo", "lanche"]`.

---

## Bloco 2: Aula Expositiva — Operações com Listas no Mobile (25 min)

### Conteúdo Teórico:
- Indexação (começa no ZERO: `mochila[0]`).
- Métodos: `.append()`, `.remove()`, `len()`.
- Percorrendo listas com `for item in mochila:`.

---

## Bloco 3: Engenharia Reversa — Batalha Naval (20 min)

Verificar como a grade de navios é uma lista de listas (matriz) no Pydroid 3.

---

## Bloco 4: Prática com IA — Inventário de RPG ou To-Do List Mobile (45 min)

### Opção A: To-Do List no Celular
Gerenciador de tarefas diárias rodando no Pydroid 3.

### Opção B: Inventário de RPG
Mochila com limite de 5 itens no celular usando `.append()`, `.remove()` e `len()`.

---

### 🏠 Micro-Missão de Casa (Para o final desta aula)

> **Escolha UMA das duas opções abaixo para realizar no Pydroid 3 / Caderno (10 a 15 min):**

#### 🎒 Opção A — "Mochila de Sobrevivência Escolar no Celular"
- **Tarefa:** Crie no Pydroid 3 uma lista `mochila = ["caderno", "estojo", "lanche"]`. Use `mochila.append("garrafa")` para adicionar a garrafa e mostre a quantidade com `print(len(mochila))`.

#### 🎵 Opção B — "Top 5 Músicas/Jogos Favoritos no Celular"
- **Tarefa:** Crie no Pydroid 3 uma lista `favoritos` com 5 músicas ou jogos. Mostre o primeiro item com `print(favoritos[0])` e o último item com `print(favoritos[-1])`.


## Resumo da Duração (15h00 às 18h00)

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | Aquecimento: A Lista do Mercado/Mochila | 15 min | 15h00 – 15h15 |
| 2 | Aula Expositiva: Operações com Listas no Mobile | 30 min | 15h15 – 15h45 |
| 3 | Engenharia Reversa: Batalha Naval (Matriz) | 25 min | 15h45 – 16h10 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h10 – 16h25** |
| 4 | Prática com IA: To-Do List ou Inventário RPG no Celular | 55 min | 16h25 – 17h20 |
| 5 | Desafio Extra: Prioridade de Itens no Pydroid 3 | 25 min | 17h20 – 17h45 |
| 6 | Encerramento e Backup | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |

---


### ⚡ Quiz de Aquecimento (Para o início da Aula 06)

#### ❓ Pergunta 1: Verdadeiro ou Falso?
A contagem de elementos em uma lista Python começa pelo índice 1.
* [ ] Verdadeiro
* [ ] Falso

#### ❓ Pergunta 2: Múltipla Escolha
Qual comando adiciona "Espada" na lista `mochila`?
* A) `mochila.append("Espada")`
* B) `mochila.add_novo("Espada")`
* C) `mochila = "Espada"`
* D) `len("Espada")`

#### ❓ Pergunta 3: Encontre o Erro! 🔍
```python
frutas = ["maçã", "banana"]
print(frutas[2])
```
**Por que o índice `[2]` deu erro `IndexError`?**

---

#### 🔑 Gabarito Comentado (Para o Tutor)
1. **FALSO!** ❌ Começa pelo índice ZERO (`[0]`).
2. **Alternativa A!** 🎯 `.append()` adiciona ao final.
3. **Os índices são 0 e 1!** 🛑 O índice 2 não existe.
