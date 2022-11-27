from PyQt5.QtCore import QObject, pyqtSlot

from models.CreateOrderModel import CreateOrderModel


class CreateOrderController(QObject):
    def __init__(self, view, model: CreateOrderModel):
        super().__init__()

        self._model = model
        self._view = view

    @pyqtSlot(str)
    def change_order_id(self, id):
        self._model.cur_order = id

    @pyqtSlot(str)
    def create_order(self, id):
        self._model.create_order(id)