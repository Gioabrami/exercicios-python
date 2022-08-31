#39. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do 
# aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais 
# baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

dicionario_entradas = {}

for n in range (0, 10):
    entrada = input ('Qual o número do aluno e sua altura (cm)? ')
    numero, altura = entrada.split ()
    dicionario_entradas [numero] = float (altura)

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

altura_max, altura_min = maximo_e_minimo (dicionario_entradas)

print (
        f'O aluno mais alto é {altura_max} com {max (dicionario_entradas.values ()):.2f}m,',
        f'e o mais baixo é {altura_min} com {min (dicionario_entradas.values ()):.2f}m'
)
