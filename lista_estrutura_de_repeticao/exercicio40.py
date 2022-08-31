#40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de 
# trânsito. Foram obtidos os seguintes dados:
#   Código da cidade;
#   Número de veículos de passeio (em 1999);
#   Número de acidentes de trânsito com vítimas (em 1999).
#   Deseja-se saber:
#   Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#   Qual a média de veículos nas cinco cidades juntas;
#   Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

cidades = []
veiculos = []
acidentes = []
indices_acidentes = []
acidentes_cidades_pequenas = []

for n in range (0,5):
    cidade = input ('Qual o código da cidade? ')
    frota = int (input ('Quantos veículos circulavam na cidade em 1999? '))
    acidente = int (input ('Quantos acidentes occorreram no ano? '))
    cidades.append (cidade)
    veiculos.append (frota)
    acidentes.append (acidente)
    indices_acidentes.append (acidente / frota)

    if frota < 2000:
        acidentes_cidades_pequenas.append (acidente)

media_veiculos = sum (veiculos) / len (veiculos)

print (
    f'O maior índice de acidentes foi de {max (indices_acidentes)} na cidade {cidades [indices_acidentes.index (max (indices_acidentes))]},',
    f'enquanto o menor foi de {min (indices_acidentes)} na cidade {cidades [indices_acidentes.index (min (indices_acidentes))]}.',
    f'\nA média de veículos das {len (cidades)} cidades é de {media_veiculos}.',
    f'\nNas cidades com menos de 2000 veículos de passeio, a média de acidentes foi de {sum (acidentes_cidades_pequenas) / len (acidentes_cidades_pequenas)}.'
)
