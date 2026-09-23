# 🗂️ Roteiro de Aula — Aula 06 (Trilha Mobile)
## Consolidação da Lógica + Estruturas Avançadas (Dicionários no Celular)

**Data:** 18 de novembro de 2026 (quarta-feira) — **Horário:** 15h00 às 18h00  
**Duração total:** 180 minutos (3h00)  
**Público-alvo:** Estudantes do Ensino Médio  
**Ferramenta de execução:** Pydroid 3 (smartphone) / VS Code + IA (Gemini/ChatGPT)  
**Pré-requisitos da aula anterior:** Fundamentos das Aulas 1 a 5 (`input`, `if/else`, `while/for`, listas, `def`)

> **🔑 Legenda do Roteiro:**
> - `[SLIDE]` → Projetar no telão (conceito visual/teórico)
> - `[IDE]` → Abrir o VS Code ou Pydroid 3 e digitar ao vivo (alunos copiam junto)
> - `[❓ ENGAJAMENTO]` → Jogar a pergunta para a turma, aguardar respostas
> - `[⏱️]` → Marcação de tempo estimado para o bloco

---

## 📅 Grade de Horários

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | **⚡ Quiz da Aula Anterior** — Revisão sobre Funções (`def`, parâmetros e `return`) | 15 min | 15h00 – 15h15 |
| 2 | **⌨️ Digitando Enquanto Acompanha na Lousa**: Dicionários (`dict`), Chave-Valor e Listas de Dicionários + **Mini Exercícios** | 35 min | 15h15 – 15h50 |
| 3 | **🔍 Analisar um Código Pronto** (Engenharia Reversa Guiada: Banco de Dados de Alunos/Produtos) | 25 min | 15h50 – 16h15 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h15 – 16h30** |
| 4 | **🤖 3 Exercícios Práticos Solo / Engenharia Reversa com IA** (Desafio do Dia - Missões A, B e C) | 50 min | 16h30 – 17h20 |
| 5 | **🔨 Quebrando o Código para Investigar Erros** (Teste de Estresse: `KeyError` & Aspas em `f-strings`) | 25 min | 17h20 – 17h45 |
| 6 | **🎯 Resumão e Conclusão das Sintaxes Aprendidas no Dia** + Celebração do Domínio da Lógica | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |

---

## 🟢 Bloco 1: Quiz da Aula Anterior e Abertura (15 min)

> **Objetivo:** Consolidar o entendimento sobre funções (`def`) da Aula 05 e introduzir os Dicionários (`dict`) como a forma mais profissional de representar dados do mundo real.

### ⏱️ [0–3 min] Boas-vindas

Projete no telão:
```
"Hoje encerramos a grande jornada da LÓGICA DE PROGRAMAÇÃO PURA! Vamos aprender DICIONÁRIOS para representar dados reais!"
```

Diga:
> *"Sejam bem-vindos à Aula 06! Hoje é um dia histórico na nossa trilha. Vocês já sabem fazer o computador falar, escutar, tomar decisões, repetir e rodar funções. Hoje vamos aprender os DICIONÁRIOS — a estrutura que empresas como Instagram, iFood e Spotify usam para representar usuários, posts e produtos!"*

---

### ⏱️ [3–15 min] ⚡ Quiz da Aula 05 (Revisão sobre Funções)

`[SLIDE]` — Projete as perguntas no telão:

#### ❓ Pergunta 1: Qual a diferença fundamental entre a instrução `print()` e a instrução `return` dentro de uma função?
- A) Nenhuma, as duas fazem exatamente a mesma coisa
- B) O `print()` mostra o dado na tela; o `return` devolve o valor para ser guardado em uma variável ou usado em lógicas
- C) O `return` apaga a função da memória
- D) O `print()` só funciona com números

**🔑 Gabarito:** **Alternativa B!** 🎯 `print()` exibe visualmente; `return` devolve para o programa continuar usando.

---

#### ❓ Pergunta 2: Se tentarmos acessar fora da função uma variável que foi criada dentro do `def`, o que acontece?
```python
def teste():
    segredo = "123"

print(segredo)
```
- A) Imprime `"123"`
- B) Imprime `None`
- C) Ocorre um erro `NameError` devido ao escopo local
- D) O Python cria uma nova variável vazia

