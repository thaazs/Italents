import random

quantidade_jogos = int(input("Digite a quantidade de jogos a serem gerados: "))

for _ in range(quantidade_jogos):
    palpite = random.sample(range(1, 61), 6)
    print("Palpite:", sorted(palpite))