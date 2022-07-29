#9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int (input ("Digite o primeiro número: "))
num2 = int (input ("Digite o segundo número: "))
num3 = int (input ("Digite o terceiro número: "))

lista = [num1, num2, num3]
lista = sorted(lista, reverse = True)

print ("Os números em ordem decrescente são: {}, {} e {}.".format (lista[0], lista[1], lista[2]))