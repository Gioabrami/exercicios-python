#5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no 
# vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = []
pares = []
impares = []

for n in range (1, 21):
    num = int (input (f'Qual o {n}º número? '))
    numeros.append (num)
    if num % 2 == 0:
        pares.append (num)
    else:
        impares.append (num)

print (numeros)
print (pares)
print (impares)
