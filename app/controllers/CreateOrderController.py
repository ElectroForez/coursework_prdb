import os

from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QLabel, QFileDialog

from common.pdf import print_widget
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

    @pyqtSlot(dict)
    def create_order(self, order):
        result = self._model.create_order(order)
        if result:
            self.print_pdf(order)

    @pyqtSlot()
    def success_create_order(self):
        self._view.close()

    @pyqtSlot()
    def add_goods(self):
        model = GoodsModel(self._model)
        model.cart = self._model.cart
        view = GoodsView(model)
        view.show()

    def print_pdf(self, order):
        text = f"""
Номер заказа: {order['id']}
Клиент: {order['client_fullname']}
Количество часов проката: {order['arenda_hours']}

Список товаров:

"""
        cart = self._model.cart
        cart_text = ""
        for good_id in cart:
            good = self._model.get_good_by_id(good_id)
            cart_text += f"{good['title']}, {good['cost_per_hour']} руб.)\n"
        text += cart_text

        text += f"Итого: {self._model.get_cart_total_price(int(order['arenda_hours']))}"
        text = text.replace('\n', '\n    ')
        label = QLabel(text)
        label.setStyleSheet('background-color: #FFF')
        file_name, _ = QFileDialog.getSaveFileName(self._view, "Сохранить чек в:", "",
                                                   "pdf (*.pdf);;All Files (*);;")
        if file_name:
            print_widget(label, file_name)