**🔑 Gabarito:** **Alternativa C!** ❌ Variáveis criadas dentro do `def` pertencem exclusivamente ao escopo local daquela função.

---

#### ❓ Pergunta 3: Múltipla Escolha
Como chamamos as informações passadas entre parênteses na criação de uma função?
- A) Loops
- B) Parâmetros ou Argumentos
- C) Tratadores de exceção
- D) Condicionais

**🔑 Gabarito:** **Alternativa B!**

---

## 🔵 Bloco 2: Digitando Enquanto Acompanha na Lousa + Mini Exercícios (35 min)

> **Objetivo:** Ensinar a estrutura de Dicionários (`dict`) com chaves e valores `{"chave": "valor"}`, acesso por chaves, modificação e agrupamento em listas de dicionários.

### ⏱️ [0–12 min] Teoria na Lousa + Live Coding 1: Criando e Acessando Dicionários

`[SLIDE]` — Projete a comparação na lousa:
```
Lista (`list`)   → Posições numéricas [0, 1, 2]:    aluno = ["Ana", 16, 9.5]
Dicionário (`dict`) → Rótulos com nomes {"chave": "valor"}:
                       aluno = {"nome": "Ana", "idade": 16, "nota": 9.5}
```

`[IDE]` — Crie o arquivo `aula06_dicionarios.py` no Pydroid 3 / VS Code. **Alunos digitam juntos**:

```python
# 1. Criando um dicionário de perfil de usuário
usuario = {
    "nickname": "DevMaster99",
    "nivel": 15,
    "vip": True,
    "itens_mochila": ["Espada", "Escudo"]
}

# 2. Acessando valores através das CHAVES
print(f"Nome do jogador: {usuario['nickname']}")
print(f"Nível atual: {usuario['nivel']}")

# 3. Alterando e adicionando novas chaves
usuario["nivel"] = 16  # Atualiza o nível
usuario["pontuacao"] = 2500  # Adiciona uma nova chave que não existia!

print(f"Perfil atualizado: {usuario}")
```

**Roteiro de fala enquanto digita:**
- *"Reparem nas chaves `{}` — é assim que definimos um dicionário."*
- *"Cada linha dentro dele é formada por um par `chave: valor`. A chave é a etiqueta (ex: `"nickname"`), e o valor é o conteúdo (ex: `"DevMaster99"`)."*

---

### ⏱️ [12–25 min] Teoria na Lousa + Live Coding 2: Lista de Dicionários

`[IDE]` — Acrescente ao mesmo código. **Alunos digitam juntos**:

```python
# 4. Lista de Dicionários — O padrão do mercado para Banco de Dados!
turma_mobile = [
    {"nome": "Ana Silva", "curso": "Mobile", "nota": 9.5},
    {"nome": "Bruno Souza", "curso": "Mobile", "nota": 8.0},
    {"nome": "Carla Lima", "curso": "Mobile", "nota": 10.0}
]

# 5. Percorrendo a lista e exibindo os dados de cada aluno
print("\n📋 BOLETIM DA TURMA:")
for aluno in turma_mobile:
    print(f"Student: {aluno['nome']} | Nota Final: {aluno['nota']}")
```

`[❓ ENGAJAMENTO]`
> **"Como faço para imprimir o nome da Carla que está no índice [2] da lista `turma_mobile`?"**  
> *(Resposta: `turma_mobile[2]['nome']` — primeiro acessamos o índice da lista, depois a chave do dicionário!)*

---

### ⏱️ [25–35 min] 🧩 Mini Exercícios Práticos Pós-Teoria (Alunos fazem agora na IDE)

Projete os 3 desafios rápidos na lousa (5 min para tentar, 5 min para correção ao vivo):

1. **Mini Desafio 1:** Crie um dicionário `produto` com `"nome"` (ex: `"Celular"`) e `"preco"` (ex: `1500.00`).
2. **Mini Desafio 2:** Imprima o preço do produto usando a chave `produto["preco"]`.
3. **Mini Desafio 3:** Use a função `.get("desconto", 0)` para buscar a chave `"desconto"` sem dar erro se ela não existir.

