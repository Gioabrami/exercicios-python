#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha 
# igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input ('Qual o nome do usuário? ')
valido = True

while valido:
    senha = input ('Qual a senha? ')

    if senha == nome:
        print ('Digite uma nova senha.')

    else:
        print ('Senha válida.')
        break
