class LeitorDeArquivos:
    def __init__ (self, arquivo):
        self.arquivo = arquivo
        # raise FileNotFoundError
        print (f'Abrindo o arquivo: {self.arquivo}')

    def ler_proxima_linha (self):
        # raise IOError
        print ('Lendo linha...')
        return 'Linha do Arquivo'

    def fechar (self):
        print ('Fechando arquivo.')

    def __enter__ (self):
        return self

    def __exit__ (self, type, valor, traceback):
        print ('Fecchando arquivo.')
        