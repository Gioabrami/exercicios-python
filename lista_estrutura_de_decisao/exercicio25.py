#25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#   "Telefonou para a vítima?"
#   "Esteve no local do crime?"
#   "Mora perto da vítima?"
#   "Devia para a vítima?"
#   "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print ("Responda com (S) Sim ou (N) Não:")
perguntas = []

perguntas.append (input ("Telefonou para a vítima? ").upper ())
perguntas.append (input ("Esteve no local do crime? ").upper ())
perguntas.append (input ("Morava perto da vítima? ").upper ())
perguntas.append (input ("Devia para a vítima? ").upper ())
perguntas.append (input ("Já trabalhou com a vítima? ").upper ())

if perguntas.count ("S") == 5:
    print ("Você é o Assassino!!")

elif perguntas.count ("S") == 3 or perguntas.count ("S") == 4:
    print ("Você é Cúmplice!")

elif perguntas.count ("S") == 2:
    print ("Você é Suspeito!")

else:
    print ("Você é Inocente.")
