#41. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
# valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#   Os juros e a quantidade de parcelas seguem a tabela abaixo:
#   
#   Quantidade de Parcelas | % de Juros sobre o valor inicial da dívida
#   1  | 0
#   3  | 10
#   6  | 15
#   9  | 20
#   12 | 25
# 
#   Exemplo de saída do programa:
# 
#   Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela
#   R$ 1.000,00 |  0  | 1 | R$  1.000,00
#   R$ 1.100,00 | 100 | 3 | R$    366,00
#   R$ 1.150,00 | 150 | 6 | R$    191,67

divida = float (input ('Qual o valor da dívida? '))
parcelas = [ 3, 6, 9, 12]
taxa = 1.1
   
print ('Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela\nR$ {:<12.2f} | R$ {:<12.2f} | {:<22} | R$ {:.2f}'.format (divida, 0, 1, divida))

for plano in parcelas:
    divida_nova = round (divida * taxa, 2)
    valor_taxa = round (divida * (taxa - 1), 2)
    print (
    '\nR$ {:<12.2f} | R$ {:<12.2f} | {:<22} | R$ {:.2f}'.format (divida_nova, valor_taxa, plano, (divida_nova / plano)))
    taxa += 0.05
