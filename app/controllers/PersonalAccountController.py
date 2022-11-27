from PyQt5.QtCore import QObject, pyqtSlot, Qt

from models.AuthorizeModel import AuthorizeModel
from models.CreateOrderModel import CreateOrderModel
from models.LoginHistoryModel import LoginHistoryModel

from views.CreateOrderView import CreateOrderView
from views.LoginHistoryView import LoginHistoryView


class PersonalAccountController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self._model = model
        self._view = view

    @pyqtSlot()
    def open_history(self):
        model = LoginHistoryModel()
        view = LoginHistoryView(model, self._view)
        view.show()

    @pyqtSlot()
    def create_order(self):
        model = CreateOrderModel()
        view = CreateOrderView(model, self._view)
        view.show()

    @pyqtSlot()
    def deauth(self):
        from views.AuthorizeView import AuthorizeView  # for avoid circular import
        model = AuthorizeModel()
        view = AuthorizeView(model)
        self._view.close()
        view.show()

    @pyqtSlot()
    def close(self):
        self._view.close()
