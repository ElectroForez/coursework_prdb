import datetime

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

from models.Db import db


class CreateOrderModel(QObject):

    order_changed = pyqtSignal(int)
    order_exists = pyqtSignal(bool)
    order_create = pyqtSignal(int)
    order_empty = pyqtSignal()
    cart_changed = pyqtSignal()

    def __init__(self, cur_employer=None):
        super().__init__()
        self._cur_order = self.get_last_order_id() + 1
        self._cart = []
        self.cur_employer = cur_employer

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

    def get_client_by_fullname(self, fullname):
        db.cursor.execute(f'select * from клиенты '
                          f'WHERE "ФИО" = \'{fullname}\'')
        result = db.cursor.fetchone()
        return result

    def create_order(self, order):
        if not len(order['cart']):
            return

        order['date_created'] = datetime.date.today()
        order['time_created'] = datetime.datetime.now().time()
        order['client_id'] = self.get_client_by_fullname(order['client_fullname'])['Код клиента']
        order['status'] = 'В прокате'
        order['employer_id'] = self.cur_employer["Код сотрудника"]

        db.cursor.execute(f'insert into заказы '
                          f'('
                          f'"Код заказа", '
                          f'"Дата создания", '
                          f'"Время заказа", '
                          f'"Код клиента", '
                          f'"Статус", '
                          f'"Время проката", '
                          f'"Код сотрудника"'
                          f')'
                          f'VALUES '
                          f'('
                          f'%s, %s, %s, %s, %s, %s, %s'
                          f')',
                          (
                          order['id'],
                          order['date_created'],
                          order['time_created'],
                          order['client_id'],
                          order['status'],
                          order['arenda_hours'],
                          order['employer_id'],
                          )
        )

        for good_id in order['cart']:
            db.cursor.execute("INSERT INTO заказы_товары "
                              "VALUES (%s, %s)", (order['id'], good_id))

        self.order_create.emit(order['id'])
