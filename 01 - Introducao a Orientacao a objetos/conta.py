
class Conta:

    # self é a referência que sabe encontrar o objeto construído em memória. 
    # self. vou até o objeto 
    # Em self.numero, o caractere "ponto" (.) é um comando de ida ao objeto e numero, titular, saldo e limite são atributos
    def __init__(self, numero, titular, saldo, limite) -> None: # função construtura
        print("Construindo objeto ...{}".format(self))
        # Atributos
        self.__numero = numero  # __ privado
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    # método privado 
    def __pode_sacar(self, valor_sacar):
        return valor_sacar <= (self.__saldo + self.__limite)

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod # metodos estáticos 
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}