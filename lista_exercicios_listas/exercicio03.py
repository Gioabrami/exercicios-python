#3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for n in range (1, 5):
    nota = float (input (f'Qual a {n}ª nota? '))
    notas.append (nota)

media = sum (notas) / len (notas)

print (
    f'As notas foram {notas}'
    f'\nA médias das notas foi de {media}'
)