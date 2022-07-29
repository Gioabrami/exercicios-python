#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#   Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input("Quanto você recebe por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalha por mês? "))

salario_total = round(salario_hora * horas_trabalhadas, 2)

print ("Você recebe no total R$ {} de salário por mês.".format(salario_total))