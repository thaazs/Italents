import random

def jogar_dado():
    return random.randint(1, 6)

def criar_jogador(nome):
    return {"nome": nome, "resultados": [], "vitorias": 0}

def main():
    num_rodadas = int(input("Quantas rodadas você deseja jogar? "))
    num_jogadores = int(input("Quantos jogadores vão participar do jogo? "))

    jogadores = []
    
    for i in range(num_jogadores):
        nome = input(f"Digite o nome do jogador {i + 1}: ")
        jogadores.append(criar_jogador(nome))

    for rodada in range(num_rodadas):
        print(f"\nRodada {rodada + 1}:")

        resultados_rodada = [jogar_dado() for _ in range(num_jogadores)]
        max_resultado = max(resultados_rodada)

        for i, jogador in enumerate(jogadores):
            jogador["resultados"].append(resultados_rodada[i])
            print(f"{jogador['nome']} tirou {resultados_rodada[i]}")

            if resultados_rodada[i] == max_resultado:
                jogador["vitorias"] += 1

    print("\nResultados finais:\n")
    for jogador in jogadores:
        print(f"{jogador['nome']} obteve {jogador['vitorias']} vitória(s).")

    jogadores.sort(key=lambda x: x['vitorias'], reverse=True)

    empate = len(jogadores) > 1 and jogadores[0]['vitorias'] == jogadores[1]['vitorias']
    if empate:
        print("\nHouve um empate!")
    else:
        print(f"\nO grande campeão é {jogadores[0]['nome']}!")

if __name__ == "__main__":
    main()
