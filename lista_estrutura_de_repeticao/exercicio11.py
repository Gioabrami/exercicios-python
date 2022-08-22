#11. Altere o programa anterior para mostrar no final a soma dos números.

import random

validar = False
while not validar:
    num1 = int (input ('Digite o primeiro número: '))
    num2 = int (input ('Digite o segundo número: '))
    if (num2 - num1) < 2:
        print ('Digite números com mais diferença entre eles.')
    else:
        validar = True

print ('Um número inteiro entre os dois escolhidos é {} e a soma entre eles é {}.'.format (random.randrange (num1 + 1, num2), (num1 + num2)))
