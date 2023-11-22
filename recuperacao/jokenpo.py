import random

def jogar():
    print("Bem-vindo ao jogo de pedra, papel e tesoura!")
    rodadas = int(input("Quantas rodadas você deseja jogar? "))
    vitorias_usuario = 0
    vitorias_computador = 0

    for rodada in range(1, rodadas + 1):
        print(f"\nRodada {rodada}:")
        print("Escolha uma opção:")
        print("1. Pedra")
        print("2. Papel")
        print("3. Tesoura")
        escolha_usuario = None
        
        while escolha_usuario not in [1, 2, 3]:
            escolha_usuario = int(input("Digite o número da sua escolha: "))
        
            if escolha_usuario not in [1, 2, 3]:
                print("Escolha inválida. Por favor, tente novamente.")
        
        opcoes = ["Pedra", "Papel", "Tesoura"]
        escolha_computador = random.randint(1, 3)
        
        print(f"Você escolheu: {opcoes[escolha_usuario-1]}")
        print(f"O computador escolheu: {opcoes[escolha_computador-1]}")
        
        resultado = (escolha_usuario - escolha_computador) % 3
        
        if resultado == 0:
            print("Empate!")
        elif resultado == 1:
            print("Você ganhou esta rodada!")
            vitorias_usuario += 1
        else:
            print("O computador ganhou esta rodada!")
            vitorias_computador += 1

    print("\n--- Resultado Final ---")
    print(f"Você ganhou {vitorias_usuario} rodada(s).")
    print(f"O computador ganhou {vitorias_computador} rodada(s).")

    if vitorias_usuario > vitorias_computador:
        print("Parabéns! Você é o grande campeão!")
    elif vitorias_usuario < vitorias_computador:
        print("O computador é o grande campeão!")
    else:
        print("Empate!")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() == "s":
        jogar()

jogar()