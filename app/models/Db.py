import psycopg2
from psycopg2.extras import RealDictCursor
import os


class Db:
    def __init__(self):
        """Инициализация соединения"""
        self.connection = psycopg2.connect(
            dbname=os.environ.get('DB_NAME', 'postgres'),
            user=os.environ.get('DB_USER', 'postgres'),
            password=os.environ.get('DB_PASS', 'postgres'),
            host=os.environ.get('DB_HOST', '127.0.0.1'),
            port=os.environ.get('DB_PORT', '5432')
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        self.simple_cursor = self.connection.cursor()
        print('successful connect to db')


db = Db()
