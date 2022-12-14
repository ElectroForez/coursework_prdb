from PyQt5.QtCore import pyqtSignal, QObject

from models.CreateOrderModel import CreateOrderModel
from models.Db import db


class GoodsModel(QObject):

    goods_changed = pyqtSignal()
    cart_changed = pyqtSignal()

    def __init__(self, create_order_model: CreateOrderModel = None):
        super().__init__()
        self.db = db
        self._filter_good_name = ""
        self._sort_field = '"id"'
        self._sort_type = "ASC"
        self._goods_category = ""
        self._limit = 6
        self._offset = 0
        self._goods = self.get_goods()
        self._cart = []

        self.createOrderModel = create_order_model

    def add_to_cart(self, good_id):
        """Добавить в корзину"""
        good = self.get_good_by_id(good_id)

        if good_id not in self._cart:
            if not good["remaining_amount"]:
                return
            self._cart.append(good_id)
        else:
            self._cart.remove(good_id)
        self.cart_changed.emit()

    # Различные геттеры и сеттеры для свойств
    @property
    def cart(self):
        return self._cart

    @cart.setter
    def cart(self, value):
        self._cart = value

    @property
    def goods(self):
        return self._goods

    @goods.setter
    def goods(self, value):
        self._goods = value
        self.goods_changed.emit()

    @property
    def filter_good_name(self):
        return self._filter_good_name

    @filter_good_name.setter
    def filter_good_name(self, value):
        self._filter_good_name = value
        self.goods = self.get_goods()

    @property
    def sort_field(self):
        return self._sort_field

    @sort_field.setter
    def sort_field(self, value):
        self._sort_field = value
        self.goods = self.get_goods()

    @property
    def sort_type(self):
        return self._sort_type

    @sort_type.setter
    def sort_type(self, value):
        self._sort_type = value
        self.goods = self.get_goods()

    @property
    def goods_category(self):
        return self._goods_category

    @goods_category.setter
    def goods_category(self, value):
        self._goods_category = value
        self.goods = self.get_goods()

    @property
    def offset(self):
        return self._offset

    @property
    def limit(self):
        return self._limit

    @offset.setter
    def offset(self, value):
        self._offset = value
        self.goods = self.get_goods()

    def get_all_goods(self):
        """Получить все товары"""
        self.db.cursor.execute('SELECT * FROM goods')

        result = self.db.cursor.fetchall()
        return result

    def get_goods(self):
        """Получить все товары с учётом параметров"""
        self.db.cursor.execute(f'select * '
                               f'from goods '
                               f'WHERE '
                               f'"title" LIKE \'%{self._filter_good_name}%\' '
                               f'AND '
                               f'"category" LIKE \'%{self._goods_category}%\''
                               f'ORDER BY {self._sort_field} {self._sort_type} '
                               f'LIMIT {self._limit} '
                               f'OFFSET {self._offset}'
                               )
        result = self.db.cursor.fetchall()
        return result

    def get_good_by_id(self, good_id):
        """получить товар по id"""
        self.db.cursor.execute(f'select * '
                               f'from goods '
                               f'WHERE '
                               f'"id" = {good_id}'
                               )
        result = self.db.cursor.fetchone()
        return result

    @cart.setter
    def cart(self, value):
        self._cart = value
