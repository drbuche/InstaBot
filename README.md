
![N|Solid](https://i.imgur.com/33xjIQf.jpg)

# InstaBot

##### Bot para automatizar curtidas e comentários! 

Pretendo adicionar mais funcionalidades e construir uma interface gráfica futuramente!



# Preparando o ambiente:

*\*Os passos com 'ou' representam possíveis soluções para problemas que possam vir a ocorrer, caso a primeira opção não funcione.*

   - Atualize o sistema.
   ```sh
sudo apt-get update 
```

   - Atualize o pip.
   ```sh
pip install --upgrade pip 

ou 

pip3 install --upgrade pip
```

  - Instale o Selenium.
   ```sh
pip install selenium

ou

pip3 install selenium
```
  - Baixe o Webdriver referente ao navegador: [Chrome](https://chromedriver.chromium.org/downloads) ou [Firefox](https://github.com/mozilla/geckodriver/releases)
    - Certifique-se de que a versão do Webdriver é compatível com a do seu navegador!
    - Caso tenha problema com algum navegador, tente com outro.
  - Mova o Webdriver (apenas o driver e não a pasta!) para:
   ```sh
sudo mv ~/local_do_driver/driver /usr/local/bin

ou

sudo mv ~/local_do_driver/driver /usr/bin

```

   - Abra a pasta que contenha o modulo [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py).
   - Abra o terminal dentro desta pasta, execute o seguinte comando:
   ```sh
sudo chmod +x main_bot.py 
```


# Utilizando!
- 1 – Em [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py), coloque as referências na lista.
    - Caso a busca seja feita for hashtags, coloque as hashtags que deseja realizar a busca dentro da lista 'hashtags'.
    - Caso prefira realizar o processo em seguidores de um perfil especifico, preencha a lista ‘perfis’ com os perfis que deseja interagir. Isso fará com que você interaja com os 120 últimos seguidores deste perfil.
- 2 – Coloque os comentários que deseja comentar nas respectivas listas:

	- **primeira_palavra**: Será sempre o primeiro elemento da sentença.
	- **complemento**: Pode ser o elemento logo após a 'primeira_palavra' ou ser o primeiro elemento da sentença, com um emoji logo em seguida.
	- **emoji**: Emoticon que será sempre o último elemento da sentença. 	
	- **Estas listas servem para criar frases aleatórias, unindo elementos distintos de forma randomica para cada comentário. Quanto mais palavras em cada grupo melhor!**
		        	
- 3 – Em [bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/bot.py), no atributo construtor da classe InstagramBot, modifique o self.driver = webdriver.Chrome/Firefox de acordo com o navegador que deseja utilizar (por definição, já esta no Chrome).

- 4 – Abra o terminal dentro da pasta que contenha o arquivo [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py) e use o comando:
 
```sh
./main_bot.py
```

- 4.5 Caso tenha algum problema com a execução do python, altere a primeira linha do modulo [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py) para:
    
 ```sh
#!/usr/bin/env python 
```
- 5 – ?????
- 6 – profit!

# Observações:
- **Durante a execução, você terá a opção de selecionar a idioma do navegador.**
    - **Certifique-se de que escolheu a opção de idioma compatível com seu navegador**
- **O bot exibira uma mensagem contendo a hashtag/perfil atual e a data/hora que inciou o ciclo em cada referência. Também atualizará o número de perfis/hashtags totais que já foram interagidos e data/hora que os finalizou.**
- **Modo apenas like: Da like em 1 foto a cada 1-2 min.**
- **Modo apenas comentar: Comenta 1 foto a cada 6-10min**
- **Modo like e comentar:**
	- *No modo hashtags – Da like a cada 1-2 min e comenta 1x a cada 10 fotos.*
	- *No modo perfil – Comenta a cada 10 fotos e da like em 3-6 fotos de cada perfil.*
- **Use bot com bom senso, como se ele imitasse uma pessoa real. Sugiro rodar entre as 7h da manhã até as 00 horas, em um período de 3-8 horas por dia, deixe alguns dias sem utilizar, etc...**
- **O tempo entre os comentários no modo like+comentar ainda está em teste.**
- **Caso tenha o erro 'Failed to Load.' e não consiga carregar fotos e perfis, tente apagar o arquivo 'geckodriver.log' dentro da pasta instabot, ele é gerado automaticamente ao executar o aplicativo. Além disso, limpe os cookies dos navegadores e certifique-se que não possui outros dispositivos acessando sua conta ao mesmo tempo pelo navegador.** 