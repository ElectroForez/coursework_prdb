import psycopg2
from psycopg2.extras import RealDictCursor


class Db:
    def __init__(self):
        """Инициализация соединения"""
        self.connection = psycopg2.connect(
            dbname='coursework_prdb',
            user='admin',
            password='qwerty',
            host='localhost'
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        self.simple_cursor = self.connection.cursor()
        print('successful connect to db')

db = Db()
