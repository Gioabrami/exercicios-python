#47. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota 
# são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que 
# receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e 
# depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e 
# depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo 
# de saída do programa deve ser conforme o exemplo abaixo:
#   Atleta: Aparecido Parente
#   Nota: 9.9
#   Nota: 7.5
#   Nota: 9.5
#   Nota: 8.5
#   Nota: 9.0
#   Nota: 8.5
#   Nota: 9.7
# 
#   Resultado final:
#   Atleta: Aparecido Parente
#   Melhor nota: 9.9
#   Pior nota: 7.5
#   Média: 9,04

def nota_competicao (nome):
    notas = []

    for n in range (1, 8):
        nota = float (input (f'Qual foi a nota do jurado? '))
        notas.append (nota)

    print (f'\nAtleta: {nome}\n')
    for n in range (0, 5):
        print (f'Nota: {notas [n]}')
    
    print (f'\nResultado Final:\nAtleta: {nome}\nMelhor nota: {max (notas)}\nPior nota: {min (notas)}')
    notas.remove (max (notas))
    notas.remove (min (notas))
    print (f'Média: {sum (notas) / len (notas):.2f}')

while True:
    nome = input ('Qual o nome do atleta? ').title ()
    if len (nome) > 0:
        nota_competicao (nome)
    else:
        break
