from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

from models.Db import db


class CreateOrderModel(QObject):

    order_changed = pyqtSignal(int)
    order_exists = pyqtSignal(bool)
    order_created = pyqtSignal(str)
    order_empty = pyqtSignal()
    cart_changed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._cur_order = self.get_last_order_id() + 1
        self._cart = []

    @property
    def cart(self):
        return self._cart

    @cart.setter
    def cart(self, value):
        self._cart = value
        self.cart_changed.emit()

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

    def get_last_order_id(self):
        db.cursor.execute('SELECT MAX("Код заказа") FROM заказы')
        result = db.cursor.fetchone()['max']
        return result

    def get_order_by_id(self, id):
        db.cursor.execute('SELECT * FROM заказы WHERE "Код заказа" = %s', (id,))
        result = db.cursor.fetchone()
        return result

    def create_order(self, id):
        print(f'Сделали заказ с номером {id}')
        self.order_created.emit(id)
        return 1

    def get_good_by_id(self, good_id):
        db.cursor.execute(f'select * '
                               f'from товары '
                               f'WHERE '
                               f'"Код товара" = {good_id}'
                               )
        result = db.cursor.fetchone()
        return result

    def get_clients(self):
        db.cursor.execute(f'select * from клиенты')
        result = db.cursor.fetchall()
        return result