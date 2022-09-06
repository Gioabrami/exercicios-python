#11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

lista1 = (input ('Digite 10 elementos: \n')).split ()
lista2 = (input ('Digite outros 10 elementos: \n')).split ()
lista3 = (input ('Digite mais 10 elementos: \n')).split ()
lista4 = []

for n in range (0, len (lista1)):
    lista4.append (lista1 [n])
    lista4.append (lista2 [n])
    lista4.append (lista3 [n])

print (lista4)
