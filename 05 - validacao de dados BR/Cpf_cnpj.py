from validate_docbr import CPF, CNPJ

# prática de programação chamada Factory
class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            return ValueError("Quantidade de digitos inválida!!")


class DocCpf:

    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:

    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)









# Teste

class CpfCnpj:
    
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if self.tipo_documento.lower() == "cpf":
            if self.cpf_e_Valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!!!")
        elif self.tipo_documento.lower() == "cnpj":
            if self.cnpj_e_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido!!!")
        else:
            raise ValueError("Documento Inválido!!")

    def __str__(self):
        if self.tipo_documento.lower() == 'cpf':
            return self.format_cpf()
        elif self.tipo_documento.lower() == 'cnpj':
            return self.format_cnpj()

    def cpf_e_Valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos inválida!!")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def cnpj_e_valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            return ValueError("Quantidade de digitos inválida!!") 

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)           