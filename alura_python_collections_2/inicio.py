
from xml.etree import ElementTree


usuarios_ds = [15, 23, 43, 56]
usuarios_ml = [13, 23, 56, 42]

assistiram = usuarios_ds.copy ()
assistiram.extend (usuarios_ml)
new_set = frozenset (set (assistiram))
print (new_set)

### Funcionam apenas entre dois conjuntos 
#print (usuarios_ds | usuarios_ml) #União de dois conjuntos (set) > '| (OU)'
#print (usuarios_ds & usuarios_ml) #Intersecção de dois conjuntos (set) > '& (E)'
#print (usuarios_ds - usuarios_ml) #Um conjunto menos o outro
#print (usuarios_ds ^ usuarios_ml) #Ou exclusivo > Mostra os valores excluindo quem aparece em ambos

meu_texto = 'meu nome é giovanni e o nome do meu irmao é guilherme'
set_texto = set (meu_texto.split ())
print (set_texto)

#Dicionarios

teste = { 'Agua' : 1, 'Terra' : 2, 'Fogo' : 3}

print (teste ['Fogo'])
teste ['Ar'] = 4
del teste ['Agua']

print ('Terra' in teste)
print (1 in teste.values ())

for elemento in teste:
    print (elemento)

for chave, valor in teste.items ():
    print (chave, '=', valor)
