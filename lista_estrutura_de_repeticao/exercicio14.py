#14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade 
# de números pares e a quantidade de números impares.

numeros = []

for x in range (1, 11):
    num = int (input (f'Digite o {x}º número: '))
    numeros.append (num)

pares = [n for n in numeros if n % 2 == 0 ]
impares = numeros

for num in pares:
    impares.remove (num)

print (
    f'Dentre os números digitados, temos {len (pares)} números pares:\n {pares}\n',
    f'Dentre os números digitados, temos {len (impares)} números ímpares:\n {impares}'
)
