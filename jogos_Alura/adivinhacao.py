import random

def jogar():
    print("Bem vindo ao jogo de adivinhação!")
    num_secreto = random.randrange(1,101)
    pontos = 100

    print ("Escolha o nível de dificuldade")
    print ("Fácil (1), Médio (2) ou Difícil (3)")
    nivel = int(input("Digite o nível escolhido: "))

    if (nivel == 1):
        tentativas = 10
        print ("Nível Fácil")

    elif (nivel ==2):
        tentativas = 7
        print ("Nível Médio")

    elif (nivel == 3):
        tentativas = 5
        print ("Nível Difícil")

    while (tentativas > 0):

        print ("Você tem mais {} tentativas restantes" .format (tentativas))
        chute = int(input("Digite um número de 1 a 100: "))

        if (chute < 1 or chute > 100):
            print ("Digite um número válido")
            continue

        print ("Você digitou ", chute)

        if (chute == num_secreto):
            print("Você acertou!")
            print ("Você fez {} pontos!".format (pontos))
            break
        elif (chute < num_secreto):
            print("Você errou. O número secreto é maior que esse!")
        elif (chute > num_secreto):
            print("Você errou. O número secreto é menor que esse!")
            
        pontos = pontos - (abs(num_secreto - chute))
        tentativas = tentativas - 1

    print ("Fim de jogo")

if (__name__ == "__main__"):
    jogar()