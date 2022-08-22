#8. Faça um programa que leia 5 números e informe a soma e a média dos números.

num1 = int (input ('Digite o primeiro número: '))
num2 = int (input ('Digite o segundo número: '))
num3 = int (input ('Digite o terceiro número: '))
num4 = int (input ('Digite o quarto número: '))
num5 = int (input ('Digite o quinto número: '))

lista = [num1, num2, num3, num4, num5]
soma = sum (lista)

print ('A soma dos números é {} e a média é {}.'.format (soma, (soma / len (lista) )))
