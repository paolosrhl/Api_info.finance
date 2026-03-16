import os
import mysql.connector
from dotenv import load_dotenv


load_dotenv()


def get_connection():
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")

    if not host or not user or not password or not database:
        raise ValueError("One or more database environment variables are missing.")

    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )