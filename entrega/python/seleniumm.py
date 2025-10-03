from http import client
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

import time

class Bot:
    def __init__(self):
        chrome_service = Service('./chromedriver.exe')

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("lang=pt-br")
        chrome_options.add_argument("--incognito")
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("window-size=1000,900")

        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        
        self.EXCLUDE = []
        self.LAST = None


    def element_presence(self, path):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, path)))


    def clicar(self, path):
        try:
            elemento = self.element_presence(path)
            elemento.click()
        except:
            time.sleep(0.5)
            elemento = self.clicar(path)
        return elemento


if __name__ == '__main__':

    # bot = Bot()
    # bot.driver.get("https://google.com")

    # form = bot.clicar("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea")
    
    # form.send_keys("Senac MG")
    # form.send_keys("\n")
    # bot.driver.close()
    
    bot = Bot()
    
    # Entra no site
    bot.driver.get("https://toolsqa.com/")
    
    # clica botao enroll yourself
    form = bot.clicar("/html/body/div[1]/div[1]/div[1]/div/div[2]/div[4]/div[1]/a")
   
    # clica campo nome
    form = bot.clicar("/html/body/div[1]/div[5]/div/div[3]/form/div[1]/input")
    form.send_keys("Ryan")
    
    # clica campo last name
    form = bot.clicar("/html/body/div[1]/div[5]/div/div[3]/form/div[2]/input")
    form.send_keys("Augusto")
    
    # Clica campo email
    form = bot.clicar("/html/body/div[1]/div[5]/div/div[3]/form/div[3]/input")
    form.send_keys("ryanpestana205@gmail.com")
    
    # Clica campo mobile
    form = bot.clicar("/html/body/div[1]/div[5]/div/div[3]/form/div[4]/input")
    form.send_keys("31981087652")
    
    # Clica campo country
    form = bot.clicar("/html/body/div[1]/div[5]/div/div[3]/form/div[5]/select")
    form.send_keys("Brazil")
    
    # Clica campo city
    form = bot.clicar("/html/body/div[1]/div[5]/div/div[3]/form/div[6]/input")
    form.send_keys("São Paulo")
    
    # Clica campo message
    form = bot.clicar("/html/body/div[1]/div[5]/div/div[3]/form/div[7]/textarea")
    form.send_keys("jkabkjahjwbkjqw")
    
    
    
    bot.driver.close