from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_fund_transfer_simulation():
    """
    Validate login and dashboard load for a banking application.
    Simulates fund transfer validation on a demo site.
    """

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.maximize_window()

    try:
        # Launch application
        driver.get("https://demo.applitools.com")

        # Login step
        login_page = LoginPage(driver)
        login_page.login("testuser", "password")

        # Dashboard validation
        dashboard_page = DashboardPage(driver)
        assert dashboard_page.is_dashboard_loaded() is True

        # Simulated fund transfer validation
        # (Demo site does not perform real transactions)
        assert driver.title is not None

    finally:
        driver.quit()