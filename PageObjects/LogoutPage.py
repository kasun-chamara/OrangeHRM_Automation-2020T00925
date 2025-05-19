from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    USER_DROPDOWN = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Logout']")
        
    def click_user_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_DROPDOWN)).click()
        
    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()
        
    def logout(self):
        self.click_user_dropdown()
        self.click_logout()
