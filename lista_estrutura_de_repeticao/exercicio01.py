#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor 
# seja inválido e continue pedindo até que o usuário informe um valor válido.

valido = True

while valido:
    nota = int ( input ('Qual a nota? '))

    if nota in range (0, 11):
        print ('Nota Válida')
        break
    
    else:
        print ('Por favr, colocar uma nota válida.')
