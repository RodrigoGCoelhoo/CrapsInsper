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

contador_rodadas = 1

#Função que printa os dados usando a função dados_front
def printar_dados(dado_1, dado_2, soma_dados, fase, contador_rodadas):
    time.sleep(2)
    print("\033[1;37mDado 1:")
    time.sleep(2)
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
def pass_line_bet():

    global soma_dados, dado_1, dado_2, fase, contador_rodadas, fichas

    if soma_dados in {7, 11}:
        print(printar_dados(dado_1, dado_2, soma_dados, fase, contador_rodadas))
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mPass Line Bet\033[0;37m você ganhou \033[1;35m{} \033[0;37mfichas mais o retorno da sua aposta!".format(nome, aposta))
        fichas += 2*aposta
        time.sleep(3)
        return fichas
    elif soma_dados in {2, 3, 12}:
        print(printar_dados(dado_1, dado_2, soma_dados, fase, contador_rodadas))
        time.sleep(1)
        print ("\033[0;37mInfelizmente, com essa jogada \033[1;32mPass Line Bet\033[0;37m você perdeu as \033[1;35m{} \033[0;37mfichas que havia apostado, \033[1;34m{}\033[0;37m!".format(aposta,nome))
        time.sleep(3)
        return fichas
    else:
        fase = "Point"
        print(printar_dados(dado_1, dado_2, soma_dados, fase, contador_rodadas))
        valor_guardado = soma_dados
        time.sleep(1)
        print("\033[1;34m{}\033[0;37m, agora você segue agora para a fase \033[1;34m{}\033[0;37m já que a soma dos dados deu \033[1;31m{}\033[0;37m.".format(nome, fase, soma_dados))
        while True:

            dado_1, dado_2, soma_dados = dados()
            contador_rodadas += 1

            if aposta == fichas:
                time.sleep(1)
                print("Como você não tem mais fichas, não é possível fazer novas apostas.")
                time.sleep(4)
                print("\n\033[1;37mRodada {} (Fase \033[1;34m{}\033[0;37m)\n".format(contador_rodadas, fase))
                time.sleep(2)
                print(printar_dados(dado_1, dado_2, soma_dados, fase, contador_rodadas))
            else:
                
                print("\n\033[1;37mRodada {} (Fase \033[1;34m{}\033[0;37m)\n".format(contador_rodadas, fase))
                time.sleep(2)

                nova_aposta_verif = input('Deseja fazer uma nova aposta ou apenas continuar com a \033[1;32mPass Line Bet\033[0;37m? (s/n)\n')

                while nova_aposta_verif not in {'s', 'n'}:
                    nova_aposta_verif = input("Digite apenas 's' ou 'n'.\nTente novamente: ")

                if nova_aposta_verif == 's':
                    nova_aposta = int(input("\033[1;31mQual o valor da sua nova aposta?\n\033[0;37m"))
                    while nova_aposta > fichas:
                        nova_aposta = int(input("\033[0;37mAposte um valor entre \033[1;37m0 e {}\033[0;37m.\nTente novamente: ".format(fichas)))
                    
                    fichas -= nova_aposta

                    loop_jogar(dado_1, dado_2, soma_dados, fase, nova_aposta)

                else:
                    print('Continuando...')
                    print(printar_dados(dado_1, dado_2, soma_dados, fase, contador_rodadas))

                if soma_dados != valor_guardado:
                    time.sleep(1)
                    print("\033[0;37mComo a soma de dados deu \033[1;31m{}\033[0;37m, você segue na Fase \033[1;34mPoint\033[0;37m e permanece com sua aposta na jogada \033[1;32mPass Line Bet\033[0;37m.".format(soma_dados))

            if soma_dados == valor_guardado:
                print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mPass Line Bet\033[0;37m você ganhou \033[1;35m{} \033[0;37mfichas mais o retorno da sua aposta!".format(nome, aposta))
                fichas += 2*aposta
                time.sleep(2)
                fase = 'Come out'
                break
            elif soma_dados == 7:
                print ("\033[0;37mInfelizmente, com essa jogada \033[1;32mPass Line Bet\033[0;37m você perdeu as \033[1;35m{} \033[0;37mfichas que havia apostado, \033[1;34m{}\033[0;37m!".format(aposta,nome))
                time.sleep(2)
                fase = 'Come out'
                break
        return fichas
              
        
#JOGADA FIELD
def field(dado_1, dado_2, soma_dados, aposta):
    global fichas
    if soma_dados in {5, 6, 7, 8}:
        print(printar_dados(dado_1, dado_2, soma_dados, fase, contador_rodadas))
        time.sleep(1)
        print ("\033[0;37mInfelizmente, com essa jogada \033[1;32mField\033[0;37m você perdeu as \033[1;35m{} \033[0;37mfichas que havia apostado, \033[1;34m{}\033[0;37m!".format(aposta,nome))
        time.sleep(2)
        return fichas
    elif soma_dados in {3, 4, 9, 10, 11}:
        print(printar_dados(dado_1, dado_2, soma_dados, fase, contador_rodadas))
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mField\033[0;37m você ganhou \033[1;35m{} \033[0;37mfichas mais o retorno da sua aposta!".format(nome, aposta))
        fichas += 2*aposta
        time.sleep(2)
        return fichas
    elif soma_dados == 2:
        print(printar_dados(dado_1, dado_2, soma_dados, fase, contador_rodadas))
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mField\033[0;37m você ganhou o dobro, \033[1;35m{} \033[0;37mfichas, mais o retorno da sua aposta!".format(nome, aposta*2))
        fichas += 3*aposta
        time.sleep(2)
        return fichas
    else:
        print(printar_dados(dado_1, dado_2, soma_dados, fase, contador_rodadas))
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mField\033[0;37m você ganhou o triplo, \033[1;35m{} \033[0;37mfichas, mais o retorno da sua aposta!".format(nome, fichas*3))
        fichas += 4*aposta
        time.sleep(2)
        return fichas

#JOGADA ANY CROPS
def any_crops(dado_1, dado_2, soma_dados, aposta):
    global fichas
    if soma_dados in {2, 3, 12}:
        print(printar_dados(dado_1, dado_2, soma_dados, fase, contador_rodadas))
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mAny Crops\033[0;37m você ganhou \033[1;35m{} \033[0;37mfichas mais o retorno da sua aposta!".format(nome, aposta))
        fichas += 8*aposta
        time.sleep(2)
        return fichas
    else:
        print(printar_dados(dado_1, dado_2, soma_dados, fase, contador_rodadas))
        time.sleep(1)
        print ("\033[0;37mInfelizmente, com essa jogada \033[1;32mAny Crops\033[0;37m você perdeu as \033[1;35m{} \033[0;37mfichas que havia apostado, \033[1;34m{}\033[0;37m!".format(aposta,nome))
        time.sleep(2)
        return fichas

#JOGADA TWELVE
def twelve(dado_1, dado_2, soma_dados, aposta):
    global fichas
    if soma_dados == 12:
        print(printar_dados(dado_1, dado_2, soma_dados, fase, contador_rodadas))
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mTwelve\033[0;37m você ganhou 30x a sua aposta, \033[1;35m{} \033[0;37mfichas mais o retorno da sua aposta!".format(nome, 30*aposta))
        fichas += 31*aposta
        time.sleep(2)
        return fichas
    else:
        print(printar_dados(dado_1, dado_2, soma_dados, fase, contador_rodadas))
        time.sleep(1)
        print ("\033[0;37mInfelizmente, com essa jogada \033[1;32mTwelve\033[0;37m você perdeu as \033[1;35m{} \033[0;37mfichas que havia apostado, \033[1;34m{}\033[0;37m!".format(aposta,nome))
        time.sleep(2)
        return fichas


# Funcao do jogo
def loop_jogar(dado_1, dado_2, soma_dados, fase, aposta):
    global fichas

    while True:
        if fase != 'Point':
            resposta = input('\n\033[1;31mEscolha o seu tipo de aposta: \n\033[1;32mPass Line Bat = \033[1;33mpass \n\033[1;32mField = \
\033[1;33mfield \n\033[1;32mAny Crops = \033[1;33many \n\033[1;32mTwelve = \033[1;33mtwelve \n\033[1;37m: ')
        else:
            resposta = input('\n\033[1;31mEscolha o seu tipo de aposta: \n\033[1;32mField = \
\033[1;33mfield \n\033[1;32mAny Crops = \033[1;33many \n\033[1;32mTwelve = \033[1;33mtwelve \n\033[1;37m: ')
        if resposta == 'pass':
            time.sleep(1)
            print("\033[1;34m{}\033[0;37m apostou \033[1;35m{} \033[0;37mfichas na jogada \033[1;32mPass Line Bet\033[0;37m.". format(nome, aposta))
            time.sleep(1)
            fichas = pass_line_bet()
            break
        elif resposta == 'field':
            time.sleep(1)
            print("\033[1;34m{}\033[0;37m apostou \033[1;35m{} \033[0;37mfichas na jogada \033[1;32mField\033[0;37m.". format(nome, aposta))
            time.sleep(2)
            fichas = field(dado_1, dado_2, soma_dados, aposta)
            break
        elif resposta == 'any':
            fichas = any_crops(dado_1, dado_2, soma_dados, aposta)
            break
        elif resposta == 'twelve':
            fichas = twelve(dado_1, dado_2, soma_dados, aposta)
            break
        else:
            print('\033[1;31mOcorreu um erro\033[0;37m, digite novamente de acordo com a legenda!')

    print('\033[0;37mAgora você tem \033[1;35m{} \033[0;37mfichas.'.format(fichas))

    return fichas


#Loop grande do jogo
fichas = 1000
fase = 'Come out'
while fichas > 0 and jogar:

    dado_1, dado_2, soma_dados = dados()

    fase = 'Come Out'
    print("\n\033[1;37mRodada {} (Fase \033[1;34m{}\033[0;37m)\n".format(contador_rodadas, fase))
    print('Você tem \033[1;35m{}\033[0;37m fichas.\n'.format(fichas))
    
    aposta = int(input("\033[1;31mQual o valor da sua aposta?\n\033[0;37m"))
    while aposta < 0 or aposta > fichas:
        aposta = int(input("\033[0;37mAposte um valor entre \033[1;37m0 e {}\033[0;37m.\nTente novamente.\n:".format(fichas)))

    fichas -= aposta
    fichas = loop_jogar(dado_1, dado_2, soma_dados, fase, aposta)
    contador_rodadas += 1

    if fichas == 0:
        time.sleep(1)
        print("Como você perdeu todas as fichas, o jogo acabou.")
        time.sleep(1)
        print("Até a próxima, \033[1;34m{}\033[0;37m!".format(nome))
        break

    time.sleep(1)
    jogar_novamente = input('\033[0;37mDeseja continuar jogando? (s/n)\n')
    if jogar_novamente == 'n' and fichas != 0:
        jogar = False
        print("Obrigado pelo jogo, \033[1;34m{}\033[0;37m! Até mais.".format(nome))






            
