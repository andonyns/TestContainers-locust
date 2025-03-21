import os
import psycopg
import time

from dotenv import load_dotenv
from models.customers import Customer

load_dotenv()

def get_connection():
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", "5432")
        username = os.getenv("DB_USERNAME", "postgres")
        password = os.getenv("DB_PASSWORD", "postgres")
        database = os.getenv("DB_NAME", "postgres")
        print(f"host={host} dbname={database} user={username} password={password} port={port}")
        return psycopg.connect(f"host={host} dbname={database} user={username} password={password} port={port}")

class DB:

    def create_table(self):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS customers (
                        id serial PRIMARY KEY,
                        name varchar not null,
                        email varchar not null)
                    """)
                conn.commit()

    def create_customer(self, name, email):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO customers (name, email) VALUES (%s, %s)", (name, email))
                conn.commit()


    def get_all_customers(self) -> list[Customer]:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers")
                time.sleep(60)
                return [Customer(cid, name, email).toJSON() for cid, name, email in cur]


    def get_customer_by_email(email) -> Customer:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name, email FROM customers WHERE email = %s", (email,))
                (cid, name, email) = cur.fetchone()
                return Customer(cid, name, email)


    def delete_all_customers():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM customers")
                conn.commit()