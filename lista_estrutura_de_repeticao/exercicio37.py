#37. Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, 
# a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes 
# da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o 
# usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os 
# códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média 
# das alturas e dos pesos dos clientes

alturas_clientes = {}
pesos_clientes = {}

continuar = True
while continuar:
    codigo = int (input ('Qual o código do cliente? '))
    if codigo == 0:
        continuar = False
    else:
        altura = float (input ('Qual a altura do cliente? '))
        peso = float (input ('Qual o peso do cliente? '))
        alturas_clientes [codigo] = altura
        pesos_clientes [codigo] = peso
        print ('Salvando...\n')

def maximo_e_minimo (dicionario):
    maximo = []
    for codigo, variavel in dicionario.items ():
        if variavel == max (dicionario.values()):
            maximo.append (codigo)
    
    minimo = []
    for codigo, variavel in dicionario.items ():
        if variavel == min (dicionario.values ()):
            minimo.append (codigo)
    
    return maximo, minimo

altura_maxima, altura_minima = maximo_e_minimo (alturas_clientes)
peso_maximo, peso_minimo = maximo_e_minimo (pesos_clientes)

print (
    f'O cliente mais alto é {altura_maxima} com {max (alturas_clientes.values ()):.2f}m, e o mais baixo é {altura_minima} com {min (alturas_clientes.values ()):.2f}m',
    f'\nO cliente mais pesado é {peso_maximo} com {max (pesos_clientes.values ()):.2f}kg, e o mais magro é {peso_minimo} com {min (pesos_clientes.values ()):.2f}kg',
    f'\nA altura média é de {sum (alturas_clientes.values ()) / len (alturas_clientes.values ()):.2f}m e o peso médio é de {sum (pesos_clientes.values ()) / len (pesos_clientes.values ()):.2f}kg'
)
