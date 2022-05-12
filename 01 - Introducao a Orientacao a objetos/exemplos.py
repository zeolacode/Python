class Pessoa:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def exibe_nome_e_sobrenome(self):
        print("{0} {1}".format(self.nome, self.sobrenome))

class Jogo:
    
    def __init__(self) -> None:
        self.contador = 0
    
    def incrementa(self):
        self.contador += 1

class Sistema:

    def __init__(self):
        self.texto = ''
    
    def le_entrada(self):
        self.texto = input()
    
    def exibe_saida(self):
        print(self.texto)


class Retangulo:

    def __init__(self, x, y):
        # atributo privado! 
        self.__x = x
        self.__y = y
        self.__area = x * y
    
    def obter_area(self):
        return self.__area