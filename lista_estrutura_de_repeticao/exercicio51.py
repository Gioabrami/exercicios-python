#51. Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
#   Imprima no final a soma da série.

serie = [1]
divisor = 3

termos = int (input ('Quantos termos? '))
print ('S = 1/1 ', end = '')
for n in range (2, termos + 1):
    serie.append (n / divisor)
    print (f'+ {n}/{divisor} ', end = '')
    divisor += 2
    
print (f'\n{round (sum (serie), 2)}')
