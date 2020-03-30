import random as rd

#Configuraçøes básicas
fichas = 1000
nome = input("Olá jogador, qual o seu nome? ")
jogar = input("Vamos jogar Craps, {}? (s/n): ".format(nome))

#Figuras dados
d1 = "+- - - -+\n|       |\n|   *   |\n|       |\n+- - - -+"
d2 = "+- - - -+\n| *     |\n|       |\n|     * |\n+- - - -+"
d3 = "+- - - -+\n| *     |\n|   *   |\n|     * |\n+- - - -+"
d4 = "+- - - -+\n| *   * |\n|       |\n| *   * |\n+- - - -+"
d5 = "+- - - -+\n| *   * |\n|   *   |\n| *   * |\n+- - - -+"
d6 = "+- - - -+\n| *   * |\n| *   * |\n| *   * |\n+- - - -+"

#Loop para setar jogar True ou False. Vai fazer mais sentido mais para frente quando quisermos fechar o loop grande do jogo
while type(jogar) == str:
    if jogar == 's':
        jogar = True
    elif jogar == 'n':
        jogar = False
    else:
        jogar = input("Responda apenas com 's' ou 'n'. Tente novamente: ")

#Função soma dos dados
def soma_dados():
    soma_dados = rd.randint(1,6) + rd.randint(1,6)
    return soma_dados

#Funções para jogadas

#JOGADA PASS LINE BET
def pass_line_bet(fase, soma_dados, aposta, fichas):
    if fase != "Come out":
        return "Essa jogada só pode ser feita na rodada 'Come out'."
    if soma_dados in {7, 11}:
        print("Parabéns {}, você ganhou!".format(nome))
        fichas += aposta
        return fichas
    elif soma_dados in {2, 3, 12}:
        print("Infelizmente você perdeu, {}.", format(nome))
        fichas -= aposta
        return fichas
    else:
        jogada = 'Point'
        valor_guardado = soma_dados
        print("Você segue agora para a fase 'Point'.")
        
#JOGADA FIELD
def field(soma_dados, aposta, fichas):
    if soma_dados in {5, 6, 7, 8}:
        print ("Infelizmente você perdeu, {}!".format(nome))
        fichas -= aposta
        return fichas
    elif soma_dados in {3, 4, 9, 10, 11}:
        print("Parabéns {}, você ganhou!".format(nome))
        fichas += aposta
        return fichas
    elif soma_dados == 2:
        print("Parabéns {}, você ganhou o dobro!".format(nome))
        fichas += 2*aposta
        return fichas
    else:
        print("Parabéns {}, você ganhou o triplo!".format(nome))
        fichas += 3*aposta
        return fichas

#JOGADA ANY CROPS
def any_crops(soma_dados, aposta, fichas):
    if soma_dados in {2, 3, 12}:
        print("Parabéns {}, você ganhou 7x!!".format(nome))
        fichas += 7*aposta
        return fichas
    else:
        print("Infelizmente você perdeu, {}".format(nome))
        fichas -= aposta
        return fichas

#JOGADA TWELVE
def twelve(soma_dados, aposta, fichas):
    if soma_dados == 12:
        print("PARABÉNS {}, você ganhou muito!!!",format(nome))
        fichas += 30*aposta
        return fichas

while fichas > 0 and True:
    tipo = input('Escolha o seu tipo de aposta:')
    if tipo 