`[IDE]` — **Gabarito rápido projetado pelo tutor:**
```python
# 1 e 2
produto = {"nome": "Celular", "preco": 1500.00}
print(f"Produto: {produto['nome']} - R$ {produto['preco']}")

# 3
desc = produto.get("desconto", 0)
print(f"Desconto: R$ {desc}")
```

---

## 🟡 Bloco 3: Analisar um Código Pronto — Engenharia Reversa (25 min)

> **Objetivo:** Inspecionar e compreender um Sistema Integrado de Gestão que une os 5 pilares da lógica: `input/print`, `variables`, `if/else`, `while/for`, `def` e `dict`.

`[SLIDE]` — Projete a missão no telão:
```
🔍 MISSÃO DETETIVE: Analise o Sistema de Cadastro de Produtos.
Identifique como a lista de dicionários armazena cada item cadastrado!
```

`[IDE]` — Projete o código `gestao_produtos.py`:

```python
# === SISTEMA DE GESTÃO DE ESTOQUE ===
estoque = []  # Lista que guardará os dicionários de produtos

def cadastrar_produto(nome, qtd, preco):
    novo_prod = {
        "nome": nome,
        "quantidade": qtd,
        "preco": preco
    }
    estoque.append(novo_prod)
    print(f"✅ Produto '{nome}' cadastrado com sucesso!")

def listar_estoque():
    print("\n📦 --- RELATÓRIO DE ESTOQUE ---")
    if len(estoque) == 0:
        print("⚠️ Nenhum produto cadastrado no momento.")
        return
    for item in estoque:
        total_item = item["quantidade"] * item["preco"]
        print(f"• {item['nome']} | Qtd: {item['quantidade']} | Valor Total: R$ {total_item:.2f}")

# --- MENU DE EXECUÇÃO ---
while True:
    print("\n🏪 --- MENU LOJA MOBILE ---")
    print("1- Cadastrar Produto | 2- Listar Estoque | 3- Sair")
    op = input("Escolha uma opção: ")
    
    if op == "1":
        try:
            n = input("Nome do produto: ")
            q = int(input("Quantidade: "))
            p = float(input("Preço unitário R$: "))
            cadastrar_produto(n, q, p)
        except ValueError:
            print("🚨 Erro: Digite valores numéricos válidos para quantidade e preço!")
    elif op == "2":
        listar_estoque()
    elif op == "3":
        print("👋 Fechando o sistema de gestão...")
        break
    else:
        print("⚠️ Opção inválida!")
```

### ❓ Perguntas Pedagógicas de Engenharia Reversa:
1. `[❓ ENGAJAMENTO]` → **"Qual estrutura de dados foi usada para representar a loja inteira e qual foi usada para representar CADA produto individual?"** *(A lista `estoque` representa o todo; cada dicionário `novo_prod` representa um produto)*
2. `[❓ ENGAJAMENTO]` → **"Onde está a blindagem que impede o programa de fechar se o usuário digitar 'cinco' na quantidade?"** *(No bloco `try/except ValueError` na opção 1)*
3. `[❓ ENGAJAMENTO]` → **"Como a função `listar_estoque()` calcula o valor total investido em cada produto?"** *(Multiplicando `item["quantidade"] * item["preco"]` em cada iteração do laço `for`)*

---

## ☕ Intervalo — 15 minutos (16h15 – 16h30)

Projete no telão:
```
☕ PAUSA PARA O LANCHE (15 min)
Ao voltar: Construa um Sistema Completo no celular com a IA!
Deixe o Pydroid 3 / VS Code aberto. 📱
```

---

## 🟠 Bloco 4: 3 Exercícios Práticos Solo / Engenharia Reversa com IA (50 min)

> **Objetivo:** Construção autônoma de sistemas completos utilizando dicionários e todos os pilares da lógica aprendidos.

`[SLIDE]` — Projete as 3 Missões no telão:

---

