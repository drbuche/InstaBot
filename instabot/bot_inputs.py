from getpass import getpass


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


def linguagem():
    while True:
        lingua = input('Qual o idioma do seu navegador?'
                          '\nDigite 1 para Inglês\n'
                          'Digite 2 para Português\n')
        if lingua == '1' or lingua == '2':
            return lingua
        else:
            print('Valor inválido!')
