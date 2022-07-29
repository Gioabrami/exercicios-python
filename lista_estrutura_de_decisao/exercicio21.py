#21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor 
# do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#   Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#   Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = int (input ("Qual o valor do saque? "))

def contagem_cedulas (saque):

    texto = []
    notas_100 = (saque // 100)
    notas_50  = ((saque % 100) // 50)
    notas_10  = ((saque % 50) // 10)
    notas_5   = ((saque % 10) // 5)
    notas_1   = ((saque % 5) // 1)

    if notas_100 == 1:
        texto.append ("uma nota de 100")
    elif notas_100 == 2:
        texto.append ("duas notas de 100")
    elif notas_100 == 3:
        texto.append ("três notas de 100")
    elif notas_100 == 4:
        texto.append ("quatro notas de 100")
    elif notas_100 == 5:
        texto.append ("cinco notas de 100")
    elif notas_100 == 6:
        texto.append ("seis notas de 100")
    
    if notas_50 == 1:
        texto.append ("uma nota de 50")
    
    if notas_10 == 1:
        texto.append ("uma nota de 10")
    elif notas_10 == 2:
        texto.append ("duas notas de 10")
    elif notas_10 == 3:
        texto.append ("três notas de 10")
    elif notas_10 == 4:
        texto.append ("quatro notas de 10")
    
    if notas_5 == 1:
        texto.append ("uma nota de 5")
    
    if notas_1 == 1:
        texto.append ("uma nota de 1")
    elif notas_1 == 2:
        texto.append ("duas notas de 1")
    elif notas_1 == 3:
        texto.append ("três notas de 1")
    elif notas_1 == 4:
        texto.append ("quatro notas de 1")

    return texto

def gera_texto (saque):

    print ("")
    texto = []
    texto = contagem_cedulas (saque)

    if len(texto) == 1:
        print (f"Para sacar a quantia de {saque} reais, o programa fornece",
            f"{texto[-1]}.")

    elif len(texto) == 2:
        print (f"Para sacar a quantia de {saque} reais, o programa fornece",
        f"{texto[-2]} e {texto[-1]}")

    elif len(texto) == 3:
        print (f"Para sacar a quantia de {saque} reais, o programa fornece",
        f"{texto[-3]}, {texto[-2]} e {texto[-1]}")

    elif len(texto) == 4:
        print (f"Para sacar a quantia de {saque} reais, o programa fornece",
        f"{texto[-4]}, {texto[-3]}, {texto[-2]} e {texto[-1]}")

    elif len(texto) == 5:
        print (f"Para sacar a quantia de {saque} reais, o programa fornece",
        f"{texto[-5]}, {texto[-4]}, {texto[-3]}, {texto[-2]} e {texto[-1]}")
    
    print ("")

if saque < 10 or saque > 600:
    print ("Valor inválido. Saques permitidos entre R$ 10.00 e R$ 600.00")
else:
    texto = gera_texto (saque)