#4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input ("Digite uma letra: ").upper()
vogais = ["A", "E", "I", "O", "U"]

if letra in vogais:
    print ("A letra é uma vogal.")
else:
    print ("A letra é uma consoante.")