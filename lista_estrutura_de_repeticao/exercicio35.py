#35. Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos 
# números primos existentes entre 1 e um número inteiro informado pelo usuário.

maximo = int (input ('Digite o número: '))
lista_primos = [2]

def divisivel_pelos_primos (numero_para_testar, lista_primos):
    for num in lista_primos:
        if numero_para_testar % num == 0:
            nao_primo = True
            break
        else:
            nao_primo = False
    return nao_primo

def teste_divisoes_restantes (numero_para_testar, lista_primos):
    for num in range (lista_primos [-1], (numero_para_testar | 2) + 1):
        if numero_para_testar % num == 0:
            primo = False
            continue
        else:
            primo = True
            break
    return primo
    

for num in range (2, maximo + 1):   #pega cada numero que vai ser testado

    teste_nao_primo = divisivel_pelos_primos (num, lista_primos)

    if teste_nao_primo:
        continue
    else:
        teste_primo = teste_divisoes_restantes (num, lista_primos)

        if teste_primo:
            lista_primos.append (num)
        else:
            continue

print (f'Há um total de {len (lista_primos)} números primos entre 1 e {maximo}.\nEles são = {lista_primos}')
