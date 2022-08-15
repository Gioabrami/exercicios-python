try:
    arquivo_contatos = open ("dados/nao-existe.py")

    for linha in arquivo_contatos:
        print (linha, end = "")

except FileNotFoundError:
    print ("Arquivo não encontrado")

finally:
    arquivo_contatos.close ()
