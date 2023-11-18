pessoas = []
idades = []

while True:
    pessoa = {}
    pessoa["nome"] = input("Digite o nome da pessoa: ")
    pessoa["sexo"] = input("Digite o sexo biológico da pessoa (M/F): ").upper()
    pessoa["idade"] = int(input("Digite a idade da pessoa: "))
    
    if pessoa["sexo"] not in ['M', 'F']:
        print("Sexo biológico inválido. Digite 'M' para masculino ou 'F' para feminino.")
        continue
    
    pessoas.append(pessoa)
    idades.append(pessoa["idade"])
    
    continuar = input("Deseja cadastrar outra pessoa? (sim/não): ").lower()
    if continuar != "sim":
        break

total_pessoas = len(pessoas)
media_idade = sum(idades) / total_pessoas

mulheres = [pessoa["nome"] for pessoa in pessoas if pessoa["sexo"] == 'F']
acima_media_idade = [pessoa["idade"] for pessoa in pessoas if pessoa["idade"] > media_idade]

print(f"\nTotal de pessoas cadastradas: {total_pessoas}")
print(f"Média de idade das pessoas: {media_idade:.2f}")
print(f"Mulheres cadastradas: {mulheres}")
print(f"Idades acima da média: {acima_media_idade}")