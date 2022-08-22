#13. Faça um programa que peça dois números, base e expoente, calcule e mostre o 
# primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

num = int (input ('Digite um número para a base: '))
exp = int (input ('Digite um número para o expoente: '))
total = num

for n in range (1, exp):
    total = total * num

print (f'O número {num} elevado a {exp} é igual a {total}.')
