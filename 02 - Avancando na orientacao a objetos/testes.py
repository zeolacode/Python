class Pessoa:
    tamanho_cpf = 11

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome
    
    def valida_cpf(self):
        return True if len(self.cpf) == __class__.tamanho_cpf else False