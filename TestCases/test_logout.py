import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
import time

class TestLogout:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.quit()
    
    def test_logout_functionality(self, setup):
        self.driver.get(self.base_url)
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        
        # Perform login
        login_page.set_username(self.username)
        login_page.set_password(self.password)
        login_page.click_login()
        
        # Perform logout
        dashboard_page.click_user_dropdown()
        dashboard_page.click_logout()
        
        # Verify we're back to login page
        assert login_page.is_login_panel_displayed() == True
        time.sleep(3)  