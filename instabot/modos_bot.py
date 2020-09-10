from datetime import datetime
from bot import *


def com_hashtags(hashtags, tipo_busca, primeira_palavra, complemento, emoji, username, password, modo_bot):
    instagram = InstagramBot(username, password, modo_bot)
    instagram.login()
    while True:
        if len(hashtags) == 0:
            instagram.close_browser()
            print('A lista de hashtags acabou!')
            sys.exit()
        try:
            tag = random.choice(hashtags)
            print('--------------------------------------------------------------------------------')
            print(f'\nHashtag: #{tag} iniciada em ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
            instagram.selecionar_fotos_hashtags(tag)
            print(f'Número de hashtags coletados: {len(instagram.pic_hrefs)}.\n')
            eval('instagram.' + tipo_busca)
            print(f'\nHashtag: #{tag} finalizada em ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print('--------------------------------------------------------------------------------\n')
            hashtags.remove(tag)
            instagram.limpar_urefs()
        except Exception:
            instagram.close_browser()
            time.sleep(60)
            instagram.login()


def com_perfil(perfis, tipo_busca, primeira_palavra, complemento, emoji, username, password, modo_bot):
    instagram = InstagramBot(username, password, modo_bot)
    instagram.login()
    while True:
        if len(perfis) == 0:
            instagram.close_browser()
            print('A lista de @perfis acabou!')
            sys.exit()
        try:
            tag = random.choice(perfis)
            print('--------------------------------------------------------------------------------')
            print(f'\nPerfil: @{tag} iniciada em ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            instagram.listar_perfis_do_perfil(tag)
            print(f'Número de perfis coletados: {len(instagram.seguidores_perfil)}.\n')
            while len(instagram.seguidores_perfil) != 0:
                time.sleep(20)
                instagram.selecionar_fotos_perfil()
                eval('instagram.' + tipo_busca)
                instagram.limpar_urefs()
            print(f'\nPerfil: @{tag} finalizado em ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print('--------------------------------------------------------------------------------\n')
            perfis.remove(tag)
        except Exception:
            instagram.close_browser()
            time.sleep(60)
            instagram.login()
