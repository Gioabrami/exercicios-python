#9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

temp_fahr = float(input("Qual a temperatura em graus Fahrenheit? "))

temp_cels = round((5 * ((temp_fahr - 32) / 9)), 1)

print ("A temperatura em graus Celsius é {}°C.".format(temp_cels))