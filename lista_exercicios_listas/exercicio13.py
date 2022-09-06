#13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
temperaturas_medias = []

for mes in range (0, len (meses)):
    temp = float ( input (f'Qual a temperatura média de {meses [mes]}? '))
    temperaturas_medias.append (temp)

media = sum (temperaturas_medias) / len (temperaturas_medias)

acima_media = [index for index, temp in enumerate (temperaturas_medias) if temp >= media]
meses_acima = [meses [index] for index in acima_media]

print (f'Os meses que tem a temperatura média acima da média anual são:\n{meses_acima}')
