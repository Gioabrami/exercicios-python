#17. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do 
# atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba 
# o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos 
# e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. 
# A saída do programa deve ser conforme o exemplo abaixo
#   Atleta: Rodrigo Curvêllo
#       Primeiro Salto: 6.5 m
#       Segundo Salto: 6.1 m
#       Terceiro Salto: 6.2 m
#       Quarto Salto: 5.4 m
#       Quinto Salto: 5.3 m
#   Resultado final:
#       Atleta: Rodrigo Curvêllo
#       Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#       Média dos saltos: 5.9 m

def prova_de_salto (nome):
    saltos = []

    for n in range (1, 6):
        salto = float (input (f'Qual foi a medida do {n}º salto? '))
        saltos.append (salto)

    print (f'\nAtleta: {nome}')
    for n in range (0, 5):
        print (f'{n + 1}º Salto: {saltos [n]} m')
    
    print (f'\nResultado Final:\nAtleta: {nome}')
    print (f'Saltos: {saltos [0]}', end = '')

    for n in range (1, 5):
        print (f' - {saltos [n]}', end = '')

    print (f'\nMédia dos saltos: {sum (saltos) / len (saltos):.2f} m')


while True:
    nome = input ('Qual o nome do atleta? ').title ()
    if len (nome) > 0:
        prova_de_salto (nome)
    else:
        break