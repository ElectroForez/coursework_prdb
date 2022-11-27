from PyQt5.QtCore import QObject, pyqtSlot

from models.CreateOrderModel import CreateOrderModel

from goods.goods_view import GoodsView
from goods.goods_model import GoodsModel

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

    @pyqtSlot()
    def add_goods(self):
        model = GoodsModel(self._model)
        model.cart = self._model.cart
        view = GoodsView(model)
        view.show()
