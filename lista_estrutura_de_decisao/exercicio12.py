#12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do 
# Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e 
# que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao 
# usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#   Desconto do IR:
#   Salário Bruto até 900 (inclusive) - isento
#   Salário Bruto até 1500 (inclusive) - desconto de 5%
#   Salário Bruto até 2500 (inclusive) - desconto de 10%
#   Salário Bruto acima de 2500 - desconto de 20% 
# Imprima na tela as informações, dispostas conforme o exemplo abaixo.

salario = int (input ("Quanto você recebe por hora? "))
horas = int (input ("Quantas horas você trabalha por mês? "))

salario_bruto = round (salario * horas, 3)
fgts = round (salario_bruto * 0.11, 3)
inss = round (salario_bruto * 0.1, 3)

if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = 5
elif salario_bruto <= 2500:
    desconto_ir = 10
elif salario_bruto > 2500:
    desconto_ir = 20

ir = salario_bruto * desconto_ir / 100
descontos = ir + inss

print (
    f"\nSalário Bruto: ({salario} * {horas}) : R$ {salario_bruto:7.2f}",
    f"\n(-) IR ({desconto_ir}%)              : R$ {ir:7.2f}",
    f"\n(-) INSS (10%)           : R$ {inss:7.2f}",
    f"\nFGTS (11%)               : R$ {fgts:7.2f}",
    f"\nTotal de descontos       : R$ {descontos:7.2f}",
    f"\nSalário Líquido          : R$ {salario_bruto - descontos:7.2f}"
)