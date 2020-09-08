from instabot.bot import *
from getpass import getpass
import sys
from datetime import datetime

if __name__ == "__main__":

    funcao = ''

    # Hashtags que deseja pesquisar
    hashtags = ['carros','ragnarok', 'praia', 'freefirebrasil']

    # Combinação de palavras para comentário aleatório -> (a + b) ou (a + c) ou (b + c)
    primeira_palavra = ['Nossa! ', 'WOW! ', 'Sério? ', 'CARAMBA! ']
    complemento = ['Que incrível!', 'Que top!', 'Que show!', 'Que TUDO!']
    emoji = ['💙️', '🥰', '💃', '💥']

    username = input('Qual o usuário?')
    password = getpass(prompt='Qual a senha?')

    while True:
        seleciona_funcao = input('Para apenas comentar,digite 1 (Leva +- 10min entre comentarios para evitar ban).'
                                 '\nPara apenas dar like, digite 2. '
                                 '\nPara comentar e dar like, digite 3 (A cada 10 likes 1 comentario). \n')
        if seleciona_funcao == '1':
            funcao = 'comentar_fotos(primeira_palavra, complemento, emoji)'
            break
        elif seleciona_funcao == '2':
            funcao = 'like_foto()'
            break
        elif seleciona_funcao == '3':
            funcao = 'like_comentar(primeira_palavra, complemento, emoji)'
            break
        else:
            print('Valor invalido!')

    instagram = InstagramBot(username, password)
    instagram.login()

    while True:
        if len(hashtags) == 0:
            instagram.close_browser()
            print('A lista de hashtags acabou!')
            sys.exit()
        try:
            tag = random.choice(hashtags)
            print(f'Hashtag atual: #{tag} em ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            instagram.selecionar_fotos(tag)
            eval('instagram.' + funcao)
            hashtags.remove(tag)
            instagram.limpar_urefs()
        except Exception:
            instagram.close_browser()
            time.sleep(60)
            instagram = InstagramBot(username, password)
            instagram.login()

