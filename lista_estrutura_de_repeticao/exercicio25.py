#25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar 
# se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a 
# turma é jovem, adulta ou idosa, conforme a média calculada.

idades = []
continuar = True

while continuar:
    num = input ('Se deseja parar, digite N\nDigite um número: ')
    try:
        num = int (num)
        idades.append (num)
    except ValueError:
        continuar = False
    
media = sum (idades) / len (idades)

if media <= 25:
    print ('Essa é uma turma Jovem!')

elif media > 60:
    print ('Essa é uma turma Idosa!')

else:
    print ('Essa pé uma turma Adulta!')
