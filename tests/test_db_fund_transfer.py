from utils.db_connection import get_db_connection

def test_fund_transfer_db_validation():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Reset balances
    cursor.execute(
        "UPDATE customers SET balance = 5000 WHERE email='testuser@gmail.com'"
    )
    cursor.execute(
        "UPDATE customers SET balance = 2000 WHERE email='receiver@gmail.com'"
    )
    connection.commit()

    # Perform transfer
    cursor.execute(
        "UPDATE customers SET balance = balance - 500 WHERE email='testuser@gmail.com'"
    )
    cursor.execute(
        "UPDATE customers SET balance = balance + 500 WHERE email='receiver@gmail.com'"
    )

    cursor.execute(
        """
        INSERT INTO transactions (from_account, to_account, amount, status)
        VALUES ('testuser@gmail.com', 'receiver@gmail.com', 500, 'SUCCESS')
        """
    )

    connection.commit()

    # Validate balances
    cursor.execute(
        "SELECT balance FROM customers WHERE email='testuser@gmail.com'"
    )
    sender_balance = cursor.fetchone()[0]

    cursor.execute(
        "SELECT balance FROM customers WHERE email='receiver@gmail.com'"
    )
    receiver_balance = cursor.fetchone()[0]

    assert sender_balance == 4500
    assert receiver_balance == 2500

    connection.close()
