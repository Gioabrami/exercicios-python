#16. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em 
# comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
# Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de 
# $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine 
# quantos vendedores receberam salários nos seguintes intervalos de valores:
#   $200 - $299
#   $300 - $399
#   $400 - $499
#   $500 - $599
#   $600 - $699
#   $700 - $799
#   $800 - $899
#   $900 - $999
#   $1000 em diante
#   Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs 
# aninhados.

valores = ('$200 - $299', '$300 - $399', '$400 - $499', '$500 - $599', '$600 - $699', '$700 - $799', '$800 - $899', '$900 - $999', '$1000 em diante')
ranking = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

while True:
    try:
        venda = int (input ('Quanto de vendas o vendedor vez esta semana? (N para sair)\n'))
    except ValueError:
        break
    
    comissao = venda * .09
    if (comissao // 100) >= 8:
        ranking [8] += 1
    else:
        ranking [comissao // 100] += 1

contador = 0
print ('\nRanking de vendas desta semana:')
for n in valores:
    if ranking [contador] == 0:
        contador += 1
        continue
    print (f'Um total de {ranking [contador]} vendedor(es) receberam entre {n}')
    contador += 1
