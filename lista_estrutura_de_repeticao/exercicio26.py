#26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores = int (input ('Quantos eleitores vão votar? '))
candidatos = {'candidato 1': 0, 'candidato 2': 0, 'candidato 3': 0}

for n in range (0, eleitores):
    validade = False
    while not validade:
        voto = input (f'Candidatos concorrendo: {candidatos.keys ()}\nPara qual candidato vai o seu voto? ').lower ()
        if voto in candidatos:
            candidatos [voto] += 1
            validade = True
        else:
            print ('Candidato inválido, tente novamente.')

print ('Resultado da Eleição:')
for candidato, votos in candidatos.items ():
    print (f'O {candidato} recebeu {votos} votos.')
