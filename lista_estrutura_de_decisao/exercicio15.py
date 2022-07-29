#15. Faça um Programa que peça os 3 lados de um triângulo. 
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#   Dicas:
#   Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#   Triângulo Equilátero: três lados iguais;
#   Triângulo Isósceles: quaisquer dois lados iguais;
#   Triângulo Escaleno: três lados diferentes;

lado1 = float (input ("Qual a medida do primeiro lado? "))
lado2 = float (input ("Qual a medida do segundo lado? "))
lado3 = float (input ("Qual a medida do terceiro lado? "))

def teste_triangulo (x, y, z):
    lados = [x, y, z]
    lados = sorted(lados)

    if (lados[0] + lados[1]) > lados[2]:
        return True
    else:
        return False

if teste_triangulo(lado1, lado2, lado3):

    if lado1 == lado2 and lado1 == lado3:
        print ("Essa figura é um Triângulo Equilátero!")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print ("Essa figura é um Triângulo Escaleno!")
    elif (lado1 == lado2 and lado1 != lado3) or (lado1 != lado2 and lado1 == lado3) or (lado2 == lado3 and lado2 != lado1):
        print ("Esse é um Triângulo Isósceles!")
        
else:
    print ("Essa figura não é um triângulo!")