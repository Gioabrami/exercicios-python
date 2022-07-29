#3. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input ("Selecione um sexo (F) Feminino e (M) Masculino: ")
sexo = sexo.upper()

if sexo == "F":
    print ("Sexo Feminino.")
elif sexo == "M":
    print ("Sexo Masculino.")
else:
    print ("Sexo Inválido.")