#19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

lista = []
continuar = True

while continuar:
    num = input ('Se deseja parar, digite N\nDigite um número entre 0 e 1000: ')
    try:
        num = int (num)
        if num < 0 or num > 1000:
            print ('Você digitou um número inválido, tente novamente.')
        else:
            lista.append (num)

    except ValueError:
        continuar = False

print (f'O menor valor da lista é {min (lista)}, o maior valor da lista é {max (lista )} e a soma dos valores da lista é {sum (lista )}.')
