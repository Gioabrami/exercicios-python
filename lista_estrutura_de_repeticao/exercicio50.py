#50. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

serie = []
divisor = 1

termos = int (input ('Quantos termos? '))
for n in range (1, termos + 1):
    serie.append (1 / divisor)
    divisor += 1

print (round (sum (serie), 2))
