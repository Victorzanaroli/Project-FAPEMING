# Roteiro de Aula — Aula 07

## Interfaces Visuais com Flet + Definição dos Projetos Finais

**Duração total:** 180 minutos (3h00) — **Horário:** 15h00 às 18h00
**Público-alvo:** Estudantes do Ensino Médio (com fundamentos de Python das Aulas 1–6)
**Pré-requisitos:** `print`, `input`, variáveis, `if/elif/else`, `while/for`, listas, funções


---

## Bloco 1: Impacto Visual — Do Terminal Preto ao App Colorido (10 min)

**Objetivo:** Causar o "efeito wow" mostrando que tudo que eles fizeram no terminal pode se transformar em um aplicativo moderno.

### Ações do Tutor:
- Projetar lado a lado:
  - **Esquerda:** O jogo de adivinhação da Aula 4 rodando no terminal preto.
  - **Direita:** O mesmo jogo com interface Flet: campo de texto bonito, botão colorido, mensagem dinâmica.
- Reação esperada: *"Uau, é o mesmo programa, mas agora parece um app de verdade!"*
- Conexão:
  > *"Até agora, vocês dominam a LÓGICA. Hoje vamos vestir essa lógica com uma ROUPA bonita usando o Flet — um framework que transforma código Python em aplicativos visuais."*

---

## Bloco 2: Aula Expositiva — Introdução ao Flet (30 min)

**Objetivo:** Ensinar os componentes básicos do Flet: Page, Text, TextField, Button, Column, Row.

### Conteúdo Teórico:

#### O que é o Flet?
> *"Flet é uma biblioteca Python que permite criar aplicativos com interface gráfica (botões, caixas de texto, cores) que rodam no desktop, celular e web — tudo com Python!"*

#### O App Mínimo
```python
import flet as ft

def main(page: ft.Page):
    # Configurações da janela
    page.title = "Meu Primeiro App"
    page.bgcolor = "#1a1a2e"
    
    # Adicionando um texto na tela
    page.add(
        ft.Text("Olá, mundo!", size=30, color="white")
    )

ft.app(target=main)
```

#### Os Componentes Essenciais
| Componente | O que faz | Exemplo visual |
|---|---|---|
| `ft.Text()` | Mostra texto na tela | Título, mensagem, resultado |
| `ft.TextField()` | Campo para o usuário digitar | Nome, nota, busca |
| `ft.ElevatedButton()` | Botão clicável | "Calcular", "Enviar" |
| `ft.Column()` | Organiza itens na VERTICAL | Empilhar elementos ↓ |
| `ft.Row()` | Organiza itens na HORIZONTAL | Alinhar elementos → |

#### Eventos — Quando o Botão é Clicado
```python
import flet as ft

def main(page: ft.Page):
    # O campo de texto
    campo_nome = ft.TextField(label="Seu nome")
    
    # O texto de resultado
    resultado = ft.Text("", size=20)
    
    # A função que roda quando o botão é clicado
    def botao_clicado(e):
        resultado.value = f"Olá, {campo_nome.value}! 🎉"
        page.update()  # FUNDAMENTAL: atualiza a tela
    
    # O botão
    botao = ft.ElevatedButton("Saudar", on_click=botao_clicado)
    
    # Montando a tela
    page.add(
        ft.Column([
            campo_nome,
            botao,
            resultado
        ])
    )

ft.app(target=main)
```

> **Regra de ouro do Flet:** Depois de mudar qualquer valor na tela, SEMPRE chame `page.update()`. Sem isso, nada aparece!

### Ações do Tutor:
- Digitar o app mínimo ao vivo e rodar — a janela do Flet abre na hora.
- Adicionar o campo de texto e botão ao vivo.
- Clicar no botão e mostrar o resultado aparecendo.
- Mudar a cor de fundo ao vivo (`page.bgcolor = "#0f0f23"`) e rodar de novo.

---

## Bloco 3: Prática Guiada — Convertendo Terminal → Flet (30 min)

**Objetivo:** Converter a Calculadora de IMC (da Aula 6) de terminal para interface Flet.

