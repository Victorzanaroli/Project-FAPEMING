"""
Flappy Bird - versão corrigida e completa
------------------------------------------
Requisitos: pip install pygame
Rodar:      python flappy_bird.py

Correções feitas em relação à versão original:
- Existiam apenas 1 cano na tela -> agora há vários canos gerados continuamente.
- Colisão em X checava só a borda direita do pássaro -> agora usa Rect.colliderect
  (checagem completa da hitbox, não só um ponto).
- Colisão de chão/teto usava o centro do pássaro -> agora usa a borda (y - raio / y + raio).
- Não existia sys.exit() após pygame.quit() -> adicionado (evita processo pendurado em
  alguns terminais/IDEs).
- Não existia tela de início nem de game over -> adicionadas (INICIO, PLACAR, JOGANDO,
  CAINDO, GAME_OVER), com botões clicáveis e reinício.
- Estética baseada na imagem de referência: céu, nuvens, silhueta de prédios, chão
  listrado, canos com "boca" e pássaro com asa/olho/bico, tudo desenhado via pygame
  (não há arquivos de imagem externos neste ambiente).
"""

import os
import random
import sys

import pygame

# ------------------------------------------------------------------
# Inicialização
# ------------------------------------------------------------------
pygame.init()

LARGURA, ALTURA = 400, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Flappy Bird")
relogio = pygame.time.Clock()
FPS = 60

# ------------------------------------------------------------------
# Cores (baseadas na referência)
# ------------------------------------------------------------------
AZUL_CEU = (78, 192, 202)
BRANCO = (255, 255, 255)
VERDE_CANO = (92, 189, 55)
VERDE_CANO_ESCURO = (58, 130, 30)
AMARELO = (255, 205, 45)
LARANJA = (235, 130, 40)
VERMELHO_BOTAO = (216, 78, 65)
MARROM_CHAO = (222, 216, 149)
MARROM_CHAO_ESCURO = (201, 176, 122)
PRETO = (40, 30, 20)
CINZA_PREDIO = (150, 205, 205)

# ------------------------------------------------------------------
# Fontes
# ------------------------------------------------------------------
fonte_titulo = pygame.font.SysFont("couriernew", 44, bold=True)
fonte_grande = pygame.font.SysFont("couriernew", 34, bold=True)
fonte_media = pygame.font.SysFont("couriernew", 22, bold=True)
fonte_pequena = pygame.font.SysFont("couriernew", 16, bold=True)

# ------------------------------------------------------------------
# Recorde (salvo em disco, na mesma pasta do script)
# ------------------------------------------------------------------
try:
    ARQUIVO_RECORDE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "recorde.txt")
except NameError:
    ARQUIVO_RECORDE = "recorde.txt"


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
        pass  # sem permissão de escrita? o jogo continua funcionando normalmente


recorde = carregar_recorde()

# ------------------------------------------------------------------
# Chão
# ------------------------------------------------------------------
ALTURA_CHAO = 80
Y_CHAO = ALTURA - ALTURA_CHAO


def desenhar_chao(superficie, deslocamento):
    pygame.draw.rect(superficie, MARROM_CHAO, (0, Y_CHAO, LARGURA, ALTURA_CHAO))
    pygame.draw.rect(superficie, VERDE_CANO_ESCURO, (0, Y_CHAO, LARGURA, 5))
    largura_listra = 34
    x = -largura_listra + deslocamento
    while x < LARGURA:
        pygame.draw.rect(superficie, MARROM_CHAO_ESCURO, (x, Y_CHAO + 8, largura_listra // 2, 10))
        x += largura_listra


# ------------------------------------------------------------------
# Texto com contorno (usado só para textos estáticos, pré-renderizado)
# ------------------------------------------------------------------
def criar_texto_contornado(fonte, texto, cor, cor_contorno):
    base = fonte.render(texto, True, cor)
    largura = base.get_width() + 8
    altura = base.get_height() + 8
    superficie = pygame.Surface((largura, altura), pygame.SRCALPHA)
    contorno = fonte.render(texto, True, cor_contorno)
    for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, 2), (-2, 2), (2, -2)]:
        superficie.blit(contorno, (4 + dx, 4 + dy))
    superficie.blit(base, (4, 4))
    return superficie


