from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

opts = Options()

driver = Chrome(options=opts, executable_path='chromedriver.exe')
try:    
    driver.get('http://desenv.quicksoft.com.br/Qcertifica/Authentication/Login.aspx')
    login = driver.find_element_by_name('ctl00$body$txtUsuario')
    senha = driver.find_element_by_name('ctl00$body$txtSenha')
    login.send_keys('sistema')
    senha.send_keys('quick99.')
    senha.send_keys(Keys.ENTER)
    driver.get(driver.current_url)
    driver.implicitly_wait(1000)
    motive = driver.find_element_by_name("ctl00$cphContext$ctrlFAS906$grdRemittances$ctl00$ctl06$gbOperationReason$gbOperationReason")
    motive.send_keys(Keys.ENTER)
    time.sleep(2)
    close = driver.find_element_by_name("ctl00$cphContext$ctrlFAS906$wndOperationReason$btnClose")
    close.send_keys(Keys.ENTER)
    time.sleep(2)
    link = driver.find_element_by_id('ctl00_cphContext_ctrlFAS906_btnAbrirGrafico')
    link.click()
    time.sleep(2)
    closeLink = driver.find_element_by_name('ctl00$cphContext$ctrlFAS906$modalGraficoFiltro$btnClose')
    closeLink.send_keys(Keys.ENTER)
    time.sleep(2)
    detalhes = driver.find_element_by_name('ctl00$cphContext$ctrlFAS906$grdDocuments$ctl00$ctl10$btnSigners')
    detalhes.click()
    time.sleep(2)
    closeDetalhes = driver.find_element_by_name('ctl00$cphContext$ctrlFAS906$mdlSigners$btnClose')
    closeDetalhes.click()
    time.sleep(2)
    check = driver.find_element_by_id('ctl00_cphContext_ctrlFAS906_grdRemittances_ctl00_ctl04_ckbSelect')
    check.click()

except:
    print('aconteceu erro na execucao')
finally:
    print('acabou')
    #driver.quit()
