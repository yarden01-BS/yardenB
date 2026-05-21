import mysql.connector
from mysql.connector import pooling
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    host="localhost",
    user="dev",
    password="password123",
    database="gestiondr1",
)


class Database:
    def __enter__(self):
        self.connection: MySQLConnection = pool.get_connection()
        self.cursor: MySQLCursor = self.connection.cursor(dictionary=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
