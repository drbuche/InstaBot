from getpass import getpass
from language import *


class Inputs:

    def __init__(self):
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
                print('Invalid Value!')

            print('--------------------------------------------------------------------------------')

    def webdriver(self):
        while True:
            driver = input(eval(self.language + '_webdriver_input'))
            if driver == '1':
                return 'webdriver.Chrome()'
            elif driver == '2':
                return 'webdriver.Firefox()'
            else:
                print('Valor inválido!')

    def login_pass(self):
        username = input(eval(self.language + '_username_input'))
        password = getpass(prompt=eval(self.language + '_pass_input'))
        return username, password

    def bot_fazer(self):
        while True:
            seleciona_tarefa = input(eval(self.language + '_bot_fazer'))
            if seleciona_tarefa == '1':
                return 'comentar_fotos(primeira_palavra, complemento, emoji)'
            elif seleciona_tarefa == '2':
                return 'like_foto()'
            elif seleciona_tarefa == '3':
                return 'like_comentar(primeira_palavra, complemento, emoji)'
            else:
                print('Invalid Value!')

    def hash_seguidores(self, hashtags):
        while True:
            seleciona_tarefa = input(eval(self.language + '_hash_seguidores'))
            if seleciona_tarefa == '1':
                print('\n--------------------------------------------------------------------------------\n')
                self.hash_local_trends(hashtags)
                print('\n--------------------------------------------------------------------------------\n')
                return 'com_hashtags(hashtags, tipo_busca, primeira_palavra, complemento, ' \
                       'emoji, username, password, modo_bot, linguagem, navegador, inicio)'
            elif seleciona_tarefa == '2':
                return 'com_perfil(perfis, tipo_busca, primeira_palavra, complemento, ' \
                       'emoji, username, password, modo_bot, linguagem, navegador, inicio)'
            else:
                print('Invalid Value!')

    def hash_local_trends(self, hashtags):
        while True:
            local_trends = input(eval(self.language + '_hash_local_trends'))
            if local_trends == '1':
                return print(eval(self.language + '_suas_hash') + str(hashtags))
            elif local_trends == '2':
                hashtags.clear()
                #Futuro auto execute do scrapy para diferentes SO
                top_5_hashtags = open("top_5_hashtags_do_dia.txt", "r")
                hashtags_bruta = top_5_hashtags.readlines()
                hashtags_lista = str(hashtags_bruta).replace('\'', '').replace('[', '').replace(']', '').split(',')
                for hashtag in hashtags_lista:
                    hashtags.append(hashtag)
                print(eval(self.language + '_top_hash') + str(hashtags))
                return top_5_hashtags.close()

            else:
                print('Invalid Value!')

    def linguagem(self):
        while True:
            lingua = input(eval(self.language + '_linguagem'))
            if lingua == '1' or lingua == '2':
                return lingua
            else:
                print('Invalid Value!')
