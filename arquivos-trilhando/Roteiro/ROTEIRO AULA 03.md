# Roteiro de Aula — Aula 03

## Tomada de Decisão: if, elif, else

**Duração total:** 150 minutos (2h30)
**Público-alvo:** Estudantes do Ensino Médio sem conhecimento prévio em programação
**Pré-requisitos da aula anterior:** Variáveis, tipos de dados (`str`, `int`, `float`), `print()`, `input()`

---

## Bloco 1: Aquecimento — Decisões do Dia a Dia (10 min)

**Objetivo:** Mostrar que decisões lógicas estão em todo lugar, muito antes do computador.

### Ações do Tutor:
- Escrever no quadro a seguinte situação:
  > *"SE está chovendo, ENTÃO levo guarda-chuva. SENÃO, uso óculos de sol."*
- Perguntar: *"Quem já tomou essa decisão hoje de manhã?"*
- Traduzir imediatamente para Python no quadro:
  ```python
  chuva = input("Está chovendo? (sim/não): ")
  
  if chuva == "sim":
      print("☂️ Leve o guarda-chuva!")
  else:
      print("😎 Use óculos de sol!")
  ```
- Rodar ao vivo no terminal para mostrar o funcionamento.
- Conectar: *"O computador toma decisões EXATAMENTE assim: ele testa uma condição e escolhe um caminho."*

---

## Bloco 2: Aula Expositiva — Estruturas Condicionais (25 min)

**Objetivo:** Formalizar `if`, `elif`, `else`, operadores de comparação e lógicos.

### Conteúdo Teórico:

#### A Estrutura `if / elif / else`
```python
nota = int(input("Digite sua nota: "))

if nota >= 70:
    print("✅ Aprovado!")
elif nota >= 40:
    print("⚠️ Recuperação!")
else:
    print("❌ Reprovado.")
```

> **Regra de ouro:** O Python decide **de cima para baixo**. Assim que encontra uma condição verdadeira, ele executa aquele bloco e **pula todos os outros**.

#### Operadores de Comparação
| Operador | Significado | Exemplo |
|----------|------------|---------|
| `==` | Igual a | `idade == 16` |
| `!=` | Diferente de | `cor != "azul"` |
| `>` | Maior que | `nota > 70` |
| `<` | Menor que | `faltas < 15` |
| `>=` | Maior ou igual | `media >= 60` |
| `<=` | Menor ou igual | `tempo <= 10` |

> **Atenção!** `=` é atribuição (guardar na caixa). `==` é comparação (verificar se é igual). São coisas completamente diferentes!

#### Operadores Lógicos (Combinar Condições)
| Operador | Significado | Exemplo |
|----------|------------|---------|
| `and` | E (as duas precisam ser verdadeiras) | `nota >= 70 and faltas <= 15` |
| `or` | OU (pelo menos uma precisa ser verdadeira) | `tipo == "ônibus" or altura > 2.5` |
| `not` | NÃO (inverte o resultado) | `not chovendo` |

```python
# Exemplo combinado
nota = 75
faltas = 10

if nota >= 70 and faltas <= 15:
    print("Aprovado com frequência!")
elif nota >= 70 and faltas > 15:
    print("Nota boa, mas reprovou por falta!")
else:
    print("Precisa melhorar a nota.")
```

### Ações do Tutor:
- Escrever cada exemplo no quadro e rodar no terminal.
- Fazer perguntas interativas: *"Se a nota for 70, ele cai no `>=70`?"* → Sim!
- Pedir para um aluno ditar uma condição do cotidiano e traduzir juntos para Python.

---

## Bloco 3: Engenharia Reversa — EscapeRoom.py (20 min)

**Objetivo:** Encontrar as estruturas condicionais dentro de um jogo real que os alunos já jogaram.

### Ações do Tutor:
- Abrir o arquivo `EscapeRoom.py` no projetor.
- Guiar a turma na inspeção:

| O que procurar | Onde está no código | Conceito reforçado |
|---|---|---|
| *"Onde o jogo decide se a escolha está certa?"* | Linhas 31–43: `if escolha == "1"` / `elif escolha == "2"` / `elif escolha == "3"` / `else` | if/elif/else |
| *"O que acontece se o jogador digitar '5'?"* | Linha 43: `else: print("⚠️ Opção inválida.")` | Tratamento de entrada inválida |
| *"Quantos caminhos de decisão existem em cada sala?"* | 4 caminhos: opções 1, 2, 3 e inválida | Múltiplos ramos |
| *"Se eu quiser adicionar uma opção 4, onde coloco?"* | Antes do `else`, adicionar outro `elif` | Extensibilidade |

### Desafio relâmpago (2 min):
> *"Modifiquem o texto da opção errada da Sala para algo engraçado e rodem."*

---

## Bloco 4: Prática com IA — Decisor de Destino Escolar (45 min)

**Objetivo:** Cada aluno cria um sistema de decisão escolar completo usando `if/elif/else`.

