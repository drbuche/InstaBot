
![N|Solid](https://i.imgur.com/33xjIQf.jpg)

# InstaBot - Python: Selenium + Scrapy

### Guide Language / Idioma do Guia:
   - [English Guide](#english-guide)
   - [Guia em Português](#guia-em-português)

***The bot works 100% in Portuguese and English!***   
***O bot funciona 100% em Português e Ingles!***

# English Guide

### What he does?

Bot to automate likes and comments using Selenium and Scrapy!

- [x] Just Like photos.
- [x] Just Comment on photos.
- [x] Like and Comment on photos.
- [x] It has 2 search modes.
    - Hashtags.
    - Followers of a profile.
- [x] It has a sub-mode that searches for Twitter Trending Topics and Hashtags in Brazil.(Improving)

*I intend to add more features and build a graphical interface in the future!*


# Index:
   
   - [Preparing the environment](#preparing-the-environment) 
        - [On Linux](#on-linux)
        - [On Windows](#on-windows)
        
   - [Using!](#using)
   
   - [Bot performance!](#bot-performance)
   
   - [Observations](#observation)

# Preparing the environment:

*\*The steps with 'or' represent possible solutions to problems that may occur if the first option does not work.*

## On Linux:
   - Update the system.
   
`` sh
sudo apt-get update
``


   - Update the pip.
   ```sh
pip install --upgrade pip 

or

pip3 install --upgrade pip
```

  - Install Selenium.
   ```sh
pip install selenium

or

pip3 install selenium
```
  - Install Scrapy.
   ```sh
pip install scrapy

or

pip3 install scrapy
```

  - Download the Webdriver for the browser: [Chrome](https://chromedriver.chromium.org/downloads) or [Firefox](https://github.com/mozilla/geckodriver/releases).
    - Make sure that the version of Webdriver is compatible with that of your browser!
    - If you have a problem with any browser, try another.
    - **I indicate the use of Firefox, as Chrome has some compatibility problems with the 'Comment' mode.**
  - Move the Webdriver (just the driver and not the folder!) To:
   ```sh
sudo mv ~/local_do_driver/driver /usr/local/bin

or

sudo mv ~/local_do_driver/driver /usr/bin

```

   - Open the folder containing the [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py) module.
   - Open the terminal inside this folder and execute the commands:
   ```sh
sudo chmod +x main_bot.py 

sudo chmod +x scrapy_twitter.py
```

## On Windows:

- Download [Python](https://www.python.org/downloads/) and install. (remember to check the Path option)
   
- Update the pip at the prompt with the command:
 ```sh
-m pip install --upgrade pip

or 

pip install --upgrade pip 
```

- Install Selenium with the command:
```sh
pip install selenium
```
- Install Scrapy with the command:
```sh
pip install scrapy
```
- If you have problems installing Scrapy, you should download [Anaconda](https://www.anaconda.com/products/individual).
    - After installing, open the Anaconda Prompt (anaconda3) and enter the command:
```sh
conda install scrapy
```

   - All procedures related to the `Scrapy` commands of the topic [Using!](#using), must be performed within this prompt.
   - If you prefer, you can install selenium inside Anaconda, after that you can perform all InstaBot commands within this prompt.

```sh
conda install selenium
```   
    

- Download the Webdriver for the browser: [Chrome](https://chromedriver.chromium.org/downloads) or [Firefox](https://github.com/mozilla/geckodriver/releases).
    
    - Make sure that the version of Webdriver is compatible with that of your browser!
    - If you have a problem with any browser, try another.
    - **I indicate the use of Firefox, as Chrome has some compatibility problems with the 'Comment' mode.** 
    - Move the Webdriver (only the driver and not the folder!) To the folder containing the module [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py).

# Using!
- 1 - In [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py) put the references in the list (*you can open it with any Notepad or using an IDE*) .
    - If the search is made for hashtags, place the hashtags you want to perform the search in the 'hashtags' list or, if you choose Trending Hashtags, make sure you have performed the scraping (step 2.5).
    - If you prefer to perform the process on followers of a specific profile, fill out the ‘perfis’ list with the profiles you want to interact with. This will make you interact with the last 120 followers of this profile.

- 2 - Put the comments you want to comment on the respective lists:

	- **first_word**: It will always be the first element of the sentence.
    - **complement**: It can be the element right after the 'first_word' or it can be the first element of the sentence, with an emoji right after it.
    - **emoji**: Emoticon that will always be the last element of the sentence.
    - **Note: Emoticons don't usually work on Chrome, only on Firefox.** 
    - ***These lists are used to create random phrases, joining different elements randomly for each comment. The more words in each group the better!***

- 2.5 - If you chose to use the 'Trending Hashtags' mode, we need to perform the scraping manually:
    - Open the terminal in the folder containing the [scrapy_twitter.py](https://github.com/drbuche/InstaBot/blob/master/instabot/scrapy_twitter.py)
    - Enter the command:
```sh
scrapy runspider scrapy_twitter.py
```
		        	
3 - Open the terminal inside the folder that contains the file [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py) and use the command:
 
- Linux:
```sh
./main_bot.py
```

- Windows:
```sh
cd C:\Users\etc\etc\até_o_local_do_main_bot.py

python main_bot.py
```


3.5 If you have any problems with python execution, change the first line of the module [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py) to:
    
 ```sh
#!/usr/bin/env python 

ou

#!/usr/bin/env python3 
```
- 4 – ?????
- 5 – profit!

# Bot Performance!

- I created an account, put some photos and followed some groups of bands, games, etc ...

- So far, with 8 days of use, the account has left ZERO and has:
    - **205 Followers.**
    - **711 Likes on the photos.**
    - **30 comments on photos.**
    - **More than 30 DM's.**

  
<p align="center">
  <img src="https://i.imgur.com/6SsM3FR.jpg">
</p>  

- Bot has been running on this account since September 11th. (8 days of use)
- I'm running the Bot for 6-8 hours a day.
- Use in **"comment + like"** mode on **profile followers**.
- To interact with the last 120 followers of the profile, I look for profiles that have an average of 15 to 50 thousand followers. (profiles with more than 100,000 followers are good, but tend to have a lot of fake accounts ...)
- I select profiles that have a niche similar to my instagram account profile.


![N|Solid](https://i.imgur.com/IjinG9z.jpg)  


<p align="center">
  <img src="https://i.imgur.com/AEkS4Uj.jpg">
</p>  

<p align="right">
  <img src="https://i.imgur.com/FVo2fb7.jpg">
</p>  

# Observation:

- **During execution, you will have the option to select the Webdriver you want to use, in addition to selecting the browser language.**
- **Make sure you choose the language option compatible with your browser, as well as that of Webdriver**
- **The bot will display a message containing the current hashtag / profile and the date / time that started the cycle in each reference. It will also update the number of profiles / total hashtags that have already been interacted and the date / time that completed them.**
- **Like only mode: Like 1 photo every 1-2 min.**
- **Comment only mode: Comment 1 photo every 6-10min**
- **Like and Comment mode:**
    - *In hashtags mode - Like every 1-2 min and comment 1x every 10 photos.*
    - *In profile mode - Comment every 10 photos and like 3-6 photos of each profile.*
- **Trending mode Hashtags collects the top 5 of the last 24h on twitter.**
    - Repeat step 2.5 of the topic [Using!](#using) whenever you want to update the list of # of the day. Otherwise, it will keep the old ones.
    - *It creates a file called [top_5_hashtags_do_dia.txt](https://github.com/drbuche/InstaBot/blob/master/instabot/top_5_hashtags_do_dia.txt), which stores the # used in the last run. This file is overwritten with each execution*
- **Use bot with common sense, as if he imitated a real person. I suggest running between 7 am until 00 am, in a period of 3-8 hours a day, leave a few days unused, etc ...**
- **The time between comments in like + comment mode is still being tested.**
- **If you have the error 'Failed to Load.' and can't upload photos and profiles, try to delete the 'geckodriver.log' file inside the instabot folder, it is automatically generated when you run the application. Also, clear your browser's cookies and make sure you don't have any other devices accessing your account at the same time through the browser.**


# [Guia em Português]()
## O que é?

Bot para automatizar curtidas e comentários usando Selenium e Scrapy! 

- [x] Apenas Curtir fotos.
- [x] Apenas Comentar em fotos.
- [x] Curtir e Comentar em fotos.
- [x] Possui 2 modos de busca.
    - Hashtags.
    - Seguidores de um perfil.
- [x] Possui um sub-modo que busca por Trending Topics e Hashtags do twitter no Brasil.

*Pretendo adicionar mais funcionalidades e construir uma interface gráfica futuramente!*

# Sumário:
    
   - [Preparando o ambiente](#preparando-o-ambiente)
        - [Linux](#linux)       
        - [Windows](#windows)
        
   - [Utilizando!](#utilizando)
   
   - [Desempenho do Bot!](#desempenho-do-bot)
   
   - [Observações](#observações)

# Preparando o ambiente:

*\*Os passos com 'ou' representam possíveis soluções para problemas que possam vir a ocorrer, caso a primeira opção não funcione.*

## Linux:
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
  - Instale o Scrapy.
   ```sh
pip install scrapy

ou

pip3 install scrapy
```

  - Baixe o Webdriver referente ao navegador: [Chrome](https://chromedriver.chromium.org/downloads) ou [Firefox](https://github.com/mozilla/geckodriver/releases).
    - Certifique-se de que a versão do Webdriver é compatível com a do seu navegador!
    - Caso tenha problema com algum navegador, tente com outro.
    - **Indico a utilização do Firefox, pois o Chrome apresenta alguns problemas de compatibilidade com o modo 'Comment'.**
  - Mova o Webdriver (apenas o driver e não a pasta!) para:
   ```sh
sudo mv ~/local_do_driver/driver /usr/local/bin

ou

sudo mv ~/local_do_driver/driver /usr/bin

```

   - Abra a pasta que contém o modulo [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py).
   - Abra o terminal dentro desta pasta e execute os comandos:
   ```sh
sudo chmod +x main_bot.py 

sudo chmod +x scrapy_twitter.py
```


## Windows:

- Baixe o [Python](https://www.python.org/downloads/) e instale (lembre-se de marcar a opção Path).
   
- Atualize o pip no prompt com o comando:
 ```sh
-m pip install --upgrade pip

ou 

pip install --upgrade pip 
```

- Instale o Selenium com o comando:
```sh
pip install selenium
```
- Instale o Scrapy com o comando:
```sh
pip install scrapy
```
- Caso tenha problemas na instalação do Scrapy, você deve baixar o [Anaconda](https://www.anaconda.com/products/individual).
    - Após instalar, abra o Anaconda Prompt (anaconda3) e digite o comando:
```sh
conda install scrapy
```

   - Todos os procedimentos referente aos comandos `Scrapy` do tópidco [Utilizando!](#utilizando) , devem ser realizados dentro deste prompt.
   - Caso preferir, você pode instalar o selenium dentro do Anaconda, após isso você pode realizar todos os comandos do InstaBot dentro deste prompt.

```sh
conda install selenium
```   
    

- Baixe o Webdriver referente ao navegador: [Chrome](https://chromedriver.chromium.org/downloads) ou [Firefox](https://github.com/mozilla/geckodriver/releases).
    - Certifique-se de que a versão do Webdriver é compatível com a do seu navegador!
    - Caso tenha problema com algum navegador, tente com outro.
    - **Indico a utilização do Firefox, pois o Chrome apresenta alguns problemas de compatibilidade com o modo 'Comment'.**
    - Mova o Webdriver (apenas o driver e não a pasta!) para a pasta que contém o modulo [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py).




# Utilizando!
- 1 – Em [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py) coloque as referências na lista (*você pode abri-lo com qualquer Notepad ou utilizando uma IDE*) .
    - Caso a busca seja feita for hashtags, coloque as hashtags que deseja realizar a busca dentro da lista 'hashtags' ou, caso opte por Trending Hashtags,  certifique-se de ter realizado o scraping (passo 2.5).
    - Caso prefira realizar o processo em seguidores de um perfil especifico, preencha a lista ‘perfis’ com os perfis que deseja interagir. Isso fará com que você interaja com os 120 últimos seguidores deste perfil.

- 2 – Coloque os comentários que deseja comentar nas respectivas listas:

	- **primeira_palavra**: Será sempre o primeiro elemento da sentença.
	- **complemento**: Pode ser o elemento logo após a 'primeira_palavra' ou ser o primeiro elemento da sentença, com um emoji logo em seguida.
	- **emoji**: Emoticon que será sempre o último elemento da sentença.
	    - **Obs: Emoticons não costumam funcionar no Chrome, apenas no Firefox.* 	
	- **Estas listas servem para criar frases aleatórias, unindo elementos distintos de forma randomica para cada comentário. Quanto mais palavras em cada grupo melhor!**

- 2.5 - Se optou por utilizar o modo 'Trending Hashtags', precisamos realizar o scraping manualmente:
    - Abra o terminal na pasta que contém o [scrapy_twitter.py](https://github.com/drbuche/InstaBot/blob/master/instabot/scrapy_twitter.py)
    - Digite o comando:
```sh
scrapy runspider scrapy_twitter.py
```
		        	
- 3 – Abra o terminal dentro da pasta que contenha o arquivo [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py) e use o comando:
 
- Linux:
```sh
./main_bot.py
```

- Windows:
```sh
cd C:\Users\etc\etc\até_o_local_do_main_bot.py

python main_bot.py
```

- 3.5 Caso tenha algum problema com a execução do python, altere a primeira linha do modulo [main_bot.py](https://github.com/drbuche/InstaBot/blob/master/instabot/main_bot.py) para:
    
 ```sh
#!/usr/bin/env python 

ou

#!/usr/bin/env python3 
```
- 4 – ?????
- 5 – profit!

# Desempenho do Bot!

- Criei uma conta do zero, coloquei algumas fotos e segui alguns grupos de bandas, jogos, etc...

- Até o momento, com 8 dias de uso, a conta saiu do ZERO e está com:
    - **205 Seguidores.**
    - **711 Likes nas fotos.**
    - **30 comentários em fotos.**
    - **Mais de 30 mensagens no Direct.**

  
<p align="center">
  <img src="https://i.imgur.com/6SsM3FR.jpg">
</p>  

- O Bot está rodando nesta conta desde o dia 11 de setembro. (8 dias de uso)
- Estou rodando o Bot de 6-8h por dia.
- Utilizo no modo **"comentar + curtir"** em **seguidores de perfis**.
- Para interagir com os últimos 120 seguidores do perfil, procuro por perfis que tem em média 15 a 50 mil seguidores. (perfis com mais de 100 mil seguidores são bons, mas costumam ter muitas contas fake...)
    - Seleciono perfis que tem um nicho parecido com o perfil da minha conta do instagram.


![N|Solid](https://i.imgur.com/IjinG9z.jpg)  


<p align="center">
  <img src="https://i.imgur.com/AEkS4Uj.jpg">
</p>  

<p align="right">
  <img src="https://i.imgur.com/FVo2fb7.jpg">
</p>  


# Observações:
- **Durante a execução, você terá a opção de selecionar o Webdriver que deseja utilizar, além de selecionar o idioma do navegador.**
    - **Certifique-se de que escolheu a opção de idioma compatível com seu navegador, assim como a do Webdriver**
- **O bot exibira uma mensagem contendo a hashtag/perfil atual e a data/hora que inciou o ciclo em cada referência. Também atualizará o número de perfis/hashtags totais que já foram interagidos e data/hora que os finalizou.**
- **Modo apenas like: Da like em 1 foto a cada 1-2 min.**
- **Modo apenas comentar: Comenta 1 foto a cada 6-10min**
- **Modo like e comentar:**
	- *No modo hashtags – Da like a cada 1-2 min e comenta 1x a cada 10 fotos.*
	- *No modo perfil – Comenta a cada 10 fotos e da like em 3-6 fotos de cada perfil.*
- **Modo Trending Hashtags coleta o top 5 das últimas 24h no twitter.**
    - Repita o passo 2.5 do tópico [Utilizando!](#utilizando) sempre que desejar atualizar a lista de # do dia. Caso contrario, ele mantera as # antigas. 
    - *Ele cria um arquivo chamado [top_5_hashtags_do_dia.txt](https://github.com/drbuche/InstaBot/blob/master/instabot/top_5_hashtags_do_dia.txt), que armazena as # utilizadas na ultima execução. Este arquivo é sobrescrito a cada execução*
- **Use bot com bom senso, como se ele imitasse uma pessoa real. Sugiro rodar entre as 7h da manhã até as 00 horas, em um período de 3-8 horas por dia, deixe alguns dias sem utilizar, etc...**
- **O tempo entre os comentários no modo like+comentar ainda está em teste.**
- **Caso tenha o erro 'Failed to Load.' e não consiga carregar fotos e perfis, tente apagar o arquivo 'geckodriver.log' dentro da pasta instabot, ele é gerado automaticamente ao executar o aplicativo. Além disso, limpe os cookies dos navegadores e certifique-se que não possui outros dispositivos acessando sua conta ao mesmo tempo pelo navegador.** 