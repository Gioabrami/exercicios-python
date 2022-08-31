#28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e 
# o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs 
# e o valor para em cada um.

colecao = int (input ('Quantos CDs você possui no total? '))
preco_cds = []

preco_cds = [float (input (f'Qual o preço do {(cd + 1)}º CD? ')) for cd in range (0, colecao)]

print ('O total investido na coleção foi R$ {:.2f}, uma média de R$ {:.2f} por CD.'.format (sum (preco_cds), (sum (preco_cds) / len (preco_cds))))
