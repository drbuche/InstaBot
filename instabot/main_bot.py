#!/usr/bin/env python3
from modos_bot import *
from getpass import getpass
from selecionar_tipo_busca import *

if __name__ == "__main__":

    # Hashtags que deseja pesquisar
    hashtags = ['hashtag1','hashtag2', 'hashtag3',]
    perfis = ['perfil1', 'perfil2', 'perfil3']

    # Combinação de palavras para comentário aleatório -> (a + b) ou (a + c) ou (b + c)
    primeira_palavra = ['Nossa! ', 'WOW! ', 'Sério isso? ', 'CARAMBA! ']
    complemento = ['Que incrível!', 'Que top!', 'Que show!', 'Que TUDO!']
    emoji = ['💙️', '🥰', '🔥', '💥']

    print('--------------------------------------------------------------------------------\n')
    username = input('Qual o usuário?\n')
    password = getpass(prompt='Qual a senha?')
    print('\n--------------------------------------------------------------------------------\n')

    tipo_busca = bot_fazer()
    print('\n--------------------------------------------------------------------------------\n')
    modo_bot = hash_seguidores()
    print('\n--------------------------------------------------------------------------------\n')
    linguagem = linguagem()
    print('\n--------------------------------------------------------------------------------\n')

    if modo_bot == '1':
        com_hashtags(hashtags, tipo_busca, primeira_palavra, complemento, emoji, username, password, modo_bot, linguagem)
    elif modo_bot == '2':
        com_perfil(perfis, tipo_busca, primeira_palavra, complemento, emoji, username, password, modo_bot, linguagem)




