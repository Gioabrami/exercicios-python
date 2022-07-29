#6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input("Qual o raio do círculo em centímetros? "))

area = round((raio**2 * math.pi) /100, 2)

print ("A área do círculo é {} centímetros quadrados".format(area))