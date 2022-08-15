arquivo = open ("dados/contatos.csv")

print (type (arquivo))
conteudo = arquivo.buffer.read()
print(conteudo)

arquivo.close ()
