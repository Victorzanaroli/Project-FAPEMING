# Roteiro de Aula — Aula 06 (Trilha Mobile)

## Modularização e Funções no Smartphone

**Duração total:** 180 minutos (3h00) — **Horário:** 15h00 às 18h00
**Público-alvo:** Estudantes do Ensino Médio
**Pré-requisitos:** Variáveis, `if/else`, `while/for`, listas, Pydroid 3


---

## Bloco 1: Aquecimento — A Receita de Bolo (10 min)

Conceito de função (`def`): Escrever a receita uma vez e reutilizar várias vezes.

```python
def fazer_lanche(sabor):
    print(f"🥪 Lanche de {sabor} preparado no capricho!")

fazer_lanche("frango")
fazer_lanche("queijo")
```

---

## Bloco 2: Aula Expositiva — def, Parâmetros e return no Mobile (25 min)

### Conteúdo Teórico:
- Definição com `def nome(parametros):`
- Diferença entre `print()` (mostra na tela) e `return` (devolve valor para guardar na variável).
- Escopo de variáveis.

---

## Bloco 3: Engenharia Reversa — Escape Room (20 min)

Verificar como funções utilitárias como `limpar_tela()` funcionam no Pydroid 3.

---

## Bloco 4: Prática com IA — Multi-Calculadora Modular no Celular (55 min)

Criar funções separadas para IMC, Conversor de Moeda/Temperatura e Média Escolar, chamando no menu principal do Pydroid 3.

---

## Bloco 5: Prompt Arquitetural — Refatoração com IA (25 min)

Usar a IA no navegador do celular para refatorar código monolítico em funções reutilizáveis.

---

## Bloco 6: Encerramento e Backup (15 min)

Verificação dos códigos no Pydroid 3, salvar no armazenamento local e encerramento.

---

## Resumo da Duração (15h00 às 18h00)

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | Aquecimento: A receita de bolo no celular | 15 min | 15h00 – 15h15 |
| 2 | Aula Expositiva: def, parâmetros, return e escopo | 30 min | 15h15 – 15h45 |
| 3 | Engenharia Reversa: Escape Room no Pydroid 3 | 25 min | 15h45 – 16h10 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h10 – 16h25** |
| 4 | Prática com IA: Multi-Calculadora Modular no Celular | 55 min | 16h25 – 17h20 |
| 5 | Prompt Arquitetural: Refatoração com IA | 25 min | 17h20 – 17h45 |
| 6 | Encerramento e Backup no Pydroid 3 | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |

---

## Conceitos de Programação Absorvidos

- [x] Definição de funções: `def nome(parametros):`
- [x] Parâmetros e argumentos no celular
- [x] `return` vs `print()` dentro de funções
- [x] Escopo de variáveis (local vs global)
- [x] Refatoração de código monolítico para modular no Pydroid 3
- [x] Uso de IA no smartphone para reorganizar código

---

### 🏠 Micro-Missão de Casa (Para o final desta aula)

> **Escolha UMA das duas opções abaixo para realizar no Pydroid 3 / Caderno (10 a 15 min):**

#### 🍔 Opção A — "A Receita do Lanche Modular no Celular"
- **Tarefa:** Crie no Pydroid 3 a função `def montar_hambúrguer(pao, carne, molho):` retornando a frase pronta com `return`. Teste chamando a função e apertando o botão Play (▶).

#### 🏷️ Opção B — "Calculadora de Desconto de Loja"
- **Tarefa:** Crie no Pydroid 3 a função `def calcular_desconto(preco):` que calcula 10% de desconto e usa `return preco * 0.90`. Teste exibindo `print(calcular_desconto(100))`.

> **Marco Pedagógico:** Ao final da Aula 6, o aluno domina toda a lógica de programação essencial no celular! Nas Aulas 7 a 9, vamos transformar essa lógica em projetos interativos.

---

## Material Didático Complementar

### ⚡ Quiz de Aquecimento (Para o início da Aula 07)

#### ❓ Pergunta 1: Verdadeiro ou Falso?
A instrução `return` devolve um valor da função para quem a chamou, enquanto o `print()` apenas exibe a mensagem na tela.
* [ ] Verdadeiro
* [ ] Falso

#### ❓ Pergunta 2: Múltipla Escolha
Como declaramos uma função em Python chamada `calcular_desconto` que recebe o parâmetro `preco`?
* A) `def calcular_desconto(preco):`
* B) `funcao calcular_desconto = preco`
* C) `def magica_do_desconto(preco):`
* D) `return def preco()`

#### ❓ Pergunta 3: Encontre o Erro! 🔍
```python
def somar(a, b)
    return a + b
```
**O que faltou na linha do `def`?**

---

#### 🔑 Gabarito Comentado (Para o Tutor)
1. **VERDADEIRO!** ✅ `return` entrega o valor.
2. **Alternativa A!** 🎯 `def nome(parametro):`.
3. **Faltou os dois pontos `:` no final!** 🛑

