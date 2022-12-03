from PyQt5.QtCore import pyqtSignal, QObject

from models.CreateOrderModel import CreateOrderModel
from models.Db import db


class CloseOrderModel(QObject):

    order_exists = pyqtSignal(bool)
    order_already_close = pyqtSignal()
    order_empty = pyqtSignal()
    order_changed = pyqtSignal(int)
    order_close = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.db = db
        self._cur_order = ""

    @property
    def cur_order(self):
        return self._cur_order

    @cur_order.setter
    def cur_order(self, value):
        self._cur_order = value
        self.order_changed.emit(value)
        if self._cur_order == "":
            self.order_empty.emit()
            return

        candidate = self.get_order_by_id(self._cur_order)
        self.order_exists.emit(bool(candidate))
        if candidate and candidate['status'].startswith('Закрыт'):
            self.order_already_close.emit()

    def get_order_by_id(self, id):
        """Получить заказ по id"""
        self.db.cursor.execute('SELECT * FROM orders WHERE "id" = %s', (id,))
        result = self.db.cursor.fetchone()
        return result

    def close_order_by_id(self, order_id):
        """Закрыть заказ по id"""
        self.db.cursor.execute(f'UPDATE orders '
                               f'SET "status" = \'Закрыт\' '
                               f'WHERE "id" = {order_id}')

        self.db.cursor.execute(f'UPDATE goods '
                               f'SET "remaining_amount" = "remaining_amount" + 1 '
                               f'WHERE "id" IN '
                               f'(SELECT "id" FROM order_goods зт '
                               f'WHERE "order_id" = {order_id})')
        self.db.connection.commit()

        self.order_close.emit(order_id)
