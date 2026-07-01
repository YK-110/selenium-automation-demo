import pytest
from pages.login_page import LoginPage

class TestLogin:
    
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        assert "inventory" in driver.current_url
    
    def test_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "wrong_password")
        assert "Epic sadface" in login_page.get_error_message()
    
    def test_empty_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.login("", "")
        assert "Username is required" in login_page.get_error_message()