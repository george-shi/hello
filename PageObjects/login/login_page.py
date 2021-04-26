from selenium.webdriver.common.by import By

class LoginPageLocator:
    user_loc = (By.XPATH, '//input[@id="account"]')
    pwd_loc = (By.ID, 'pwd')
    login