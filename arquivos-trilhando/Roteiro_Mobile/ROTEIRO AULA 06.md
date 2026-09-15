# Roteiro de Aula — Aula 06 (Trilha Mobile)

## Consolidação de Lógica + Estruturas Avançadas (Dicionários) no Celular

**Duração total:** 180 minutos (3h00) — **Horário:** 15h00 às 18h00
**Público-alvo:** Estudantes do Ensino Médio
**Pré-requisitos da aula anterior:** Fundamentos completos das Aulas 1–5 (Variáveis, `if/else`, `while/for`, listas, funções, Pydroid 3)

---

## Bloco 1: Aquecimento — Integrando Todos os Fundamentos de Lógica (15 min)

**Objetivo:** Mostrar como os 5 pilares (`print/input`, variáveis, `if/else`, `while/for`, `def`) se conectam no celular para formar um app completo.

### Ações do Tutor:
- Escrever no quadro o mapa da lógica Python:
  ```
  ENTRADA (input) → MEMÓRIA (variáveis/listas/dicionários) → DECISÃO (if/else) → REPETIÇÃO (while/for) → MODULARIZAÇÃO (def) → SAÍDA (print)
  ```
- Mostrar como cada pilar se encaixa nos projetos executados no Pydroid 3.

---

## Bloco 2: Aula Expositiva — Estruturas de Dados Avançadas: Dicionários (30 min)

**Objetivo:** Apresentar a estrutura de Dicionários em Python (`{"chave": "valor"}`), permitindo representar objetos reais (ex: alunos, produtos, personagens) no smartphone.

### Conteúdo Teórico:

#### 1. Criando e Acessando Dicionários
```python
# Um dicionário guarda pares de chave e valor
aluno = {
    "nome": "Ana Silva",
    "idade": 16,
    "curso": "Python com IA",
    "nota": 95
}

# Acessando pela chave
print(aluno["nome"])  # Ana Silva
print(aluno["nota"])  # 95
```

#### 2. Dicionários em Listas (Banco de Dados simples no Pydroid 3)
```python
turma = [
    {"nome": "Ana", "nota": 95},
    {"nome": "Bruno", "nota": 80},
    {"nome": "Carla", "nota": 90}
]

for aluno in turma:
    print(f"Aluno: {aluno['nome']} | Nota: {aluno['nota']}")
```

---

## Bloco 3: Engenharia Reversa Guiada no Pydroid 3 (25 min)

**Objetivo:** Analisar um código que integra Dicionários, Listas e Funções com menu `while`.

---

## Resumo da Duração (15h00 às 18h00)

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | Aquecimento: O mapa completo da lógica Python | 15 min | 15h00 – 15h15 |
| 2 | Aula Expositiva: Dicionários no Pydroid 3 | 30 min | 15h15 – 15h45 |
| 3 | Engenharia Reversa no Pydroid 3 | 25 min | 15h45 – 16h10 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h10 – 16h25** |
| 4 | Prática com IA: Sistema Integrado de Gestão no Celular | 55 min | 16h25 – 17h20 |
| 5 | Prompt Arquitetural: Refatoração para Interface Visível | 25 min | 17h20 – 17h45 |
| 6 | Encerramento e Preparação para Flet (Aula 7) | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |

---

## Bloco 4: Prática com IA — Sistema Integrado de Gestão no Celular (55 min)

**Objetivo:** Construir um sistema robusto no Pydroid 3 que junta menu `while`, cadastro em dicionário e funções de consulta.

---

## Bloco 5: Prompt Arquitetural — Refatoração para Interface Visível (25 min)

Preparação dos dados e funções para a transição do terminal para o Flet no celular na Aula 7.

---

## Bloco 6: Encerramento e Backup (15 min)

> **Marco Pedagógico:** Ao final da Aula 6, o aluno domina toda a lógica de programação essencial no celular! Nas Aulas 7 a 9, vamos transformar essa lógica em aplicativos visuais de verdade.

---

## Conceitos de Programação Absorvidos

- [x] Estruturas de dados avançadas: Dicionários (`dict`) no Pydroid 3
- [x] Combinação de Listas de Dicionários
- [x] Integração total: `input` → Variáveis → `if/else` → `while` → `list/dict` → `def`
- [x] Arquitetura de código pré-GUI no smartphone

---

### 🏠 Micro-Missão de Casa (Para o final desta aula)

> **Escolha UMA das duas opções abaixo para realizar no Pydroid 3 ou Caderno (10 a 15 min):**

#### 📱 Opção A — "O Perfil de Usuário do Seu App no Celular"
- **Tarefa:** Crie no Pydroid 3 um dicionário chamado `usuario` com as chaves `"nome"`, `"idade"`, `"bio"` e `"foto_perfil"`. Peça para o usuário preencher com `input()` e exiba o cartão de perfil no terminal.

#### 🎮 Opção B — "O Inventário de RPG com Dicionário"
- **Tarefa:** Crie no Pydroid 3 um dicionário para um item de jogo contendo `"nome"`, `"tipo"` (espada/escudo/poção), `"poder"` e `"preco"`. Exiba uma mensagem formatada mostrando as estatísticas do item!
