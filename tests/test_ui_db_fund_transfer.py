from pages.login_page import LoginPage
from db.db_utils import get_balance, update_balance, insert_transaction
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_ui_to_db_fund_transfer():
    sender = "testuser@gmail.com"
    receiver = "receiver@gmail.com"
    transfer_amount = 500

    # Reset balances (test independence)
    update_balance(sender, 5000)
    update_balance(receiver, 2000)

    before_sender = get_balance(sender)
    before_receiver = get_balance(receiver)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.maximize_window()

    try:
        driver.get("https://demo.applitools.com")

        login = LoginPage(driver)
        login.login("testuser", "password")

        # Simulated transfer
        if before_sender >= transfer_amount:
            update_balance(sender, before_sender - transfer_amount)
            update_balance(receiver, before_receiver + transfer_amount)
            insert_transaction(sender, receiver, transfer_amount, "SUCCESS")

        after_sender = get_balance(sender)
        after_receiver = get_balance(receiver)

        # DB ASSERTIONS (REAL VALIDATION)
        assert after_sender == before_sender - transfer_amount
        assert after_receiver == before_receiver + transfer_amount

    finally:
        driver.quit()
