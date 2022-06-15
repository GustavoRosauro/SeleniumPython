from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
class Driver:
    def __init__(self):
        self.driver = ''
    def open_connections(self):
        opts = Options()        
        self.driver = Chrome(options=opts, executable_path='chromedriver.exe')
    def return_drive_informations(self):
        return self.driver