from datetime import datetime
from bot import *


def com_hashtags(hashtags, tipo_busca, primeira_palavra, complemento,
                 emoji, username, password, modo_bot, linguagem, navegador):
    instagram = InstagramBot(username, password, modo_bot, linguagem, navegador)
    instagram.login()
    while True:
        if len(hashtags) != 0:
            try:
                tag = random.choice(hashtags)
                print('--------------------------------------------------------------------------------')
                print(f'\nHashtag: #{tag} iniciada em ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
                instagram.selecionar_fotos_hashtags(tag)
                print(f'Número de hashtags coletados: {len(instagram.pic_hrefs)}.\n')
                instagram.tabela_stdout()
                eval('instagram.' + tipo_busca)
                print('----------------------------------------')
                print(f'\nHashtag: #{tag} finalizada em ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                print('--------------------------------------------------------------------------------\n')
                hashtags.remove(tag)
                instagram.limpar_urefs()
            except Exception:
                instagram.deu_ruim()
        else:
            instagram.close_browser()
            print('A lista de hashtags acabou!  ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sys.exit()


def com_perfil(perfis, tipo_busca, primeira_palavra, complemento,
               emoji, username, password, modo_bot, linguagem, navegador):
    instagram = InstagramBot(username, password, modo_bot, linguagem, navegador)
    time.sleep(5)
    instagram.login()
    while True:
        if len(perfis) != 0:
            try:
                tag = random.choice(perfis)
                print('--------------------------------------------------------------------------------')
                print(f'\nPerfil: @{tag} iniciada em ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                instagram.listar_perfis_do_perfil(tag)
                print(f'Número de seguidores coletados: {len(instagram.seguidores_perfil)}.\n')
                instagram.tabela_stdout()
                while len(instagram.seguidores_perfil) != 0:
                    time.sleep(20)
                    instagram.selecionar_fotos_perfil()
                    eval('instagram.' + tipo_busca)
                    instagram.limpar_urefs()
                print('-------------------------------------------------------------------')
                print(f'\nPerfil: @{tag} finalizado em ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                print('--------------------------------------------------------------------------------\n')
                perfis.remove(tag)
            except Exception:
                instagram.deu_ruim()
        else:
            instagram.close_browser()
            print('A lista de @perfis acabou!  ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sys.exit()

