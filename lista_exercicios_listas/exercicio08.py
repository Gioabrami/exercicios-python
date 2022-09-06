#8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu 
# respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

lista_total = []

for n in range (1, 6):
    lista = [input (f'Qual a idade e altura da {n}ª pessoa? ')]
    lista_total.append (lista)

for pessoa in range (len (lista_total), 0, -1):
    idade, altura = (lista_total [pessoa -1] [0]).split ()
    print (f'A {pessoa}ª pessoa tem {idade} anos e mede {altura}m')
