"""
Jogo da Cobrinha - versão corrigida e completa
------------------------------------------------
Requisitos: pip install pygame
Rodar:      python cobrinha.py

Correções feitas em relação à versão original:
- BUG: duas teclas de direção apertadas dentro do mesmo frame permitiam a
  cobra reverter 180° e bater nela mesma de forma "injusta". Corrigido
  tirando um "retrato" (snapshot) da direção atual no início do frame e
  validando as teclas contra esse retrato, não contra variáveis que já
  podem ter mudado dentro do mesmo laço de eventos.
- `quit()` sem `import sys` -> trocado por `sys.exit()` (mais robusto em
  qualquer terminal/IDE).
- `gerar_comida()` podia sortear uma posição em cima do próprio corpo da
  cobra -> agora sorteia de novo até achar uma célula livre.
- A fonte era recriada a cada frame dentro de desenhar_pontuacao() ->
  agora é criada uma única vez, fora do laço principal.
- Não existia tela de início nem de game over -> adicionadas, com recorde
  salvo em arquivo (igual fizemos no Flappy Bird).
- Estética baseada na imagem de referência: tabuleiro em xadrez verde,
  barra superior com ícone de maçã + placar e troféu + recorde, cobra
  azul arredondada com olhos e uma folhinha na cabeça, maçã vermelha com
  folha - tudo desenhado via pygame (sem arquivos de imagem externos).
"""

import os
import random
import sys

import pygame

# ------------------------------------------------------------------
# Inicialização e grade do jogo
# ------------------------------------------------------------------
pygame.init()

TAMANHO_CELULA = 20
COLUNAS = 30
LINHAS = 20
LARGURA = COLUNAS * TAMANHO_CELULA          # 600
ALTURA_JOGO = LINHAS * TAMANHO_CELULA        # 400
ALTURA_BARRA = 60
ALTURA_TOTAL = ALTURA_JOGO + ALTURA_BARRA

tela = pygame.display.set_mode((LARGURA, ALTURA_TOTAL))
pygame.display.set_caption("Jogo da Cobrinha")
relogio = pygame.time.Clock()
FPS_JOGO = 10

# ------------------------------------------------------------------
# Cores (baseadas na referência)
# ------------------------------------------------------------------
VERDE_TAB_1 = (159, 212, 86)
VERDE_TAB_2 = (148, 200, 76)
VERDE_BARRA = (74, 112, 46)
VERDE_BARRA_BORDA = (55, 87, 33)
AZUL_COBRA = (66, 118, 227)
AZUL_COBRA_ESCURO = (47, 92, 191)
BRANCO = (255, 255, 255)
AZUL_OLHO = (35, 60, 120)
VERMELHO_MACA = (219, 63, 46)
VERMELHO_MACA_ESCURO = (178, 44, 32)
VERDE_FOLHA = (63, 150, 63)
AMARELO_TROFEU = (231, 180, 33)
AMARELO_TROFEU_ESCURO = (188, 140, 20)
PRETO = (20, 20, 20)
LARANJA_BOTAO = (235, 130, 40)
VERMELHO_BOTAO = (200, 60, 50)

# ------------------------------------------------------------------
# Fontes (criadas uma única vez)
# ------------------------------------------------------------------
fonte_titulo = pygame.font.SysFont("couriernew", 40, bold=True)
fonte_grande = pygame.font.SysFont("couriernew", 30, bold=True)
fonte_media = pygame.font.SysFont("couriernew", 22, bold=True)
fonte_pequena = pygame.font.SysFont("couriernew", 16, bold=True)
fonte_barra = pygame.font.SysFont("couriernew", 24, bold=True)

# ------------------------------------------------------------------
# Recorde (salvo em disco, na mesma pasta do script)
# ------------------------------------------------------------------
try:
    _PASTA_SCRIPT = os.path.dirname(os.path.abspath(__file__))
except NameError:
    _PASTA_SCRIPT = "."

ARQUIVO_RECORDE = os.path.join(_PASTA_SCRIPT, "recorde_cobra.txt")


