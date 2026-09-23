# Roteiro de Aula — Aula 08 (Trilha Mobile)

## Sprint de Desenvolvimento: App Mobile com IA + Flet Avançado (Navegação, Temas e Ícones)

**Data:** 02 de dezembro de 2026 (quarta-feira) — **Horário:** 15h00 às 18h00
**Duração total:** 180 minutos (3h00)
**Público-alvo:** Estudantes do Ensino Médio
**Pré-requisitos:** Protótipo do App em Flet/Python funcional, conceitos das Aulas 1–7

> **🔑 Legenda do Roteiro:**
> - `[SLIDE]` → Projetar no telão (conceito visual/teórico)
> - `[IDE]` → Abrir o VS Code e digitar ao vivo (alunos copiam junto)
> - `[❓ ENGAJAMENTO]` → Jogar a pergunta para a turma, aguardar respostas
> - `[⏱️]` → Marcação de tempo estimado para o bloco

---

## 📅 Grade de Horários

| Bloco | Atividade | Duração | Horário |
|-------|-----------|---------|---------|
| 1 | **⚡ Quiz de Aquecimento** — Revisão da Aula 07 (Flet básico) | 15 min | 15h00 – 15h15 |
| 2 | Flet Avançado: Navegação entre Telas, Temas de Cor e Ícones | 30 min | 15h15 – 15h45 |
| 3 | Revisão Rápida dos Protótipos das Equipes | 15 min | 15h45 – 16h00 |
| **☕** | **Intervalo / Pausa para Lanche** | **15 min** | **16h00 – 16h15** |
| 4 | Sprint de Desenvolvimento com IA (Parte 1 + 2) | 80 min | 16h15 – 17h35 |
| 5 | Estrutura do Pitch + Ensaio Rápido | 10 min | 17h35 – 17h45 |
| 6 | Encerramento e Checklist da Apresentação | 15 min | 17h45 – 18h00 |
| **Total** | | **180 min (3h00)** | **15h00 – 18h00** |

---

## ⚡ Bloco 1: Quiz de Aquecimento — Revisão da Aula 07 (15 min)

> **Objetivo:** Ativar o conhecimento dos componentes básicos do Flet antes de avançar para os componentes de navegação.

`[SLIDE]` — Projete as perguntas no telão uma a uma.

---

### ❓ Pergunta 1: Verdadeiro ou Falso?
> *"No Flet, após alterar o valor de um componente (como `resultado.value = "Sucesso!"`), o Flet atualiza a tela automaticamente sem precisar chamar nenhuma função."*
- [ ] Verdadeiro
- [ ] Falso

**🔑 Gabarito:** **FALSO!** ❌ Sempre precisamos chamar `page.update()` depois de alterar qualquer componente para que a mudança apareça na tela.

---

### ❓ Pergunta 2: Múltipla Escolha
Qual componente do Flet cria uma **caixa onde o usuário pode digitar texto**?
- A) `ft.Text()`
- B) `ft.ElevatedButton()`
- C) `ft.TextField()`
- D) `ft.Column()`

**🔑 Gabarito:** **Alternativa C!** 🎯 `ft.TextField()` cria o campo de entrada. `ft.Text()` só exibe texto estático.

---

### ❓ Pergunta 3: Encontre o Erro! 🔍
```python
def botao_clicado(e):
    resultado.value = "Bem-vindo!"
    # Falta alguma coisa aqui?
```
**O que falta para a mensagem aparecer na tela?**

**🔑 Gabarito:** Falta `page.update()` ao final da função! Sem ela, o valor muda na memória, mas a tela não é redesenhada.

---

`[❓ ENGAJAMENTO]` — Roda rápida:
> **"Mostra aí o protótipo da tela do caderno que vocês fizeram de casa! Quantas telas o app de vocês vai ter?"**

---

## 🎨 Bloco 2: Flet Avançado — Navegação, Temas e Ícones (30 min)

> **Objetivo:** Elevar a qualidade visual dos apps com navegação entre telas, paletas de cores e ícones — transformando protótipos simples em apps com aparência profissional.

### ⏱️ [0–10 min] Tema de Cor Global

`[SLIDE]` — Mostre dois apps lado a lado: um com fundo padrão (branco) e outro com Dark Mode personalizado.

