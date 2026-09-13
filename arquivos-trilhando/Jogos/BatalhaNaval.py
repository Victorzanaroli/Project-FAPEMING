import os
import random

def jogar_batalha_naval():
    # 1. VARIÁVEIS VISUAIS (A munição perfeita para o "Hack" dos alunos)
    agua = "~"
    tiro_certo = "X"
    tiro_errado = "O"

    # Cria o tabuleiro vazio (Matriz 5x5)
    tabuleiro = [
        [agua, agua, agua, agua, agua],
        [agua, agua, agua, agua, agua],
        [agua, agua, agua, agua, agua],
        [agua, agua, agua, agua, agua],
        [agua, agua, agua, agua, agua]
    ]

    # Sorteia 3 posições secretas para esconder os Vírus
    alvos = []
    while len(alvos) < 3:
        linha = random.randint(0, 4)
        coluna = random.randint(0, 4)
        if (linha, coluna) not in alvos:
            alvos.append((linha, coluna))

    tentativas = 8
    acertos = 0

    # Loop principal do jogo
    while tentativas > 0 and acertos < 3:
        # Limpa o terminal a cada rodada
        os.system('cls' if os.name == 'nt' else 'clear')

        # 2. A ÁREA DOS PRINTS (Interface do Jogo - Onde você ensina a matéria)
        print("=======================================")
        print(" 🚢 BATALHA NAVAL: CAÇA AOS VÍRUS 💻")
        print("=======================================")
        print(f"🔋 Tentativas restantes: {tentativas}")
        print(f"🎯 Vírus destruídos: {acertos} de 3")
        print("---------------------------------------")

        # Imprime o cabeçalho das colunas
        print("     1 2 3 4 5")
        print("    ----------")
        
        # Imprime o mapa com os números das linhas ao lado
        for i, linha in enumerate(tabuleiro):
            print(f" {i+1} | " + " ".join(linha))
        
        print("---------------------------------------")

        # 3. O INPUT (Ouvindo as coordenadas do jogador)
        print("Digite as coordenadas para lançar o míssil:")
        try:
            # Subtraímos 1 porque no Python a contagem começa do zero
            linha_tiro = int(input("👉 Linha (1 a 5): ")) - 1
            coluna_tiro = int(input("👉 Coluna (1 a 5): ")) - 1
        except ValueError:
            print("❌ Erro: Digite apenas números!")
            input("Pressione ENTER para continuar...")
            continue

        # Regra 1: Evitar que o jogador atire fora do mapa
        if linha_tiro < 0 or linha_tiro > 4 or coluna_tiro < 0 or coluna_tiro > 4:
            print("❌ Míssil perdido! Atire apenas entre 1 e 5.")
            input("Pressione ENTER para continuar...")
            continue

        # Regra 2: Evitar atirar no mesmo lugar duas vezes
        if tabuleiro[linha_tiro][coluna_tiro] != agua:
            print("⚠️ Você já atirou nessa coordenada, capitão!")
            input("Pressione ENTER para continuar...")
            continue

        # Diminui uma tentativa e checa se acertou o alvo
        tentativas -= 1
        if (linha_tiro, coluna_tiro) in alvos:
            tabuleiro[linha_tiro][coluna_tiro] = tiro_certo
            acertos += 1
            print("\n💥 KABOOM! Você destruiu um vírus maligno!")
        else:
            tabuleiro[linha_tiro][coluna_tiro] = tiro_errado
            print("\n💦 SPLASH! Tiro na água...")
        
        input("Pressione ENTER para a próxima rodada...")

    # 4. TELA DE FIM DE JOGO
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================")
    if acertos == 3:
        print("🏆 VITÓRIA! O SISTEMA ESTÁ SALVO! 🏆")
    else:
        print("💀 GAME OVER! OS VÍRUS DOMINARAM TUDO. 💀")
    print("=======================================")

if __name__ == "__main__":
    jogar_batalha_naval()