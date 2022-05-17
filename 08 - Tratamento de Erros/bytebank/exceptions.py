
from lib2to3.pgen2.token import OP


class OperacaoFinanceiraError(Exception):
    pass


class SaldoInsuficienteError(OperacaoFinanceiraError):
    
    def __init__(self, message='', saldo=None, valor=None, *args):
        self.saldo = saldo
        self.valor = valor
        msg = 'Saldo insuficiente para efetuar a transção\n' \
              f'Saldo atual: {self.saldo} Valor a ser sacado: {self.valor}'
        self.msg = message or msg
        super(SaldoInsuficienteError, self).__init__(self.msg, self.saldo, self.valor,*args)
