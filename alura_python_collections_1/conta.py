from abc import abstractmethod, ABCMeta
from functools import total_ordering # Implementar a ordenação dentro da classe
from operator import attrgetter

@total_ordering
class Conta:

    def __init__ (self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def deposita (self, valor):
        self._saldo += valor
    
    def __eq__ (self, outro):
        return self._codigo == outro._codigo
    
    def __lt__ (self, outro):
        return self._saldo < outro._saldo

    def __str__ (self):
        return f'Código da Conta {self._codigo} - Saldo {self._saldo}'
    
    @abstractmethod
    def passa_o_mes (self):
        pass

class ContaCorrente (Conta):

    def passa_o_mes (self):
        self._saldo -= 2

class ContaPoupanca (Conta):
    
    def passa_o_mes (self):
        self._saldo *= 1.01
        self._saldo -= 3

@total_ordering
class ContaSalario:

    def __init__ (self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__ (self, outro):
        return self._codigo == outro._codigo
    
    def __lt__ (self, outro):
        return self._saldo < outro._saldo
    
    def deposita (self, valor):
        self._saldo += valor
    
    def __str__ (self):
        return f'Código da Conta {self._codigo} - Saldo {self._saldo}'

conta_gui = ContaCorrente (15)
conta_gui.deposita (300)

conta_dani = ContaCorrente (3232)
conta_dani.deposita (250)

conta_caio = ContaPoupanca (17)
conta_caio.deposita (1000)

contas = [conta_gui, conta_dani]
contas.append (conta_caio)

conta1 = ContaSalario (37)
conta1.deposita (220)

conta2 = ContaSalario (37)

print (conta1 == conta2) # Falso pois não ocupam o mesmo espaço na memória
# Implementando __eq__ na ContaSalario

# def extrai_saldo (conta):
#     return conta._saldo
    
# for conta in sorted (contas, key = extrai_saldo):
#     print (conta)
#     #Implementando o __lt__ na Conta

# print (conta_dani < conta_gui)

# for conta in sorted (contas):
#     print (conta)


# for conta in sorted (contas, key = attrgetter ('_saldo', '_codigo')):
#     print (conta)

for conta in contas:
    print (conta)

print (conta_gui < conta_dani, 'Conta Gui e Conta Dani')
print (conta_caio <= conta_gui, 'Conta Caio e Conta Gui')
