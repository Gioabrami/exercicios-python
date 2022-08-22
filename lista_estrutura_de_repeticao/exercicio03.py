#3. Faça um programa que leia e valide as seguintes informações:
#   Nome: maior que 3 caracteres;
#   Idade: entre 0 e 150;
#   Salário: maior que zero;
#   Sexo: 'f' ou 'm';
#   Estado Civil: 's', 'c', 'v', 'd';

def validar_nome ():
    validar_nome = False
    while not validar_nome:
        nome = input ('Informe seu nome: ')
        if len (nome) < 3:
            print ('Nome inválido') 
        else:
            validar_nome = True
        
def validar_idade ():
    validar_idade = False
    while not validar_idade:
        idade = int (input ('Informe sua idade: '))
        if idade > 0 and idade <= 150:
            validar_idade = True
        else:
            print ('Idade inválida') 

def validar_salario ():
    validar_salario = False
    while not validar_salario:
        salario = float (input ('Informe o seu salário: '))
        if salario > 0:
            validar_salario = True
        else:
            print ('Salário inválido')

def validar_sexo ():
    validar_sexo = False
    while not validar_sexo:
        sexo = input ('(F) Feminino ou (M) Masculino\nInforme seu sexo: ').upper ()
        if sexo == 'F' or sexo == 'M':
            validar_sexo = True
        else:
            print ('Sexo inválido')

def validar_estado_civil ():
    validar_estado_civil = False
    classes = ['S', 'C', 'V', 'D']
    while not validar_estado_civil:
        estado_civil = input ('(S) Solteiro, (C) Casado, (V) Viúvo ou (D) Divorciado\nInforme seu Estado Civil: ').upper ()
        if estado_civil in classes:
            validar_estado_civil = True
        else:
            print ('Estado Civil inválido')


validar_nome ()
validar_idade ()
validar_salario ()
validar_sexo ()
validar_estado_civil ()
print ('Obrigado pela sua atenção!')
