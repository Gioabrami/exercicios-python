#24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele 
# deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#   par ou ímpar;
#   positivo ou negativo;
#   inteiro ou decimal.

num1 = float (input ("Qual o primeiro número? "))
num2 = float (input ("Qual o segundo número? "))
operacao = input ("Qual operação deseja realizar? (Responda com + , - , * ou / )" )

if operacao == "+":
    resultado = num1 + num2

elif operacao == "-":
    resultado = num1 - num2

elif operacao == "*":
    resultado = num1 * num2

elif operacao == "/":
    resultado  = num1 / num2

if (resultado % 2) == 0:
    quesito1 = "par"
else:
    quesito1 = "ímpar"

if resultado >= 0:
    quesito2 = "positivo"
else:
    quesito2 = "negativo"

if (resultado % 1) == 0:
    quesito3 = "inteiro"
else:
    quesito3 = "decimal"

print (f"O resultado é {resultado}. Ele é um número {quesito1}, {quesito2} e {quesito3}.")
