from PyQt5.QtCore import QObject, pyqtSlot

from models.CapchaDialogModel import CapchaDialogModel
from models.PersonalAccountModel import PersonalAccountModel
from views.PersonalAccountView import PersonalAccountView


class AuthorizeController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self._model = model
        self._view = view

    @pyqtSlot(str, str)
    def authorize(self, login, password):
        if not (login and password):
            self._view.show_error("Заполните все поля")
            return

        candidate = self._model.verify_credentials(login, password)
        if candidate:
            model = PersonalAccountModel(candidate)
            view = PersonalAccountView(model)
            view.show()
            self._view.close()
        else:
            self._view.show_error("Неверный логин или пароль")
            self._model.try_auth += 1

    @pyqtSlot()
    def create_capcha(self):
        self._view.on_capcha()

        from views.CapchaDialogView import CapchaDialogView
        model = CapchaDialogModel()
        view = CapchaDialogView(model, self._view)
        view.show()
