
from conta import Conta

conta1 = Conta (123, "Joao", 50.0, 1000.0)
conta2 = Conta (321, "Marco", 100.0, 1000.0)

conta1.deposita (150)
conta1.extrato ()

conta1.saca (100)
conta1.extrato ()