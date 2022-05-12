arquivo = open('dados/contatos.csv', mode='a+')

print(type(arquivo.buffer))


texto_em_bytes = bytes('Esse é um texto em bytes', 'latin_1')
#print(texto_em_bytes)
#print(type(texto_em_bytes))

contato = bytes('15,Verônica,veronica@veronica.com\n', encoding='latin_1')
arquivo.buffer.write(contato)

arquivo.close()