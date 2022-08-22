#16. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500.

fibonacci = [0,1]

while fibonacci[-1] <= 500:
    num = fibonacci [-1] + fibonacci [-2]
    fibonacci.append (num)

print (f'A sequencia de Fibonacci desejada até ultapassar 500 é:\n {fibonacci}')