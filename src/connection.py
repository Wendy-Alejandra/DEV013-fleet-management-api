"""Database connection"""
import os
import psycopg2

try:
    connection = psycopg2.connect(
        host = os.getenv('POSTGRES_HOST'),
        user = os.getenv('POSTGRES_USER'),
        password = os.getenv('POSTGRES_PASSWORD'),
        database = os.getenv('POSTGRES_DATABASE'),
        port = 5432
    )
    print("Succefully connected")
except Exception as ex:
    print(ex)
