#9. Faça um Programa que leia um vetor A com 10 números inteiros, 
# calcule e mostre a soma dos quadrados dos elementos do vetor.

A = input ('Digite 10 números inteiros: ')
A = A.split ()

resultado = 0
for num in A:
    numero = int (num)
    resultado += numero * numero

print (resultado)
