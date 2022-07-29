#7. Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int (input ("Digite o primeiro número: "))
num2 = int (input ("Digite o segundo número: "))
num3 = int (input ("Digite o terceiro número: "))

lista = [num1, num2, num3]

print ("O maior valor é {}, e o menor valor é {}.".format (max(lista), min(lista)))