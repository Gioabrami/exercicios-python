#19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#   Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#   326 = 3 centenas, 2 dezenas e 6 unidades
#   12 = 1 dezena e 2 unidades 
# Testar com: 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = int (input ("Digite um número até 1000: "))

def teste_plurais(num):

    texto = []
    cent = num //100
    dez = (num // 10) % 10
    uni = (num % 100) % 10

    if cent == 1:
        texto.append (f"{cent} centena")
    elif cent > 1:
        texto.append (f"{cent} centenas")
    
    if dez == 1:
        texto.append (f"{dez} dezena")
    elif dez > 1:
        texto.append (f"{dez} dezenas")

    if uni == 1:
        texto.append (f"{uni} unidade")
    elif uni > 1:
        texto.append (f"{uni} unidades")
    
    return texto

def gera_texto (num):

    numero = str(num)
    texto = []

    texto = teste_plurais (num)

    if len(texto) == 1:
        print (f"{numero} = {texto[-1]}")
    elif len(texto) == 2:
        print (f"{numero} = {texto[-2]} e {texto[-1]}")
    elif len(texto) == 3:
        print (f"{numero} = {texto[-3]}, {texto[-2]} e {texto[-1]}")

lista = [326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

for item in lista:
    gera_texto(item)
