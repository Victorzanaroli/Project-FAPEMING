# Roteiro de Aula — Aula 05 (Trilha Mobile)

## Modularização e Funções: def, Parâmetros e return no Celular

**Duração total:** 180 minutos (3h00) — **Horário:** 15h00 às 18h00
**Público-alvo:** Estudantes do Ensino Médio
**Pré-requisitos da aula anterior:** Variáveis, tipos, `if/elif/else`, `while`, `for`, listas, Pydroid 3

---

## Bloco 1: Aquecimento — A Receita de Bolo no Celular (15 min)

**Objetivo:** Mostrar que funções são "receitas" reutilizáveis que organizam o código.

### Ações do Tutor:
- Analogia no quadro:
  > *"Imaginem que vocês precisam fazer 3 bolos para uma festa. Vocês escrevem a receita 3 vezes? Não! Vocês escrevem a receita UMA VEZ e seguem ela 3 vezes. Em programação, isso se chama FUNÇÃO (`def`)."*
- Escrever no Pydroid 3 / quadro:
  ```python
  # A "receita" (função)
  def fazer_bolo(sabor):
      print(f"🎂 Preparando bolo de {sabor}...")

  # Usando a receita 3 vezes
  fazer_bolo("chocolate")
  fazer_bolo("morango")
  ```

---

## Bloco 2: Aula Expositiva — def, Parâmetros e return (30 min)

**Objetivo:** Formalizar a criação de funções, passagem de parâmetros e retorno de valores com `return` no Pydroid 3.

### Conteúdo Teórico:

#### 1. Criando uma Função com `def`
```python
def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo ao curso!")

saudacao("Ana")  # Chama a função
```

#### 2. Parâmetros e a instrução `return`
```python
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media  # Devolve o valor para guardar na variável

resultado = calcular_media(80, 90)
print(f"Sua média é: {resultado}")
```

> **Diferença vital:** `print()` apenas mostra na tela; `return` devolve o valor para ser usado em outras partes do programa!

---

## Bloco 3: Engenharia Reversa Guiada no Pydroid 3 (25 min)

**Objetivo:** Identificar funções utilitárias no código real (`limpar_tela()`, `jogar_sala()`).

---

## Resumo da Duração (15h00 às 18h00)

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | Aquecimento: A receita de bolo no celular | 15 min | 15h00 – 15h15 |
| 2 | Aula Expositiva: def, parâmetros, return e escopo | 30 min | 15h15 – 15h45 |
| 3 | Engenharia Reversa no Pydroid 3 | 25 min | 15h45 – 16h10 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h10 – 16h25** |
| 4 | Prática com IA: Multi-Calculadora Modular no Celular | 55 min | 16h25 – 17h20 |
| 5 | Prompt Arquitetural: Refatoração com IA | 25 min | 17h20 – 17h45 |
| 6 | Encerramento e Backup no Pydroid 3 | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |

---

## Bloco 4: Prática com IA — Multi-Calculadora Modular no Celular (55 min)

**Objetivo:** Criar um programa modularizado onde cada calculadora (IMC, Média, Conversor de Moeda) é sua própria função com `def` e `return` no Pydroid 3.

### Prompt Modelo:
```
Crie uma Multi-Calculadora em Python para rodar no Pydroid 3 com as seguintes funcionalidades,
cada uma em uma FUNÇÃO SEPARADA com def e return:
1. calcular_imc(peso, altura)
2. converter_temperatura(celsius)
3. calcular_media(n1, n2)

Use um menu principal while True para chamar cada função.
```

---

## Bloco 5: Prompt Arquitetural — Refatoração com IA (25 min)

Usar a IA no celular para refatorar código monolítico em funções limpas.

---

## Bloco 6: Encerramento e Backup (15 min)

Salvar arquivos no Pydroid 3 e verificar domínio sobre funções.

---

## Conceitos de Programação Absorvidos

- [x] Definição de funções com `def` no celular
- [x] Parâmetros e argumentos
- [x] Retorno de valores com `return` vs `print()`
- [x] Modularização e refatoração de código no Pydroid 3

---

### 🏠 Micro-Missão de Casa (Para o final desta aula)

> **Escolha UMA das duas opções abaixo para realizar no Pydroid 3 ou Caderno (10 a 15 min):**

#### 🍔 Opção A — "A Receita do Lanche Modular no Celular"
- **Tarefa:** Escreva no Pydroid 3 a função `montar_hambúrguer(pao, carne, molho)` que usa `return` para entregar a frase do pedido. Teste chamando com seus ingredientes favoritos!

#### 🏷️ Opção B — "Calculadora de Desconto de Loja"
- **Tarefa:** Crie no Pydroid 3 uma função `calcular_desconto(preco)` que aplica 10% de desconto e retorna o valor final com `return preco * 0.90`. Teste exibindo o resultado!
