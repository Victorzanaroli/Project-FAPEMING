import os
import random

def jogar_pacman():
    # 1. VARIÁVEIS VISUAIS (Perfeito para os alunos hackearem depois)
    pacman = "C"
    fantasma = "F"
    pastilha = "."
    parede = "#"
    vazio = " "

    # 2. O MAPA DO JOGO (Matriz)
    mapa = [
        ["#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", ".", ".", "#"],
        ["#", ".", "#", "#", "#", ".", "#"],
        ["#", ".", ".", "F", ".", ".", "#"],
        ["#", ".", "#", "#", "#", ".", "#"],
        ["#", "C", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#"]
    ]

    # Posições iniciais
    pac_x, pac_y = 5, 1
    pontos = 0

    # Loop principal do jogo
    while True:
        # Limpa o terminal para dar o efeito de "jogo rodando"
        os.system('cls' if os.name == 'nt' else 'clear')

        # 3. A ÁREA DOS PRINTS (A Interface do Jogo)
        print("=============================")
        print("   🕹️ PAC-MAN DO TERMINAL   ")
        print("=============================")
        print(f"💰 PONTUAÇÃO ATUAL: {pontos}")
        print("-----------------------------")

        # Imprime o mapa linha por linha
        for linha in mapa:
            print(" ".join(linha))
        
        print("-----------------------------")
        print("Comandos: W (Cima), S (Baixo), A (Esquerda), D (Direita)")
        
        # 4. O INPUT (Ouvindo o jogador)
        jogada = input("👉 Faça sua jogada e aperte ENTER: ").lower()

        # Guarda a posição antiga
        antigo_x, antigo_y = pac_x, pac_y

        # Movimento do jogador
        if jogada == 'w': pac_x -= 1
        elif jogada == 's': pac_x += 1
        elif jogada == 'a': pac_y -= 1
        elif jogada == 'd': pac_y += 1
        else:
            print("❌ Tecla errada! Pressione enter para continuar.")
            input()
            continue

        # Regra de colisão com a parede
        if mapa[pac_x][pac_y] == parede:
            pac_x, pac_y = antigo_x, antigo_y # Bateu e voltou
            print("💥 AI! Você bateu a cabeça na parede!")
            input("Pressione ENTER para continuar...")
        
        # Regra de comer a pastilha
        elif mapa[pac_x][pac_y] == pastilha:
            pontos += 10

        # Atualiza a posição do Pac-Man no mapa
        mapa[antigo_x][antigo_y] = vazio
        mapa[pac_x][pac_y] = pacman

        # Regra de Game Over (Bater no Fantasma)
        if mapa[pac_x][pac_y] == fantasma:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("💀 GAME OVER! 💀")
            print("O fantasma devorou você!")
            print(f"Sua pontuação final foi: {pontos}")
            break

if __name__ == "__main__":
    jogar_pacman()