# 🛠️ Roteiro de Aula — Aula 05 (Trilha Mobile)
## Modularização e Funções: `def`, Parâmetros e `return` no Celular

**Data:** 11 de novembro de 2026 (quarta-feira) — **Horário:** 15h00 às 18h00  
**Duração total:** 180 minutos (3h00)  
**Público-alvo:** Estudantes do Ensino Médio  
**Ferramenta de execução:** Pydroid 3 (smartphone) / VS Code + IA (Gemini/ChatGPT)  
**Pré-requisitos da aula anterior:** Variáveis, `if/else`, `while`, `for`, `try/except`, Listas (Aulas 1 a 4)

> **🔑 Legenda do Roteiro:**
> - `[SLIDE]` → Projetar no telão (conceito visual/teórico)
> - `[IDE]` → Abrir o VS Code ou Pydroid 3 e digitar ao vivo (alunos copiam junto)
> - `[❓ ENGAJAMENTO]` → Jogar a pergunta para a turma, aguardar respostas
> - `[⏱️]` → Marcação de tempo estimado para o bloco

---

## 📅 Grade de Horários

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | **⚡ Quiz da Aula Anterior** — Revisão sobre Listas (`list`, `append`, `len`) | 15 min | 15h00 – 15h15 |
| 2 | **⌨️ Digitando Enquanto Acompanha na Lousa**: Criando Funções (`def`), Parâmetros e `return` + **Mini Exercícios** | 35 min | 15h15 – 15h50 |
| 3 | **🔍 Analisar um Código Pronto** (Engenharia Reversa Guiada: Sistema Modular com Funções) | 25 min | 15h50 – 16h15 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h15 – 16h30** |
| 4 | **🤖 3 Exercícios Práticos Solo / Engenharia Reversa com IA** (Desafio do Dia - Missões A, B e C) | 50 min | 16h30 – 17h20 |
| 5 | **🔨 Quebrando o Código para Investigar Erros** (Teste de Estresse: Escopo & `NameError`) | 25 min | 17h20 – 17h45 |
| 6 | **🎯 Resumão e Conclusão das Sintaxes Aprendidas no Dia** + Micro-Tarefa | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |

---

## 🟢 Bloco 1: Quiz da Aula Anterior e Abertura (15 min)

> **Objetivo:** Recapitular a manipulação de coleções com listas da Aula 04 e introduzir o conceito de modularização por meio de funções reutilizáveis.

### ⏱️ [0–3 min] Boas-vindas

Projete no telão:
```
"Hoje vocês vão aprender a criar suas próprias FERRAMENTAS no Python usando FUNÇÕES (def)!"
```

Diga:
> *"Sejam bem-vindos à Aula 05! Até agora escrevemos códigos em bloco único. Mas imagine se em uma fábrica o funcionário tivesse que reinventar o robô toda vez que fosse apertar um parafuso. Não faz sentido! Em programação, quando temos uma tarefa repetitiva, criamos uma FUNÇÃO (`def`). Ela é uma receita salva na memória que podemos chamar quantas vezes quisermos!"*

---

### ⏱️ [3–15 min] ⚡ Quiz da Aula 04 (Revisão sobre Listas)

`[SLIDE]` — Projete as perguntas no telão:

#### ❓ Pergunta 1: Qual comando adiciona um novo item no FINAL de uma lista em Python?
- A) `lista.add("novo")`
- B) `lista.append("novo")`
- C) `lista.push("novo")`
- D) `lista.insert_end("novo")`

**🔑 Gabarito:** **Alternativa B!** 🎯 O método `.append()` adiciona o elemento ao final da lista.

---

#### ❓ Pergunta 2: O que acontece ao tentar executar o código abaixo?
```python
jogadores = ["Ana", "Bruno"]
print(jogadores[2])
```
- A) Imprime `"Bruno"`
- B) Imprime `None`
- C) Dispara um erro `IndexError: list index out of range`
- D) Cria um novo jogador vazio

