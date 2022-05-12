
contato_carol = '11,Carol,carol@carol.com.br\n'
contato_andresa = '12,Andresa,andresa@andresa.com.br\n'

with open('dados/contatos-escrita.csv', 'w') as arquivo1:
    arquivo1.write(contato_carol)

with open('dados/contatos-escrita.csv', 'a') as arquivo2:
    arquivo2.write(contato_andresa)
