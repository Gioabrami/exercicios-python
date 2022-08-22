#21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int (input ('Digite um número: '))
primo = True

for n in range (2, num):
    if num % n == 0:
        primo = False

print (f'O número {num} é primo') if primo else print (f'O número {num} não é primo')
