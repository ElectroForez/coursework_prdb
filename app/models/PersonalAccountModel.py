from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

from models.User import UserModel


class PersonalAccountModel(QObject):

    def __init__(self, user):
        super().__init__()
        self._user_model = UserModel()
        self._cur_user = user

    @property
    def user(self):
        """Текущий пользователь"""
        return self._cur_user
