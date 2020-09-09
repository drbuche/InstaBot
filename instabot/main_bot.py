from instabot.modos_bot import *
from getpass import getpass
from instabot.selecionar_tipo_busca import *

if __name__ == "__main__":

    # Hashtags que deseja pesquisar
    hashtags = ['emcasa','minecraftbrasil', 'gamerbrasil', 'freefirebrasil']
    perfis = ['otakupt_oficial', 'leagueoflegendsbrasil', 'animes_brasil.1']

    # Combinação de palavras para comentário aleatório -> (a + b) ou (a + c) ou (b + c)
    primeira_palavra = ['Nossa! ', 'WOW! ', 'Sério isso? ', 'CARAMBA! ']
    complemento = ['Que incrível!', 'Que top!', 'Que show!', 'Que TUDO!']
    emoji = ['💙️', '🥰', '💃', '💥']

    username = input('Qual o usuário?')
    password = getpass(prompt='Qual a senha?')

    tipo_busca = bot_fazer()
    modo_bot = hash_seguidores()

    if modo_bot == '1':
        com_hashtags(hashtags, tipo_busca, primeira_palavra, complemento, emoji, username, password)
    elif modo_bot == '2':
        com_perfil(perfis, tipo_busca, primeira_palavra, complemento, emoji, username, password)




