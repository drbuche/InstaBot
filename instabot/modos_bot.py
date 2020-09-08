from datetime import datetime
from instabot.bot import *
import sys


def com_hashtags(hashtags, tipo_busca, primeira_palavra, complemento, emoji, username, password):
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
            instagram.selecionar_fotos_hashtags(tag)
            eval('instagram.' + tipo_busca)
            hashtags.remove(tag)
            instagram.limpar_urefs()
        except Exception:
            instagram.close_browser()
            time.sleep(60)
            instagram = InstagramBot(username, password)
            instagram.login()


def com_perfil(perfis, tipo_busca, primeira_palavra, complemento, emoji, username, password):
    instagram = InstagramBot(username, password)
    instagram.login()
    while True:
        if len(perfis) == 0:
            instagram.close_browser()
            print('A lista de hashtags acabou!')
            sys.exit()
        try:
            tag = random.choice(perfis)
            print(f'Perfil atual: #{tag} em ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            instagram.listar_perfis_do_perfil(tag)
            while len(instagram.seguidores_perfil) != 0:
                time.sleep(20)
                instagram.selecionar_fotos_perfil()
                eval('instagram.' + tipo_busca)
                instagram.limpar_urefs()
            perfis.remove(tag)
        except Exception:
            instagram.close_browser()
            time.sleep(60)
            instagram = InstagramBot(username, password)
            instagram.login()
