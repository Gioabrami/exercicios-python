#15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.

fibonacci = [1]

termos = int (input ('Quantos termos a sequência terá? '))

for n in range (1, termos):
    if len (fibonacci) > 1:
        num = fibonacci[-1] + fibonacci[-2]
    else:
        num = fibonacci[-1]

    fibonacci.append (num)

print (fibonacci)
