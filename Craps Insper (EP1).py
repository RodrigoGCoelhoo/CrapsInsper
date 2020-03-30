import random as rd

#Configuraçøes básicas
fichas_jogador = 1000
nome = input("Olá jogador, qual o seu nome? ")
jogar = input("Vamos jogar Craps? (s/n): ")

#Loop para setar jogar True ou False. Vai fazer mais sentido mais para frente quando quisermos fechar o loop grande do jogo
    while type(jogar) == str:
        if jogar == 's':
            jogar = True
        elif jogar == 'n'
            jogar = False
        else:
            jogar = input("Responda apenas com 's' ou 'n'. Tente novamente: ")



while jogar:






def pergunta_aposta():
    resposta = input('Quantas fichas quer apostar? ')

    while verif = False:
        verif = verif_aposta()



def verif_aposta(valor_aposta, montante)
    if valor_aposta > montante:
        return False
    else:
        return True