import random

def jogar ():

    print(12 * " * ")
    print(" Bem vindo ao jogo de advinhação !! ")
    print(12 * " * ")

    numero_correto = random.randrange(1,101)

    total_de_tentativas = 0

    pontos = 1000

    print(numero_correto) #remover depois

    print(" Selecione o nível de dificuldade ")

    print(" (1) Fácil (2) Médio (3) Difícil")

    nivel = int(input(" qual o nível? "))
           
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        
        if (nivel > 3):
            print(" Parabéns, você tentou quebrar as regras e a dificuldade difícil foi selecionada. ")
        elif (nivel == 0):
            print(" Parabéns, você tentou quebrar as regras e a dificuldade difícil foi selecionada. ")
        total_de_tentativas = 5


    rodada = 1

    for rodada in range(1, total_de_tentativas + 1 ) :

        print(" Tentativa {} de {}".format(rodada, total_de_tentativas))

        palpite = input(" Digite o seu palpite entre 1 e 100 : ")

        print("Você digitou {}".format(palpite))

        palpite_int=(int(palpite))

        if palpite_int < 1 or palpite_int > 100:
            print("Apenas números entre 0 e 100")
            continue

        palpite_maior = palpite_int > numero_correto

        palpite_menor = palpite_int < numero_correto

        acertou = palpite_int == numero_correto

        errou = palpite_int != numero_correto



        if acertou:
            print(" Você acertou e fez {} pontos ! ".format(pontos))
            break
        

            
        else:
            pontos_perdidos = abs(numero_correto - palpite_int)
            pontos = pontos - pontos_perdidos
            pontos_atualizados = str(pontos_perdidos)

            if palpite_maior:
                print("O seu palpite foi {}, e você perdeu {} pontos. tente um número menor.".format(palpite, pontos_atualizados))
            elif palpite_menor:
                print("O seu palpite foi {}, e você perdeu {} pontos. Tente um número maior.".format(palpite, pontos_atualizados))
            
        
    print(" Fim de jogo. ") 

if(__name__ == "__main__"):
    jogar()

