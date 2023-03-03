from random import randint
from time import sleep
from threading import Timer
import os

tentativa = 0
num_digitado = 0
diferenca = 0
acerto = 0
vida = diferenca + 50
start = 0

def erro():
    if vida <= 0 and tentativa <= 3:
        print("Poxa, que azar! 😩\nSua vida zerou e acabou suas chances, tente novamente!!")
    elif tentativa == 3:
        print("Tentativas excedidas, tente novamente!")

def comeco():
    start = int(input("Digite [1] para começar o jogo.\n"))

    while start != 1:
        print("Opção invalida, Insire novamente o numero pedido para jogar!")
        start = int(input("Digite [1] para começar o jogo.\n"))

    if start == 1:
        for i in range(5, 0, -1):
            print(f"Começando o jogo em {i} segundos ")
            sleep(1)
            print("="*100)
        temp = Timer(3.0, tempoaca)
        temp.start()

def nSort():
    n_sorteado = randint(1, 100)
    return n_sorteado

def qntdVida():
    diferenca = abs(sortedNum - num_digitado)
    return diferenca

sortedNum = nSort()

def tempoaca(msg="\nInfelizmente seu tempo acabou!"):
    print(msg)
    pid = os.getpid()
    os.kill(pid, 0)

def numrecebido():
    num_recebido = num_digitado
    return num_recebido

def apresenta():
    print("="*100)
    print("\n      BEM VINDO AO JOGO, TENTE ADIVINHAR O VALOR SORTEADO.")
    print("                      Como funciona?")
    print(" Você possui 50 de vida, 3 tentativas e 30 segundos para adivinhar;")
    print(" A diferença do número digitado para o numero sorteado será o dano que você sofrera na vida.")
    print(" Lembrando que, o numero está entre 1 e 100. Boa sorte e bom jogo!!\n")
    print("=" * 100)
    return apresenta




apresenta()
comeco()
print("Vida {}".format(vida))




while tentativa < 3 and vida > 0 and acerto != 1:
    tentativa += 1
    num_digitado = int(input(f"Digite sua {tentativa}ª tentativa: "))
    difVid = qntdVida()

    if sortedNum == num_digitado:
        acerto += 1
        print("Parabens!!!!! Voce acertou o numero!!! 😄😄")
        tempoaca("Jogo finalizado.")
        exit()

    vida -= difVid
    print("Vida {}".format(vida))


erro()
tempoaca("Jogo finalizado.")
