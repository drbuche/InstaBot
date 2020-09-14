from getpass import getpass


def webdriver():
    while True:
        driver = input('Qual seu Webdriver?\n'
                       'Chrome: digite 1.\n'
                       'Firefox: digite 2.\n')
        if driver == '1':
            return 'webdriver.Chrome()'
        elif driver == '2':
            return 'webdriver.Firefox()'
        else:
            print('Valor inválido!')


def login_pass():
    username = input('Qual o usuário?\n')
    password = getpass(prompt='\nQual a senha?')
    return username, password


def bot_fazer():
    while True:
        seleciona_tarefa = input('Para apenas comentar,digite 1 (Leva de 6-10 min entre comentários).'
                                 '\nPara apenas dar like, digite 2 (1 like a cada 1-2 min). '
                                 '\nPara comentar e dar like, digite 3 (A cada 10 likes 1 comentário). \n')
        if seleciona_tarefa == '1':
            return 'comentar_fotos(primeira_palavra, complemento, emoji)'
        elif seleciona_tarefa == '2':
            return 'like_foto()'
        elif seleciona_tarefa == '3':
            return 'like_comentar(primeira_palavra, complemento, emoji)'
        else:
            print('Valor inválido!')


def hash_seguidores():
    while True:
        seleciona_tarefa = input('Para trabalhar em hashtags digite 1.'
                                 '\nPara trabalhar em seguidores de um perfil digite 2.\n')
        if seleciona_tarefa == '1' or seleciona_tarefa == '2':
            return seleciona_tarefa
        else:
            print('Valor inválido!')


def hash_local_trends(hashtags):
    while True:
        local_trends = input('Para trabalhar em hashtags personalizadas, digite 1.'
                             '\nPara trabalhar com as top 5 # do brasil (da última hora no twitter), digite 2.\n')
        if local_trends == '1':
            return print(f'Suas hashtags são: ' + str(hashtags))
        elif local_trends == '2':
            hashtags.clear()
            #Futuro auto execute do scrapy para diferentes SO
            top_5_hashtags = open("top_5_hashtags_do_dia.txt", "r")
            hashtags_bruta = top_5_hashtags.readlines()
            hashtags_lista = str(hashtags_bruta).replace('\'', '').replace('[', '').replace(']', '').split(',')
            for hashtag in hashtags_lista:
                hashtags.append(hashtag)
            print(f'As top 5 hashtags são: ' + str(hashtags))
            return top_5_hashtags.close()

        else:
            print('Valor inválido!')


def linguagem():
    while True:
        lingua = input('Qual o idioma do seu navegador?'
                          '\nDigite 1 para Inglês\n'
                          'Digite 2 para Português\n')
        if lingua == '1' or lingua == '2':
            return lingua
        else:
            print('Valor inválido!')
