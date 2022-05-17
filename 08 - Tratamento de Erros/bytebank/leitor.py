class LeitorDeArquivo:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        print(f'Abrindo arquivo: {self.arquivo}')
    
    def ler_proxima_linha(self):
        raise IOError
        print('Lendo linha...')
        return 'Linha de arquivo'
    
    def fechar(self):
        print('Fechando arquivo.')
    
    def __enter__(self):         # entrada do escopo 
        return self
    
    def __exit__(self, type, valor, traceback):  # saída do escopo
        print("Fechando arquivo.")