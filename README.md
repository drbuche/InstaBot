
![N|Solid](https://i.imgur.com/33xjIQf.jpg)

# InstaBot

##### Bot para automatizar curtidas e comentários! 

Pretendo adicionar mais funcionalidades e construir uma interface gráfica futuramente!



#### Preparando o ambiente:
   - Atualize o pip.
   ```sh
pip install --upgrade pip 
```
  - Instale o Selenium.
   ```sh
pip install selenium
```
  - Baixe o Webdriver referente ao navegador: [Chrome](https://chromedriver.chromium.org/downloads) ou [Firefox](https://github.com/mozilla/geckodriver/releases)
  - Mova o Webdriver para:
   ```sh
sudo mv ~/local_do_driver/driver /usr/local/bin
```


# Utilizando!
- 1 – Em [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py), coloque as hashtags que deseja realizar a busca dentro da lista 'hashtags'.
    - Caso prefira realizar o processo em seguidores de um perfil especifico, preencha a lista ‘perfis’ com os perfis que deseja interagir. Isso fara com que você interaja com os 108 últimos seguidores deste perfil.
- 2 – Coloque os comentários que deseja comentar nas respectivas listas:

	- primeira_palavra: Será sempre o primeiro elemento da sentença.
	- complemento: Pode ser o elemento logo após a 'primeira_palavra' ou ser o primeiro elemento da sentença, com um emoji logo em seguida.
	- emoji: Emoticon que será sempre o último elemento da sentença. 	
	- **Estas listas servem para criar frases aleatórias, unindo elementos distintos de forma randomica para cada comentário.**
		        	
- 3 – Em [bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/bot.py), no atributo construtor da classe InstagramBot, modifique o self.driver = webdriver.Chrome/Firefox de acordo com o navegador que deseja utilizar (por definição, já esta no Firefox, indico usá-lo).
- 3 – run
- 4 – ?????
- 5 – profit!

*obs: O bot exibira uma mensagem contendo a hashtag/perfil atual e a data/hora que inciou o ciclo na referente hashtag.*