#20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial 
# várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

def fatorial():
    validar = False
    while not validar:
        num = int (input ('Qual o número escolhido (entre 0 e 16)? '))
        if num <= 16:
            validar = True
        else:
            print ('O número escolhido é inválido.')

    fatorial = num - 1
    total = num

    for n in range (0, fatorial):
        total = total * fatorial
        fatorial -= 1

    print (f'O retultado da fatorial de {num} é igual a {total}.')

ativo = True

while ativo:
    fatorial ()
    repetir = input ('Deseja tentar novamente (S/N)? ').upper ()
    if repetir == 'N':
        break

print ('Até a próxima!')
