#23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido 
# pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para 
# encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes 
# (divisões) executados.

maximo = int (input ('Digite o número limite para os testes: '))
lista_primos = [2]
divisoes = 0

def divisivel_pelos_primos (numero_para_testar, lista_primos, divisoes):
    for num in lista_primos:
        divisoes += 1
        if numero_para_testar % num == 0:
            nao_primo = True
            break
        else:
            nao_primo = False
    
    return nao_primo, divisoes

def teste_divisoes_restantes (numero_para_testar, lista_primos, divisoes):
    for num in range (lista_primos [-1], (numero_para_testar | 2) + 1):
        divisoes += 1
        if numero_para_testar % num == 0:
            primo = False
            continue
        else:
            primo = True
            break
        
    return primo, divisoes
    

for num in range (2, maximo + 1):   #pega cada numero que vai ser testado

    teste_nao_primo, divisoes = divisivel_pelos_primos (num, lista_primos, divisoes)

    if teste_nao_primo:
        continue

    else:
        teste_primo, divisoes = teste_divisoes_restantes (num, lista_primos, divisoes)

        if teste_primo:
            lista_primos.append (num)

        else:
            continue

print (f'Primos = {lista_primos}\nTotal de divisões = {divisoes}')
