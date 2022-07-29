#13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#   utilizando as seguintes fórmulas:
    #Para homens: (72.7*h) - 58
    #Para mulheres: (62.1*h) - 44.7

altura = float(input("Qual a sua altura? "))
sexo = input("Você é homem (H) ou mulher (M)? ").upper()

if sexo == "H":
    peso = round((72.7 * altura) - 58, 2)
else:
    peso = round((62.1 * altura) - 44.7, 2)

print ("Seu peso ideal é {} kg.".format (peso))