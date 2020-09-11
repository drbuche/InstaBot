
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
    - Certifique-se de que a versão do Webdriver é compatível com a do seu navegador!
  - Mova o Webdriver para:
   ```sh
sudo mv ~/local_do_driver/driver /usr/local/bin
```


# Utilizando!
- 1 – Em [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py), coloque as referências na lista.
    - Caso a busca seja feita for hashtags, coloque as hashtags que deseja realizar a busca dentro da lista 'hashtags'.
    - Caso prefira realizar o processo em seguidores de um perfil especifico, preencha a lista ‘perfis’ com os perfis que deseja interagir. Isso fará com que você interaja com os 120 (em média) últimos seguidores deste perfil.
- 2 – Coloque os comentários que deseja comentar nas respectivas listas:

	- primeira_palavra: Será sempre o primeiro elemento da sentença.
	- complemento: Pode ser o elemento logo após a 'primeira_palavra' ou ser o primeiro elemento da sentença, com um emoji logo em seguida.
	- emoji: Emoticon que será sempre o último elemento da sentença. 	
	- **Estas listas servem para criar frases aleatórias, unindo elementos distintos de forma randomica para cada comentário. Quanto mais palavras em cada grupo melhor!**
		        	
- 3 – Em [bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/bot.py), no atributo construtor da classe InstagramBot, modifique o self.driver = webdriver.Chrome/Firefox de acordo com o navegador que deseja utilizar (por definição, já esta no Firefox).
- 3 – run
- 4 – ?????
- 5 – profit!

# Observações:
- **Durante a execução você terá a opção de selecionar a linguagem do navegador.**
    - **Certifique-se de que escolheu a opção de linguagem compatível com seu navegador**
- **O bot exibira uma mensagem contendo a hashtag/perfil atual e a data/hora que inciou o ciclo em cada referência. Também atualizará o número de perfis/hashtags totais que já foram interagidos.**
- **Modo apenas like: Da like em 1 foto a cada 1-2 min.**
- **Modo apenas comentar: Comenta 1 foto a cada 6-10min**
- **Modo like e comentar:**
	- *No modo hashtags – Da like a cada 1-2 min e comenta 1x a cada 10 fotos.*
	- *No modo perfil – Comenta a cada 10 fotos e da like em 3-6 fotos de cada perfil.*
- **O tempo entre os comentários no modo like+comentar ainda está em teste.**