# Roteiro de Aula — Aula 07 (Trilha Mobile)

## Prototipagem de Apps Mobile: Flet/GUI + Definição dos Projetos Finais

**Duração total:** 180 minutos (3h00) — **Horário:** 15h00 às 18h00
**Público-alvo:** Estudantes do Ensino Médio
**Pré-requisitos:** Fundamentos de Python das Aulas 1–6 (variáveis, `if/else`, `while/for`, listas, funções)

---

## Bloco 1: Impacto Visual — Do Terminal para o App Mobile (15 min)

**Objetivo:** Mostrar como transformar scripts de terminal em um aplicativo visual moderno que roda na tela do celular e no computador.

### Ações do Tutor:
- Projetar o app do terminal ao lado da versão visual em Flet: botões coloridos, caixas de entrada de texto bonitas, layouts de tela de celular.

---

## Bloco 2: Aula Expositiva — Componentes de Interface Mobile (30 min)

### Conteúdo Teórico:
- O que é o Flet e como ele cria apps mobile e web usando apenas Python.
- Componentes fundamentais:
  - `ft.Text()` → Títulos e rótulos
  - `ft.TextField()` → Caixa de digitação do usuário
  - `ft.ElevatedButton()` → Botão clicável de ação
  - `ft.Column()` → Empilhar elementos na vertical (como na tela do celular)
  - `page.update()` → Atualizar os elementos visuais da tela

---

## Bloco 3: Prática Guiada — Convertendo Calculadora de IMC para App Visual (25 min)

Pegar a função `calcular_imc(peso, altura)` da Aula 6 e conectar a uma tela interativa com dois campos `TextField` e um botão.

---

## Bloco 4: Brainstorming dos Projetos Finais Mobile (ODS) (55 min)

**Objetivo:** Formar duplas/trios e escolher o problema da escola ou bairro vinculado aos Objetivos de Desenvolvimento Sustentável (ODS) que o App Mobile irá resolver.

### Exemplos de Projetos Mobile:
1. 📱 **Assistente de Estudos com IA:** App para gerar quizzes e organizar revisões no celular.
2. ♻️ **Calculadora de Reciclagem & Impacto:** Informa a economia de plástico/papel e indica pontos de coleta.
3. 🏫 **Guia da Comunidade Escolar:** Agenda de eventos, provas e lembretes de prioridade.

---

## Bloco 5: Validação dos Esboços e Escolha das ODS em Grupo (25 min)

Revisão dos esboços em papel de cada equipe, refinamento do fluxo de telas e definição de papéis na dupla/trio.

---

## Bloco 6: Encerramento e Organização de Equipes (15 min)

Registro dos temas dos projetos finais mobile, orientações para a Aula 8 (Desenvolvimento Acelerado com IA).

---

## Resumo da Duração (15h00 às 18h00)

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | Impacto Visual: Do Terminal para o App Mobile | 15 min | 15h00 – 15h15 |
| 2 | Aula Expositiva: Componentes de Interface Mobile (Flet) | 30 min | 15h15 – 15h45 |
| 3 | Prática Guiada: Calculadora IMC Visual no Celular | 25 min | 15h45 – 16h10 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h10 – 16h25** |
| 4 | Brainstorming dos Projetos Finais Mobile (ODS) | 55 min | 16h25 – 17h20 |
| 5 | Validação dos Esboços e Escolha das ODS em Grupo | 25 min | 17h20 – 17h45 |
| 6 | Encerramento e Organização de Equipes | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |

---

## Conceitos de Programação Absorvidos

- [x] Conceito de GUI (Interface Gráfica de Usuário) no celular
- [x] Componentes básicos do Flet (`Text`, `TextField`, `ElevatedButton`, `Column`)
- [x] Eventos de clique (`on_click`)
- [x] Atualização de tela (`page.update()`)
- [x] Alinhamento com Objetivos de Desenvolvimento Sustentável (ODS)

---

### 🏠 Micro-Missão de Casa (Para o final desta aula)

> **Escolha UMA das duas opções abaixo para realizar no Caderno / Smartphone (10 a 15 min):**

#### 🎨 Opção A — "UI Designer de Caderno (Protótipo Mobile)"
- **Tarefa:** Esboce no caderno a tela do seu App Mobile rotulando os elementos do Flet (`ft.Text`, `ft.TextField`, `ft.ElevatedButton`) e indicando a cor de fundo da tela (`page.bgcolor`).

#### 🎤 Opção B — "Pesquisa de Usuário no WhatsApp"
- **Tarefa:** Mande mensagem no WhatsApp para 2 amigos ou familiares perguntando o que eles gostariam de ver em um app que resolve o problema do seu projeto final. Anote as ideias!


---

## Material Didático Complementar

### ⚡ Quiz de Aquecimento (Para o início da Aula 08)

#### ❓ Pergunta 1: Verdadeiro ou Falso?
No Flet, após alterar qualquer valor na tela (como `resultado.value = "Sucesso!"`), devemos chamar `page.update()` para atualizar visualmente a tela.
* [ ] Verdadeiro
* [ ] Falso

#### ❓ Pergunta 2: Múltipla Escolha
Qual componente do Flet cria uma caixa onde o usuário pode digitar texto?
* A) `ft.TextField()`
* B) `ft.ElevatedButton()`
* C) `ft.CaixaDoBatman()`
* D) `ft.Text()`

#### ❓ Pergunta 3: Encontre o Erro! 🔍
```python
def botao_clicado(e):
    mensagem.value = "Bem-vindo!"
```
**O que faltou para a mensagem aparecer na tela?**

---

#### 🔑 Gabarito Comentado (Para o Tutor)
1. **VERDADEIRO!** ✅ `page.update()` renderiza na tela.
2. **Alternativa A!** 🎯 `ft.TextField()`.
3. **Faltou `page.update()`!** 🛑