### 🛡️ MISSÃO A — "Ficha Completa de RPG" *(Foco em Dicionários e Jogos)*

**Prompt para copiar na IA (Gemini/ChatGPT):**
```
Atue como desenvolvedor Python de RPG.
Crie um gerador de ficha de personagem no Pydroid 3 / VS Code:
1. Crie um dicionario chamado heroi com as chaves: "nome", "classe", "vida", "mana", "ataque".
2. Peça o nome e a classe ao usuário com input().
3. Se a classe for "Guerreiro", defina vida=120 e ataque=25. Se for "Mago", defina vida=80 e ataque=40 (use if/elif/else).
4. Exiba a ficha formatada acessando cada chave do dicionário.
5. Máximo 25 linhas, comentários em português.
```

**Desafio Extra:** Adicionar uma chave `"mochila"` que guarda uma lista de 3 itens dentro do dicionário.

---

### 📱 MISSÃO B — "O Cadastro de Contatos da Agenda" *(Foco em Aplicativos)*

**Prompt para copiar na IA (Gemini/ChatGPT):**
```
Atue como desenvolvedor de aplicativos mobile.
Crie um gerenciador de Contatos telefônicos em Python:
1. Crie uma lista agenda = [].
2. Use um laço while True com menu: 1-Novo Contato | 2-Ver Contatos | 3-Sair.
3. Cada contato deve ser um dicionário com "nome" e "telefone".
4. Na opção 1, crie o dicionário e adicione à lista com append().
5. Na opção 2, use um laço for para exibir os nomes e números formatados.
6. Máximo 30 linhas, sem bibliotecas externas.
```

**Desafio Extra:** Permitir que o usuário pesquise um contato pelo nome.

---

### 🚗 MISSÃO C — "O Estacionamento Inteligente" *(Foco em Gestão)*

**Prompt para copiar na IA (Gemini/ChatGPT):**
```
Atue como desenvolvedor de sistemas urbanos.
Crie um controle de estacionamento no terminal:
1. Crie um dicionário vagas = {} onde a chave é o número da vaga (ex: "Vaga 1") e o valor é a placa do carro.
2. Crie uma função estacionar_carro(vaga, placa) que guarda no dicionário.
3. Crie uma função liberar_vaga(vaga) que remove do dicionário usando del ou .pop().
4. Monte um menu interativo para o operador testar as funções.
5. Máximo 30 linhas, com comentários explicativos.
```

**Desafio Extra:** Tratar a tentativa de estacionar em uma vaga que já está ocupada.

---

### 🎯 Atuação do Monitor/Tutor durante a Prática:
Circular pela sala e encorajar a consolidação:
- `[❓ ENGAJAMENTO]` → *"Me mostra onde você usou a chave do dicionário para resgatar o valor."*
- `[❓ ENGAJAMENTO]` → *"Qual a vantagem de usar dicionário em vez de uma lista normal para guardar a ficha do personagem?"*

---

## 🟣 Bloco 5: Quebrando o Código para Investigar Erros (25 min)

> **Objetivo:** Inspecionar e resolver erros típicos de manipulação de dicionários (`KeyError` e formatação em `f-strings`).

`[SLIDE]` — Projete a tabela de Testes de Estresse:

```
🔨 OPERAÇÃO DESTRUIÇÃO: Cuidado com a KeyError!
O Python não aceita consultar uma chave que não foi criada no dicionário.
```

| Teste | O que fazer no código | Qual erro o Python dispara? | Solução Definitiva |
|-------|-----------------------|-----------------------------|--------------------|
| 1. Chave Inexistente | Tentar imprimir `usuario["email"]` sem ter criado essa chave | `KeyError: 'email'` | Usar o método `.get("email", "Não informado")` |
| 2. Aspas duplas dentro de `f-string` | Escrever `f"Nome: {aluno["nome"]}"` com aspas iguais | `SyntaxError: f-string: unmatched '"'` | Usar aspas simples na chave: `f"Nome: {aluno['nome']}"` |
| 3. Digitar chave errada | Confundir maiúscula/minúscula `usuario["Nome"]` vs `"nome"` | `KeyError` | Python é case-sensitive! As chaves devem bater 100% |

