#7. Faça um Programa que leia um vetor de 5 números inteiros, 
# mostre a soma, a multiplicação e os números.

vetor = input ('Digite 5 números inteiros: ').split ()
numeros = [int (n) for n in vetor]
multiplicacao = 1

for n in numeros:
    multiplicacao *= n

print (f'A soma dos números é: {sum (numeros)} \nA multiplicação dos números é: {multiplicacao} \nOs números são: {numeros}')
