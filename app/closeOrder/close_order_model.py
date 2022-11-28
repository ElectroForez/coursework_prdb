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
        if candidate and candidate['Cтатус'].startswith('Закрыт'):
            self.order_already_close.emit()

    def get_order_by_id(self, id):
        self.db.cursor.execute('SELECT * FROM заказы WHERE "Код заказа" = %s', (id,))
        result = self.db.cursor.fetchone()
        return result

    def close_order_by_id(self, order_id):
        self.db.cursor.execute(f'UPDATE заказы '
                               f'SET "Cтатус" = \'Закрыт\' '
                               f'WHERE "Код заказа" = {order_id}')

        self.db.cursor.execute(f'UPDATE товары т '
                               f'SET "Оставшееся кол-во" = "Оставшееся кол-во" + 1 '
                               f'WHERE "Код товара" IN '
                               f'(SELECT "Код товара" FROM заказы_товары зт '
                               f'WHERE "Код заказа" = {order_id})')
        self.db.connection.commit()

        self.order_close.emit(order_id)
