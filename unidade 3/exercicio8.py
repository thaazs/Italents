estoque = {"produto1": 10, "produto2": 20, "produto3": 30}

produto = input("Digite o nome do produto: ").lower()

if produto in estoque:
    quantidade_solicitada = int(input("Digite a quantidade desejada: "))
    
    if quantidade_solicitada <= estoque[produto]:
        estoque[produto] -= quantidade_solicitada
        print(f"\nCompra realizada com sucesso! Você comprou {quantidade_solicitada} unidades do {produto}.")
        print(f"Estoque restante: {estoque}")
    else:
        print("Quantidade indisponível no estoque.")
else:
    print("Produto não disponível.")