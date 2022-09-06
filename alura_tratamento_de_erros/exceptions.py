class OperacaoFinanceiraError(Exception):
    pass   


class SaldoInsuficienteError (Exception):
    def __init__ (self, mensagem = '', saldo = None, valor = None, *args):
        self.saldo = saldo
        self.valor = valor
        msg = 'Saldo insuficiente para efetuar a operação\n' \
            f'Saldo atual: {self.saldo}, Valor a ser sacado: {self.valor}'

        super (SaldoInsuficienteError, self).__init__ (mensagem or msg, self.saldo, self.valor, *args)
        #Da preferencia para passar a mensagem solicitada, senão passa a msg padrão
