from acesso_cp import BuscaEndereco
import requests

cep = "01001000"

objeto_cep = BuscaEndereco(cep)
# print(objeto_cep)

# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r.text)
# print(r.json())

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)