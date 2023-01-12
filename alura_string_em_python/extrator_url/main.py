from extrator_url import ExtratorURL

url = "bytebank.com/cambio?quantidade=200&moedaOrigem=real&moedaDestino=libraEsterlina"
url_tratada = ExtratorURL(url)

quantidade = int(url_tratada.get_valor_parametro('quantidade'))
moedaOrigem = url_tratada.get_valor_parametro('moedaOrigem')
moedaDestino = url_tratada.get_valor_parametro('moedaDestino')

valores_conversao = {'real':5.26, 'dolar':1, 'libraEsterlina': 0.82, 'iene': 132.05}

quantidade_destino = round((quantidade / valores_conversao[moedaOrigem]) * valores_conversao[moedaDestino], 2)

print (quantidade_destino)
