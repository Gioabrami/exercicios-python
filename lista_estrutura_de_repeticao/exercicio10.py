#10. Faça um programa que receba dois números inteiros e gere os números inteiros 
# que estão no intervalo compreendido por eles.

import random

validar = False
while not validar:
    num1 = int (input ('Digite o primeiro número: '))
    num2 = int (input ('Digite o segundo número: '))
    if (num2 - num1) < 2:
        print ('Digite números com mais diferença entre eles.')
    else:
        validar = True

print (random.randrange (num1 + 1, num2))
