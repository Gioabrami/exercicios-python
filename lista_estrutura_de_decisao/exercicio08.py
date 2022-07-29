#8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

preco1 = int (input ("Qual o preço do primeiro produto? "))
preco2 = int (input ("Qual o preço do segundo produto? "))
preco3 = int (input ("Qual o preço do terceiro produto? "))

lista = {preco1: "Produto 1", preco2: "Produto 2", preco3: "Produto 3"}

print ("Você deve comprar o {}.".format (lista[min(lista)]))