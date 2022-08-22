#6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

sequencia = list (range (1, 21))
continuar = True

while continuar:
    tipo = input ('Imprimir na (V) Vertical ou (H) Horizontal? ').upper ()
    if tipo == 'V':
        for num in sequencia:
            print (num)
    elif tipo == 'H':
        print (sequencia)
    else:
        print ('Digite um valor válido (V/H)')
    
    novamente = input ('Deseja tentar novamente (S/N)? ').upper ()
    if novamente == 'S':
        continue
    else:
        continuar = False
    