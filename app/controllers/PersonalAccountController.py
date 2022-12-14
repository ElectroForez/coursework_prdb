from PyQt5.QtCore import QObject, pyqtSlot, Qt

from addGood.add_good_model import AddGoodModel
from addGood.add_good_view import AddGoodView
from closeOrder.close_order_model import CloseOrderModel
from closeOrder.close_order_view import CloseOrderView
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
        """Открыть окно с историей входа"""
        model = LoginHistoryModel()
        view = LoginHistoryView(model, self._view)
        view.show()

    @pyqtSlot()
    def create_order(self):
        """Открыть окно с созданием заказа"""
        model = CreateOrderModel(self._model.user)
        view = CreateOrderView(model, self._view)
        view.show()

    @pyqtSlot()
    def close_order(self):
        """Открыть окно с закрытием заказа"""
        model = CloseOrderModel()
        view = CloseOrderView(model, self._view)
        view.show()

    @pyqtSlot()
    def add_good(self):
        """Открыть окно с добавлением товара"""
        model = AddGoodModel()
        view = AddGoodView(model, self._view)
        view.show()

    @pyqtSlot()
    def deauth(self):
        """Деавторизация"""
        from views.AuthorizeView import AuthorizeView  # for avoid circular import
        model = AuthorizeModel()
        view = AuthorizeView(model)
        self._view.close()
        view.show()

    @pyqtSlot()
    def close(self):
        """Закрытие экрана"""
        self._view.close()
