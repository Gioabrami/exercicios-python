#15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando 
# a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta 
# entrada de dados, faça:
#   Mostre a quantidade de valores que foram lidos;
#   Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#   Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#   Calcule e mostre a soma dos valores;
#   Calcule e mostre a média dos valores;
#   Calcule e mostre a quantidade de valores acima da média calculada;
#   Calcule e mostre a quantidade de valores abaixo de sete;
#   Encerre o programa com uma mensagem;

notas = []

while True:
    nota = float (input ('Qual a nota? '))
    if nota == -1:
        break
    else:
        notas.append (nota)

media = sum (notas) / len (notas)
acima_media = [nota for nota in notas if nota > media]

print (f'Foram obtidos um total de {len (notas)} notas.')

for n in notas:
    print (n, end = ' ')

for n in notas:
    print (n, end = '\n')

print (
    f'A soma das notas foi de {sum (notas)}.\n'
    f'A média das notas foi de {media:.2f}.\n'
    f'Tiveram um total de {len (acima_media)} de notas acima da média.\n'
    f'Tiveram um total de {len (notas) - len (acima_media)} de notas abaixo da média.'
    'Até a próxima!'
)