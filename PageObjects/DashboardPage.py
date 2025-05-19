from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
    # Locators
    DASHBOARD_HEADER = (By.XPATH, "//h6[contains(@class, 'oxd-topbar-header-breadcrumb-module')]")

    def get_dashboard_header(self):
        return self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_HEADER)).text
