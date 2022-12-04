from PyQt5.QtCore import QObject, pyqtSlot


class GoodsController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self._model = model
        self._view = view

    @pyqtSlot(str)
    def filter_by_login(self, value):
        """Фильтрование по логину"""
        self._model.history = self._model.get_history_by_login(value)

    @pyqtSlot(str)
    def sort_type_change(self, value):
        """Изменение порядка сортировки"""
        if value == "По возрастанию":
            self._model.sort_type = "ASC"
        else:
            self._model.sort_type = "DESC"

    @pyqtSlot(str)
    def sort_field_change(self, value):
        """Изменение поля сортировки"""
        if value == "Имя":
            self._model.sort_field = '"title"'
        elif value == "Цена":
            self._model.sort_field = '"cost_per_hour"'

    @pyqtSlot(str)
    def good_category_change(self, value):
        """Изменение категории"""
        if value == "Все категории":
            self._model.goods_category = ""
        else:
            self._model.goods_category = value

    @pyqtSlot()
    def next_click(self):
        """Следующая страница"""
        self._model.offset += self._model.limit
        goods_len = len(self._model.get_goods())
        if not goods_len:
            self._model.offset -= self._model.limit

    @pyqtSlot()
    def prev_click(self):
        """Предыдущая страница"""
        if (self._model.offset - self._model.limit) < 0:
            self._model.offset = 0
        else:
            self._model.offset -= self._model.limit

    @pyqtSlot(str)
    def good_name_change(self, value):
        """Изменение фильтра товара по имени"""
        self._model.filter_good_name = value

    @pyqtSlot(int)
    def add_good(self, value):
        """Добавление модели"""
        self._model.add_to_cart(value)

    @pyqtSlot()
    def complete(self):
        """При завершении выбора"""
        self._model.createOrderModel.cart = self._model.cart
        self._view.close()