`[IDE]` — Como definir o tema do app:
```python
import flet as ft

def main(page: ft.Page):
    # Personalizando o visual global do app
    page.title = "Meu App Mobile"
    page.bgcolor = "#1e1e2e"          # Cor de fundo (hex ou nome)
    page.theme_mode = ft.ThemeMode.DARK  # Modo escuro

    # Cor padrão dos componentes
    page.theme = ft.Theme(color_scheme_seed="purple")

    titulo = ft.Text(
        "🚀 Bem-vindo ao Meu App!",
        size=24,
        weight=ft.FontWeight.BOLD,
        color="#cdd6f4"
    )
    page.add(titulo)

ft.app(target=main)
```

**Roteiro de fala:**
- *"`page.bgcolor` define a cor de fundo de toda a tela — use código hex como `#1e1e2e` para tons escuros chiques!"*
- *"`page.theme_mode = ft.ThemeMode.DARK` ativa o Dark Mode globalmente."*
- *"`color_scheme_seed` é a cor principal do app — o Flet usa ela para gerar botões, campos e destaques de forma harmônica."*

`[❓ ENGAJAMENTO]` → **"Qual cor vai ser o tema do app de vocês? Cada equipe escolhe agora!"**

---

### ⏱️ [10–20 min] Ícones nos Botões

`[IDE]` — Botões com ícones ficam muito mais profissionais:
```python
import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#1e1e2e"
    page.title = "App com Ícones"

    # Botão com ícone embutido
    btn_calcular = ft.ElevatedButton(
        text="Calcular",
        icon=ft.Icons.CALCULATE,
        icon_color="#cba6f7",
        bgcolor="#313244",
        color="white"
    )

    btn_salvar = ft.ElevatedButton(
        text="Salvar",
        icon=ft.Icons.SAVE,
        bgcolor="#a6e3a1",
        color="#1e1e2e"
    )

    btn_voltar = ft.ElevatedButton(
        text="Voltar",
        icon=ft.Icons.ARROW_BACK,
        bgcolor="#f38ba8",
        color="white"
    )

    page.add(
        ft.Column([btn_calcular, btn_salvar, btn_voltar], spacing=12)
    )

ft.app(target=main)
```

**Roteiro de fala:**
- *"`ft.Icons.CALCULATE` é um ícone do catálogo do Material Design — o Flet tem centenas deles!"*
- *"Peçam para a IA: `'Me lista 10 ícones do ft.Icons relacionados a saúde'` — ela vai sugerir os mais adequados para o tema do projeto de vocês."*

`[❓ ENGAJAMENTO]` → **"Que ícone combinaria com o tema do app de vocês?"**

---

### ⏱️ [20–30 min] Navegação entre Telas com `ft.NavigationBar`

`[IDE]` — O padrão mais usado em apps mobile:
```python
import flet as ft

def main(page: ft.Page):
    page.title = "App com Navegação"
    page.bgcolor = "#1e1e2e"

    # --- Conteúdo de cada "tela" ---
    tela_home = ft.Column([
        ft.Text("🏠 Tela Principal", size=22, color="white", weight=ft.FontWeight.BOLD),
        ft.Text("Bem-vindo ao app!", color="#cdd6f4"),
    ], visible=True)

    tela_calcular = ft.Column([
        ft.Text("🧮 Calculadora", size=22, color="white", weight=ft.FontWeight.BOLD),
        ft.TextField(label="Digite um valor", bgcolor="#313244", color="white"),
        ft.ElevatedButton("Calcular", icon=ft.Icons.CALCULATE),
    ], visible=False)

    tela_sobre = ft.Column([
        ft.Text("ℹ️ Sobre o App", size=22, color="white", weight=ft.FontWeight.BOLD),
        ft.Text("Criado por: [Seu Nome]", color="#cdd6f4"),
        ft.Text("Aulas de Python com IA — FAPEMING 2026", color="#a6adc8"),
    ], visible=False)

    # --- Lógica de navegação ---
    def mudar_tela(e):
        tela_home.visible = (e.control.selected_index == 0)
        tela_calcular.visible = (e.control.selected_index == 1)
        tela_sobre.visible = (e.control.selected_index == 2)
        page.update()

    # --- Barra de navegação inferior ---
    nav = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Início"),
            ft.NavigationBarDestination(icon=ft.Icons.CALCULATE, label="Calcular"),
            ft.NavigationBarDestination(icon=ft.Icons.INFO, label="Sobre"),
        ],
        on_change=mudar_tela,
        bgcolor="#313244",
        selected_index=0
    )

    page.add(tela_home, tela_calcular, tela_sobre)
    page.navigation_bar = nav

ft.app(target=main)
```

