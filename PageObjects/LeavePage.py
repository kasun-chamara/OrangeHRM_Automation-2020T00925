from selenium.webdriver.common.by import By

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        
    # Locators
    LEAVE_HEADER = (By.XPATH, '//h6[text()="My Leave"]')
    
    def get_leave_page_title(self):
        return self.driver.title
    
    def is_leave_header_displayed(self):
        return self.driver.find_element(*self.LEAVE_HEADER).is_displayed()