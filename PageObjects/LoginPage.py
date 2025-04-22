from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
    # Locators
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    LOGIN_PANEL_HEADER = (By.XPATH, '//h5[text()="Login"]')
    
    def get_login_page_title(self):
        return self.driver.title
    
    def set_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).clear()
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
    
    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).clear()
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
    
    def is_login_panel_displayed(self):
        return self.driver.find_element(*self.LOGIN_PANEL_HEADER).is_displayed()