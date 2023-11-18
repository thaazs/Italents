alunos = {}

for _ in range(5):
    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a média do aluno: "))
    
    if media >= 7:
        situacao = "Aprovado"
    elif 5 <= media < 7:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    
    alunos[nome] = {"Média": media, "Situação": situacao}

print("\nInformações dos alunos:")
for nome, info in alunos.items():
    print(f"{nome}: Média = {info['Média']}, Situação = {info['Situação']}")