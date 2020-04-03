import random as rd
import time


#Configurações básicas
nome = input("\033[0;37mOlá jogador, qual o seu nome? \n")
time.sleep(1)
jogar = input("\033[0;37mVamos jogar \033[1;37mCraps\033[0;37m, \033[1;34m{}\033[0;37m? (s/n): \n".format(nome))
fichas = 1000

while jogar not in {'n','s'}:
    jogar = input("Responda apenas com 's' ou 'n'.\nTente novamente: ")

if jogar == 'n':
    print('Obrigado, \033[1;34m{}\033[0;37m! Até mais então.'.format(nome))
    exit()
else:
    jogar = True

#Regras
time.sleep(1)
verif_regras = input('Você sabe as regras? (s/n)\n')
time.sleep(1)
while verif_regras not in {'s','n'}:
    verif_regras = input('Responda apenas "s" ou "n". Tente novamente:\n')
if verif_regras == 'n':
    time.sleep(1)
    print("Você irá fazer uma aposta em cima da \033[4;37msoma\033[0;37m de dois dados que serão lançados aleatoriamente.")
    time.sleep(5)
    print("A tabela a seguir informa em que fase você pode fazer cada jogada e em quais resultados você perde ou ganha:\n")
    time.sleep(6)
    print('+--------------------------------------------------------------------------------------------------------------------------+')
    print('| \033[1;32mJogada\033[0;37m           | Fase \033[1;34mCome Out\033[0;37m | Fase \033[1;34mPoint\033[0;37m | \033[1;31mSoma que perde a aposta\033[0;37m            | \033[1;36mSoma que ganha a aposta\033[0;37m             |')
    print('+--------------------------------------------------------------------------------------------------------------------------+')
    tab = ([['Pass Line Bet *', '✓', 'x', '2, 3 e 12', '7 e 11'],
    ['Field', '✓', '✓', '5, 6, 7 e 8', '3, 4, 9, 10, 11, 2 (2x) e 12 (3x)'], 
    ['Any Crops', '✓', '✓', '4, 5, 6, 7, 8, 9, 10 e 11', '2 (7x), 3 (7x) e 12 (7x)'],
    ['Twelve', '✓', '✓', '2, 3, 4, 5, 6, 7, 8, 9, 10 e 11', '12 (30x)           '] ]) 

    for item in tab:
        print('|\033[1;32m', item[0],  ' '*(15 - len(item[0])), '\033[0;37m|',  ' '*5, item[1], ' '*5, '|', ' '*3, item[2], ' '*4, '| ', item[3], ' '*(32 - len(item[3])), '| ', item[4], ' '*(33 - len(item[4])), '|')

    print('+--------------------------------------------------------------------------------------------------------------------------+')
    print('\n(\033[1;32m*\033[0;37m) Caso acerte os números 4, 5, 6, 8, 9 e 10, você passa para a fase \033[1;34mPoint\033[0;37m), em que só sairá caso a soma dos novos danos\n\
    lançados dê 7, em que você \033[1;31mperde a aposta\033[0;37m), ou dê igual à soma dos dados na última fase \033[1;34mCome out\033[0;37m), em que você \033[1;36mganha a aposta\033[0;37m).\n\
    Durante a fase \033[1;34mPoint\033[0;37m) você poderá continuar fazendo outras apostas.\n')
    time.sleep(10)

    vamos_jogar = input('Vamos ao jogo então, \033[1;34m{}\033[0;37m? (s/n)\n'.format(nome))
    while vamos_jogar not in {'s','n'}:
        vamos_jogar = input("Não entendi sua resposta. Digite apenas 's' ou 'n'.\n")
    if vamos_jogar == 'n':
        time.sleep(1)
        print('O jogo é difícil mesmo! Até mais, \033[1;34m{}\033[0;37m'.format(nome))
        exit()
        
time.sleep(1)
print('Então vamos lá!')

#Figuras dados
fig_d1 = "+- - - -+\n|       |\n|   *   |\n|       |\n+- - - -+"
fig_d2 = "+- - - -+\n| *     |\n|       |\n|     * |\n+- - - -+"
fig_d3 = "+- - - -+\n| *     |\n|   *   |\n|     * |\n+- - - -+"
fig_d4 = "+- - - -+\n| *   * |\n|       |\n| *   * |\n+- - - -+"
fig_d5 = "+- - - -+\n| *   * |\n|   *   |\n| *   * |\n+- - - -+"
fig_d6 = "+- - - -+\n| *   * |\n| *   * |\n| *   * |\n+- - - -+"

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
def printar_dados():
    time.sleep(1)
    print("\033[0;37mBoa sorte! Lançando dados...")
    time.sleep(2)
    print("\033[1;37mDado 1:")
    time.sleep(1)
    print(dados_front(dado_1))
    time.sleep(1)
    print("Dado 2:")
    time.sleep(1)
    print(dados_front(dado_2))
    time.sleep(1)
    soma_str = '\033[1;31m{}\033[0;37m'.format(soma_dados)
    return "Soma dos dados: " + soma_str


#Funções para jogadas:

