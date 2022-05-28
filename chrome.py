from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

opts = Options()

driver = Chrome(options=opts, executable_path='chromedriver.exe')
try:
    driver.get('https://portal.qcertifica.com.br/Authentication/Login.aspx?enc=IuazGqDuFUuv0DlQ9kwRLn8grINIeo9xG89TdjTBfbo=')
    login = driver.find_element_by_name('ctl00$body$txtUsuario')
    senha = driver.find_element_by_name('ctl00$body$txtSenha')
    login.send_keys('1')
    senha.send_keys('2')
    senha.send_keys(Keys.ENTER)

finally:
    print('acabou')
    # driver.quit()