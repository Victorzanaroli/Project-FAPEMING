import tkinter as tk
import random

# Configurações
COLUNAS, LINHAS = 10, 20
TAMANHO = 30
LARGURA = COLUNAS * TAMANHO
ALTURA = LINHAS * TAMANHO
VELOCIDADE = 500  # ms

CORES = ['cyan', 'blue', 'orange', 'yellow', 'green', 'purple', 'red']

FORMATOS = {
    'I': [[1,1,1,1]],
    'O': [[1,1],[1,1]],
    'T': [[0,1,0],[1,1,1]],
    'S': [[0,1,1],[1,1,0]],
    'Z': [[1,1,0],[0,1,1]],
    'J': [[1,0,0],[1,1,1]],
    'L': [[0,0,1],[1,1,1]],
}

class Tetris:
    def __init__(self, root):
        self.root = root
        self.root.title("Tetris")
        self.root.resizable(False, False)

        # Frame principal
        frame = tk.Frame(root, bg='#111')
        frame.pack(padx=10, pady=10)

        # Canvas do jogo
        self.canvas = tk.Canvas(frame, width=LARGURA, height=ALTURA, bg='#1a1a2e', highlightthickness=0)
        self.canvas.grid(row=0, column=0, rowspan=20, padx=(0,10))

        # Painel lateral
        painel = tk.Frame(frame, bg='#111', width=120)
        painel.grid(row=0, column=1, sticky='n')

        tk.Label(painel, text="PRÓXIMA", fg='#aaa', bg='#111', font=('Courier', 10, 'bold')).pack(pady=(0,4))
        self.canvas_preview = tk.Canvas(painel, width=120, height=90, bg='#1a1a2e', highlightthickness=0)
        self.canvas_preview.pack(pady=(0,16))

        tk.Label(painel, text="PONTOS", fg='#aaa', bg='#111', font=('Courier', 10, 'bold')).pack()
        self.lbl_pontos = tk.Label(painel, text="0", fg='white', bg='#111', font=('Courier', 20, 'bold'))
        self.lbl_pontos.pack(pady=(0,12))

        tk.Label(painel, text="NÍVEL", fg='#aaa', bg='#111', font=('Courier', 10, 'bold')).pack()
        self.lbl_nivel = tk.Label(painel, text="1", fg='white', bg='#111', font=('Courier', 20, 'bold'))
        self.lbl_nivel.pack(pady=(0,12))

        tk.Label(painel, text="LINHAS", fg='#aaa', bg='#111', font=('Courier', 10, 'bold')).pack()
        self.lbl_linhas = tk.Label(painel, text="0", fg='white', bg='#111', font=('Courier', 20, 'bold'))
        self.lbl_linhas.pack(pady=(0,20))

        self.btn_reiniciar = tk.Button(painel, text="Reiniciar", command=self.reiniciar,
                                       bg='#333', fg='white', font=('Courier', 9),
                                       relief='flat', padx=8, pady=4)
        self.btn_reiniciar.pack()

        tk.Label(painel, text="\n←→ mover\n↑ rotacionar\n↓ acelerar\nEspaço: drop", 
                 fg='#555', bg='#111', font=('Courier', 8), justify='left').pack(pady=(16,0))

        # Estado do jogo
        self.iniciar()

        # Teclas
        self.root.bind('<Left>',  lambda e: self.mover(-1, 0))
        self.root.bind('<Right>', lambda e: self.mover(1, 0))
        self.root.bind('<Down>',  lambda e: self.mover(0, 1))
        self.root.bind('<Up>',    lambda e: self.rotacionar())
        self.root.bind('<space>', lambda e: self.drop())
        self.root.bind('<p>',     lambda e: self.pausar())

    def iniciar(self):
        self.grade = [[None]*COLUNAS for _ in range(LINHAS)]
        self.pontos = 0
        self.nivel = 1
        self.linhas_total = 0
        self.pausado = False
        self.fim = False
        self.proxima_peca = self.nova_peca()
        self.peca_atual = None
        self.spawn()
        self.atualizar()

    def reiniciar(self):
        if hasattr(self, '_after_id'):
            self.root.after_cancel(self._after_id)
        self.iniciar()

    def nova_peca(self):
        nome = random.choice(list(FORMATOS.keys()))
        cor = random.choice(CORES)
        return {'nome': nome, 'formato': [linha[:] for linha in FORMATOS[nome]], 'cor': cor}

    def spawn(self):
        self.peca_atual = self.proxima_peca
        self.proxima_peca = self.nova_peca()
        fmt = self.peca_atual['formato']
        self.px = COLUNAS // 2 - len(fmt[0]) // 2
        self.py = 0
        self.desenhar_preview()
        if self.colide(fmt, self.px, self.py):
            self.fim = True

    def colide(self, fmt, px, py):
        for r, linha in enumerate(fmt):
            for c, val in enumerate(linha):
                if val:
                    nx, ny = px + c, py + r
                    if nx < 0 or nx >= COLUNAS or ny >= LINHAS:
                        return True
                    if ny >= 0 and self.grade[ny][nx]:
                        return True
        return False

    def mover(self, dx, dy):
        if self.pausado or self.fim:
            return
        fmt = self.peca_atual['formato']
        if not self.colide(fmt, self.px + dx, self.py + dy):
            self.px += dx
            self.py += dy
            self.desenhar()

    def rotacionar(self):
        if self.pausado or self.fim:
            return
        fmt = self.peca_atual['formato']
        novo = [list(x) for x in zip(*fmt[::-1])]
        # Wall kick básico
        for dx in [0, -1, 1, -2, 2]:
            if not self.colide(novo, self.px + dx, self.py):
                self.peca_atual['formato'] = novo
                self.px += dx
                self.desenhar()
                return

    def drop(self):
        if self.pausado or self.fim:
            return
        while not self.colide(self.peca_atual['formato'], self.px, self.py + 1):
            self.py += 1
        self.travar()

    def pausar(self):
        if self.fim:
            return
        self.pausado = not self.pausado
        if not self.pausado:
            self.atualizar()

    def travar(self):
        fmt = self.peca_atual['formato']
        cor = self.peca_atual['cor']
        for r, linha in enumerate(fmt):
            for c, val in enumerate(linha):
                if val and self.py + r >= 0:
                    self.grade[self.py + r][self.px + c] = cor
        self.limpar_linhas()
        self.spawn()

    def limpar_linhas(self):
        novas = [l for l in self.grade if any(c is None for c in l)]
        qtd = LINHAS - len(novas)
        if qtd:
            # Pontuação estilo Tetris original
            pts = [0, 100, 300, 500, 800][min(qtd, 4)] * self.nivel
            self.pontos += pts
            self.linhas_total += qtd
            self.nivel = self.linhas_total // 10 + 1
            self.grade = [[None]*COLUNAS for _ in range(qtd)] + novas
            self.lbl_pontos.config(text=str(self.pontos))
            self.lbl_nivel.config(text=str(self.nivel))
            self.lbl_linhas.config(text=str(self.linhas_total))

    def velocidade_atual(self):
        return max(80, VELOCIDADE - (self.nivel - 1) * 40)

    def atualizar(self):
        if self.fim:
            self.desenhar()
            return
        if not self.pausado:
            fmt = self.peca_atual['formato']
            if not self.colide(fmt, self.px, self.py + 1):
                self.py += 1
            else:
                self.travar()
            self.desenhar()
        self._after_id = self.root.after(self.velocidade_atual(), self.atualizar)

    def sombra(self):
        fmt = self.peca_atual['formato']
        sy = self.py
        while not self.colide(fmt, self.px, sy + 1):
            sy += 1
        return sy

    def desenhar(self):
        self.canvas.delete('all')

        # Grade de fundo
        for r in range(LINHAS):
            for c in range(COLUNAS):
                x1, y1 = c*TAMANHO, r*TAMANHO
                x2, y2 = x1+TAMANHO, y1+TAMANHO
                cor = self.grade[r][c]
                if cor:
                    self.canvas.create_rectangle(x1+1, y1+1, x2-1, y2-1, fill=cor, outline='#000', width=1)
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill='', outline='#222', width=1)

        if not self.fim:
            # Sombra (ghost piece)
            sy = self.sombra()
            for r, linha in enumerate(self.peca_atual['formato']):
                for c, val in enumerate(linha):
                    if val:
                        x1 = (self.px+c)*TAMANHO
                        y1 = (sy+r)*TAMANHO
                        self.canvas.create_rectangle(x1+1, y1+1, x1+TAMANHO-1, y1+TAMANHO-1,
                                                     fill='', outline=self.peca_atual['cor'], width=1, dash=(3,3))

            # Peça atual
            for r, linha in enumerate(self.peca_atual['formato']):
                for c, val in enumerate(linha):
                    if val:
                        x1 = (self.px+c)*TAMANHO
                        y1 = (self.py+r)*TAMANHO
                        self.canvas.create_rectangle(x1+1, y1+1, x1+TAMANHO-1, y1+TAMANHO-1,
                                                     fill=self.peca_atual['cor'], outline='#000', width=1)
        else:
            # Game Over
            self.canvas.create_rectangle(0, ALTURA//2-60, LARGURA, ALTURA//2+60, fill='#000', outline='')
            self.canvas.create_text(LARGURA//2, ALTURA//2-20, text="GAME OVER",
                                    fill='red', font=('Courier', 22, 'bold'))
            self.canvas.create_text(LARGURA//2, ALTURA//2+20, text=f"Pontos: {self.pontos}",
                                    fill='white', font=('Courier', 14))

        if self.pausado:
            self.canvas.create_rectangle(0, ALTURA//2-40, LARGURA, ALTURA//2+40, fill='#000', outline='')
            self.canvas.create_text(LARGURA//2, ALTURA//2, text="PAUSADO  [P]",
                                    fill='yellow', font=('Courier', 18, 'bold'))

    def desenhar_preview(self):
        self.canvas_preview.delete('all')
        fmt = self.proxima_peca['formato']
        cor = self.proxima_peca['cor']
        ts = 22
        offset_x = (120 - len(fmt[0])*ts) // 2
        offset_y = (90  - len(fmt)*ts) // 2
        for r, linha in enumerate(fmt):
            for c, val in enumerate(linha):
                if val:
                    x1 = offset_x + c*ts
                    y1 = offset_y + r*ts
                    self.canvas_preview.create_rectangle(x1+1, y1+1, x1+ts-1, y1+ts-1,
                                                         fill=cor, outline='#000', width=1)

root = tk.Tk()
app = Tetris(root)
root.mainloop()
