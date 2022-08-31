#45. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa 
# deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e 
# assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno 
# utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os 
# alunos terem respondido informar:  
#   Maior e Menor Acerto;
#   Total de Alunos que utilizaram o sistema;
#   A Média das Notas da Turma.
# Gabarito da Prova:
#   01 - A      02 - B      03 - C      04 - D      05 - E
#   06 - E      07 - D      08 - C      09 - B      10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito 
# da prova antes dos alunos usarem o programa.

gabarito = []
for pergunta in range (1,11):
    gabarito_novo = input (f'Qual a resposta da questão {pergunta}? ').upper ()
    gabarito.append (gabarito_novo)

def respostas_por_aluno (gabarito):
    respostas = []
    pergunta = 1
    while pergunta <= len (gabarito):
        resposta = input (f'Qual a resposta para a pergunta {pergunta}? ').upper ()
        respostas.append (resposta)
        pergunta += 1
    
    acertos = 0
    for n in range(0, len (gabarito)):
        if respostas [n] == gabarito [n]:
            acertos += 1
    
    return acertos

print ('\nVamos dar inicio ao teste!')
acertos_turma = []
while True:
    acertos_turma.append (respostas_por_aluno (gabarito))

    continuar = input ('\nMais algum aluno para responder ao teste (S/N)? ').upper ()
    if continuar == 'N':
        break

print (
    f'A maior nota da turma foi de {max (acertos_turma)}\nA menor nota da turma foi de {min (acertos_turma)}',
    f'\nUm total de {len (acertos_turma)} alunos fizeram o teste.\nA média da turma foi de {sum (acertos_turma) / len (acertos_turma)}.'
    )
