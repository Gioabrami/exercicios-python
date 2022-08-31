#24. Faça um programa que calcule o mostre a média aritmética de N notas.

notas = []
continuar = True

while continuar:
    num = input ('Se deseja parar, digite N\nDigite uma nota: ')
    try:
        num = float (num)
        notas.append (num)
    except ValueError:
        continuar = False

print (notas)
print ('A média aritmética das notas apresentadas é {:.2f}.'.format (sum (notas) / len (notas)))
