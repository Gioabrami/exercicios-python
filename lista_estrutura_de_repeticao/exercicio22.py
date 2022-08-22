#22. Altere o programa de cálculo dos números primos, informando, 
# caso o número não seja primo, por quais número ele é divisível.

num = int (input ('Digite um número: '))
primo = True
divisores = [1]

for n in range (2, num):
    if num % n == 0:
        primo = False
        divisores.append (n)

divisores.append (num)

print (f'O número {num} é primo') if primo else print (f'O número {num} não é primo, ele é divisível por:\n {divisores}')
