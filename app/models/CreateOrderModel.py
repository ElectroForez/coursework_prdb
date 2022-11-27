from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

from models.Db import db


class CreateOrderModel(QObject):

    order_changed = pyqtSignal(int)
    order_exists = pyqtSignal(bool)
    order_created = pyqtSignal(str)
    order_empty = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._cur_order = self.get_last_order_id() + 1

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
