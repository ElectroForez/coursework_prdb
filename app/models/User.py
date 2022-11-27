from models.Db import db


class UserModel:
    def __init__(self):
        super().__init__()
        self.db = db
        self.get_users()

    @property
    def users(self):
        return self.get_users()

    def get_users(self):
        self.db.cursor.execute("SELECT * FROM сотрудники")
        result = self.db.cursor.fetchall()
        return result

    def get_user(self, login, password):
        self.db.cursor.execute(f'SELECT * FROM сотрудники '
                               f'WHERE '
                               f'Логин = %s '
                               f'AND '
                               f'Пароль = %s',
                               (
                                   login,
                                   password
                               ))
        result = self.db.cursor.fetchone()
        return result