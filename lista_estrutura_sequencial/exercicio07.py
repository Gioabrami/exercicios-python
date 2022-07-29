#7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

aresta = float(input("Informe a medida do lado do quadrado: "))
area = round(aresta**2, 2)

print ("A área do quadrado é {}, e o dobro dela é {}".format(area, area*2))