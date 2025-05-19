import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage


class TestLogin:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        yield
        self.driver.quit()
    
    def test_verify_login_page_title(self):
        login_page = LoginPage(self.driver)
        assert "Login" in login_page.get_login_page_title()
        