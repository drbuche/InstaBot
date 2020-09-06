from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    pic_hrefs = []

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    @staticmethod
    def digite_como_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1, 5) / 30)

    def close_browser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(4)

    def selecionar_fotos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        for _ in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                hrefs_na_tela = driver.find_elements_by_tag_name('a')
                hrefs_na_tela = [elem.get_attribute('href') for elem in hrefs_na_tela
                                 if '.com/p/' in elem.get_attribute('href')]
                [self.pic_hrefs.append(href) for href in hrefs_na_tela if href not in self.pic_hrefs]
            except Exception:
                continue

    def comentar_fotos(self, comentarios):
        driver = self.driver
        numero_de_fotos = len(self.pic_hrefs)  # Implementar contador futuramente
        for foto_atual in self.pic_hrefs:
            driver.get(foto_atual)
            time.sleep(2)
            try:
                time.sleep(random.randint(2, 4))
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(2, 4))
                self.digite_como_pessoa(random.choice(comentarios), campo_comentario)
                time.sleep(2)
                driver.find_element_by_xpath("//button[contains(text(),'Post')]").click()
                time.sleep(random.randint(30, 40))
            except Exception:
                time.sleep(2)
            numero_de_fotos -= 1

    def like_foto(self, like=True):
        driver = self.driver
        numero_de_fotos = len(self.pic_hrefs)
        estado_atual_like = 'Like' if like else 'Unlike'

        for foto_atual in self.pic_hrefs:
            driver.get(foto_atual)
            time.sleep(2)
            try:
                time.sleep(random.randint(2, 4))
                self.driver.find_element_by_xpath("//*[@aria-label='{}']".format(estado_atual_like)).click()
                time.sleep(random.randint(25, 35))
            except Exception:
                time.sleep(2)
            numero_de_fotos -= 1

    def like_comentar(self, comentarios, like=True):
        driver = self.driver
        numero_de_fotos = len(self.pic_hrefs)
        estado_atual_like = 'Like' if like else 'Unlike'

        for foto_atual in self.pic_hrefs:
            driver.get(foto_atual)
            time.sleep(2)
            try:
                time.sleep(random.randint(2, 4))
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(2, 4))
                self.digite_como_pessoa(random.choice(comentarios), campo_comentario)
                time.sleep(2)
                driver.find_element_by_xpath("//button[contains(text(),'Post')]").click()
                time.sleep(2)
                self.driver.find_element_by_xpath("//*[@aria-label='{}']".format(estado_atual_like)).click()
                time.sleep(random.randint(30, 40))
            except Exception:
                time.sleep(2)
            numero_de_fotos -= 1

