#15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
#Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#   salário bruto.
#   quanto pagou ao INSS.
#   quanto pagou ao sindicato.
#   o salário líquido.
#   calcule os descontos e o salário líquido, conforme a tabela abaixo:

salario_hora = float(input("Quanto você recebe por hora? "))
horas_trabalhadas = int(input("Quantas horas você trabalha no mês? "))

salario_bruto = round (salario_hora * horas_trabalhadas, 3)
ir = round (0.11 * salario_bruto, 3)
inss = round (0.08 * (salario_bruto - ir), 3)
sindicato = round (0.05 * (salario_bruto - ir - inss), 3)
salario_liquido = round (salario_bruto - ir - inss - sindicato, 3)

print ("Seu salário bruto é de R$ {:.2f}.".format (salario_bruto))
print ("Você pagou R$ {:.2f} ao INSS.".format (inss))
print ("Você pagou R$ {:.2f} ao sindicato.".format (sindicato))
print ("Seu salário líquido é de R$ {:.2f}.".format (salario_liquido))