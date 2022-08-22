#5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de 
# crescimento iniciais. Valide a entrada e permita repetir a operação.

def rodar ():
    validar_paises = False
    while not validar_paises:
        pais_A = int (input ('Qual a população do pais A? '))
        pais_B = int (input ('Qual a pupolação do pais B? '))
        if pais_A < pais_B:
            validar_paises = True
        else:
            print ('A população do país A deve ser menor que a do pais B.\nPopulações inválidas, escolha novamente.')

    validar_taxas = False
    while not validar_taxas:
        taxa_A = float (input ('Qual a taxa de crescimento do país A (%)? '))
        taxa_B = float (input ('Qual a taxa de crescimento do país B (%)? '))
        if taxa_A > taxa_B:
            validar_taxas = True
        else:
            print ('A taxa do pais A deve ser maior que a do pais B.\nTaxas de crescimento inválidas, escolha novamente.')

    ano = 0

    while pais_A < pais_B:
        pais_A += pais_A * taxa_A / 100
        pais_B += pais_B *  taxa_B / 100
        ano += 1

        print ('A = {:.2f}, B = {:.2f}, ano = {}'.format (pais_A, pais_B, ano))

    print ('Levaram {} anos para as populações se equalizarem.'.format (ano))

ativo = True

while ativo:
    rodar ()
    repetir = input ('Deseja tentar novamente (S/N)? ').upper ()
    if repetir == 'N':
        break

print ('Até a próxima!')
