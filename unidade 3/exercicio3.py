numeros = []

while True:
    valor = input("Digite um valor (ou 'sair' para encerrar): ")
    
    if valor.lower() == 'sair':
        break
    
    valor = int(valor)
    
    if valor not in numeros:
        numeros.append(valor)

print("Valores únicos digitados em ordem crescente:", sorted(numeros))
