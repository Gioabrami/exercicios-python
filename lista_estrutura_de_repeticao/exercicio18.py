#18. Faça um programa que, dado um conjunto de N números, 
# determine o menor valor, o maior valor e a soma dos valores.

lista = []
continuar = True

while continuar:
    num = input ('Se deseja parar, digite N\nDigite um número: ')
    try:
        num = int (num)
        lista.append (num)
    except ValueError:
        continuar = False

#print (lista)
print (f'O menor valor da lista é {min (lista)}, o maior valor da lista é {max (lista )} e a soma dos valores da lista é {sum (lista )}.')
