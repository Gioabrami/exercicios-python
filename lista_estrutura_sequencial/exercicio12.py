#12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#   usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Qual a sua altura? "))

peso = round((72.7 * altura) - 58, 2)

print ("O seu peso ideal é {} kg.".format (peso))