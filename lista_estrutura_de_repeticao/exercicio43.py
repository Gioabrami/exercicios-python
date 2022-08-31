#43. O cardápio de uma lanchonete é o seguinte:
#   Especificação | Código | Preço
#   Cachorro Quente | 100 | R$ 1,20
#   Bauru Simples | 101 | R$ 1,30
#   Bauru com ovo | 102 | R$ 1,50
#   Hambúrguer | 103 | R$ 1,20
#   Cheeseburguer | 104 | R$ 1,30
#   Refrigerante | 105 | R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

lista_produtos = {100: ('Cachorro Quenta', 1.20), 101: ('Bauru Simples', 1.30), 102: ('Bauru com Ovo', 1.50), 103: ('Hambúrgues', 1.20), 104: ('Cheeseburguer', 1.30), 105: ('Refrigerante', 1.00)}
pedido = {}

continuar = True
while continuar:
    produto = int (input ('Qual o código do produto? '))
    quantidade = int (input ('Qual a quantidade? '))
    pedido [produto] = lista_produtos [produto] [0], quantidade

    continuar = input ('Mais algum produto (S/N)? ').upper ()
    if continuar == 'N':
        break

print (' Produto         | Quantidade | Valor')

total = 0
for codigo, outros in pedido.items ():
     valor = outros [1] * lista_produtos [codigo] [1]
     total += valor
     print (' {:<15} |    {:<4}    | R$ {:.2f}'.format (outros [0], outros [1], valor))

print (' Total Geral =                | R$ {:.2f}'.format (total))
