from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

def test_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://demo.applitools.com")

    login = LoginPage(driver)
    login.login("testuser", "password")

    assert "ACME" in driver.title
    driver.quit()