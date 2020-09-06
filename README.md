
![N|Solid](https://i.imgur.com/33xjIQf.jpg)

# InstaBot

##### Bot para automatizar curtidas e comentários! 

Pretendo adicionar mais funcionalidades e construir uma interface gráfica futuramente!



#### Preparando o ambiente:
   - Atualize o pip.
   ```sh
$ pip install --upgrade pip 
```
  - Instale o Selenium.
   ```sh
$ pip install selenium
```
  - Baixe o Webdriver ou utilize o que deixei na pasta - Baixe o Webdriver ou utilize o que deixei na pasta ['Webdriver'](https://github.com/drbuche/InstaBot/tree/master/Webdriver).
  - Mova o Webdriver para:
   ```sh
sudo mv ~/local_do_driver/driver /usr/local/bin
```


# Utilizando!
- 1 - Em [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py), coloque as hashtags que deseja realizar a busca dentro da lista hashtags.
- 2 – Coloque os comentarios que deseja comentar na lista comentarios.
- 3 - Em [bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/bot.py), no atributo construtor da classe InstagramBot, modifique o self.driver = webdriver.Chrome/Firefox de acordo com o navegador que deseja utilizar (por definição, já esta no Firefox, indico usá-lo).
- 3 - run
- 4 – ?????
- 5 – profit!
