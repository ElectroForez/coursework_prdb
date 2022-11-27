from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from models.Db import db


class LoginHistoryModel(QObject):

    history_changed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._history = self.get_history_from_db()

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value):
        self._history = value
        self.history_changed.emit()

    def get_history_from_db(self):
        db.cursor.execute("SELECT * FROM история_входа")
        result = db.cursor.fetchall()
        return result

    def get_history_by_login(self, login):
        db.cursor.execute("SELECT * FROM история_входа "
                          f"WHERE Логин LIKE '%{login}%'")
        result = db.cursor.fetchall()
        return result