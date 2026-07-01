import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

@pytest.fixture
def driver():
    service = Service(executable_path="./msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()