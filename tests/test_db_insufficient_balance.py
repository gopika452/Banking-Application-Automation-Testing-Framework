import mysql.connector

def test_fund_transfer_insufficient_balance():
    # Step 1: Connect to DB
    conn = mysql.connector.connect(
        host="localhost",
        user="bank_test_user",
        password="bank123",
        database="banking_test"
    )
    cursor = conn.cursor()

    sender_email = "testuser@gmail.com"
    transfer_amount = 100000  # deliberately too high

    # Step 2: Get sender balance BEFORE transfer
    cursor.execute(
        "SELECT balance FROM customers WHERE email=%s",
        (sender_email,)
    )
    sender_balance_before = cursor.fetchone()[0]

    # Step 3: Business logic check
    if sender_balance_before < transfer_amount:
        status = "FAILED"

        # Step 4: Log failed transaction
        cursor.execute("""
            INSERT INTO transactions (from_account, to_account, amount, status)
            VALUES (%s, %s, %s, %s)
        """, (sender_email, "dummy@bank.com", transfer_amount, status))

        conn.commit()

    # Step 5: Get sender balance AFTER transfer
    cursor.execute(
        "SELECT balance FROM customers WHERE email=%s",
        (sender_email,)
    )
    sender_balance_after = cursor.fetchone()[0]

    # Step 6: Assertions (THIS IS THE TEST)
    assert sender_balance_before == sender_balance_after
    assert status == "FAILED"

    cursor.close()
    conn.close()
