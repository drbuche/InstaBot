from instabot.bot import *
from getpass import getpass
import sys
from datetime import datetime

if __name__ == "__main__":

    funcao = ''
    hashtags = ['lolbr','festa', 'gamer', 'rpg']
    comentarios = ["Show!", "S2 S2!", "Amei!", "STATUS ATUAL: APAIXONADA!"]

    username = input('Qual o usuário?')
    password = getpass(prompt='Qual a senha?')

    while True:
        seleciona_funcao = input('Para apenas comentar,digite 1. \nPara apenas dar like, digite 2. '
                                 '\nPara comentar e dar like, digite 3. \n')
        if seleciona_funcao == '1':
            funcao = 'comentar_fotos(comentarios)'
            break
        elif seleciona_funcao == '2':
            funcao = 'like_foto()'
            break
        elif seleciona_funcao == '3':
            funcao = 'like_comentar(comentarios)'
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