### Instrução para os alunos:
> *"Vocês já têm a função `calcular_imc()` da aula passada. Agora vamos dar uma roupa visual para ela."*

### Prompt Modelo:
```
Converta este código Python de terminal para uma interface gráfica usando Flet.

Código original:
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
print(calcular_imc(peso, altura))

Regras:
1. Crie dois campos de texto (TextField) para peso e altura.
2. Crie um botão "Calcular IMC" que chama a função calcular_imc.
3. Mostre o resultado em um Text abaixo do botão.
4. Use cores agradáveis (fundo escuro, texto claro).
5. Adicione comentários em português explicando os componentes Flet.
6. Não mude a lógica da função, apenas a interface.
```

### Ações do Tutor:
- Circular verificando se os alunos entendem a diferença entre `input()` (terminal) e `ft.TextField()` (visual).
- Verificar se entenderam o `page.update()`.
- Perguntar: *"A função `calcular_imc()` mudou alguma coisa?"* → Não! A lógica é a mesma, só a interface é diferente.

---

## Bloco 4: Brainstorming de Projetos Finais (30 min)

**Objetivo:** Definir os temas dos projetos finais vinculados aos ODS e à comunidade.

### Ações do Tutor:
- Apresentar brevemente os ODS relevantes (projetar no quadro):
  - **ODS 4 — Educação de Qualidade:** Apps que ajudem no estudo
  - **ODS 9 — Indústria, Inovação e Infraestrutura:** Ferramentas tecnológicas
  - **ODS 11 — Cidades e Comunidades Sustentáveis:** Soluções para a escola/bairro
  - **ODS 13 — Ação contra a Mudança Global do Clima:** Conscientização ambiental

- Formar duplas ou trios.
- Cada grupo deve responder 3 perguntas no papel:
  1. *"Qual problema da escola ou do bairro vocês querem resolver?"*
  2. *"Qual ODS esse problema se conecta?"*
  3. *"O que o app precisa fazer (2–3 funcionalidades)?"*

### Sugestões de Projetos (para quem não tiver ideia):

| Tema | ODS | Funcionalidades básicas |
|---|---|---|
| Calculadora de Reciclagem | 13 | Classificar resíduos, calcular economia ambiental, gerar relatório |
| Assistente de Estudos com IA | 4 | Gerar questões sobre matérias, cronograma de revisão, dicas de estudo |
| Organizador de Feira Cultural | 11 | Cadastrar apresentações, gerenciar horários, votação de melhor stand |
| Monitor de Consumo de Água | 6 | Registrar consumo diário, comparar com meta, sugerir economia |
| Quiz Educativo sobre Varginha | 4 | Perguntas sobre história local, pontuação, ranking |
| Agenda Escolar Inteligente | 4 | Cadastrar provas, calcular dias restantes, lembrete de prioridade |

---

## Bloco 5: Prototipagem Rápida com IA (20 min)

**Objetivo:** Cada grupo gera a tela inicial do projeto no Flet usando IA.

### Instrução:
> *"Ainda não se preocupem com a lógica. Montem apenas a TELA INICIAL do app: título, campos de entrada e botões. A lógica vem na próxima aula."*

### Prompt Template:
```
Crie a interface inicial de um aplicativo em Python usando Flet para [TEMA DO PROJETO].
O app deve ter:
1. Um título bonito centralizado no topo.
2. [NÚMERO] campos de entrada (TextField) para [DESCREVER].
3. Um botão principal "[AÇÃO]".
4. Uma área de resultado abaixo do botão.
5. Use um tema escuro com cores agradáveis.
6. Por enquanto, o botão pode apenas mostrar "Funcionalidade em desenvolvimento".
7. Adicione comentários em português.
```

### Ações do Tutor:
- Cada grupo roda o protótipo — deve abrir uma janela bonita com os campos, mesmo que o botão não faça nada ainda.
- Registrar os temas escolhidos numa planilha.

---

## Bloco 6: Encerramento (10 min)

### Ações do Tutor:
- Listar os projetos de cada grupo no quadro.
- Orientar: *"Na próxima aula, vocês vão integrar a lógica Python dentro dessa interface e adicionar IA. Tragam ideias de funcionalidades extras!"*
- Exportar logs e salvar códigos.

