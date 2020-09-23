from datetime import datetime
from bot import *
import i18n


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
                print(f'\nHashtag: #{tag} ' + i18n.t('com_hashtags_inicia') + ' ' +
                      datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
                instagram.selecionar_fotos_hashtags(tag)
                print(f'{i18n.t("num_com_hashtags_coletadas")} {len(instagram.pic_hrefs)} \n')
                instagram.tabela_stdout()
                eval('instagram.' + tipo_busca)
                print('\n----------------------------------------\n')
                print(f'\nHashtag: #{tag} ' + i18n.t('com_hashtags_finalizada') +
                      datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                print('\n--------------------------------------------------------------------------------\n')
                hashtags.remove(tag)
                instagram.limpar_urefs()
            except Exception as e:
                print(f'\n {e} \n')
                instagram.deu_ruim()
        else:
            instagram.close_browser()
            print(i18n.t('lista_com_hashtags_acabou') + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sys.exit()


def com_local(local, tipo_busca, primeira_palavra, complemento,
                 emoji, username, password, modo_bot, linguagem, navegador, inicio):
    instagram = InstagramBot(username, password, modo_bot, linguagem, navegador, inicio)
    time.sleep(5)
    instagram.login()
    while True:
        if len(local) != 0:
            try:
                tag = random.choice(local)
                regex_tag = tag.replace('https://www.instagram.com/explore/locations/', '').split('/')
                print('--------------------------------------------------------------------------------')
                print(f'\nLocal: 📍{regex_tag[1]} ' + i18n.t('com_hashtags_inicia') + ' ' +
                      datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
                instagram.selecionar_fotos_local(tag)
                print(f'{i18n.t("num_com_hashtags_coletadas")} {len(instagram.pic_hrefs)} \n')
                instagram.tabela_stdout()
                eval('instagram.' + tipo_busca)
                print('\n----------------------------------------\n')
                print(f'\nLocal: 📍{regex_tag[1]} ' + i18n.t('lista_com_locais_acabou') +
                      datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                print('\n--------------------------------------------------------------------------------\n')
                local.remove(tag)
                instagram.limpar_urefs()
            except Exception as e:
                print(f'\n {e} \n')
                instagram.deu_ruim()
        else:
            instagram.close_browser()
            print(i18n.t('lista_com_hashtags_acabou') + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
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
                print('\n' + i18n.t("sem_hashtags_inicia") + f'@{tag} ' + i18n.t("com_hashtags_inicia")
                 + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                instagram.listar_perfis_do_perfil(tag)
                print(f'{i18n.t("sem_hashtags_numero_seg")} {len(instagram.seguidores_perfil)}.\n')
                instagram.tabela_stdout()
                while len(instagram.seguidores_perfil) != 0:
                    time.sleep(20)
                    instagram.selecionar_fotos_perfil()
                    eval('instagram.' + tipo_busca)
                    instagram.limpar_urefs()
                print('\n-------------------------------------------------------------------\n')
                print('\n' + i18n.t("sem_hashtags_inicia") + f' @{tag} ' + i18n.t("com_hashtags_finalizada")
                 + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                print('\n--------------------------------------------------------------------------------\n')
                perfis.remove(tag)
            except Exception as e:
                print(f'\n {e} \n')
                instagram.deu_ruim()
        else:
            instagram.close_browser()
            print(i18n.t('lista_sem_hashtags_acabou') + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sys.exit()