**Roteiro de fala:**
- *"A navegação funciona assim: cada 'tela' é uma `ft.Column` com `visible=True` ou `False`. Quando o usuário toca na barra inferior, a função `mudar_tela` liga uma e apaga as outras."*
- *"É o mesmo princípio de qualquer app de celular! Instagram, iFood, Google Maps — todos usam essa barra de navegação inferior."*
- *"Peçam para a IA adaptar esse modelo para o tema do projeto de vocês — ela sabe fazer isso!"*

`[❓ ENGAJAMENTO]` → **"Quantas abas o app de vocês vai precisar? O que vai em cada uma?"**

---

## 📋 Bloco 3: Revisão Rápida dos Protótipos das Equipes (15 min)

> **Objetivo:** Cada equipe apresenta o estado atual do app (5–7 min para todas as equipes) e define o que vai implementar no sprint desta aula.

### Ações do Tutor:
- Cada equipe mostra a tela inicial do app e diz qual problema resolve (máx. 1 min por equipe).
- O tutor faz 1 pergunta rápida por equipe: *"Qual é a função `def` principal do app de vocês?"*
- Cada equipe anota no caderno **3 metas para o sprint de hoje:** o que vai implementar nas próximas 2 horas.

---

## ☕ Intervalo — 15 minutos (16h00 – 16h15)

Antes de liberar, projete no telão:
```
☕ INTERVALO!
Quando voltar: 80 minutos de SPRINT PURO.
Meta: sair daqui com o app funcionando e bonito.
Revejam as 3 metas que vocês anotaram! 🎯
```

---

## 🔨 Bloco 4: Sprint de Desenvolvimento com IA (80 min)

> **Objetivo:** Cada equipe implementa as funcionalidades planejadas usando a IA como parceira, aplicando os recursos avançados do Flet aprendidos hoje.

### Regras do Sprint:

`[SLIDE]` — Projete no telão durante todo o bloco:
```
🚀 REGRAS DO SPRINT:
1. Cada equipe tem 3 metas anotadas — foque nelas!
2. Use a IA para implementar: cole seu código + peça a modificação específica.
3. DEU ERRO? Copie o erro → cole na IA → peça explicação e correção.
4. Tutor e monitor circulam — levante a mão se travar por mais de 5 min!
5. A cada 25 min: pause, teste o app no celular, anote o que funcionou.
```

### Prompts de Apoio por Desafio:

#### 🎨 Para melhorar o visual:
```
Meu app Flet usa Python. Aqui está meu código atual:
[COLE SEU CÓDIGO]

Preciso que você:
1. Aplique um tema escuro com bgcolor="#1e1e2e"
2. Adicione ícones nos botões usando ft.Icons
3. Melhore o espaçamento com spacing e padding
4. Mantenha toda a lógica existente intacta
```

#### 🧭 Para adicionar navegação:
```
Meu app Flet tem [X] funcionalidades principais: [liste elas].
Adicione uma ft.NavigationBar com [X] abas correspondentes.
Use visible=True/False para alternar entre elas.
Mantenha toda a lógica de cálculo/processamento intacta.
```

#### 🛡️ Para melhorar a robustez:
```
No meu app Flet, quando o usuário deixa o campo [nome do campo] em branco
ou digita um texto inválido onde espera número, o app quebra com ValueError.
Adicione try/except nos campos de entrada e exiba uma mensagem de erro
amigável na tela usando um ft.Text com color="red".
```

### 🎯 Checkpoints do Monitor (a cada 25 min):

**Checkpoint 1 (16h40):** *"Mostra o app rodando. Quantas das 3 metas estão prontas?"*

**Checkpoint 2 (17h05):** *"Testa no Pydroid 3 agora. O que aparece na tela do celular?"*

**Checkpoint 3 (17h30):** *"Qual é a função `def` mais importante do app? Me explica o que ela faz."*

---

