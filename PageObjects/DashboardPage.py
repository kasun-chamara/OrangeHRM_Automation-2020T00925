from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        
    # Locators
    DASHBOARD_HEADER = (By.XPATH, '//h6[text()="Dashboard"]')
    MY_LEAVE_BUTTON = (By.XPATH, '//button[@title="My Leave"]')
    USER_DROPDOWN = (By.XPATH, '//span[@class="oxd-userdropdown-tab"]')
    LOGOUT_LINK = (By.XPATH, '//a[text()="Logout"]')
    
    def get_dashboard_page_title(self):
        return self.driver.title
    
    def is_dashboard_header_displayed(self):
        return self.driver.find_element(*self.DASHBOARD_HEADER).is_displayed()
    
    def click_my_leave(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MY_LEAVE_BUTTON)
        ).click()
    
    def click_user_dropdown(self):
        self.driver.find_element(*self.USER_DROPDOWN).click()
    
    def click_logout(self):
        self.driver.find_element(*self.LOGOUT_LINK).click()