### Instrução para os alunos:
> *"Vocês vão criar um sistema que a secretaria da escola poderia usar para decidir a situação de cada aluno automaticamente."*

### Prompt Modelo (projetar no quadro):
```
Crie um programa em Python para terminal que simule a decisão de aprovação escolar.
O programa deve perguntar:
1. Nome do aluno
2. Nota do 1º bimestre (0 a 100)
3. Nota do 2º bimestre (0 a 100)
4. Número de faltas

Regras de decisão:
- Calcular a média das duas notas.
- Se a média >= 70 E faltas <= 15 → Aprovado ✅
- Se a média >= 40 E faltas <= 15 → Recuperação ⚠️
- Se faltas > 15 → Reprovado por falta ❌ (independente da nota)
- Senão → Reprovado por nota ❌

O código deve usar if, elif e else com operadores and/or.
Adicione comentários em português explicando cada condição.
Use apenas print() e input(). Converta as entradas para int().
```

### Ações do Tutor:
- Circular pelo laboratório verificando se os alunos estão usando o prompt de forma estruturada.
- Identificar alunos que copiaram o código sem ler — pedir que expliquem o que cada `if` faz.
- Se o código der erro, orientar o uso do prompt de depuração.

---

## Bloco 5: Desafio Surpresa — O "Plot Twist" (20 min)

**Objetivo:** Testar se o aluno realmente entendeu a lógica ou se apenas copiou da IA. Este é um **momento-chave para a pesquisa** (Artigo 1: ajuda vs. dependência).

### A Mudança de Regra:
> *"ATENÇÃO! A escola acabou de mudar a regra: quem tirou nota acima de 95 no primeiro bimestre pode ter 5 faltas extras de tolerância antes de reprovar. Alterem o código MANUALMENTE, sem pedir para a IA!"*

### O que se espera:
- **Alunos que entenderam a lógica:** Vão localizar o bloco de faltas e adicionar uma condição (`if nota1 > 95: faltas_max = 20`).
- **Alunos que apenas copiaram da IA:** Não saberão onde mexer e tentarão gerar um prompt novo (o que reforça o ponto pedagógico sobre dependência).

### Ações do Tutor:
- Observar e anotar discretamente quais alunos conseguiram e quais não (dados qualitativos para o Artigo 1).
- Após 10 minutos, resolver juntos no projetor:
  ```python
  # Regra nova: nota1 acima de 95 dá tolerância extra
  if nota1 > 95:
      faltas_max = 20
  else:
      faltas_max = 15
  
  if media >= 70 and faltas <= faltas_max:
      print("✅ Aprovado!")
  ```
- Fechar com a reflexão:
  > *"Quem conseguiu alterar sozinho? Parabéns, vocês já estão pensando como programadores. Quem não conseguiu, é exatamente por isso que a gente não apenas copia da IA — a gente desmonta e entende."*

---

## Bloco 6: Encerramento e Backup (10 min)

**Objetivo:** Salvar o progresso e preparar a próxima aula.

### Ações do Tutor:
- Verificar quais alunos completaram o desafio.
- Orientar o salvamento dos arquivos `.py`.
- Exportar os logs `.jsonl` do dia.
- Pedir compartilhamento dos chats via formulário.
- Frase de fechamento:
  > *"Hoje vocês ensinaram o computador a tomar decisões. Na próxima aula, vamos ensinar ele a REPETIR tarefas sem cansar — imaginem um robô que faz a chamada de 40 alunos em 1 segundo!"*

---

## Resumo da Duração

| Bloco | Atividade | Duração |
|-------|-----------|---------|
| 1 | Aquecimento: Decisões do cotidiano | 10 min |
| 2 | Aula Expositiva: if, elif, else, operadores | 25 min |
| 3 | Engenharia Reversa: EscapeRoom.py | 20 min |
| 4 | Prática com IA: Decisor Escolar | 45 min |
| 5 | Desafio Surpresa: Plot Twist (alteração manual) | 20 min |
| 6 | Encerramento e Backup | 10 min |
| **Total** | | **130 min** |

> **Margem:** 20 minutos para imprevistos técnicos.

---

## Conceitos de Programação Absorvidos

- [x] Estrutura condicional: `if`, `elif`, `else`
- [x] Operadores de comparação: `==`, `!=`, `>`, `<`, `>=`, `<=`
- [x] Operadores lógicos: `and`, `or`, `not`
- [x] Condicionais aninhadas
- [x] Alteração manual de código (independência da IA)

## Recursos Utilizados da Pasta do Projeto

- `Jogos/EscapeRoom.py` — Material de Engenharia Reversa
- Formulário Google de coleta de chats
- Script de captura de logs (.jsonl)

## Vínculo com a Pesquisa

- **Artigo 1 (Crossover):** O "Plot Twist" do Bloco 5 é um momento de medição qualitativa sobre dependência cognitiva da IA.
- **Artigo 2 (Learning Analytics):** Os logs de prompt do Bloco 4 alimentam a taxonomia P1–P5.
