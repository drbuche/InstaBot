#!/usr/bin/env python3
from modos_bot import *
from bot_inputs import *
import os
import i18n

if __name__ == "__main__":
    # Software - Lenguage Selection
    inicio = Inputs()
    i18n.set('locale', inicio.language)

    # Hashtags que deseja pesquisar
    hashtags = ['hashtag1', 'hashtag2', 'hashtag3']
    perfis = ["perfil1", "perfil2", "perfil3"]

    # Combinação de palavras para comentário aleatório -> (a + b) ou (a + c) ou (b + c)
    primeira_palavra = ['Nossa! ', 'WOW! ', 'Sério isso? ', 'CARAMBA! ']
    complemento = ['Que incrível!', 'Que top!', 'Que show!', 'Que TUDO!']
    emoji = ['💙️', '🥰', '🔥', '💥']

    print('--------------------------------------------------------------------------------\n')
    navegador = inicio.webdriver()
    print('--------------------------------------------------------------------------------\n')
    username, password = inicio.login_pass()
    print('\n--------------------------------------------------------------------------------\n')
    tipo_busca = inicio.bot_fazer()
    print('\n--------------------------------------------------------------------------------\n')
    modo_bot = inicio.hash_seguidores(hashtags)
    print('\n--------------------------------------------------------------------------------\n')

    eval(modo_bot)
