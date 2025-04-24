import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
import time

class TestLogin:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.quit()
    
    def test_home_page_title(self, setup):
        self.driver.get(self.base_url)
        login_page = LoginPage(self.driver)
        
        # Verify login page title
        assert login_page.get_login_page_title() == "OrangeHRM"
        
        # Verify login panel is displayed
        assert login_page.is_login_panel_displayed() == True
    
    def test_login_functionality(self, setup):
        self.driver.get(self.base_url)
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        
        # Perform login
        login_page.set_username(self.username)
        login_page.set_password(self.password)
        login_page.click_login()
        
        # Verify dashboard page is loaded
        assert dashboard_page.is_dashboard_header_displayed() == True
        time.sleep(3)  