#JOGADA PASS LINE BET
def pass_line_bet(aposta):

    global soma_dados
    global dado_1
    global dado_2
    global fase
    global contador_rodadas
    global fichas

    if soma_dados in {7, 11}:
        print(printar_dados())
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mPass Line Bet\033[0;37m você ganhou \033[1;35m{} \033[0;37mfichas mais o retorno das \033[1;35m{}\033[0;37m fichas da sua aposta!".format(nome, aposta, aposta))
        fichas += 2*aposta
        time.sleep(3)
        return fichas

    elif soma_dados in {2, 3, 12}:
        print(printar_dados())
        time.sleep(1)
        print ("\033[0;37mInfelizmente, com essa jogada \033[1;32mPass Line Bet\033[0;37m você perdeu as \033[1;35m{} \033[0;37mfichas que havia apostado, \033[1;34m{}\033[0;37m!".format(aposta,nome))
        time.sleep(3)
        return fichas

    else:
        fase = "Point"
        print(printar_dados())
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
                print("+-----------------------+\n\033[1;37m| Rodada {} (Fase \033[1;34m{}\033[0;37m) |\n+-----------------------+".format(contador_rodadas, fase))
                time.sleep(2)
                print(printar_dados())
            else:
                time.sleep(1)
                print("+-----------------------+\n\033[1;37m| Rodada {} (Fase \033[1;34m{}\033[0;37m) |\n+-----------------------+".format(contador_rodadas, fase))
                time.sleep(1)
                print('\033[0;37mAgora você tem \033[1;35m{} \033[0;37mfichas em caixa e mais \033[1;35m{}\033[0;37m fichas em jogo com a aposta \033[1;32mPass Line Bet\033[0;37m.'.format(fichas, aposta))
                time.sleep(1)

                if fichas == 0:
                    time.sleep(3)
                    print('Você não pode apostas mais pois não possue mais fichas. O jogo continuará automaticamente!')

                else:
                    nova_aposta_verif = input('Deseja fazer uma nova aposta ou apenas continuar com a \033[1;32mPass Line Bet\033[0;37m? (s/n)\n')

                    while nova_aposta_verif not in {'s', 'n'}:
                        nova_aposta_verif = input("Digite apenas 's' ou 'n'.\nTente novamente: ")

                    if nova_aposta_verif == 's':
                        nova_aposta = int(input("\033[1;31mQual o valor da sua nova aposta?\n\033[0;37m"))
                        while nova_aposta > fichas:
                            nova_aposta = int(input("\033[0;37mAposte um valor entre \033[1;37m0 e {}\033[0;37m.\nTente novamente: ".format(fichas)))
                        
                        fichas -= nova_aposta

                        loop_jogar(nova_aposta)

                print(printar_dados())

                if soma_dados != valor_guardado and soma_dados != 7:
                    time.sleep(1)
                    print("\033[0;37mComo a soma de dados deu \033[1;31m{}\033[0;37m, você segue na Fase \033[1;34mPoint\033[0;37m e permanece com sua aposta na jogada \033[1;32mPass Line Bet\033[0;37m.".format(soma_dados))

            if soma_dados == valor_guardado:
                print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mPass Line Bet\033[0;37m você ganhou \033[1;35m{} \033[0;37mfichas mais o retorno das \033[1;35m{}\033[0;37m fichas da sua aposta!".format(nome, aposta, aposta))
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
def field(aposta):

    global fichas

    if soma_dados in {5, 6, 7, 8}:
        print(printar_dados())
        time.sleep(1)
        print ("\033[0;37mInfelizmente, com essa jogada \033[1;32mField\033[0;37m você perdeu as \033[1;35m{} \033[0;37mfichas que havia apostado, \033[1;34m{}\033[0;37m!".format(aposta,nome))
        time.sleep(2)
        return fichas

    elif soma_dados in {3, 4, 9, 10, 11}:
        print(printar_dados())
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mField\033[0;37m você ganhou \033[1;35m{} \033[0;37mfichas mais o retorno das \033[1;35m{}\033[0;37m fichas da sua aposta!".format(nome, aposta, aposta))
        fichas += 2*aposta
        time.sleep(2)
        return fichas

    elif soma_dados == 2:
        print(printar_dados())
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mField\033[0;37m você ganhou o dobro, \033[1;35m{} \033[0;37mfichas, mais o retorno das \033[1;35m{}\033[0;37m fichas da sua aposta!".format(nome, 2*aposta, aposta))
        fichas += 3*aposta
        time.sleep(2)
        return fichas

    else:
        print(printar_dados())
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mField\033[0;37m você ganhou o triplo, \033[1;35m{} \033[0;37mfichas, mais o retorno das \033[1;35m{}\033[0;37m fichas da sua aposta!".format(nome, 3*aposta, aposta))
        fichas += 4*aposta
        time.sleep(2)
        return fichas

#JOGADA ANY CROPS
def any_crops(aposta):

    global fichas

    if soma_dados in {2, 3, 12}:
        print(printar_dados())
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mAny Crops\033[0;37m você ganhou \033[1;35m{} \033[0;37mfichas mais o retorno das \033[1;35m{}\033[0;37m fichas da sua aposta!".format(nome, 7*aposta, aposta))
        fichas += 8*aposta
        time.sleep(2)
        return fichas

    else:
        print(printar_dados())
        time.sleep(1)
        print ("\033[0;37mInfelizmente, com essa jogada \033[1;32mAny Crops\033[0;37m você perdeu as \033[1;35m{} \033[0;37mfichas que havia apostado, \033[1;34m{}\033[0;37m!".format(aposta,nome))
        time.sleep(2)
        return fichas

#JOGADA TWELVE
def twelve(aposta):

    global fichas

    if soma_dados == 12:
        print(printar_dados())
        time.sleep(1)
        print("\033[0;37mParabéns \033[1;34m{}\033[0;37m, com essa jogada \033[1;32mTwelve\033[0;37m você ganhou 30x a sua aposta, \033[1;35m{} \033[0;37mfichas mais o retorno das \033[1;35m{}\033[0;37m fichas da sua aposta!".format(nome, aposta*30, aposta))
        fichas += 31*aposta
        time.sleep(2)
        return fichas

    else:
        print(printar_dados())
        time.sleep(1)
        print ("\033[0;37mInfelizmente, com essa jogada \033[1;32mTwelve\033[0;37m você perdeu as \033[1;35m{} \033[0;37mfichas que havia apostado, \033[1;34m{}\033[0;37m!".format(aposta,nome))
        time.sleep(2)
        return fichas


# Funcao do jogo
def loop_jogar(aposta):

    global fichas

    while True:

        if fase != 'Point':
            resposta = input('\033[1;31mEscolha o seu tipo de aposta: \n\033[1;32mPass Line Bat = \033[1;33mpass \n\033[1;32mField = \033[1;33mfield \n\033[1;32mAny Crops = \033[1;33many \n\033[1;32mTwelve = \033[1;33mtwelve \n\033[1;37m: ')
        else:
            resposta = input('\033[1;31mEscolha o seu tipo de aposta: \n\033[1;32mField = \033[1;33mfield \n\033[1;32mAny Crops = \033[1;33many \n\033[1;32mTwelve = \033[1;33mtwelve \n\033[1;37m: ')

        if resposta == 'pass':
            time.sleep(1)
            print("\033[1;34m{}\033[0;37m apostou \033[1;35m{} \033[0;37mfichas na jogada \033[1;32mPass Line Bet\033[0;37m.". format(nome, aposta))
            time.sleep(1)
            fichas = pass_line_bet(aposta)
            break

        elif resposta == 'field':
            time.sleep(1)
            print("\033[1;34m{}\033[0;37m apostou \033[1;35m{} \033[0;37mfichas na jogada \033[1;32mField\033[0;37m.". format(nome, aposta))
            time.sleep(2)
            fichas = field(aposta)
            break

        elif resposta == 'any':
            time.sleep(1)
            print("\033[1;34m{}\033[0;37m apostou \033[1;35m{} \033[0;37mfichas na jogada \033[1;32mAny Crops\033[0;37m.". format(nome, aposta))
            time.sleep(2)
            fichas = any_crops(aposta)
            break

        elif resposta == 'twelve':
            time.sleep(1)
            print("\033[1;34m{}\033[0;37m apostou \033[1;35m{} \033[0;37mfichas na jogada \033[1;32mTwelve\033[0;37m.". format(nome, aposta))
            time.sleep(2)
            fichas = twelve(aposta)
            break

        else:
            print('\033[1;31mOcorreu um erro\033[0;37m, digite novamente de acordo com a legenda!')

    return fichas


#Loop grande do jogo
while fichas > 0 and jogar:

    dado_1, dado_2, soma_dados = dados()
    fase = 'Come Out'

    time.sleep(1)
    print("+--------------------------+\n\033[1;37m| Rodada {} (Fase \033[1;34m{}\033[0;37m) |\n+--------------------------+".format(contador_rodadas, fase))
    time.sleep(1)
    print('Você tem \033[1;35m{}\033[0;37m fichas.'.format(fichas))
    time.sleep(1)
    aposta = int(input("\033[1;31mQual o valor da sua aposta?\n\033[0;37m"))
    nova_aposta = 0
    while aposta < 1 or aposta > fichas:
        aposta = int(input("\033[0;37mAposte um valor entre \033[1;37m1 e {}\033[0;37m.\nTente novamente.\n:".format(fichas)))

    time.sleep(1)
    fichas -= aposta
    fichas = loop_jogar(aposta)

    if fase == 'Point':
        print('\033[0;37mAgora você tem \033[1;35m{} \033[0;37mfichas em caixa e mais \033[1;35m{}\033[0;37m fichas em jogo com a aposta \033[1;32mPass Line Bet\033[0;37m.'.format(fichas, aposta))
    else:
        print('\033[0;37mAgora você tem \033[1;35m{} \033[0;37mfichas.'.format(fichas))

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
        time.sleep(1)
        print("Você saiu com \033[1;35m{}\033[0;37m fichas.".format(fichas))
        time.sleep(1)
        print("Obrigado pelo jogo, \033[1;34m{}\033[0;37m! Até mais!".format(nome))