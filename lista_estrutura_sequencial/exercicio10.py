#10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temp_cels = float(input("Qual a temperatura em graus Celsius? "))

temp_fahr = round(((temp_cels * 9)/ 5) + 32, 1)

print ("A temperatura em graus Fahrenheit é {}°F.".format(temp_fahr))