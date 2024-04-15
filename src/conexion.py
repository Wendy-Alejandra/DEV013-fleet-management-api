"""Database connection"""
import os
import psycopg2

print(os.getenv('POSTGRES_HOST'))
connection = psycopg2.connect(
    host = os.getenv('POSTGRES_HOST'),
    user = os.getenv('POSTGRES_USER'),
    password = os.environ.get('POSTGRES_PASSWORD'),
    database = os.getenv('POSTGRES_DATABASE')
)

print("Succefully connected")
