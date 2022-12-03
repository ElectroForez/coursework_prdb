import datetime

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

from models.User import UserModel
from models.Db import db


class AuthorizeModel(QObject):

    user_authorized = pyqtSignal(bool)
    block_auth = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._user_model = UserModel()
        self._cur_user = None
        self._try_auth = 0

    @property
    def cur_user(self):
        return self._cur_user

    @cur_user.setter
    def cur_user(self, value):
        self._cur_user = value

    def verify_credentials(self, login, password):
        """Проверить данные для входа"""
        candidate = self._user_model.get_user(login, password)
        input_type = 'успешно' if candidate else 'не успешно'
        time = datetime.datetime.now()
        self.add_to_history(login, input_type, time)
        return candidate

    def add_to_history(self, login, input_type, time):
        """Добавить попытку в историю входа"""
        db.simple_cursor.execute(f'INSERT INTO login_history '
                         f'("login", "entry_type", "entry_time") '
                         f'VALUES (%s, %s, %s)',
                         (
                             login,
                             input_type,
                             time
                         ))

    # номер попытки авторизоваться
    @property
    def try_auth(self):
        return self._try_auth

    @try_auth.setter
    def try_auth(self, value):
        self._try_auth = value
        if self._try_auth >= 4:
            self.block_auth.emit()