## 🎤 Bloco 5: Estrutura do Pitch + Ensaio Rápido (10 min)

> **Objetivo:** Cada equipe define quem fala o quê na apresentação da Feira Final.

`[SLIDE]` — Projete a estrutura:
```
🎤 ESTRUTURA DO PITCH (5 minutos por equipe):

[30s] ❓ O PROBLEMA
      "O app resolve um problema real: ..."

[2min] 📱 A DEMONSTRAÇÃO
       Execução ao vivo — mostre o app funcionando no celular!
       Toque em todas as abas/funcionalidades.

[1min30s] 💻 O CÓDIGO
           "A função mais importante é o def [nome]()..."
           "Usamos try/except para tratar erros de..."
           "A navegação entre telas funciona com ft.NavigationBar..."

[1min] 🤖 COMO A IA AJUDOU
        "Usamos a IA para criar / corrigir / melhorar..."
```

**Ações do Tutor:**
- Cada equipe divide os papéis: quem fala o Problema, quem faz a Demo, quem explica o Código.
- 1 ensaio rápido de 30 segundos por equipe (só o início do pitch).

---

## 🔴 Bloco 6: Encerramento e Checklist da Apresentação (15 min)

### Checklist Final antes de Sair:

`[SLIDE]` — Projete o checklist:
```
✅ CHECKLIST DA AULA 08:

[ ] O app roda sem erros no VS Code
[ ] O app roda no Pydroid 3 (celular)
[ ] Tem pelo menos 1 função def com lógica principal
[ ] Tem try/except nos campos de entrada
[ ] Tem tema de cor definido (bgcolor + cores nos componentes)
[ ] Tem ícones nos botões principais
[ ] O código está salvo no celular E no drive/pendrive
[ ] Os papéis do pitch estão definidos (quem fala o quê)

🎯 META PARA A PRÓXIMA AULA (09/12 — Sprint Final):
     Chegar com o app 90% pronto para o polimento final!
```

**Frase de fechamento:**
> *"Hoje vocês elevaram o nível — os apps agora têm navegação, ícones e tema visual. Na próxima semana é o Sprint Final: o tutor revisa o código de cada equipe e vocês fazem os ajustes finais antes da Feira. Salvem tudo!"*

---

## ✅ Conceitos de Programação Absorvidos

- [x] Tema de cor global no Flet (`page.bgcolor`, `page.theme_mode`, `color_scheme_seed`)
- [x] Ícones do Material Design em botões (`ft.Icons.*`)
- [x] Estilização de componentes: `bgcolor`, `color`, `weight`, `size`
- [x] Navegação entre telas com `ft.NavigationBar` e lógica `visible=True/False`
- [x] Integração de lógica Python (def, try/except, listas) com interface Flet estilizada

---

## 🔑 Gabarito de Respostas — Para o Tutor

| Pergunta de Engajamento | Resposta Esperada |
|------------------------|-------------------|
| Por que precisamos de `page.update()`? | Sem ele, a mudança ocorre na memória mas a tela não é redesenhada |
| Como funciona a navegação com `visible`? | Apenas uma `Column` fica `visible=True` por vez; as outras ficam ocultas |
| O que `color_scheme_seed` faz? | Define a cor principal do tema — o Flet deriva automaticamente todas as cores dos componentes a partir dela |
| Por que adicionar `try/except` nos campos do Flet? | O usuário pode deixar em branco ou digitar texto onde espera número, causando `ValueError` |

---

### 🏠 Tarefa de Casa (Para entregar na Aula 09 — Sprint Final)

> **Fazer em casa antes da Aula 09 (09/12):**

#### ✅ Obrigatório:
1. **Teste de estresse:** Execute o app e tente quebrar ele digitando entradas inesperadas (texto onde espera número, campos em branco, símbolos). Anote no caderno o que falhou.
2. **Ensaio do Pitch:** Ensaie a apresentação completa (5 min) pelo menos 2 vezes com o cronômetro do celular.

#### ⭐ Bônus (se sobrar tempo):
3. **Melhoria visual:** Peça para a IA sugerir melhorias de cor, espaçamento ou layout para o app.
4. **Tela "Sobre":** Adicione uma aba "Sobre o App" no `ft.NavigationBar` com o nome da equipe, o problema resolvido e o ODS vinculado.
