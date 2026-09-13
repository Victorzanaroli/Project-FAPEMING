# Roteiro de Aula — Aula 08

## Integração: Flet + IA (Antigravity) + GEMINI.md

**Duração total:** 150 minutos (2h30)
**Público-alvo:** Estudantes do Ensino Médio (com fundamentos de Python + Flet da Aula 7)
**Pré-requisitos:** Todos os conceitos das Aulas 1–7, protótipo visual do Flet funcional

---

## Bloco 1: Revisão dos Protótipos (10 min)

**Objetivo:** Cada grupo mostra o protótipo da interface e recebe feedback rápido.

### Ações do Tutor:
- Cada grupo tem **30 segundos** para projetar a tela do app e dizer:
  1. Nome do projeto
  2. Qual problema resolve
  3. O que falta implementar
- O tutor anota na lousa o status de cada grupo:
  - ✅ Interface pronta
  - ⚠️ Interface parcial
  - ❌ Precisa de ajuda
- Direcionar monitores para as equipes que estão atrasadas.

---

## Bloco 2: Aula Expositiva — GEMINI.md e Integração com IA (25 min)

**Objetivo:** Ensinar o conceito de arquivo de contexto (`GEMINI.md`) e como integrar funcionalidades de IA no aplicativo.

### O que é o GEMINI.md?
> *"É o 'manual de instruções' que vocês escrevem para a IA. Quando vocês definem regras no GEMINI.md, a IA sabe exatamente o contexto do projeto e respeita as limitações que vocês impõem."*

#### Estrutura do GEMINI.md
```markdown
# Projeto: [Nome do App]

## Contexto
Este é um aplicativo escolar desenvolvido por alunos do Ensino Médio
em Varginha-MG como parte do projeto "Trilhando o Caminho do Código".

## Tecnologias
- Python 3
- Flet (interface gráfica)
- Gemini CLI (assistência de IA)

## Regras Inegociáveis
1. Todo código deve usar apenas bibliotecas padrão + Flet.
2. Os comentários devem ser em português.
3. A interface deve ter tema escuro.
4. O código deve ser modular (funções separadas).
5. Não use classes ou orientação a objetos.

## Funcionalidades do App
1. [Funcionalidade 1 - descrição]
2. [Funcionalidade 2 - descrição]
3. [Funcionalidade 3 - descrição]

## Público-Alvo
Estudantes e professores de escolas públicas.
```

### Como a IA Usa o GEMINI.md
- Quando o aluno chama o Gemini CLI na pasta do projeto, ele lê automaticamente o `GEMINI.md`.
- A IA passa a respeitar as regras definidas: não usa bibliotecas proibidas, mantém o estilo de código, etc.
- É como "treinar" a IA para o seu projeto específico.

### Integrando IA no App (Nível Básico)
Para esta primeira integração, a IA atua como **assistente de conteúdo** dentro do app:

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Assistente Escolar"
    page.bgcolor = "#1a1a2e"
    
    pergunta = ft.TextField(label="Faça uma pergunta sobre a matéria")
    resposta = ft.Text("", size=14, color="white")
    
    def perguntar(e):
        # Aqui a IA processaria a pergunta
        # Por enquanto, simula uma resposta
        resposta.value = f"Processando sua pergunta: '{pergunta.value}'..."
        page.update()
    
    page.add(
        ft.Column([
            ft.Text("🤖 Assistente de Estudos", size=28, color="cyan"),
            pergunta,
            ft.ElevatedButton("Perguntar à IA", on_click=perguntar),
            resposta
        ])
    )

ft.app(target=main)
```

### Ações do Tutor:
- Mostrar ao vivo a criação de um `GEMINI.md` e como ele muda o comportamento da IA.
- Rodar o exemplo de integração e explicar: *"Na apresentação, vocês podem simular a resposta da IA ou, se der tempo, integrar de verdade."*

---

## Bloco 3: Sprint de Desenvolvimento (60 min)

**Objetivo:** Tempo focado para as equipes desenvolverem os projetos finais com suporte dos monitores.

### Estrutura do Sprint:
- **Cada equipe deve seguir este ciclo:**
  1. **Escrever a lógica** → Funções Python que resolvem o problema (ex: `calcular_reciclagem()`, `gerar_questao()`)
  2. **Conectar à interface Flet** → Vincular as funções aos botões e campos da tela
  3. **Testar** → Rodar o app e verificar se funciona
  4. **Depurar com IA** → Colar erros no Gemini e pedir correções

### Checklist de Desenvolvimento (entregar impresso para cada grupo):

```
CHECKLIST DO PROJETO FINAL
─────────────────────────────────────
Grupo: _______________  Tema: _______________

