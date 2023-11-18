respostas_positivas = 0

pergunta1 = input("Você telefonou para a vítima? (s/n): ")
pergunta2 = input("Esteve no local do crime? (s/n): ")
pergunta3 = input("Mora perto da vítima? (s/n): ")
pergunta4 = input("Devia para a vítima? (s/n): ")
pergunta5 = input("Já trabalhou com a vítima? (s/n): ")

if pergunta1.lower() == "s":
    respostas_positivas += 1
if pergunta2.lower() == "s":
    respostas_positivas += 1
if pergunta3.lower() == "s":
    respostas_positivas += 1
if pergunta4.lower() == "s":
    respostas_positivas += 1
if pergunta5.lower() == "s":
    respostas_positivas += 1

if respostas_positivas == 2:
    print("Suspeito")
elif 3 <= respostas_positivas <= 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")