---

## Resumo da Duração (15h00 às 18h00)

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | Impacto Visual: Terminal vs Flet | 15 min | 15h00 – 15h15 |
| 2 | Aula Expositiva: Componentes Flet | 35 min | 15h15 – 15h50 |
| 3 | Prática Guiada: IMC Terminal → Flet | 30 min | 15h50 – 16h20 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h20 – 16h35** |
| 4 | Brainstorming de Projetos Finais (ODS) | 35 min | 16h35 – 17h10 |
| 5 | Prototipagem Rápida com IA | 35 min | 17h10 – 17h45 |
| 6 | Encerramento | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |


---

## Conceitos de Programação Absorvidos

- [x] Framework Flet: `ft.app()`, `ft.Page`
- [x] Componentes: `ft.Text`, `ft.TextField`, `ft.ElevatedButton`
- [x] Layout: `ft.Column`, `ft.Row`
- [x] Eventos: `on_click`, handler functions
- [x] `page.update()` — atualização da interface
- [x] Transição de paradigma: terminal → GUI

## Preparação Técnica Necessária

> **ANTES desta aula, o tutor deve garantir que todos os notebooks têm o Flet instalado:**
> ```
> pip install flet
> ```
> Testar com o app mínimo em pelo menos 3 máquinas.

---

## Material Didático Complementar

### ⚡ Quiz de Aquecimento (Para o início da Aula 08)

#### ❓ Pergunta 1: Verdadeiro ou Falso?
No Flet, depois de alterar o texto ou o valor de qualquer componente na tela (por exemplo, `resultado.value = "Sucesso!"`), é obrigatório chamar o comando `page.update()`, caso contrário a tela não atualiza visualmente.
* [ ] Verdadeiro
* [ ] Falso

#### ❓ Pergunta 2: Múltipla Escolha
Qual componente do Flet devemos utilizar quando queremos criar uma caixa onde o usuário possa digitar um texto ou um número?
* A) `ft.TextField()`
* B) `ft.ElevatedButton()`
* C) `ft.CaixaDeTextoDoBatman()`
* D) `ft.Text()`

#### ❓ Pergunta 3: Encontre o Erro! 🔍
Um aluno criou um botão no Flet para exibir uma mensagem de boas-vindas, mas quando ele clica no botão, nada acontece na tela:
```python
def botao_clicado(e):
    texto_mensagem.value = "Bem-vindo ao nosso aplicativo!"
    # O botão foi clicado e o valor mudou, mas a tela continua idêntica!
```
**Qual comando essencial do Flet está faltando no final da função `botao_clicado`?**

---

#### 🔑 Gabarito Comentado (Para o Tutor)
1. **VERDADEIRO!** ✅ O Flet guarda as alterações em memória e só renderiza na tela quando executamos `page.update()`.
2. **Alternativa A!** 🎯 `ft.TextField()` cria o campo digitável. `ft.Text()` só exibe texto fixo e a opção C não existe na biblioteca!
3. **Faltou o `page.update()`!** 🛑 Sem chamar `page.update()`, o Flet não sabe que precisa redesenhar o componente na tela. 
   * *Correção:* Adicionar `page.update()` na última linha da função.

---

### 🏠 Micro-Missão de Casa (Para o final desta aula)

> **Escolha UMA das duas opções abaixo para realizar (10 a 15 min):**

#### 🎨 Opção A — "UI Designer de Caderno" (Protótipo da Tela)
- **Tarefa:** Desenhe à mão livre no caderno um esboço simples da tela do **Projeto Final** da sua equipe em Flet rotulando os componentes:
  - Título (`ft.Text`)
  - Caixas de entrada (`ft.TextField`)
  - Botão principal (`ft.ElevatedButton`)
  - Área de resultado (`ft.Text`)

#### 🎤 Opção B — "Pesquisa de Usuário / Entrevista de Campo"
- **Tarefa:** Converse com 2 colegas ou familiares e faça 2 perguntas simples sobre o problema que o app da sua equipe vai resolver. Anote no caderno as respostas para ajudar no ajuste da interface e funcionalidades na próxima aula!


