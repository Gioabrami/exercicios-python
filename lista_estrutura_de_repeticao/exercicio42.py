#42. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos 
# deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados 
# deverá terminar quando for lido um número negativo.

numeros = []

continuar = True
while continuar:
    num = int (input ('Qual o número? '))
    if num >= 0:
        numeros.append (num)
    else:
        break

continuar = True
contagem = 0
inicial = 1
final = 26
while continuar:
    for n in range (inicial, final):
        contagem += numeros.count (n)

    if inicial == 1:
        contagem += numeros.count (0)
        print ('Existem {} números entre 0 e {}.'.format (contagem, final - 1))
    else:
        print ('Existem {} números entre {} e {}.'.format (contagem, inicial, final - 1))

    contagem = 0
    inicial += 25
    final += 25

    if final > 101:
        break
