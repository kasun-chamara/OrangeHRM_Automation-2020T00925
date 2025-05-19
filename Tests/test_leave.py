import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
from PageObjects.LeavePage import LeavePage

class TestLeave:
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
    
    def test_leave_functionality(self):
        dashboard_page = LeavePage(self.driver)
        dashboard_page.click_my_leave()
        
        leave_page = LeavePage(self.driver)
        assert "Leave" in leave_page.get_leave_header()