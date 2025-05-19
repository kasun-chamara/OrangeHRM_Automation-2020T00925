import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.LogoutPage import LogoutPage

class TestLogout:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        
        # Login 
        login_page = LoginPage(self.driver)
        login_page.login(self.username, self.password)
        yield
        self.driver.quit()
    
    def test_logout_functionality(self):
        logout_page = LogoutPage(self.driver)
        logout_page.logout()
        
        login_page = LoginPage(self.driver)
        assert "Login" in login_page.get_login_page_title()