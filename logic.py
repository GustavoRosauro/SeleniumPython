from digitalSigner import DigitalSigner
from driver import Driver

from login import Login

try:    
    driver = Driver()
    driver.open_connections()
    login = Login('sistema','quick99.')
    login.execute_login(driver)    
    signer = DigitalSigner()
    signer.execute_tests(driver)
finally:
    print('acabou')
    #driver.quit()
