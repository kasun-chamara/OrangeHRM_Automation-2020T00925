from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
    # Locators
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGIN_PAGE_TITLE = (By.XPATH, "//h5[contains(@class, 'orangehrm-login-title')]")
    
    def get_login_page_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.LOGIN_PAGE_TITLE)).text
    
    def enter_username(self, username):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(username)
        
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)
        
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()