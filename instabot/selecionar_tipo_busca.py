def bot_fazer():
    while True:
        seleciona_tarefa = input('Para apenas comentar,digite 1 (Leva +- 10min entre comentarios para evitar ban).'
                                 '\nPara apenas dar like, digite 2. '
                                 '\nPara comentar e dar like, digite 3 (A cada 10 likes 1 comentario). \n')
        if seleciona_tarefa == '1':
            return 'comentar_fotos(primeira_palavra, complemento, emoji)'
        elif seleciona_tarefa == '2':
            return 'like_foto()'
        elif seleciona_tarefa == '3':
            return 'like_comentar(primeira_palavra, complemento, emoji)'
        else:
            print('Valor invalido!')


def hash_seguidores():
    while True:
        seleciona_tarefa = input('Para trabalhar em hashtags digite 1.'
                                 '\nPara trabalhar em seguidores de um perfil digite 2.\n')
        if seleciona_tarefa == '1' or seleciona_tarefa == '2':
            return seleciona_tarefa
        else:
            print('Valor invalido!')
