#17. Faça um Programa que peça um número correspondente a um determinado ano e 
# em seguida informe se este ano é ou não bissexto.

ano = int (input ("Qual o ano para conferir? "))

if (ano % 4) == 0:
    print (f"O ano {ano} é bissexto.")
else:
    print (f"O ano {ano} não é bissexto.")