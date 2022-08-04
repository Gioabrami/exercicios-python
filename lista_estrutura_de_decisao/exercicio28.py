#28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o 
# cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo 
# e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
#  tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

carne = int (input ("Qual a carne? (1) Filé Duplo, (2) Alcatra ou (3) Picanha? "))
quilos = float (input ("Quantos quilos de carne? "))
cartao = input ("Possui cartão Tabajara? (S) Sim ou (N) Não? ").upper ()

def preco_final (carne, quilos):
    precos_carnes = [4.9, 5.8, 5.9, 6.8, 6.9, 7.8]

    if carne == 1:
        if quilos < 5:
            preco = precos_carnes [0]
        else:
            preco = precos_carnes [1]

    elif carne == 2:
        if quilos < 5:
            preco = precos_carnes [2]
        else:
            preco = precos_carnes [3]

    elif carne == 3:
        if quilos < 5:
            preco = precos_carnes [4]
        else:
            preco = precos_carnes [5]
    
    return preco

def nome_carne (carne):
    if carne == 1:
        nome = "Filé Duplo"
    elif carne == 2:
        nome = "Alcatra"
    elif carne == 3:
        nome = "Picanha"
    
    return nome

preco = preco_final (carne, quilos)
nome = nome_carne (carne)

if cartao == "S":
    pagamento = "Cartão Tabajara"
    total = round (preco * quilos * 0.95, 2)
    desconto = round (preco * quilos * 0.05, 2)
else:
    pagamento = "Dinheiro"
    total = round(preco * quilos, 2)
    desconto = 0

print (
    "\n***** CUPOM FISCAL *****"
    f"\n{nome} - R$ {preco} /kg"
    f"\nCompra: {quilos} kg"
    f"\nTotal: R$ {(preco * quilos)}"
    f"\nPagamento com {pagamento}"
    f"\nDesconto: R$ {desconto}"
    f"\nValor a pagar R$ {total}"
)
