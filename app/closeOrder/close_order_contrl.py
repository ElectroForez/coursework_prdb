from PyQt5.QtCore import QObject, pyqtSlot


class CloseOrderController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self._model = model
        self._view = view

    @pyqtSlot(str)
    def change_order_id(self, id):
        """поменять номер заказа"""
        self._model.cur_order = id

    @pyqtSlot(str)
    def close_order(self, order_id):
        """закрыть заказ"""
        self._model.close_order_by_id(order_id)

    @pyqtSlot()
    def success_close_order(self):
        """Успешное закрытие заказа"""
        self._view.close()
