#18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input ("Informe uma data no formato dd/mm/aaaa: ")
dia = int(data[0:2])
mes = data[3:5]
ano = int(data[6:10])

meses_31 = [ "01", "03", "05", "07", "08", "10", "12"]
meses_30 = [ "04", "06", "09", "11"]

def ano_valido(ano):
    if ano > 0:
        return True
    else:
        return False

def mes_valido(mes):
    if mes in meses_31 or mes in meses_30 or mes == "02":
        return True
    else:
        return False

def dia_valido(dia, mes, ano):

    if mes in meses_31:
        if dia in range (1, 32):
            return True
    
    elif mes in meses_30:
        if dia in range (1, 31):
            return True

    elif mes == "02" and (ano % 4) == 0:
        if dia in range (1, 30):
            return True
        else:
            return False
    
    elif mes == "02" and (ano % 4) != 0:
        if dia in range (1, 29):
            return True
        else:
            return False

    else:
        return False

print (ano_valido(ano), mes_valido(mes), dia_valido(dia, mes, ano))


if ano_valido(ano) and mes_valido(mes) and dia_valido(dia, mes, ano):
    print (f"A data de {dia}/{mes}/{ano} é válida!")
else:
    print (f"A data de {dia}/{mes}/{ano} é inválida!")