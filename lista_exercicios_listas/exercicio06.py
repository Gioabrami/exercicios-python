#6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de 
# cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias = []

for aluno in range (1, 11):
    notas_por_aluno = []
    for n in range (1, 5):
        nota = float (input (f'Qual a {n}ª nota do {aluno}º aluno? '))
        notas_por_aluno.append (nota)
    
    media = sum (notas_por_aluno) / len (notas_por_aluno)
    medias.append (media)

aprovados = [x for x in medias if x >= 7]

print (f'Tiveram um total de {len (aprovados)} alunos com a média maior ou igual a 7.0')