**🔑 Gabarito:** **Alternativa C!** ❌ A lista só tem índices `0` ("Ana") e `1` ("Bruno"). O índice `2` não existe!

---

#### ❓ Pergunta 3: Qual a utilidade da função `len(minha_lista)`?
**🔑 Gabarito:** Retorna o número total de elementos (tamanho) contidos dentro da lista.

`[❓ ENGAJAMENTO]`
> **"E se a gente quisesse uma função que calcula a média de notas de um aluno toda vez que for chamada? Vamos aprender a criar isso agora!"**

---

## 🔵 Bloco 2: Digitando Enquanto Acompanha na Lousa + Mini Exercícios (35 min)

> **Objetivo:** Ensinar a definição de funções com `def`, a passagem de parâmetros e a instrução vital `return` (diferenciando-a de um simples `print`).

### ⏱️ [0–12 min] Teoria na Lousa + Live Coding 1: Criando Funções e Parâmetros

`[SLIDE]` — Analogia no telão:
```
A RECEITA DE BOLO:
def fazer_bolo(sabor):     → Definição da receita (passa o parâmetro 'sabor')
    print(f"🎂 Assando bolo de {sabor}...")

fazer_bolo("Chocolate")    → Chamada 1
fazer_bolo("Cenoura")      → Chamada 2
```

`[IDE]` — Crie o arquivo `aula05_funcoes.py` no Pydroid 3 / VS Code. **Alunos digitam juntos**:

```python
# 1. Definindo uma função simples sem retorno
def dar_boas_vindas(nome_usuario):
    print(f"✨ Olá, {nome_usuario}! Bem-vindo ao app Trilha Mobile!")

# Chamando a função para 2 usuários diferentes
dar_boas_vindas("Carlos")
dar_boas_vindas("Mariana")

# 2. Função com múltiplos parâmetros
def exibir_perfil(nome, idade, cidade):
    print(f"\n👤 Perfil: {nome} | 🎂 {idade} anos | 📍 {cidade}")

exibir_perfil("Beatriz", 17, "Belo Horizonte")
```

**Roteiro de fala enquanto digita:**
- *"O `def` vem de 'define'. Estamos avisando o Python: 'aprenda a fazer essa instrução e guarde esse nome'."*
- *"O que fica dentro dos parênteses `(nome_usuario)` é o PARÂMETRO — a informação que a função precisa receber para trabalhar."*

---

### ⏱️ [12–25 min] Teoria na Lousa + Live Coding 2: O Poder do `return`

`[SLIDE]` — Projete no telão:
```
print()  →  APENAS MOSTRA na tela (o valor "some" no ar)
return   →  DEVOLVE o resultado para ser guardado em uma variável ou usado em contas
```

`[IDE]` — Acrescente ao mesmo código. **Alunos digitam juntos**:

```python
# 3. Função que CALCULA e RETORNA um valor com return
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media  # Devolve o valor calculado!

# Guardando o retorno da função em uma variável externa
media_final = calcular_media(8.5, 9.5)
print(f"\n📊 A média final do aluno é: {media_final}")

# Usando o retorno diretamente em um if/else
if media_final >= 7.0:
    print("🎉 Aluno APROVADO!")
else:
    print("📋 Aluno em RECUPERAÇÃO.")
```

`[❓ ENGAJAMENTO]`
> **"Se eu esquecer a palavra `return` dentro da função, o que a variável `media_final` vai guardar?"**  
> *(Resposta: Vai guardar `None`! Sem o return, a função não devolve nada!)*

---

### ⏱️ [25–35 min] 🧩 Mini Exercícios Práticos Pós-Teoria (Alunos fazem agora na IDE)

Projete os 3 desafios rápidos na lousa (5 min para tentar, 5 min para correção ao vivo):

