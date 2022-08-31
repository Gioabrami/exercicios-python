#32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#   Fatorial de: 5
#   5! =  5 . 4 . 3 . 2 . 1 = 120

num = int (input ('Qual o número desejado? '))
total = num
print (f'{num}! = {num} ', end = '')

for n in range (1, num):
    atual = num - n
    total = total * atual
    print (f'. {atual} ', end = '')

print (f'= {total}')
