import random

numero_escolhido = random.randint(0, 10)

tentativa = int(input("Tente adivinhar o número entre 0 e 10: "))

if tentativa == numero_escolhido:
    print(f"Parabéns! Você acertou. O número era {numero_escolhido}.")
else:
    print(f"Você errou. O número correto era {numero_escolhido}.")
