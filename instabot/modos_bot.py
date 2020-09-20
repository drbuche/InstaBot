from datetime import datetime
from bot import *
from language import *


def com_hashtags(hashtags, tipo_busca, primeira_palavra, complemento,
                 emoji, username, password, modo_bot, linguagem, navegador, inicio):
    instagram = InstagramBot(username, password, modo_bot, linguagem, navegador, inicio)
    time.sleep(5)
    instagram.login()
    while True:
        if len(hashtags) != 0:
            try:
                tag = random.choice(hashtags)
                print('--------------------------------------------------------------------------------')
                print(f'\nHashtag: #{tag} ' + eval(inicio.language + '_com_hashtags_inicia') + ' ' +
                      datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
                instagram.selecionar_fotos_hashtags(tag)
                print(f'{eval(inicio.language + "_num_com_hashtags_coletadas")} {len(instagram.pic_hrefs)} \n')
                instagram.tabela_stdout()
                eval('instagram.' + tipo_busca)
                print('\n----------------------------------------\n')
                print(f'\nHashtag: #{tag} ' + eval(inicio.language + '_com_hashtags_finalizada') +
                      datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                print('\n--------------------------------------------------------------------------------\n')
                hashtags.remove(tag)
                instagram.limpar_urefs()
            except Exception as e:
                print(f'\n {e} \n')
                instagram.deu_ruim()
        else:
            instagram.close_browser()
            print(eval(inicio.language + '_lista_com_hashtags_acabou') + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sys.exit()


def com_perfil(perfis, tipo_busca, primeira_palavra, complemento,
               emoji, username, password, modo_bot, linguagem, navegador, inicio):
    instagram = InstagramBot(username, password, modo_bot, linguagem, navegador, inicio)
    time.sleep(5)
    instagram.login()
    while True:
        if len(perfis) != 0:
            try:
                tag = random.choice(perfis)
                print('--------------------------------------------------------------------------------')
                print('\n' + eval(inicio.language + "_sem_hashtags_inicia") + f'@{tag} ' + eval(inicio.language +
                      "_com_hashtags_inicia") + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                instagram.listar_perfis_do_perfil(tag)
                print(f'{eval(inicio.language + "_sem_hashtags_numero_seg")} {len(instagram.seguidores_perfil)}.\n')
                instagram.tabela_stdout()
                while len(instagram.seguidores_perfil) != 0:
                    time.sleep(20)
                    instagram.selecionar_fotos_perfil()
                    eval('instagram.' + tipo_busca)
                    instagram.limpar_urefs()
                print('\n-------------------------------------------------------------------\n')
                print('\n' + eval(inicio.language + "_sem_hashtags_inicia") + f' @{tag} ' + eval(inicio.language +
                      "_com_hashtags_finalizada") + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                print('\n--------------------------------------------------------------------------------\n')
                perfis.remove(tag)
            except Exception as e:
                print(f'\n {e} \n')
                instagram.deu_ruim()
        else:
            instagram.close_browser()
            print(eval(inicio.language + '_lista_sem_hashtags_acabou') + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sys.exit()

