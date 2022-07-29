#18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um 
#link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo 
#usando este link (em minutos).

import math

arquivo = float(input("Qual o tamanho do arquivo em MB? "))
velocidade = float(input("Qual a velocidade da internet em Mbps? "))

download = math.ceil ((arquivo / velocidade) / 60)

print ("O download terminará em aproximadamente {} minutos.".format (download))