### 🧪 Exercício de Debugging com IA:

Projete o código quebrado de `KeyError` e peça aos alunos para usarem a IA para consertar com o método `.get()`:

```python
# CÓDIGO COM BUG DE KEYERROR
perfil = {"nome": "Lucas", "idade": 16}
print(f"Email do usuário: {perfil['email']}")  # 🚨 ERRO!
```

**Prompt de investigação para a IA:**
```
Meu código Python deu este erro no Pydroid 3:
KeyError: 'email'

Explique por que esse erro aconteceu e como posso usar
o método .get() para evitar que o programa trave quando a chave não existir.
```

---

## 🔴 Bloco 6: Resumão, Conclusão e Marco Pedagógico (15 min)

### ⏱️ [0–8 min] Resumão das Sintaxes

`[SLIDE]` — Projete o mapa final dos 5 Pilares da Lógica Python:

```
🏆 OS 5 PILARES DA LÓGICA DE PROGRAMAÇÃO DOMINADOS:

1. Entrada / Saída   → print() e input() (conversão str, int, float)
2. Decisão           → if / elif / else (operadores >, <, ==, !=, and, or)
3. Repetição & Erros → while, for, break e try/except (prevenção de bugs)
4. Coleções          → Listas [] e Dicionários {} (armazenamento de dados reais)
5. Modularização     → Funções def com parâmetros e return
```

---

### ⏱️ [8–15 min] 🎉 Transição para a Segunda Fase do Curso (Flet / Telas Visuais)

Diga:
> *"PARABÉNS A TODOS! Vocês completaram a primeira metade do curso. Hoje vocês dominam a lógica que qualquer programador profissional de backend utiliza no mundo real. A partir da Aula 07, vamos pegar toda essa lógica e construir APLICATIVOS VISUAIS de verdade no celular usando o framework FLET! Nos vemos na Aula 07 com telas, botões e cores!"*

---

## ✅ Conceitos de Programação Absorvidos

- [x] Estrutura de dados chave-valor (`dict`)
- [x] Acesso, inserção e alteração de chaves em dicionários
- [x] Consulta segura de chaves com a função `.get()`
- [x] Construção de coleções complexas (listas de dicionários)
- [x] Integração total dos 5 pilares da lógica de programação no terminal/Pydroid 3
- [x] Resolução de exceções de chave (`KeyError`) e sintaxe de `f-string`

---

## 🔑 Gabarito de Respostas — Para o Tutor

| Pergunta de Engajamento | Resposta Esperada |
|------------------------|-------------------|
| Qual a principal diferença entre Lista (`list`) e Dicionário (`dict`)? | Listas são ordenadas e acessadas por números `[0]`; Dicionários são acessados por chaves personalizadas `["nome"]` |
| O que faz o método `dicionario.get("chave", "padrão")`? | Retorna o valor da chave se ela existir; se não existir, retorna o valor padrão sem travar com `KeyError` |
| Como formatar corretamente uma chave de dicionário dentro de uma `f-string`? | Usando aspas simples na chave interna: `f"Olá {dic['nome']}"` para não conflitar com as aspas externas |
| O que representa uma Lista de Dicionários? | Representa uma tabela ou banco de dados, onde a lista guarda as linhas e cada dicionário guarda as colunas daquele registro |

---

## 🏠 Micro-Missão de Casa (Entregar na Aula 07)

> **Escolha UMA das duas opções abaixo para realizar no Pydroid 3 do celular (10 a 15 min):**

### 📱 Opção A — "O Perfil de Usuário do Seu App"
Crie no Pydroid 3 um dicionário chamado `usuario` com as chaves `"nome"`, `"idade"`, `"bio"` e `"foto_perfil"`. Peça para o usuário preencher com `input()` e exiba o cartão de perfil no terminal.

### 🎮 Opção B — "O Inventário de RPG com Dicionário"
Crie no Pydroid 3 um dicionário para um item de jogo contendo `"nome"`, `"tipo"` (espada/escudo/poção), `"poder"` e `"preco"`. Exiba uma mensagem formatada mostrando as estatísticas do item!
