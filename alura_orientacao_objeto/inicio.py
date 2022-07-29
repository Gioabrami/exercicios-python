
def cria_conta (conta, titular, saldo, limite):
    conta = {"numero": conta, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposito (conta, valor):
    conta["saldo"] += valor

def saque (conta, valor):
    conta["saldo"] -= valor

def extrato (conta):
    print ("O saldo disponível é de R$ {}.".format (conta["saldo"]))

conta = cria_conta (123, "Joao", 50.0, 1000.0)

extrato (conta)