def carregar_recorde():
    try:
        with open(ARQUIVO_RECORDE, "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError, OSError):
        return 0


def salvar_recorde(valor):
    try:
        with open(ARQUIVO_RECORDE, "w") as f:
            f.write(str(valor))
    except OSError:
        pass


recorde = carregar_recorde()

# ------------------------------------------------------------------
# Comida
# ------------------------------------------------------------------
def gerar_comida(pixels):
    while True:
        comida_x = random.randrange(0, LARGURA, TAMANHO_CELULA)
        comida_y = random.randrange(0, ALTURA_JOGO, TAMANHO_CELULA)
        if [comida_x, comida_y] not in pixels:
            return comida_x, comida_y


def desenhar_maca(superficie, cx, cy, raio):
    pygame.draw.circle(superficie, VERMELHO_MACA, (cx, cy), raio)
    pygame.draw.circle(superficie, VERMELHO_MACA_ESCURO, (cx, cy), raio, 2)
    pygame.draw.circle(superficie, BRANCO, (cx - raio // 3, cy - raio // 3), max(1, raio // 4))
    folha = [
        (cx + 1, cy - raio),
        (cx + raio, cy - raio - raio // 2),
        (cx + raio // 3, cy - raio + 2),
    ]
    pygame.draw.polygon(superficie, VERDE_FOLHA, folha)


def desenhar_trofeu(superficie, cx, cy, tam):
    largura_copo = tam
    altura_copo = int(tam * 0.7)
    copo = pygame.Rect(0, 0, largura_copo, altura_copo)
    copo.center = (cx, cy - tam // 6)
    pygame.draw.rect(superficie, AMARELO_TROFEU, copo, border_radius=3)
    pygame.draw.rect(superficie, AMARELO_TROFEU_ESCURO, copo, 2, border_radius=3)
    pygame.draw.circle(superficie, AMARELO_TROFEU_ESCURO, (copo.left, copo.centery), max(2, tam // 6), 2)
    pygame.draw.circle(superficie, AMARELO_TROFEU_ESCURO, (copo.right, copo.centery), max(2, tam // 6), 2)
    haste = pygame.Rect(0, 0, max(2, tam // 6), tam // 4)
    haste.midtop = (cx, copo.bottom)
    pygame.draw.rect(superficie, AMARELO_TROFEU, haste)
    base = pygame.Rect(0, 0, int(tam * 0.6), max(3, tam // 8))
    base.midtop = (cx, haste.bottom)
    pygame.draw.rect(superficie, AMARELO_TROFEU, base, border_radius=2)


# ------------------------------------------------------------------
# Tabuleiro
# ------------------------------------------------------------------
def desenhar_tabuleiro(superficie):
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            cor = VERDE_TAB_1 if (linha + coluna) % 2 == 0 else VERDE_TAB_2
            rect = pygame.Rect(
                coluna * TAMANHO_CELULA,
                ALTURA_BARRA + linha * TAMANHO_CELULA,
                TAMANHO_CELULA,
                TAMANHO_CELULA,
            )
            pygame.draw.rect(superficie, cor, rect)


# ------------------------------------------------------------------
# Barra superior (placar / recorde / pausa)
# ------------------------------------------------------------------
RECT_PAUSA = pygame.Rect(LARGURA - 46, 14, 32, 32)


def desenhar_barra(superficie, pontuacao, recorde_atual, pausado):
    pygame.draw.rect(superficie, VERDE_BARRA, (0, 0, LARGURA, ALTURA_BARRA))
    pygame.draw.rect(superficie, VERDE_BARRA_BORDA, (0, ALTURA_BARRA - 4, LARGURA, 4))

    desenhar_maca(superficie, 30, 30, 13)
    texto_pontos = fonte_barra.render(str(pontuacao), True, BRANCO)
    superficie.blit(texto_pontos, (54, 18))

    desenhar_trofeu(superficie, 160, 30, 22)
    texto_recorde = fonte_barra.render(str(recorde_atual), True, BRANCO)
    superficie.blit(texto_recorde, (185, 18))

    desenhar_pausa(superficie, RECT_PAUSA, pausado)


def desenhar_pausa(superficie, rect, pausado):
    pygame.draw.rect(superficie, LARANJA_BOTAO, rect, border_radius=5)
    pygame.draw.rect(superficie, VERMELHO_BOTAO, rect, 2, border_radius=5)
    if pausado:
        pontos_triangulo = [
            (rect.x + 11, rect.y + 7),
            (rect.x + 11, rect.y + 25),
            (rect.x + 25, rect.y + 16),
        ]
        pygame.draw.polygon(superficie, BRANCO, pontos_triangulo)
    else:
        pygame.draw.rect(superficie, BRANCO, (rect.x + 10, rect.y + 7, 4, 18))
        pygame.draw.rect(superficie, BRANCO, (rect.x + 18, rect.y + 7, 4, 18))


# ------------------------------------------------------------------
# Cobra
# ------------------------------------------------------------------
def desenhar_cobra(superficie, pixels, direcao):
    for pixel in pixels[:-1]:
        rect = pygame.Rect(pixel[0], ALTURA_BARRA + pixel[1], TAMANHO_CELULA, TAMANHO_CELULA)
        pygame.draw.rect(superficie, AZUL_COBRA, rect, border_radius=7)
        pygame.draw.rect(superficie, AZUL_COBRA_ESCURO, rect, 2, border_radius=7)

    cabeca_x, cabeca_y = pixels[-1]
    rect_cabeca = pygame.Rect(cabeca_x, ALTURA_BARRA + cabeca_y, TAMANHO_CELULA, TAMANHO_CELULA)
    pygame.draw.rect(superficie, AZUL_COBRA, rect_cabeca, border_radius=9)
    pygame.draw.rect(superficie, AZUL_COBRA_ESCURO, rect_cabeca, 2, border_radius=9)

    vel_x, vel_y = direcao
    cx, cy = rect_cabeca.center
    deslocamento = 5
    if vel_x > 0:
        olho1, olho2 = (cx + deslocamento, cy - 5), (cx + deslocamento, cy + 5)
    elif vel_x < 0:
        olho1, olho2 = (cx - deslocamento, cy - 5), (cx - deslocamento, cy + 5)
    elif vel_y < 0:
        olho1, olho2 = (cx - 5, cy - deslocamento), (cx + 5, cy - deslocamento)
    else:
        olho1, olho2 = (cx - 5, cy + deslocamento), (cx + 5, cy + deslocamento)

    for olho in (olho1, olho2):
        pygame.draw.circle(superficie, BRANCO, olho, 4)
        pygame.draw.circle(superficie, AZUL_OLHO, olho, 2)

    folha = [
        (rect_cabeca.left + 4, rect_cabeca.top),
        (rect_cabeca.left - 2, rect_cabeca.top - 8),
        (rect_cabeca.left + 9, rect_cabeca.top - 3),
    ]
    pygame.draw.polygon(superficie, VERDE_FOLHA, folha)


# ------------------------------------------------------------------
# Botões
# ------------------------------------------------------------------
def rect_centralizado(centro, largura, altura):
    r = pygame.Rect(0, 0, largura, altura)
    r.center = centro
    return r


RECT_REINICIAR = rect_centralizado((LARGURA // 2, ALTURA_TOTAL // 2 + 90), 210, 46)


def desenhar_botao(superficie, rect, texto):
    pygame.draw.rect(superficie, LARANJA_BOTAO, rect, border_radius=8)
    pygame.draw.rect(superficie, VERMELHO_BOTAO, rect, 3, border_radius=8)
    label = fonte_media.render(texto, True, BRANCO)
    superficie.blit(label, label.get_rect(center=rect.center))


# ------------------------------------------------------------------
# Estados
# ------------------------------------------------------------------
JOGANDO = "jogando"
GAME_OVER = "game_over"


def novo_jogo():
    x = (COLUNAS // 2) * TAMANHO_CELULA
    y = (LINHAS // 2) * TAMANHO_CELULA
    pixels = [[x, y]]
    comida_x, comida_y = gerar_comida(pixels)
    return {
        "x": x,
        "y": y,
        "vel_x": 0,
        "vel_y": 0,
        "pixels": pixels,
        "tamanho_cobra": 1,
        "comida": (comida_x, comida_y),
    }


jogo = novo_jogo()
estado = JOGANDO
mostrar_intro = True
pausado = False

rodando = True
while rodando:
    relogio.tick(FPS_JOGO)

    # snapshot da direção atual do início do frame - evita o bug de
    # reversão instantânea quando duas teclas são apertadas no mesmo frame
    vel_x_quadro, vel_y_quadro = jogo["vel_x"], jogo["vel_y"]

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False

            elif estado == JOGANDO:
                if evento.key == pygame.K_p:
                    pausado = not pausado
                elif not pausado:
                    if evento.key == pygame.K_UP and vel_y_quadro == 0:
                        jogo["vel_x"], jogo["vel_y"] = 0, -TAMANHO_CELULA
                        mostrar_intro = False
                    elif evento.key == pygame.K_DOWN and vel_y_quadro == 0:
                        jogo["vel_x"], jogo["vel_y"] = 0, TAMANHO_CELULA
                        mostrar_intro = False
                    elif evento.key == pygame.K_LEFT and vel_x_quadro == 0:
                        jogo["vel_x"], jogo["vel_y"] = -TAMANHO_CELULA, 0
                        mostrar_intro = False
                    elif evento.key == pygame.K_RIGHT and vel_x_quadro == 0:
                        jogo["vel_x"], jogo["vel_y"] = TAMANHO_CELULA, 0
                        mostrar_intro = False

            elif estado == GAME_OVER:
                if evento.key == pygame.K_SPACE:
                    jogo = novo_jogo()
                    estado = JOGANDO
                    mostrar_intro = True
                    pausado = False

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            pos = evento.pos
            if estado == JOGANDO and RECT_PAUSA.collidepoint(pos):
                pausado = not pausado
            elif estado == GAME_OVER and RECT_REINICIAR.collidepoint(pos):
                jogo = novo_jogo()
                estado = JOGANDO
                mostrar_intro = True
                pausado = False

    # ---------------- Atualização ----------------
    if estado == JOGANDO and not pausado and not mostrar_intro:
        jogo["x"] += jogo["vel_x"]
        jogo["y"] += jogo["vel_y"]

        if jogo["x"] < 0 or jogo["x"] >= LARGURA or jogo["y"] < 0 or jogo["y"] >= ALTURA_JOGO:
            estado = GAME_OVER
        else:
            cabeca = [jogo["x"], jogo["y"]]
            pixels = jogo["pixels"]
            pixels.append(cabeca)
            if len(pixels) > jogo["tamanho_cobra"]:
                del pixels[0]

            for pixel in pixels[:-1]:
                if pixel == cabeca:
                    estado = GAME_OVER
                    break

            comida_x, comida_y = jogo["comida"]
            if jogo["x"] == comida_x and jogo["y"] == comida_y:
                jogo["tamanho_cobra"] += 1
                jogo["comida"] = gerar_comida(pixels)

        if estado == GAME_OVER:
            pontuacao_final = jogo["tamanho_cobra"] - 1
            if pontuacao_final > recorde:
                recorde = pontuacao_final
                salvar_recorde(recorde)

    # ---------------- Desenho ----------------
    desenhar_tabuleiro(tela)

    comida_x, comida_y = jogo["comida"]
    desenhar_maca(
        tela,
        comida_x + TAMANHO_CELULA // 2,
        ALTURA_BARRA + comida_y + TAMANHO_CELULA // 2,
        TAMANHO_CELULA // 2 - 1,
    )

    direcao_atual = (jogo["vel_x"], jogo["vel_y"]) if (jogo["vel_x"] or jogo["vel_y"]) else (1, 0)
    desenhar_cobra(tela, jogo["pixels"], direcao_atual)

    desenhar_barra(tela, jogo["tamanho_cobra"] - 1, recorde, pausado)

    if mostrar_intro and estado == JOGANDO:
        overlay = pygame.Surface((LARGURA, ALTURA_JOGO), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 90))
        tela.blit(overlay, (0, ALTURA_BARRA))
        titulo = fonte_titulo.render("Jogo da Cobrinha", True, BRANCO)
        tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, ALTURA_TOTAL // 2 - 40)))
        dica = fonte_media.render("Use as setas para começar", True, BRANCO)
        tela.blit(dica, dica.get_rect(center=(LARGURA // 2, ALTURA_TOTAL // 2 + 10)))
        dica2 = fonte_pequena.render("P para pausar  •  ESC para sair", True, BRANCO)
        tela.blit(dica2, dica2.get_rect(center=(LARGURA // 2, ALTURA_TOTAL // 2 + 40)))

    elif estado == JOGANDO and pausado:
        overlay = pygame.Surface((LARGURA, ALTURA_JOGO), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 90))
        tela.blit(overlay, (0, ALTURA_BARRA))
        aviso = fonte_grande.render("PAUSADO", True, BRANCO)
        tela.blit(aviso, aviso.get_rect(center=(LARGURA // 2, ALTURA_TOTAL // 2)))

    elif estado == GAME_OVER:
        overlay = pygame.Surface((LARGURA, ALTURA_JOGO), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 130))
        tela.blit(overlay, (0, ALTURA_BARRA))
        titulo = fonte_titulo.render("Fim de Jogo!", True, BRANCO)
        tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, ALTURA_TOTAL // 2 - 70)))
        placar = fonte_media.render(f"Pontos: {jogo['tamanho_cobra'] - 1}", True, BRANCO)
        tela.blit(placar, placar.get_rect(center=(LARGURA // 2, ALTURA_TOTAL // 2 - 20)))
        recorde_texto = fonte_media.render(f"Recorde: {recorde}", True, BRANCO)
        tela.blit(recorde_texto, recorde_texto.get_rect(center=(LARGURA // 2, ALTURA_TOTAL // 2 + 15)))
        desenhar_botao(tela, RECT_REINICIAR, "REINICIAR")
        dica = fonte_pequena.render("ou pressione ESPAÇO", True, BRANCO)
        tela.blit(dica, dica.get_rect(center=(LARGURA // 2, ALTURA_TOTAL // 2 + 130)))

    pygame.display.update()

pygame.quit()
sys.exit()
