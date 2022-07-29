#22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

num = int (input ("Digite um número inteiro: "))

if num % 2 == 0:
    print (f"O número {num} é par!")
elif num % 2 == 1:
    print (f"O número {num} é ímpar!")