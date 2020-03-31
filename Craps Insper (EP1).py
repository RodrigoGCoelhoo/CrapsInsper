import random as rd
import time

#Configurações básicas

nome = input("\033[0;37mOlá jogador, qual o seu nome? \n")
jogar = input("\033[0;37mVamos jogar \033[1;37mCraps\033[0;37m, \033[1;34m{}\033[0;37m? (s/n): \n".format(nome))

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
def printar_dados():
    print("\033[1;37mDado 1:")
    time.sleep(1)
    print(dados_front(dado_1))
    time.sleep(1)
    print("Dado 2:")
    time.sleep(1)
    print(dados_front(dado_2))
    time.sleep(1)
    print("Soma dos dados:")
    time.sleep(1)
    soma_str = '\033[1;31m{}\033[0;37m'.format(soma_dados)
    return soma_str
    
    
#Funções para jogadas:

#JOGADA PASS LINE BET
def pass_line_bet(fichas, soma_dados):
    if soma_dados in {7, 11}:
        print(printar_dados())
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mPass Line Bet\033[0;37m você ganhou \033[1;35m{} \033[0;37mfichas!".format(nome, aposta))
        fichas += aposta
        time.sleep(3)
        return fichas
    elif soma_dados in {2, 3, 12}:
        print(printar_dados())
        time.sleep(1)
        print ("\033[0;37mInfelizmente, com essa jogada \033[1;32mPass Line Bet\033[0;37m você perdeu \033[1;35m{} \033[0;37mfichas, \033[1;34m{}\033[0;37m!".format(aposta,nome))
        fichas -= aposta
        time.sleep(3)
        return fichas
    else:
        fase = "Point"
        print(printar_dados())
        valor_guardado = soma_dados
        print("\033[1;34m{}\033[0;37m, agora você segue agora para a fase \033[1;34m{}\033[0;37m já que a soma dos dados deu \033[1;31m{}\033[0;37m.".format(nome, fase, soma_dados))
        while True:

            dado_1, dado_2, soma_dados = dados()

            print(loop_jogar(fichas, soma_dados))

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
def field(fichas):
    if soma_dados in {5, 6, 7, 8}:
        print(printar_dados())
        time.sleep(1)
        print ("\033[0;37mInfelizmente, com essa jogada \033[1;32mField\033[0;37m você perdeu \033[1;35m{} \033[0;37mfichas, \033[1;34m{}\033[0;37m!".format(aposta,nome))
        fichas -= aposta
        time.sleep(3)
        return fichas
    elif soma_dados in {3, 4, 9, 10, 11}:
        print(printar_dados())
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mField\033[0;37m você ganhou \033[1;35m{} \033[0;37mfichas!".format(nome, aposta))
        fichas += aposta
        time.sleep(3)
        return fichas
    elif soma_dados == 2:
        print(printar_dados())
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mField\033[0;37m você ganhou o dobro: \033[1;35m{} \033[0;37mfichas!".format(nome, aposta*2))
        fichas += 2*aposta
        time.sleep(3)
        return fichas
    else:
        print(printar_dados())
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mField\033[0;37m você ganhou o triplo: \033[1;35m{} \033[0;37mfichas!".format(nome, fichas*3))
        fichas += 3*aposta
        time.sleep(3)
        return fichas

#JOGADA ANY CROPS
def any_crops(fichas):
    if soma_dados in {2, 3, 12}:
        print(printar_dados())
        print("\033[0;37mParabéns \033[1;34m{}, com essa jogada \033[1;32mAny Crops\033[0;37mvocê ganhou 7x!!".format(nome))
        fichas += 7*aposta
        print('\033[0;37mAgora você tem {} \033[0;37mfichas'.format(fichas))
        return fichas
    else:
        print(printar_dados())
        print("\033[0;37mInfelizmente, com essa jogada \033[1;32mAny Crops\033[0;37m você perdeu, {}".format(nome))
        fichas -= aposta
        print('\033[0;37mAgora você tem {} fichas'.format(fichas))
        return fichas

#JOGADA TWELVE
def twelve(fichas):
    if soma_dados == 12:
        print(printar_dados())
        print("\033[0;37mPARABÉNS {}, com essa jogada \033[1;32mTwelve\033[0;37m você ganhou muito!!!".format(nome))
        fichas += 30*aposta
        print('\033[0;37mAgora você tem {} \033[0;37mfichas'.format(fichas))
        return fichas
    else:
        print(printar_dados())
        print("\033[0;37mInfelizmente, com essa jogada \033[1;32mTwelve\033[0;37m você perdeu, {}".format(nome))
        fichas -= aposta
        print('\033[0;37mAgora você tem {} \033[0;37mfichas'.format(fichas))
        return fichas


# Funcao do jogo
def loop_jogar(fichas, soma_dados):
    while True:
        if fase != 'Point':
            resposta = input('\033[1;31mEscolha o seu tipo de aposta: \n\033[1;32mPass Line Bat = \033[1;33mpass \n\033[1;32mField = \
\033[1;33mfield \n\033[1;32mAny Crops = \033[1;33many \n\033[1;32mTwelve = \033[1;33mtwelve \n\033[1;37m: ')
        else:
            resposta = input('\033[1;31mEscolha o seu tipo de aposta: \n\033[1;32mField = \
\033[1;33mfield \n\033[1;32mAny Crops = \033[1;33many \n\033[1;32mTwelve = \033[1;33mtwelve \n\033[1;37m: ')
        if resposta == 'pass':
            time.sleep(1)
            print("\033[1;34m{}\033[0;37m apostou na jogada \033[1;32mPass Line Bet\033[1;35m {} \033[0;37mfichas.". format(nome, aposta))
            time.sleep(1)
            fichas = pass_line_bet(fichas, soma_dados)
            break
        elif resposta == 'field':
            time.sleep(1)
            print("\033[1;34m{}\033[0;37m apostou \033[1;35m{} \033[0;37mfichas na jogada \033[1;32mField\033[0;37m.". format(nome, aposta))
            time.sleep(2)
            fichas = field(fichas)
            break
        elif resposta == 'any':
            fichas = any_crops(fichas)
            break
        elif resposta == 'twelve':
            fichas = twelve(fichas)
            break
        else:
            print('\033[1;31mOcorreu um erro\033[0;37m, digite novamente de acordo com a legenda!')

    print('\033[0;37mAgora você tem \033[1;35m{} \033[0;37mfichas.'.format(fichas))

    return fichas


#Loop grande do jogo
fichas = 1000
while fichas > 0 and jogar:

    dado_1, dado_2, soma_dados = dados()

    fase = 'Come Out'
    print('Você tem \033[1;35m{}\033[0;37m fichas e está na fase \033[1;34m{}\033[0;37m.'.format(fichas, fase))
    
    aposta = int(input("\033[1;31mQual o valor da sua aposta?\n\033[0;37m"))
    while aposta < 0 or aposta > fichas:
        aposta = int(input("\033[0;37mAposte um valor entre \033[1;37m0 e {}\033[0;37m.\nTente novamente: ".format(fichas)))

    fichas = loop_jogar(fichas, soma_dados)

    if fichas == 0:
        time.sleep(1)
        print("Como você perdeu todas as fichas, o jogo acabou.\nAté a próxima, \033[1;34m{}\033[0;37m!".format(nome))
        break

    time.sleep(1)
    jogar_novamente = input('\033[0;37mDeseja continuar jogando? (s/n)\n')
    if jogar_novamente == 'n' and fichas != 0:
        jogar = False
        print("Obrigado pelo jogo, \033[1;34m{}\033[0;37m! Até mais.".format(nome))






            
