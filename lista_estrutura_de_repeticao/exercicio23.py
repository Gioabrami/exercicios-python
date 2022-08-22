#23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido 
# pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para 
# encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes 
# (divisões) executados.

maximo = int (input ('Digite o número limite para os testes: '))
primos = [2]
divisoes = 0

for num in range (2, maximo + 1):   #pega cada numero que vai ser testado
    for posicao in primos:            #tenta dividir o número pelos primos que eu já tenho
        resultado = num % primos [posicao - 1]
        print ('Teste da divisão', num, '/', primos [posicao - 1])
        divisoes += 1               #conta a divisão
        if resultado == 0:        #se a divisão for exata, não é primo e não precisa continuar tentando
            break
        elif num % primo > 0:
            for n in range (primos [-1], (num | 2) + 1, 2): #continua tentando do último primo até metade do número, pulando os pares
                divisoes += 1
                if num % n == 0:
                    break
                else:
                    primos.append (num)

print (f'Primos = {primos}\nTotal de divisões = {divisoes}')
