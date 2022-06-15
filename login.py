from selenium.webdriver.common.keys import Keys

from driver import Driver

class Login:
    def __init__(self,user,password):
        self.user = user,
        self.password = password
    def execute_login(self,driver):            
        driver = driver.return_drive_informations()
        driver.get('http://desenv.quicksoft.com.br/Qcertifica/Authentication/Login.aspx')
        login = driver.find_element_by_name('ctl00$body$txtUsuario')
        senha = driver.find_element_by_name('ctl00$body$txtSenha')
        login.send_keys(self.user)
        senha.send_keys(self.password)
        senha.send_keys(Keys.ENTER)