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
def dados():
    dado_1 = rd.randint(1,6)
    dado_2 = rd.randint(1,6)
    soma_dados = dado_1 + dado_2
    return dado_1, dado_2, soma_dados

def dados_front(dado_1, dado_2)


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
        print("Infelizmente você perdeu, {}.".format(nome))
        fichas -= aposta
        return fichas
    else:
        fase = "Point"
        valor_guardado = soma_dados
        print("Você segue agora para a fase 'Point'.")
        while True:
            soma_dados = soma_dados()[2]
            if soma_dados == valor_guardado:
                jogador ganha
                fase = 'Come out'
                break
            elif soma_dados == 7:
                jogador perde
                fase = 'Come out'
                break
            
                
        
#JOGADA FIELD
def field(aposta, fichas):
    if soma_dados() in {5, 6, 7, 8}:
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

#Loop grande do jogo

while fichas > 0 and jogar:

    dado_1, dado_2, soma_dados = soma_dados()

    while True:
        print('Você está na fase \033[1;34mCome Out')
        tipo = input('\033[1;31mEscolha o seu tipo de aposta: \n\033[1;32mPass Line Bat = \033[1;33mpass \n\033[1;32mField = \
\033[1;33mfield \n\033[1;32mAny Crops = \033[1;33many \n\033[1;32mTwelve = \033[1;33mtwelve \n\033[1;37m:')
        if tipo == 'pass':
            fichas = pass_line_bet()
            break
        elif tipo == 'field':
            fichas = field()
            break
        elif tipo == 'any':
            fichas = any_crops()
            break
        elif tipo == 'twelve':
            fichas = twelve()
            break
        else:
            print('\033[1;31mVocê não escreveu direito, digite novamente de acordo com a legenda!')

            
            
