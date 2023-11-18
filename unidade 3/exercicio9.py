dados_funcionario = {}

dados_funcionario["nome"] = input("Digite o nome do funcionário: ")
dados_funcionario["ano_nascimento"] = int(input("Digite o ano de nascimento do funcionário: "))
dados_funcionario["ctps"] = int(input("Digite o número da CTPS (0 se não tiver): "))

if dados_funcionario["ctps"] != 0:
    dados_funcionario["ano_contratacao"] = int(input("Digite o ano de contratação: "))
    dados_funcionario["salario"] = float(input("Digite o salário: "))
    
    anos_contribuicao = 35
    idade_aposentadoria = dados_funcionario["ano_contratacao"] + anos_contribuicao - dados_funcionario["ano_nascimento"]
    
    dados_funcionario["idade_aposentadoria"] = idade_aposentadoria

print("\nInformações do funcionário:")
for chave, valor in dados_funcionario.items():
    print(f"{chave.capitalize()}: {valor}")