1. **Mini Desafio 1:** Crie uma função chamada `dobro(numero)` que retorna o número multiplicado por 2 com `return`.
2. **Mini Desafio 2:** Chame a função `dobro(15)` e imprima o resultado na tela.
3. **Mini Desafio 3:** Crie uma função `verificar_par(num)` que retorna `True` se o número for par (`num % 2 == 0`) e `False` caso contrário.

`[IDE]` — **Gabarito rápido projetado pelo tutor:**
```python
# 1 e 2
def dobro(numero):
    return numero * 2

res = dobro(15)
print(f"O dobro de 15 é: {res}")

# 3
def verificar_par(num):
    return num % 2 == 0

print(verificar_par(4))  # True
```

---

## 🟡 Bloco 3: Analisar um Código Pronto — Engenharia Reversa (25 min)

> **Objetivo:** Inspecionar a arquitetura de uma Multi-Calculadora modularizada composta por várias funções `def` integradas a um menu `while`.

`[SLIDE]` — Projete a missão no telão:
```
🔍 MISSÃO DETETIVE: Analise a Multi-Calculadora.
Identifique onde cada função é definida e em qual linha do menu ela é chamada!
```

`[IDE]` — Projete o código `multi_calc.py`:

```python
# === MULTI-CALCULADORA MODULAR ===

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def converter_celsius_fahrenheit(celsius):
    f = (celsius * 1.8) + 32
    return f

def calcular_desconto(preco, percentual):
    valor_desconto = preco * (percentual / 100)
    preco_final = preco - valor_desconto
    return preco_final

# --- MENU PRINCIPAL DO APLICATIVO ---
while True:
    print("\n🧮 --- MENU DE FERRAMENTAS ---")
    print("1- Indice de Massa Corporal (IMC)")
    print("2- Conversor de Temperatura (ºC ➡️ ºF)")
    print("3- Calculadora de Desconto")
    print("4- Sair")
    
    opcao = input("Escolha a ferramenta desejada: ")
    
    if opcao == "1":
        p = float(input("Seu peso (kg): "))
        a = float(input("Sua altura (m): "))
        resultado = calcular_imc(p, a)
        print(f"⚖️ Seu IMC é: {resultado:.2f}")
        
    elif opcao == "2":
        temp = float(input("Temperatura em ºC: "))
        res_f = converter_celsius_fahrenheit(temp)
        print(f"🌡️ {temp}ºC equivale a {res_f:.1f}ºF")
        
    elif opcao == "3":
        val = float(input("Preço original: R$ "))
        desc = float(input("Porcentagem de desconto (%): "))
        final = calcular_desconto(val, desc)
        print(f"🏷️ Preço com desconto: R$ {final:.2f}")
        
    elif opcao == "4":
        print("👋 Encerrando ferramentas. Até logo!")
        break
    else:
        print("⚠️ Opção inválida!")
```

### ❓ Perguntas Pedagógicas de Engenharia Reversa:
1. `[❓ ENGAJAMENTO]` → **"Quantas funções personalizadas foram criadas antes do laço `while`?"** *(3 funções: imc, temperatura e desconto)*
2. `[❓ ENGAJAMENTO]` → **"Qual instrução garante que a temperatura convertida saia da função `converter_celsius_fahrenheit` para ser exibida no print?"** *(A instrução `return f`)*
3. `[❓ ENGAJAMENTO]` → **"O que aconteceria com a legibilidade do código se colocássemos todas as contas dentro do `if/elif` sem usar `def`?"** *(O código ficaria gigante, bagunçado e impossível de reutilizar em outros lugares!)*

---

## ☕ Intervalo — 15 minutos (16h15 – 16h30)

Projete no telão:
```
☕ PAUSA PARA O LANCHE (15 min)
Ao voltar: Crie seu próprio App Modularizado com funções usando IA!
Deixe o Pydroid 3 / VS Code aberto. 📱
```

---

## 🟠 Bloco 4: 3 Exercícios Práticos Solo / Engenharia Reversa com IA (50 min)

> **Objetivo:** Construção autônoma de módulos de código com funções reutilizáveis, parâmetros e `return` utilizando a IA.

