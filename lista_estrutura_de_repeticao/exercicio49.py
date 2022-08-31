#49. Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
#   Imprima no final a soma da série.

serie = [1]
dividendo = 2
divisor = 3

termos = int (input ('Quantos termos? '))
print ('S = 1/1 ', end = '')
for n in range (2, termos + 1):
    serie.append (dividendo / divisor)
    print (f'+ {dividendo}/{divisor} ', end = '')
    dividendo += 1
    divisor += 2
    

print (f'\n{round (sum (serie), 2)}')
