#44. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
# Os códigos utilizados são:
#   1 , 2, 3, 4  - Votos para os respectivos candidatos 
#   (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#   5 - Voto Nulo
#   6 - Voto em Branco
# Faça um programa que calcule e mostre:
#   O total de votos para cada candidato;
#   O total de votos nulos;
#   O total de votos em branco;
#   A percentagem de votos nulos sobre o total de votos;
#   A percentagem de votos em branco sobre o total de votos.
# Para finalizar o conjunto de votos tem-se o valor zero.

candidatos = ['João', 'José', 'Maria', 'Fernanda']
votos = []

print (' 1 - João\n 2 - José\n 3 - Maria\n 4 - Fernanda', '\n 5 - Voto Nulo\n 6 - Voto em Branco')

while True:
    voto = int (input ('Qual o seu voto? '))
    if voto in [1, 2, 3, 4, 5, 6]:
        print ('Salvando...')
        votos.append (voto)
    
    elif voto == 0:
        break

    else:
        print ('Voto inválido!')
        continue

codigo = 1
for candidato in candidatos:
    print (f'O Candidato(a) {candidato} ganhou {votos.count (codigo)}')
    codigo += 1

print (f'Houveram {votos.count (5)} Votos Nulos\nHouveram {votos.count (6)} Votos em Branco')
porcent_nulos = round (votos.count (5) / len (votos) * 100, 2)
porcent_brancos = round (votos.count (6) / len (votos) * 100, 2)
print (f'Votos Nulos foram {porcent_nulos}%\nVotos em Branco foram {porcent_brancos}%')
