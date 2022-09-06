#10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 
# elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

lista1 = (input ('Digite 10 elementos: \n')).split ()
lista2 = (input ('Digite outros 10 elementos: \n')).split ()
lista3 = []

for n in range (0, len (lista1)):
    lista3.append (lista1 [n])
    lista3.append (lista2 [n])

print (lista3)
