# Roteiro de Aula — Aula 03

## Tomada de Decisão: if, elif, else

**Duração total:** 180 minutos (3h00) — **Horário:** 15h00 às 18h00
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

## Resumo da Duração (15h00 às 18h00)

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | Aquecimento: Decisões do cotidiano | 15 min | 15h00 – 15h15 |
| 2 | Aula Expositiva: if, elif, else, operadores | 30 min | 15h15 – 15h45 |
| 3 | Engenharia Reversa: EscapeRoom.py | 25 min | 15h45 – 16h10 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h10 – 16h25** |
| 4 | Prática com IA: Decisor Escolar | 50 min | 16h25 – 17h15 |
| 5 | Desafio Surpresa: Plot Twist (alteração manual) | 25 min | 17h15 – 17h40 |
| 6 | Lançamento do Mini-Projeto de Intervalo + Encerramento | 20 min | 17h40 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |


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

---

## Material Didático Complementar

### ⚡ Quiz de Aquecimento (Para o início da Aula 04)

#### ❓ Pergunta 1: Verdadeiro ou Falso?
Em Python, o sinal `=` serve para TESTAR se duas coisas são iguais, enquanto o sinal `==` serve para GUARDAR um valor dentro de uma variável.
* [ ] Verdadeiro
* [ ] Falso

#### ❓ Pergunta 2: Múltipla Escolha
Um segurança virtual de evento VIP precisa deixar entrar quem tem pelo menos 18 anos **E** está com o nome na lista VIP. Qual condição representa essa regra corretamente?
* A) `if idade >= 18 and lista_vip == "sim":`
* B) `if idade = 18 or lista_vip = "sim":`
* C) `if idade > 18 or dancou_passinho == True:`
* D) `if idade + lista_vip == 100:`

#### ❓ Pergunta 3: Encontre o Erro! 🔍
Um aluno tentou criar um teste de nota escolar, mas o computador reclamou de erro de sintaxe:
```python
nota = 80
if nota = 70
    print("Aprovado!")
```
**Quais são os DOIS erros na linha do `if`?**

---

#### 🔑 Gabarito Comentado (Para o Tutor)
1. **FALSO!** ❌ É exatamente o contrário! `=` é atribuição (guarda na caixa) e `==` é comparação (verifica se é igual).
2. **Alternativa A!** 🎯 Usa o operador `and` (ambas devem ser verdadeiras) e `>=` para idade maior ou igual a 18. A opção C é absurda.
3. **Erros:** 1) Usou `=` (atribuição) em vez de `==` ou `>=` (comparação). 2) Faltou colocar os dois pontos `:` no final da linha do `if` (`if nota >= 70:`).

---

### 🏠 Micro-Missão do Intervalo de 1 Mês (Para a volta na Aula 04)

#### 🚀 Mini-Projeto de Intervalo: Escolha 1 das 3 Opções de Jogos/Chatbots

Como a turma terá 1 mês de intervalo antes da Aula 04, os alunos deverão escolher **UM** dos 3 projetos autorais abaixo para desenvolver no computador ou no celular (Pydroid 3). No início da Aula 04, faremos uma **Mini-Feira de Projetos (15-20 min)** para apresentação dos resultados!

---

#### 🎮 Opção 1: "Tamagotchi Escolar" (Foco em Máquina de Estados com `while` Infinito)
- **A Ideia:** Um Bichinho Virtual (ou o próprio aluno como personagem) que precisa equilibrar Estudo, Sono e Diversão.
- **Lógica Principal:**
  - Variáveis inteiras iniciais: `energia = 100`, `conhecimento = 0`, `estresse = 0`.
  - Laço `while` que roda enquanto `energia > 0 and estresse < 100 and conhecimento < 100`.
- **Menu Básico:** Exibe opções: `1-Estudar`, `2-Dormir`, `3-Jogar celular`.
  - *Se 1 (Estudar):* `conhecimento += 10`, `energia -= 20`, `estresse += 10`.
  - *Se 2 (Dormir):* `energia += 50`, `estresse -= 10`.
  - *Se 3 (Jogar):* `estresse -= 30`, `energia -= 10`.
  - O laço repete mostrando o status atualizado do personagem.
- **Missão Extra (Para o Mês):** 
  - Vitória se `conhecimento >= 100` -> `print("🎉 Parabéns! Você passou de ano com sucesso!")`.
  - Derrota se `energia <= 0` -> `print("💀 Você desmaiou de cansaço!")`.
  - Derrota se `estresse >= 100` -> `print("🤯 Você surtou de estresse!")`.
  - *Desafio IA:* Usar a IA para ajudar a ajustar os números no código (`+10`, `-20`) para que o jogo fique bem balanceado!

---

#### ⚔️ Opção 2: "A Jornada do Herói" (Mini RPG Textual em Salas Encadeadas)
- **A Ideia:** Um jogo de aventura onde o jogador avança de sala em sala e precisa tomar decisões que gastam sua vida.
- **Lógica Principal:**
  - Variável inicial `vida = 100`. Estrutura linear de salas.
  - Entra na Sala 1, lê um texto, faz uma escolha com `input()`. Se a escolha for ruim, `vida = vida - 40`.
  - Usar `if vida > 0:` para permitir que o jogador avance para as salas seguintes.
- **Missão Extra (Para o Mês):** 
  - Criar o "Chefão Final" na última sala com `vida_chefe = 50`.
  - Usar um laço `while vida_chefe > 0 and vida > 0:` onde o jogador ataca (`vida_chefe -= 15`) e toma dano (`vida -= 10`) a cada rodada de combate até um dos dois zerar a vida!

---

#### 🧩 Opção 3: "O Teste de Personalidade Buzzfeed" (Foco em Condicionais `if/elif/else`)
- **A Ideia:** Um quiz interativo com 3 a 5 perguntas (*"Qual herói da Marvel você é?"* ou *"Qual profissão combina com você?"*).
- **Lógica Principal:**
  - Variáveis separadas de pontuação para cada perfil (ex: `pontos_aranha = 0`, `pontos_thor = 0`).
  - Perguntas com `print()` e capturas de opção com `input()` (`A`, `B` ou `C`).
  - Estruturas `if` somam pontos na variável correspondente.
- **Missão Extra (Para o Mês):**
  - Criar um grande bloco `if/elif/else` no final para analisar e declarar automaticamente o perfil campeão.
  - Tratar erros de digitação: se o usuário digitar uma opção inválida (ex: `"X"`), usar um `else:` avisando *"Resposta inválida! Você perdeu os pontos desta rodada"*.



