#34. Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int (input ('Digite um número: '))
primo = True
for n in range (2, num):
    if num % n == 0:
        primo = False

print (f'O número {num} é primo') if primo else print (f'O número {num} não é primo')
