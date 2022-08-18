lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista.append (11)   # adiciona valor no final da lista (só um valor de cada vez)
lista.remove (4)    # remove valor da lista quando encontrado
lista.append (6)   
lista.remove (6)   # remove o primeiro valor encontrado
lista.insert (2, 50)    # adiciona o valor 50 na posição 2
lista.extend ([20, 21, 22, 23])   #adiciona multiplos valores no final da lista
lista.clear ()      #limpa a lista toda

lista = [18, 21, 25, 26, 31, 40]

len (lista)     # tamanho da lista - 6
lista [2]       # valaor na posição 2 - 25

if 18 in lista:
    lista.remove(18)

idades = [15, 87, 65, 56, 32, 49, 37]

# i in range ( len (idades)):
#     print (i, idades [i])

for indice, idade in enumerate (idades):
    print (indice, idade)

print (sorted (idades)) #ordena e gera uma lista

idades.sort () #ordena na lista mesmo
    