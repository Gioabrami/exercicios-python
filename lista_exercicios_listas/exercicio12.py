#12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos 
# com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = [32,89,65,34,22,34,76,12,13,29,28,54,24,12,13,13,15,16]
alturas = [1.87,1.65,1.23,1.89,1.90,1.32,1.56,1.87,1.04,1.21,1.06,1.76,1.58,1.70,2.0,1.40,1.55,1.70]

maiores_que_13 = [index for index, idade in enumerate(idades) if idade >= 13]
alturas_maiores_que_13 = [alturas[index] for index in maiores_que_13]

media = sum (alturas) / len (alturas)

contador = 0

for n in alturas_maiores_que_13:
    if n < media:
        contador += 1

print (f'Existem {contador} alunos com 13 ou mais anos e com altura menor que a média da sala.')
