import random

def jogar():
    print("Bem vindo ao jogo de forca!")

    palavra_secreta = gera_palavra_secreta()
    letras_acertadas = ["_" for letra in palavra_secreta]
    print (letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = palpite()

        if chute in palavra_secreta:
            letras_acertadas = chute_certo(chute, palavra_secreta, letras_acertadas)
            
        else:
            erros = chute_errado(erros)

        enforcou = erros ==6
        acertou = "_" not in letras_acertadas
        print (letras_acertadas)    

    if acertou:
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)

def mensagem_vencedor():
    print ("Você ganhou!!")

def mensagem_perdedor(palavra_secreta):
    print ("Você perdeu")
    print ("A palavra secreta era", palavra_secreta)

def chute_certo(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas [index] = letra
        index += 1
    return letras_acertadas

def chute_errado(erros):
    erros += 1
    chances = 6 - erros
    print ("Você tem mais {} tentativas".format (chances))
    return erros

def palpite():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return chute

def gera_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavra = []

    for linha in arquivo:
        palavra.append(linha.strip())
    arquivo.close()

    palavra_secreta = random.choice(palavra).upper()
    return palavra_secreta

if (__name__ == "__main__"):
    jogar()