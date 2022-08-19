meu_texto = '''
No meio do caminho tinha uma pedra
Tinha uma pedra no meio do caminho
Tinha uma pedra
No meio do caminho tinha uma pedra
Nunca me esquecerei desse acontecimento
Na vida de minhas retinas tão fatigadas
Nunca me esquecerei que no meio do caminho
Tinha uma pedra
Tinha uma pedra no meio do caminho
No meio do caminho tinha uma pedra
'''
meu_texto = meu_texto.lower()

# palavras = {}

# for palavra in meu_texto:
#     palavras [palavra] = meu_texto.count (palavra)

# for item in palavras.items ():
#     print (item)


# dicionario = defaultdict (int, palavras)

# class Conta:
#     def __init__ (self):
#         print ('Criando uma conta')

# contas = defaultdict (Conta)

# contador_palavras = Counter (meu_texto) # tudo em uma linha só
# print (contador_palavras)
from collections import defaultdict, Counter

def analisa_frequencia_de_letras(texto):
  contador = Counter(texto.lower())
  total_de_caracteres = sum(contador.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in contador.items()]
  proporcoes = Counter(dict(proporcoes))
  mais_comuns = proporcoes.most_common(10)

  for caractere, proporcao in mais_comuns:
    print('{} => {:.2f} %'.format (caractere, proporcao))

analisa_frequencia_de_letras (meu_texto)
