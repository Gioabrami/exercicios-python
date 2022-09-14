#22. Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a 
# intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar 
# todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para 
# verificar o que se pode aproveitar deles.
#   Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá 
# receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o 
# tipo de defeito:
#   necessita da esfera;
#   necessita de limpeza
#   necessita troca do cabo ou conector
#   quebrado ou inutilizado
# Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte 
# relatório:

#   Quantidade de mouses: 100
#       Situação | Quantidade | Percentual
#       1- necessita da esfera | 40 | 40%
#       2- necessita de limpeza | 30 | 30%
#       3- necessita troca do cabo ou conector | 15 | 15%
#       4- quebrado ou inutilizado | 15 | 15%

situacao = ['necessita de esfera', 'necessita de limpeza', 'necessita troca do cabo ou conector', 'quebrado ou inutilizado']
resumo_avaliacao = {1:0, 2:0, 3:0, 4:0}

print ('Tipos de defeitos:\n 1- Necessita de esfera\n2- Necessita de limpeza\n3- Necessita troca do cabo ou conector\n4- Quebrado ou Inutilizado\n')
while True:
    avaliacao = int (input ('Qual a avaliação do mouse (0=fim)? '))
    if avaliacao == 0:
        break
    else:
        resumo_avaliacao [avaliacao] += 1

print (
    f'Quantidade de mouses: {sum (resumo_avaliacao.values ())}\n'
    '               Situação                | Quantidade | Percentual'
    )

for problema, quantidade in resumo_avaliacao.items ():
    percentual = quantidade / sum (resumo_avaliacao.values ()) * 100
    print (f' {situacao [problema - 1]:<37} | {quantidade:^10} | {percentual:.2f}%')