# ------------------------------------------------------------------
# Pássaro
# ------------------------------------------------------------------
class Passaro:
    def __init__(self):
        self.x = 65
        self.raio = 16
        self.reset()

    def reset(self):
        self.y = float(ALTURA // 2)
        self.velocidade_y = 0.0
        self.angulo = 0

    def pular(self):
        self.velocidade_y = -8.5

    def atualizar(self):
        self.velocidade_y += 0.5
        self.velocidade_y = min(self.velocidade_y, 11)
        self.y += self.velocidade_y
        self.angulo = max(-25, min(85, -self.velocidade_y * 4))

    def get_rect(self):
        return pygame.Rect(int(self.x - self.raio), int(self.y - self.raio), self.raio * 2, self.raio * 2)

    def desenhar(self, superficie):
        tam = self.raio * 2 + 14
        sup = pygame.Surface((tam, tam), pygame.SRCALPHA)
        c = tam // 2
        r = self.raio

        flap_cima = (pygame.time.get_ticks() // 150) % 2 == 0
        offset_asa = -2 if flap_cima else 2

        pygame.draw.ellipse(sup, AMARELO, (c - r, c - r, r * 2, r * 2))
        pygame.draw.ellipse(sup, PRETO, (c - r, c - r, r * 2, r * 2), 2)
        pygame.draw.ellipse(sup, LARANJA, (c - r + 3, c - 2 + offset_asa, r, r - 4))
        pygame.draw.circle(sup, BRANCO, (c + 5, c - 6), 5)
        pygame.draw.circle(sup, PRETO, (c + 7, c - 6), 2)
        pygame.draw.polygon(
            sup,
            LARANJA,
            [(c + r - 4, c - 2), (c + r + 9, c + 2), (c + r - 4, c + 7)],
        )
        pygame.draw.polygon(
            sup,
            PRETO,
            [(c + r - 4, c - 2), (c + r + 9, c + 2), (c + r - 4, c + 7)],
            1,
        )

        sup_rot = pygame.transform.rotate(sup, self.angulo)
        rect = sup_rot.get_rect(center=(int(self.x), int(self.y)))
        superficie.blit(sup_rot, rect)


# ------------------------------------------------------------------
# Cano
# ------------------------------------------------------------------
class Cano:
    LARGURA = 60
    ESPACO = 155
    VELOCIDADE = 3

    def __init__(self, x):
        self.x = float(x)
        margem = 70
        self.altura_topo = random.randint(margem, Y_CHAO - self.ESPACO - margem)
        self.passou = False

    def atualizar(self):
        self.x -= self.VELOCIDADE

    def fora_da_tela(self):
        return self.x < -self.LARGURA

    def rects(self):
        topo = pygame.Rect(int(self.x), 0, self.LARGURA, self.altura_topo)
        y_base = self.altura_topo + self.ESPACO
        base = pygame.Rect(int(self.x), y_base, self.LARGURA, Y_CHAO - y_base)
        return topo, base

    def desenhar(self, superficie):
        topo, base = self.rects()
        for rect in (topo, base):
            pygame.draw.rect(superficie, VERDE_CANO, rect)
            pygame.draw.rect(superficie, VERDE_CANO_ESCURO, rect, 3)

        lip_topo = pygame.Rect(int(self.x) - 4, topo.height - 26, self.LARGURA + 8, 26)
        lip_base = pygame.Rect(int(self.x) - 4, base.y, self.LARGURA + 8, 26)
        for lip in (lip_topo, lip_base):
            pygame.draw.rect(superficie, VERDE_CANO, lip)
            pygame.draw.rect(superficie, VERDE_CANO_ESCURO, lip, 3)


# ------------------------------------------------------------------
# Fundo (nuvens + prédios com leve paralaxe)
# ------------------------------------------------------------------
class Fundo:
    def __init__(self):
        self.nuvens = [
            [random.randint(0, LARGURA), random.randint(30, 170), random.randint(24, 42)]
            for _ in range(4)
        ]
        self.deslocamento_predios = 0.0

    def atualizar(self):
        for nuvem in self.nuvens:
            nuvem[0] -= 0.4
            if nuvem[0] < -60:
                nuvem[0] = LARGURA + 60
                nuvem[1] = random.randint(30, 170)
        self.deslocamento_predios = (self.deslocamento_predios - 0.6) % 90

    def desenhar(self, superficie):
        base_predios = Y_CHAO
        x = -90 + self.deslocamento_predios
        i = 0
        while x < LARGURA + 90:
            altura_predio = 55 + (i % 3) * 22
            pygame.draw.rect(superficie, CINZA_PREDIO, (x, base_predios - altura_predio, 55, altura_predio))
            x += 90
            i += 1
        for cx, cy, r in self.nuvens:
            pygame.draw.circle(superficie, BRANCO, (int(cx), int(cy)), r)
            pygame.draw.circle(superficie, BRANCO, (int(cx) + r // 2, int(cy) + 6), int(r * 0.7))
            pygame.draw.circle(superficie, BRANCO, (int(cx) - r // 2, int(cy) + 8), int(r * 0.6))


# ------------------------------------------------------------------
# Botões (retângulos fixos)
# ------------------------------------------------------------------
def rect_centralizado(centro, largura, altura):
    r = pygame.Rect(0, 0, largura, altura)
    r.center = centro
    return r


RECT_START = rect_centralizado((LARGURA // 2, 380), 160, 46)
RECT_PLACAR = rect_centralizado((LARGURA // 2, 440), 160, 46)
RECT_VOLTAR = rect_centralizado((LARGURA // 2, 440), 160, 46)
RECT_REINICIAR = rect_centralizado((LARGURA // 2, 420), 190, 46)
RECT_PAUSA = pygame.Rect(LARGURA - 46, 14, 32, 32)


def desenhar_botao(superficie, rect, texto):
    pygame.draw.rect(superficie, LARANJA, rect, border_radius=8)
    pygame.draw.rect(superficie, VERMELHO_BOTAO, rect, 3, border_radius=8)
    label = fonte_media.render(texto, True, BRANCO)
    superficie.blit(label, label.get_rect(center=rect.center))


def desenhar_pausa(superficie, rect, pausado):
    pygame.draw.rect(superficie, LARANJA, rect, border_radius=5)
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


# Textos estáticos pré-renderizados (evita renderizar fonte toda hora)
SUP_TITULO = criar_texto_contornado(fonte_titulo, "Flappy Bird", AMARELO, PRETO)
SUP_GAMEOVER = criar_texto_contornado(fonte_grande, "GAME OVER", (240, 60, 50), PRETO)

# ------------------------------------------------------------------
# Estados do jogo
# ------------------------------------------------------------------
INICIO, PLACAR, JOGANDO, CAINDO, GAME_OVER = "inicio", "placar", "jogando", "caindo", "game_over"


def novo_jogo():
    p = Passaro()
    canos_iniciais = [Cano(LARGURA + 120)]
    return p, canos_iniciais, 0


passaro, canos, pontos = novo_jogo()
fundo = Fundo()
deslocamento_chao = 0.0
estado = INICIO
pausado = False

rodando = True
while rodando:
    relogio.tick(FPS)

    # ---------------- Eventos ----------------
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False

            elif evento.key == pygame.K_SPACE:
                if estado == INICIO:
                    estado = JOGANDO
                    passaro.pular()
                elif estado == JOGANDO and not pausado:
                    passaro.pular()
                elif estado == GAME_OVER:
                    passaro, canos, pontos = novo_jogo()
                    estado = INICIO

            elif evento.key == pygame.K_p and estado == JOGANDO:
                pausado = not pausado

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            pos = evento.pos

            if estado == INICIO:
                if RECT_START.collidepoint(pos):
                    estado = JOGANDO
                    passaro.pular()
                elif RECT_PLACAR.collidepoint(pos):
                    estado = PLACAR

            elif estado == PLACAR:
                if RECT_VOLTAR.collidepoint(pos):
                    estado = INICIO

            elif estado == JOGANDO:
                if RECT_PAUSA.collidepoint(pos):
                    pausado = not pausado
                elif not pausado:
                    passaro.pular()

            elif estado == GAME_OVER:
                if RECT_REINICIAR.collidepoint(pos):
                    passaro, canos, pontos = novo_jogo()
                    estado = INICIO

    # ---------------- Atualização ----------------
    fundo.atualizar()

    if estado in (JOGANDO,) and not pausado:
        deslocamento_chao = (deslocamento_chao - Cano.VELOCIDADE) % 34
    elif estado == INICIO or estado == PLACAR:
        deslocamento_chao = (deslocamento_chao - 1.5) % 34

    if estado == JOGANDO and not pausado:
        passaro.atualizar()

        for cano in canos:
            cano.atualizar()
        if canos[-1].x < LARGURA - 190:
            canos.append(Cano(LARGURA + 20))
        canos = [c for c in canos if not c.fora_da_tela()]

        rect_passaro = passaro.get_rect()
        colidiu = False
        for cano in canos:
            topo, base = cano.rects()
            if rect_passaro.colliderect(topo) or rect_passaro.colliderect(base):
                colidiu = True
            if not cano.passou and cano.x + Cano.LARGURA < passaro.x:
                cano.passou = True
                pontos += 1

        if passaro.y - passaro.raio <= 0:
            passaro.y = passaro.raio
            passaro.velocidade_y = 0
            colidiu = True

        if colidiu:
            estado = CAINDO

        if passaro.y + passaro.raio >= Y_CHAO:
            passaro.y = Y_CHAO - passaro.raio
            estado = GAME_OVER
            if pontos > recorde:
                recorde = pontos
                salvar_recorde(recorde)

    elif estado == CAINDO:
        # pássaro continua caindo por gravidade, canos e chão param, até tocar o chão
        passaro.atualizar()
        if passaro.y + passaro.raio >= Y_CHAO:
            passaro.y = Y_CHAO - passaro.raio
            estado = GAME_OVER
            if pontos > recorde:
                recorde = pontos
                salvar_recorde(recorde)

    # ---------------- Desenho ----------------
    tela.fill(AZUL_CEU)
    fundo.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)
    desenhar_chao(tela, deslocamento_chao)
    passaro.desenhar(tela)

    if estado == INICIO:
        tela.blit(SUP_TITULO, SUP_TITULO.get_rect(center=(LARGURA // 2, 130)))
        dica = fonte_pequena.render("ESPAÇO ou clique para começar", True, PRETO)
        tela.blit(dica, dica.get_rect(center=(LARGURA // 2, 190)))
        desenhar_botao(tela, RECT_START, "START")
        desenhar_botao(tela, RECT_PLACAR, "SCORE")

    elif estado == PLACAR:
        titulo = fonte_grande.render("Recorde", True, PRETO)
        tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, 220)))
        valor = fonte_titulo.render(str(recorde), True, LARANJA)
        tela.blit(valor, valor.get_rect(center=(LARGURA // 2, 280)))
        desenhar_botao(tela, RECT_VOLTAR, "VOLTAR")

    elif estado in (JOGANDO, CAINDO):
        texto_pontos = fonte_grande.render(str(pontos), True, BRANCO)
        contorno_pontos = fonte_grande.render(str(pontos), True, PRETO)
        pos_pontos = texto_pontos.get_rect(center=(LARGURA // 2, 50))
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            tela.blit(contorno_pontos, pos_pontos.move(dx, dy))
        tela.blit(texto_pontos, pos_pontos)

        if estado == JOGANDO:
            desenhar_pausa(tela, RECT_PAUSA, pausado)
            if pausado:
                aviso = fonte_media.render("PAUSADO", True, PRETO)
                tela.blit(aviso, aviso.get_rect(center=(LARGURA // 2, ALTURA // 2)))

    elif estado == GAME_OVER:
        tela.blit(SUP_GAMEOVER, SUP_GAMEOVER.get_rect(center=(LARGURA // 2, 170)))
        placar = fonte_media.render(f"Pontos: {pontos}", True, PRETO)
        tela.blit(placar, placar.get_rect(center=(LARGURA // 2, 240)))
        recorde_texto = fonte_media.render(f"Recorde: {recorde}", True, PRETO)
        tela.blit(recorde_texto, recorde_texto.get_rect(center=(LARGURA // 2, 275)))
        desenhar_botao(tela, RECT_REINICIAR, "REINICIAR")
        dica = fonte_pequena.render("ou pressione ESPAÇO", True, PRETO)
        tela.blit(dica, dica.get_rect(center=(LARGURA // 2, 470)))

    pygame.display.update()

pygame.quit()
sys.exit()
