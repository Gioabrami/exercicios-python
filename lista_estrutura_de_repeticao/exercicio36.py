#36. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo 
# usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e 
# final devem ser informados também pelo usuário, conforme exemplo abaixo:
#   Montar a tabuada de: 5 
#   Começar por: 4
#   Terminar em: 7
# 
#   Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#   5 X 4 = 20
#   5 X 5 = 25 
#   5 X 6 = 30
#   5 X 7 = 35
#   Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

numero = int (input ('De que número você quer a tabuada? '))

verificar = False
while not verificar:
    inicio_tabuada = int (input ('De que número devo iniciar a tabuada? '))
    final_tabuada =  int (input ('E até que número vou fazer a tabuada? '))
    if inicio_tabuada > final_tabuada:
        print ('O início deve ter um valor menor que o final. Tente novamente.')
    else:
        verificar = True

print (f'Vou montar a tabuada do {numero} começando em {inicio_tabuada} e terminando em {final_tabuada}:')
for n in range (inicio_tabuada, final_tabuada + 1):
    print (f'{numero} X {n} = {numero * n}')
