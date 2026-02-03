import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MySQL@123",
        database="banking_test"
    )
    return connection
