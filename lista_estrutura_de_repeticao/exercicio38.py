#38. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#   Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#   Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#   A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do 
# ano anterior.
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o 
# programa permitindo que o usuário digite o salário inicial do funcionário.

salario = float (input ('Qual era o salario inicial do empregado em 1995? '))
taxa_aumento = 1.5 / 100
ano_atual = int (input ('Qual o ano atual? '))

for ano in range (1995, ano_atual):
    salario += salario * taxa_aumento
    taxa_aumento *= 2
    
print (f'O salário atual do empregado é de R$ {salario:.2f} no ano de {ano_atual}.')
