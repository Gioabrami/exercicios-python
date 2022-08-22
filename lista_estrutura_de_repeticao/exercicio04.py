#4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de 
# crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do 
# país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

pais_A = 80000
pais_B = 200000
taxa_A = 0.03
taxa_B = 0.015
ano = 0

while pais_A < pais_B:
    pais_A += pais_A * taxa_A
    pais_B += pais_B * taxa_B
    ano += 1

    #print (f'A = {pais_A}, B = {pais_B}, ano = {ano}')

print ('Levaram {} anos para as populações se equalizarem.'.format (ano))
