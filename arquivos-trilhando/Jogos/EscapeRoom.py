import os
import time

def limpar_tela():
    # Comando nativo para limpar o terminal e dar efeito de transição de tela
    os.system('cls' if os.name == 'nt' else 'clear')

def jogar_escape_room():
    # ================= INTRODUÇÃO =================
    limpar_tela()
    print("=============================================")
    print(" 🗝️ ESCAPE ROOM: CAÇA AO TESOURO NO APÊ 🗝️")
    print("=============================================")
    print("Você está atrasado para sair, mas a porta está trancada!")
    print("Sua missão: Encontrar a chave perdida pelo apartamento.")
    print("=============================================\n")
    input("Pressione ENTER para começar a busca na Sala...")

    # ================= CÔMODO 1: SALA =================
    achou_sala = False
    while not achou_sala:
        limpar_tela()
        print("🛋️ VOCÊ ESTÁ NA SALA")
        print("Onde quer procurar a primeira pista?")
        print("1. Embaixo do sofá")
        print("2. Dentro do vaso de plantas")
        print("3. Na estante de livros")
        
        escolha = input("\n👉 Digite 1, 2 ou 3: ")
        
        if escolha == "1":
            print("\n❌ Nada de chave. Só achei uma prova antiga da FUVEST cheia de pó.")
            time.sleep(3)
        elif escolha == "2":
            print("\n❌ Não está aqui. Só tem terra.")
            time.sleep(3)
        elif escolha == "3":
            print("\n✅ BINGO! No meio dos livros de Física e Matemática, achei um bilhete!")
            print("📝 O bilhete diz: 'A chave não está aqui. Procure onde a comida é feita.'")
            achou_sala = True
            input("\nPressione ENTER para ir para a Cozinha...")
        else:
            print("\n⚠️ Opção inválida. Tente novamente.")
            time.sleep(2)

    # ================= CÔMODO 2: COZINHA =================
    achou_cozinha = False
    while not achou_cozinha:
        limpar_tela()
        print("🍳 VOCÊ ESTÁ NA COZINHA")
        print("O bilhete mandou vir para cá. Onde você procura?")
        print("1. Na geladeira")
        print("2. Na gaveta de talheres")
        print("3. Dentro do micro-ondas")
        
        escolha = input("\n👉 Digite 1, 2 ou 3: ")
        
        if escolha == "1":
            print("\n❌ Nada aqui, apenas uma garrafa de água vazia.")
            time.sleep(3)
        elif escolha == "2":
            print("\n✅ BINGO! Achei um guardanapo amassado no fundo da gaveta.")
            print("📝 Está escrito: 'Estou com muito sono, fui deitar.'")
            achou_cozinha = True
            input("\nPressione ENTER para ir para o Quarto...")
        elif escolha == "3":
            print("\n❌ Não está aqui. Só cheiro de pipoca velha.")
            time.sleep(3)
        else:
            print("\n⚠️ Opção inválida. Tente novamente.")
            time.sleep(2)

    # ================= CÔMODO 3: QUARTO =================
    achou_quarto = False
    while not achou_quarto:
        limpar_tela()
        print("🛏️ VOCÊ ESTÁ NO QUARTO")
        print("Onde está a próxima pista?")
        print("1. Na escrivaninha de estudos")
        print("2. No guarda-roupa")
        print("3. Embaixo do travesseiro")
        
        escolha = input("\n👉 Digite 1, 2 ou 3: ")
        
        if escolha == "1":
            print("\n❌ Nada de chave. Só meu caderno de Química aberto.")
            time.sleep(3)
        elif escolha == "2":
            print("\n❌ Um monte de roupas bagunçadas, mas nenhuma chave.")
            time.sleep(3)
        elif escolha == "3":
            print("\n✅ BINGO! Achei um post-it grudado no lençol.")
            print("📝 Está escrito: 'Fui me lavar, a chave caiu por lá.'")
            achou_quarto = True
            input("\nPressione ENTER para entrar no Banheiro da Suíte...")
        else:
            print("\n⚠️ Opção inválida. Tente novamente.")
            time.sleep(2)

    # ================= CÔMODO 4: BANHEIRO =================
    achou_banheiro = False
    while not achou_banheiro:
        limpar_tela()
        print("🚿 VOCÊ ESTÁ NO BANHEIRO (ÚLTIMO CÔMODO!)")
        print("A chave tem que estar aqui! Onde você procura?")
        print("1. Na pia")
        print("2. Dentro do box do chuveiro")
        print("3. Ao lado da privada")
        
        escolha = input("\n👉 Digite 1, 2 ou 3: ")
        
        if escolha == "1":
            print("\n❌ Apenas pasta de dente e escovas. Continue procurando!")
            time.sleep(3)
        elif escolha == "2":
            print("\n❌ O chão está molhado, mas a chave não está aqui.")
            time.sleep(3)
        elif escolha == "3":
            print("\n🎉 VOCÊ ACHOU! A chave estava caída ao lado da privada!")
            achou_banheiro = True
            time.sleep(2)
        else:
            print("\n⚠️ Opção inválida. Tente novamente.")
            time.sleep(2)

    # ================= FINAL =================
    limpar_tela()
    print("=============================================")
    print(" 🏆 PARABÉNS! VOCÊ ESCAPOU DO APARTAMENTO! 🏆")
    print("=============================================")
    print("Você destrancou a porta e conseguiu sair a tempo.")
    print("Obrigado por jogar!")

if __name__ == "__main__":
    jogar_escape_room()