`[SLIDE]` — Projete as 3 Missões no telão:

---

### 🍔 MISSÃO A — "O Kiosk de Fast Food Modular" *(Foco em Restauração)*

**Prompt para copiar na IA (Gemini/ChatGPT):**
```
Atue como desenvolvedor Python mobile.
Crie um aplicativo de totem de pedidos de lanche no Pydroid 3 / VS Code.
Regras:
1. Crie uma função montar_pedido(lanche, bebida, sobremesa) que recebe os 3 itens e retorna uma frase formatada de confirmação.
2. Crie uma função calcular_total(preco_lanche, preco_bebida) que retorna a soma com 10% de taxa de serviço.
3. Peça os dados ao usuário com input(), chame as 2 funções e exiba o resumo na tela.
4. Máximo 25 linhas, comentários explicativos em português.
```

**Desafio Extra:** Adicione uma verificação com `if` para conceder frete grátis se o total for maior que R$ 50,00.

---

### 🎮 MISSÃO B — "O Gerador de Status de RPG" *(Foco em Jogos)*

**Prompt para copiar na IA (Gemini/ChatGPT):**
```
Atue como game designer Python.
Crie um sistema modular de criação de personagens para terminal:
1. Crie a função rolar_atributos() que gera 3 números aleatórios entre 10 e 20 para Força, Agilidade e Magia.
2. Crie a função calcular_poder_total(forca, agilidade, magia) que retorna a média dos atributos.
3. Crie a função classificar_classe(poder) que retorna "Guerreiro" (se poder>15) ou "Aprendiz".
4. Imprima a ficha completa do herói chamando todas as funções.
5. Máximo 30 linhas, sem bibliotecas externas complexas (use import random).
```

**Desafio Extra:** Peça à IA para formatar a saída com caixas de texto com emojis.

---

### 💳 MISSÃO C — "O Validador Financeiro de Pix" *(Foco em Fintech)*

**Prompt para copiar na IA (Gemini/ChatGPT):**
```
Atue como desenvolvedor backend de fintech.
Crie um validador de transferências bancárias em Python:
1. Crie uma função validar_chave_pix(chave) que retorna True se a chave tiver mais de 5 caracteres.
2. Crie uma função aplicar_cupom(valor, cupom) que retorna o valor com R$ 10 de desconto se o cupom for "PRIMEIROPIX".
3. Crie um laço while que pede a chave e o valor, chama as funções de validação e confirma o envio.
4. Máximo 30 linhas, comentários didáticos.
```

**Desafio Extra:** Tratar erro de entrada no valor da transferência usando `try/except`.

---

### 🎯 Atuação do Monitor/Tutor durante a Prática:
Circular pela sala e incentivar o raciocínio:
- `[❓ ENGAJAMENTO]` → *"Onde no seu código a função devolve o valor de volta para a variável principal?"*
- `[❓ ENGAJAMENTO]` → *"O que acontece se você mudar os valores dos parâmetros na hora de chamar a função?"*

---

## 🟣 Bloco 5: Quebrando o Código para Investigar Erros (25 min)

> **Objetivo:** Investigar erros comuns relacionados a escopo de variáveis (escopo local vs global) e problemas na chamada de funções.

`[SLIDE]` — Projete a tabela de Testes de Estresse:

```
🔨 OPERAÇÃO DESTRUIÇÃO: Investigando falhas em Funções!
Variáveis criadas dentro de uma função nascem e morrem dentro dela.
```

| Teste | O que fazer no código | Qual erro o Python dispara? | Causa Raiz |
|-------|-----------------------|-----------------------------|------------|
| 1. Escopo Local | Tentar acessar `print(media)` fora da função onde ela foi criada | `NameError: name 'media' is not defined` | A variável `media` só existe dentro do bloco `def` |
| 2. Falta de Argumento | Chamar `calcular_imc(70)` passando 1 parâmetro em vez de 2 | `TypeError: missing 1 required positional argument` | A função exige exatamente o número de argumentos especificados |
| 3. Esquecer o `return` | Fazer a conta sem `return` e tentar somar o resultado | `TypeError: unsupported operand type(s) for +: 'NoneType'` | Sem `return`, a função retorna `None` |

