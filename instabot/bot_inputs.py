from getpass import getpass
import i18n
import os

class Inputs:

    def __init__(self):
        i18n.load_path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'locale'))
        i18n.set('filename_format', '{locale}.{format}')
        i18n.set('fallback', 'en')
        print(i18n.t("pass_input"))
        while True:
            print('-----------------------------Software Language----------------------------------')
            language_selection = input("For english: Type 1\n"
                                       "Para Português: Digite 2\n")

            if language_selection =='1':
                self.language = 'en'
                return

            elif language_selection == '2':
                self.language = 'pt'
                return

            else:
                print(i18n.t('invalid_value'))

            print('--------------------------------------------------------------------------------')

    def webdriver(self):
        while True:
            driver = input(i18n.t('webdriver_input'))
            if driver == '1':
                return 'webdriver.Chrome()'
            elif driver == '2':
                return 'webdriver.Firefox()'
            else:
                print(i18n.t('invalid_value'))

    def login_pass(self):
        username = input(i18n.t('username_input'))
        password = getpass(prompt=i18n.t('pass_input'))
        return username, password

    def bot_fazer(self):
        while True:
            seleciona_tarefa = input(i18n.t('bot_fazer'))
            if seleciona_tarefa == '1':
                return ['comentar_fotos', primeira_palavra, complemento, emoji]
            elif seleciona_tarefa == '2':
                return ['like_foto']
            elif seleciona_tarefa == '3':
                return ['like_comentar', primeira_palavra, complemento, emoji]
            else:
                print(i18n.t('invalid_value'))

    def hash_seguidores(self, hashtags):
        while True:
            seleciona_tarefa = input(i18n.t('hash_seguidores'))
            if seleciona_tarefa == '1':
                print('\n--------------------------------------------------------------------------------\n')
                self.hash_local_trends(hashtags)
                print('\n--------------------------------------------------------------------------------\n')
                return ['com_hashtags', hashtags, tipo_busca, primeira_palavra, complemento,
                        emoji, username, password, modo_bot, linguagem, navegador, inicio]
            elif seleciona_tarefa == '2':
                return ['com_perfil', perfis, tipo_busca, primeira_palavra, complemento,
                        emoji, username, password, modo_bot, linguagem, navegador, inicio]
            else:
                print(i18n.t('invalid_value'))

    def hash_local_trends(self, hashtags):
        while True:
            local_trends = input(i18n.t('hash_local_trends'))
            if local_trends == '1':
                return print(i18n.t('suas_hash') + str(hashtags))
            elif local_trends == '2':
                hashtags.clear()
                #Futuro auto execute do scrapy para diferentes SO
                top_5_hashtags = open("top_5_hashtags_do_dia.txt", "r")
                hashtags_bruta = top_5_hashtags.readlines()
                hashtags_lista = str(hashtags_bruta).replace('\'', '').replace('[', '').replace(']', '').split(',')
                for hashtag in hashtags_lista:
                    hashtags.append(hashtag)
                print(i18n.t('top_hash') + str(hashtags))
                return top_5_hashtags.close()

            else:
                print(i18n.t('invalid_value'))

    def linguagem(self):
        while True:
            lingua = input(i18n.t('linguagem'))
            if lingua == '1' or lingua == '2':
                return lingua
            else:
                print(i18n.t('invalid_value'))
