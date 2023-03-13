#Bibliotecas
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://scitec.ultralims.com.br/public/index.php")

navegador.find_element('xpath', '//*[@id="login"]').send_keys('thiago.lirio')
navegador.find_element('xpath', '//*[@id="password"]').send_keys('thiago150899')
navegador.find_element('xpath', '//*[@id="password"]').get_attribute('value')
print(navegador.find_element('xpath', '//*[@id="password"]').get_attribute('value'))
time.sleep(1)
"""
    #Criando o navegador
    #navegador = p.chromium.launch(headless=False)
    #pagina = navegador.new_page()
    #Mandando a pagina ir para a tela de login do ultralims
    pagina.goto("https://scitec.ultralims.com.br/public/index.php")
    #Preenchendo as informações de login
    pagina.fill('xpath=//*[@id="login"]', "thiago.lirio")
    pagina.fill('//*[@id="password"]', "thiago150899")
    pagina.locator('//*[@id="login-form"]/div[3]/input[2]').click()
    pagina.locator('// *[ @ id = "botaoModal"]').click()
    time.sleep(1)
    pagina.locator('// html/body/div[1]/aside/div/section').hover()
    time.sleep(1)
    pagina.locator('//*[@id="menuSideBar"]/li[4]/a').click()
    time.sleep(1)
    pagina.locator('//*[@id="menuSideBar"]/li[4]/ul/li[2]').click()
    
    time.sleep(80)
"""

