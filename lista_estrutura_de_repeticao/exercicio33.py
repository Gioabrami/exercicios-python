#33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia
# as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas 
# informadas, bem como a média das temperaturas.

temperaturas = []
continuar = True
while continuar:
    temp = input ('Se deseja finalizar, digite N.\nQual a temperatura? ')
    try:
        temp = float (temp)
        temperaturas.append (temp)
    except ValueError:
        continuar = False

print (
    f'A máxima foi de {max (temperaturas):.2f}°C',
    f'\nA mínima foi de {min (temperaturas):.2f}°C',
    f'\nA média das temperaturas foi de {sum (temperaturas) / len (temperaturas):.2f}°C'
    )
