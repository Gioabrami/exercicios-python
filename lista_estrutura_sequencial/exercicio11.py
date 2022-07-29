#11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    #o produto do dobro do primeiro com metade do segundo .
    #a soma do triplo do primeiro com o terceiro.
    #o terceiro elevado ao cubo.

num1 = int(input("Informe o primeiro número inteiro: "))
num2 = int(input("Informe o segundo número inteiro: "))
num3 = float(input("Informe o número real: "))

resp1 = (2* num1) * (num2/ 2)
resp2 = 3* num1 + num3
resp3 = round(num3**3, 3)

print ("O produto do dobro de {} com a metade de {} é {}.".format (num1, num2, resp1))
print ("A soma do triplo de {} com {} é {}.".format (num1, num3, resp2))
print ("{} elevado ao cubo é {}.".format (num3, resp3))