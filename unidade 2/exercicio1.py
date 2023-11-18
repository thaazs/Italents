# Taxas de câmbio (valores do dia 18/11/2023)
taxa_dolar = 4.91
taxa_euro = 5.364
taxa_libra = 6.11
taxa_dolar_canadense = 3.57
taxa_peso_argentino = 0.014
taxa_peso_chileno = 0.0055

valor_em_reais = float(input("Digite o valor em reais (R$): "))

valor_em_dolar = valor_em_reais / taxa_dolar
valor_em_euro = valor_em_reais / taxa_euro
valor_em_libra = valor_em_reais / taxa_libra
valor_em_dolar_canadense = valor_em_reais / taxa_dolar_canadense
valor_em_peso_argentino = valor_em_reais / taxa_peso_argentino
valor_em_peso_chileno = valor_em_reais / taxa_peso_chileno

print(f"USD {valor_em_dolar:.2f}")
print(f"EUR {valor_em_euro:.2f}")
print(f"GBP {valor_em_libra:.2f}")
print(f"C$ {valor_em_dolar_canadense:.2f}")
print(f"ARS {valor_em_peso_argentino:.2f}")
print(f"CLP {valor_em_peso_chileno:.2f}")