### 🧪 Exercício de Debugging com IA:

Projete o código com bug de escopo abaixo e solicite que os alunos usem a IA para entender o motivo do erro:

```python
# CÓDIGO COM BUG DE ESCOPO PROPOSITÁAL
def somar(a, b):
    resultado_soma = a + b

somar(5, 10)
print(resultado_soma)  # 🚨 ERRO!
```

**Prompt de investigação para a IA:**
```
Meu código Python no Pydroid 3 deu este erro:
NameError: name 'resultado_soma' is not defined

Explique o conceito de ESCOPO LOCAL de variáveis em funções
e como corrijo o código usando a instrução 'return'.
```

---

## 🔴 Bloco 6: Resumão e Conclusão das Sintaxes Aprendidas (15 min)

### ⏱️ [0–8 min] Resumão das Sintaxes

`[SLIDE]` — Projete no telão:

```
🎯 SINTAXES DOMINADAS NA AULA 05:

✅ def minha_funcao(): → Define um bloco de código reutilizável
✅ def acao(parametro):→ Função que recebe informações de fora
✅ return valor        → Devolve o resultado processado para quem chamou
✅ Escopo Local        → Variáveis criadas dentro do def pertencem só a ele
✅ None                → Valor retornado por padrão quando uma função não usa return
✅ NameError           → Erro gerado ao tentar usar uma variável de escopo inacessível
```

---

### ⏱️ [8–15 min] Encerramento e Micro-Tarefa de Casa

Diga:
> *"Hoje demos um passo gigante rumo ao desenvolvimento de software profissional! Seu código agora é organizado em módulos reutilizáveis. Na próxima aula aprenderemos Dicionários e juntaremos TODOS esses 5 pilares antes de criarmos apps com tela visual!"*

---

## ✅ Conceitos de Programação Absorvidos

- [x] Declaração e invocação de funções com `def`
- [x] Passagem de parâmetros e argumentos
- [x] Retorno explícito de valores com a palavra-chave `return`
- [x] Diferenciação crucial entre `print()` (exibição) e `return` (processamento)
- [x] Compreensão de Escopo Local vs Escopo Global
- [x] Resolução de erros de argumento (`TypeError`) e de escopo (`NameError`)

---

## 🔑 Gabarito de Respostas — Para o Tutor

| Pergunta de Engajamento | Resposta Esperada |
|------------------------|-------------------|
| Qual a diferença de `print()` e `return` dentro de uma função? | `print()` apenas exibe texto no console; `return` envia o dado de volta para ser usado em variáveis ou lógica posterior |
| O que acontece se eu tentar usar uma variável criada dentro de um `def` do lado de fora? | Dispara `NameError`, pois ela é uma variável local do escopo daquela função |
| Quantos valores uma função pode retornar? | Pode retornar um valor simples, múltiplos valores (tupla) ou coleções como listas e dicionários |
| O que é um parâmetro de função? | É uma variável reservada na definição do `def` para receber o valor que será enviado na chamada |

---

## 🏠 Micro-Missão de Casa (Entregar na Aula 06)

> **Escolha UMA das duas opções abaixo para realizar no Pydroid 3 do celular (10 a 15 min):**

### 🍔 Opção A — "A Receita do Lanche Modular"
Escreva no Pydroid 3 a função `montar_hamburguer(pao, carne, molho)` que usa `return` para entregar a frase formatada do pedido. Teste chamando com seus ingredientes favoritos!

### 🏷️ Opção B — "Calculadora de Desconto de Loja"
Crie no Pydroid 3 uma função `calcular_desconto(preco)` que aplica 10% de desconto e retorna o valor final com `return preco * 0.90`. Teste exibindo o resultado formatado!
