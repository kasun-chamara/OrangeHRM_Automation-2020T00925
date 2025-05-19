from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)
        
    # Locators
    LEAVE_HEADER = (By.XPATH, "//h6[contains(@class, 'oxd-topbar-header-breadcrumb-module')]")
    MY_LEAVE_BUTTON = (By.XPATH, "//button[@title='My Leave']")
    
    def get_leave_header(self):
        return self.wait.until(EC.visibility_of_element_located(self.LEAVE_HEADER)).text
    
    def click_my_leave(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_LEAVE_BUTTON)).click()