#27. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade 
# de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = int (input ('Quantas turmas são no total? '))
alunos_por_turma = []

for n in range (0, turmas):
    validar = False
    while not validar:
        alunos = int (input ('Quantos alunos tem nessa turma? '))
        if alunos > 40:
            print ('Número inválido de alunos. A turma não deve ter mais de 40 alunos.')
        else:
            validar = True
    
    alunos_por_turma.append (alunos)

print (alunos_por_turma)
print (f'A número médio de alunos por turma é de {(sum (alunos_por_turma) / len (alunos_por_turma))}.')
