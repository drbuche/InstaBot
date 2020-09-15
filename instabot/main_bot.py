#!/usr/bin/env python3
from modos_bot import *
from bot_inputs import *

if __name__ == "__main__":

    # Hashtags que deseja pesquisar
    hashtags = ['hashtag1', 'hashtag2', 'hashtag3']
    perfis = ["nerdbunker"]

    # Combinação de palavras para comentário aleatório -> (a + b) ou (a + c) ou (b + c)
    primeira_palavra = ['Nossa! ', 'WOW! ', 'Sério isso? ', 'CARAMBA! ']
    complemento = ['Que incrível!', 'Que top!', 'Que show!', 'Que TUDO!']
    emoji = ['💙️', '🥰', '🔥', '💥']

    print('--------------------------------------------------------------------------------\n')
    navegador = webdriver()
    print('--------------------------------------------------------------------------------\n')
    username, password = login_pass()
    print('\n--------------------------------------------------------------------------------\n')
    tipo_busca = bot_fazer()
    print('\n--------------------------------------------------------------------------------\n')
    modo_bot = hash_seguidores(hashtags)
    print('\n--------------------------------------------------------------------------------\n')
    linguagem = linguagem()
    print('\n--------------------------------------------------------------------------------\n')

    eval(modo_bot)
