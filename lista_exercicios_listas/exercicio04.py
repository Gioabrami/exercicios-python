#4. Faça um Programa que leia um vetor de 10 caracteres, e diga 
# quantas consoantes foram lidas. Imprima as consoantes.

palavra = input ('Digite 10 caracteres:\n')
vogais = {'a':'', 'e':'', 'i':'', 'o':'', 'u':''}

final = palavra.translate ( str.maketrans (vogais))
print (final)
