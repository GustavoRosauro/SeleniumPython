from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

opts = Options()

driver = Chrome(options=opts, executable_path='chromedriver.exe')
try:
    driver.get('https://www.quicksoft.com.br/')
    tagA = driver.find_element_by_link_text('Acesso ao Cliente')
    tagA.send_keys(Keys.ENTER)
    driver.get('https://portal.qcertifica.com.br/Authentication/Login.aspx')
    login = driver.find_element_by_name('ctl00$body$txtUsuario')
    senha = driver.find_element_by_name('ctl00$body$txtSenha')
    login.send_keys(
        'eu sou um robo em python falem com o Arquiteto Gustavo Rosauro')
    senha.send_keys('realizando testes automatizados')
    senha.send_keys(Keys.ENTER)

finally:
    print('acabou')
    #driver.quit()
