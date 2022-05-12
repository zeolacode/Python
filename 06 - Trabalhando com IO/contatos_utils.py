
import encodings
from bson import encode

import csv, pickle, json
from contato import Contato

def csv_para_contatos(caminho, encoding='latin_1'):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)
        
        for linha in leitor:
            id, nome, email = linha
            contato = Contato(id, nome, email)
            contatos.append(contato)
    
    return contatos

def contatos_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo:
        pickle.dump(contatos, arquivo)

def pickle_para_contatos(caminho):
    with open(caminho, 'rb') as arquivo:
        contatos = pickle.load(arquivo)
    
    return contatos

def contatos_para_json(contatos, caminho):
    with open(caminho, 'w') as arquivo:
        json.dump(contatos.__dict__, arquivo, default=_contato_para_json)

def _contato_para_json(contato):
    return contato.__dict__

def json_para_contatos(caminho):
    contatos = []
    with open(caminho) as arquivos:
        contatos_json = json.load(arquivos)

        for contato in contatos_json:
            c = Contato(**contato) # contato['id'], contato['nome'], contato['email'] desempacotamento
            contatos.append(c)
        
    return contatos