[ ] A interface abre sem erros
[ ] Os campos de entrada (TextField) funcionam
[ ] O botão principal executa a função correta
[ ] O resultado aparece na tela após clicar
[ ] O código tem pelo menos 2 funções (def)
[ ] O GEMINI.md do projeto está criado
[ ] O código tem comentários em português
[ ] O app resolve o problema proposto
[ ] O grupo sabe explicar pelo menos 3 linhas do código
```

### Ações do Tutor:
- Circular pelas equipes a cada 10 minutos.
- Priorizar equipes com dificuldades técnicas (Flet não instalado, erros de importação).
- Se uma equipe estiver avançada, desafiar: *"Adicionem uma segunda tela ou funcionalidade."*

---

## Bloco 4: Preparação da Apresentação (20 min)

**Objetivo:** Estruturar o roteiro de apresentação para a Aula 9.

### Cada grupo deve preparar (máximo 5 minutos por grupo):

1. **O Problema (30s):** Qual problema da escola/comunidade o app resolve?
2. **A Demo (2min):** Demonstração ao vivo do app funcionando.
3. **O Código (1min30s):** Mostrar 1 trecho de código e explicar a lógica.
4. **A IA (1min):** Como a IA ajudou (e onde atrapalhou) no desenvolvimento.

### Ações do Tutor:
- Distribuir um template de roteiro de apresentação.
- Cronometrar um ensaio rápido (cada grupo faz um "treino" de 1 minuto).

---

## Bloco 5: Teste Final Completo (10 min)

**Objetivo:** Cada grupo roda o app do início ao fim e registra bugs restantes.

### Ações do Tutor:
- Pedir que cada grupo rode o app na frente do monitor.
- Anotar quais projetos estão 100% funcionais e quais precisam de ajustes.
- Orientar: *"Se tiver bug, vocês têm até a próxima aula para arrumar. Usem a IA para depurar em casa ou no início da Aula 9."*

---

## Bloco 6: Encerramento e Commit Final (10 min)

### Ações do Tutor:
- Garantir que todos os projetos estão salvos.
- Exportar os logs `.jsonl` acumulados.
- Frase de fechamento:
  > *"Semana que vem é a nossa FEIRA DE SOLUÇÕES! Vocês vão apresentar os projetos para convidados. Revisem o código, ensaiem a apresentação e lembrem: na hora da demonstração, o app precisa funcionar do início ao fim!"*

---

## Resumo da Duração

| Bloco | Atividade | Duração |
|-------|-----------|---------|
| 1 | Revisão dos Protótipos (30s por grupo) | 10 min |
| 2 | Aula Expositiva: GEMINI.md + Integração IA | 25 min |
| 3 | Sprint de Desenvolvimento | 60 min |
| 4 | Preparação da Apresentação | 20 min |
| 5 | Teste Final Completo | 10 min |
| 6 | Encerramento e Commit Final | 10 min |
| **Total** | | **135 min** |

> **Margem:** 15 minutos para suporte técnico emergencial.

---

## Conceitos de Programação Absorvidos

- [x] Arquivo de contexto `GEMINI.md`
- [x] Integração de módulos Python com interface Flet
- [x] Ciclo de desenvolvimento: Escrever → Conectar → Testar → Depurar
- [x] Preparação e comunicação técnica (apresentação de projeto)

## Recursos Necessários

- Flet instalado em todos os notebooks (`pip install flet`)
- Gemini CLI configurado e autenticado
- Template do GEMINI.md (o tutor cria um modelo base antes da aula)
- Checklist impresso para cada grupo
- Template de roteiro de apresentação

## Vínculo com a Pesquisa

- **Artigo 2 (DBR / Learning Analytics):** Esta aula é a principal fonte de artefatos de código para análise de maturidade (complexidade ciclomática, modularidade, acoplamento).
- Os logs de prompts desta aula capturam a categoria P5 (Arquitetura & Contextualização via GEMINI.md).
