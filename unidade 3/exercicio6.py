clientes = {"fulano": 18, "fulana": 16, "ciclano": 20, "ciclanA": 15, "cicLano": 22}
maiores = 0
menores = 0

for nome, idade in clientes.items():
    if idade >= 18:
        print(f"{nome} é maior de idade.")
        maiores += 1
    else:
        print(f"{nome} é menor de idade.")
        menores += 1

print(f"\nQuantidade de clientes maiores de idade: {maiores}")
print(f"Quantidade de clientes menores de idade: {menores}")