import os.path

from PyQt5.QtCore import pyqtSlot, QTimer, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QMessageBox, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QPushButton
from goods.goods_design import Ui_Form

from goods.good_contrl import GoodsController
from goods.goods_model import GoodsModel


class GoodsView(QWidget):

    def __init__(self, model: GoodsModel, parent=None):
        super().__init__(parent)

        self._parent = parent
        self._model = model
        self._controller = GoodsController(self, self._model)
        self._ui = Ui_Form()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self._ui.setupUi(self)
        self.init_slots()
        self.init_data()

    def init_slots(self):
        """Инициализация слотов"""
        self._model.goods_changed.connect(self.on_goods_change)
        self._ui.sort_type_box.currentTextChanged.connect(self._controller.sort_type_change)
        self._ui.field_box.currentTextChanged.connect(self._controller.sort_field_change)
        self._ui.type_box.currentTextChanged.connect(self._controller.good_category_change)
        self._ui.next_btn.clicked.connect(self._controller.next_click)
        self._ui.prev_btn.clicked.connect(self._controller.prev_click)
        self._ui.goods_name_edit.textChanged.connect(self._controller.good_name_change)
        self._ui.see_cart.clicked.connect(self.on_see_cart)
        self._model.cart_changed.connect(self.on_cart_changed)
        self._ui.create_order.clicked.connect(self._controller.complete)

    def init_data(self):
        """Инициализация данных"""
        self.draw_goods()
        self.on_cart_changed()

    @pyqtSlot()
    def on_goods_change(self):
        """слот для изменения товаров"""
        self.draw_goods()

    def draw_goods(self):
        """Отрисовка товаров"""
        for i in reversed(range(self._ui.goodsGrid.count())):
            self._ui.goodsGrid.itemAt(i).widget().setParent(None)

        goods = self._model.goods[:self._model.limit]

        positions = [(i, j) for i in range(2) for j in range(3)]

        for position, good in zip(positions, goods):
            good_widget = self.get_good_widget(good)

            self._ui.goodsGrid.addWidget(good_widget, *position)

    @pyqtSlot()
    def on_cart_changed(self):
        """Слот для изменений в корзине"""
        self._ui.cart_count.setText(str(len(self._model.cart)))
        self.draw_goods()

    def get_good_widget(self, good):
        """Получить виджет товара"""
        widget = QWidget()
        widget.setMaximumSize(270, 270)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(good["title"]))

        photo_label = QLabel()
        if good["img"]:
            photo = QPixmap(os.path.join("img", good["img"]))
            photo.scaled(150, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            photo_label.setPixmap(photo)
        else:
            photo_label.setText("Нет фото")
        photo_label.setFixedSize(150, 50)
        photo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(photo_label)

        layout.addWidget(self.get_property_layout("Руб/час", good["cost_per_hour"]))
        layout.addWidget(self.get_property_layout("Категория", good["category"]))

        remaining_amount = good["remaining_amount"]
        if good["id"] in self._model.cart:
            remaining_amount -= 1
            add_to_cart_text = "Добавлено"
        else:
            add_to_cart_text = "Добавить в заказ"

        layout.addWidget(self.get_property_layout("Осталось", remaining_amount))

        add_to_cart = QPushButton(add_to_cart_text)
        add_to_cart.clicked.connect(lambda: self._controller.add_good(good["id"]))
        layout.addWidget(add_to_cart)
        widget.setLayout(layout)
        widget.setStyleSheet("background-color: white; color: black;")

        return widget

    def get_property_layout(self, name, value):
        """
        Контейнер для горизонтального
        отображения свойства и его значения
        """
        value = str(value)
        widget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(QLabel(name + ":"))
        layout.addWidget(QLabel(value))
        widget.setLayout(layout)
        return widget

    @pyqtSlot()
    def on_see_cart(self):
        """При клике на просмотр корзины"""
        msg_box = QMessageBox()
        text = "Список:\n" if len(self._model.cart) else "Список пуст"

        for good_id in self._model.cart:
            text += self._model.get_good_by_id(good_id)['title'] + "\n"

        msg_box.setText(text)
        msg_box.setWindowTitle("Заказ")
        msg_box.exec()
