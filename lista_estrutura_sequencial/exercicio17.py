#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área 
#a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta 
#é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e 
#sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

parede = float(input("Qual a área em metros quadrados que será pintada? "))

tinta = round(parede / 6, 3)

latas = math.ceil (tinta / 18)
galoes = math.ceil (tinta / 3.6)
misturado_latas = math.floor ((tinta * 1.1) / 18)
misturado_galoes = math.ceil(((tinta * 1.1) % 18) / 3.6)

print ("Você necessita de {} latas de tinta. O preço total é de R$ {:.2f}.".format (latas, latas * 80))
print ("Você necessita de {} galões de tinta. O preço total é de R$ {:.2f}.".format (galoes, galoes * 25))
print ("Para evitar desperdícios, a melhor opção de compra são {} latas de tinta e {} galões de tinta. O preço total será de R$ {:.2f}."
.format (misturado_latas, misturado_galoes, (misturado_latas * 80 + misturado_galoes * 25)))