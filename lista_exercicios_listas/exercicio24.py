#24. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados 
# em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de 
# contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
import random

lancamentos = int (input ('Quantas vezes quer jogar o dado? '))
resultados = []

for n in range (0, lancamentos):
    resultados.append (random.randrange (1, 7))

for n in range (1, 7):
    print (f'O numero {n} saiu {resultados.count (n)} vezes!')
