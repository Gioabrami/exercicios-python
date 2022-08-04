#27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade 
# (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morango = float (input ("Quantos kg de morango você quer? "))
maca = float (input ("Quantos kg de maçã você quer? "))

if morango < 5:
    preco_morango = 2.5
else:
    preco_morango = 2.2

if maca < 5:
    preco_maca = 1.8
else:
    preco_maca = 1.5

total = (morango * preco_morango) + (maca * preco_maca)

if total > 25 or (morango + maca) >= 8:
    total = total * 0.9

print (f"O valor total a pagar é de R$ {total}.")
