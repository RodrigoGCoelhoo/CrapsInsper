import random as rd
import time

#Configuraçøes básicas

nome = input("Olá jogador, qual o seu nome? ")
jogar = input("Vamos jogar Craps, {}? (s/n): ".format(nome))

#Figuras dados
fig_d1 = "+- - - -+\n|       |\n|   *   |\n|       |\n+- - - -+"
fig_d2 = "+- - - -+\n| *     |\n|       |\n|     * |\n+- - - -+"
fig_d3 = "+- - - -+\n| *     |\n|   *   |\n|     * |\n+- - - -+"
fig_d4 = "+- - - -+\n| *   * |\n|       |\n| *   * |\n+- - - -+"
fig_d5 = "+- - - -+\n| *   * |\n|   *   |\n| *   * |\n+- - - -+"
fig_d6 = "+- - - -+\n| *   * |\n| *   * |\n| *   * |\n+- - - -+"

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

#Função que retorna a imagem do dado
def dados_front(dado):
    lista_dados = [fig_d1, fig_d2, fig_d3, fig_d4, fig_d5, fig_d6]
    for item in lista_dados:
        if (lista_dados.index(item) + 1) == dado:
            return item

#Função que printa os dados usando a função dados_front
def printar_dados()
    print("Dado 1:") 
    print(dados_front(dado_1))
    print("Dado 2:")
    print(dados_front(dado_2))
    print("Soma dos dados:", soma_dados)
    return 
    
    
#Funções para jogadas:

#JOGADA PASS LINE BET
def pass_line_bet(fichas):
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

            dado_1, dado_2, soma_dados = dados()

            while True:
                tipo = input('\033[1;31mEscolha o seu tipo de aposta: \n\033[1;32mField = \033[1;33mfield \n\
\033[1;32mAny Crops = \033[1;33many \n\033[1;32mTwelve = \033[1;33mtwelve \n\033[1;32mNenhuma nova aposta = \033[1;33mn\n\033[1;37m: ' )
                if tipo == 'field':
                    fichas = field(aposta, fichas)
                    break
                elif tipo == 'any':
                    fichas = any_crops(aposta, fichas)
                    break
                elif tipo == 'twelve':
                    fichas = twelve(aposta, fichas)
                    break
                else:
                    print('\033[1;31Você não escreveu direito, digite novamente de acordo com a legenda!')

            if soma_dados == valor_guardado:
                fichas += aposta
                fase = 'Come out'
                break
            elif soma_dados == 7:
                fichas -= aposta
                fase = 'Come out'
                break
        return fichas
            
                
        
#JOGADA FIELD
<<<<<<< HEAD
def field(fichas)
    print("Dado 1:\n", dados_front(dado_1))
    print("Dado 2:\n", dados_front(dado_2))
    print("Soma dos dados: ", soma_dados)
=======
def field(fichas):
>>>>>>> a0a9fb2644d548fffcfc893d49bcbabe93e5bb19
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
def any_crops(fichas):
    if soma_dados in {2, 3, 12}:
        print("Parabéns {}, você ganhou 7x!!".format(nome))
        fichas += 7*aposta
        return fichas
    else:
        print("Infelizmente você perdeu, {}".format(nome))
        fichas -= aposta
        return fichas

#JOGADA TWELVE
def twelve(fichas):
    if soma_dados == 12:
        print("PARABÉNS {}, você ganhou muito!!!",format(nome))
        fichas += 30*aposta
        return fichas

#Loop grande do jogo
fichas = 9000
while fichas > 0 and jogar:

    dado_1, dado_2, soma_dados = soma_dados()
    print('Você tem {} fichas'.format(fichas))
    print('Você está na fase \033[1;34mCome Out')
    fase = 'Come Out'


    while True:
        tipo = input('\033[1;31mEscolha o seu tipo de aposta: \n\033[1;32mPass Line Bat = \033[1;33mpass \n\033[1;32mField = \
\033[1;33mfield \n\033[1;32mAny Crops = \033[1;33many \n\033[1;32mTwelve = \033[1;33mtwelve \n\033[1;37m: ')
        if tipo == 'pass':
            fichas = pass_line_bet(fichas)
            break
        elif tipo == 'field':
            fichas = field(fichas)
            break
        elif tipo == 'any':
            fichas = any_crops(fichas)
            break
        elif tipo == 'twelve':
            fichas = twelve(fichas)
            break
        else:
            print('\033[1;31mVocê não escreveu direito, digite novamente de acordo com a legenda!')

if fichas <= 0:
    print("Você perdeu todas as fichas")




            
            
