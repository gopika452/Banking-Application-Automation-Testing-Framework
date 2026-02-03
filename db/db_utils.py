import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
         host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "banking_test")
    )

def get_balance(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT balance FROM customers WHERE email=%s", (email,)
    )
    balance = cursor.fetchone()[0]
    conn.close()
    return balance

def update_balance(email, amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE customers SET balance=%s WHERE email=%s",
        (amount, email)
    )
    conn.commit()
    conn.close()

def insert_transaction(sender, receiver, amount, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions
        (from_account, to_account, amount, status)
        VALUES (%s, %s, %s, %s)
    """, (sender, receiver, amount, status))
    conn.commit()
    conn.close()
