import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class ConexaoDB:
    def __init__(self):
        self.config = {
            "dbname": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "host": os.getenv("DB_HOST"),
            "port": os.getenv("DB_PORT")
        }

    def conectar(self):
        try:
            return psycopg2.connect(**self.config)
        except Exception as erro:
            print("Erro de conexão:", erro)
            return None