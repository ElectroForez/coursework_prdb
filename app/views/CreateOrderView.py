import sys
from random import randint

from PyQt5.QtCore import pyqtSlot, QRegExp, Qt, QPoint
from PyQt5.QtGui import QPixmap, QRegExpValidator, QColor, QPainter, QFont
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QWidget, QMessageBox, QApplication

from models.CreateOrderModel import CreateOrderModel
from views.createOrderDesign import Ui_Form
from models.PersonalAccountModel import PersonalAccountModel

from controllers.CreateOrderController import CreateOrderController


class CreateOrderView(QWidget):

    def __init__(self, model: CreateOrderModel, parent=None):
        super().__init__(parent)

        self._model = model
        self._controller = CreateOrderController(self, self._model)
        self._ui = Ui_Form()
        self.setWindowFlags(Qt.Window)

        self._ui.setupUi(self)
        self.init_slots()
        self.init_data()

    def init_slots(self):
        self._model.order_exists.connect(self.on_order_exists)
        self._ui.order_id_edit.textChanged.connect(self._controller.change_order_id)
        self._ui.create_order_btn.clicked\
            .connect(lambda: self._controller.create_order(self._ui.order_id_edit.text()))
        self._model.order_created.connect(self.on_create_order)
        self._model.order_empty.connect(self.on_order_empty)
        self._model.cart_changed.connect(self.on_cart_changed)
        self._ui.add_goods.clicked.connect(self._controller.add_goods)

    def init_data(self):
        stu_id_regx = QRegExp('^[0-9]{10}$')
        stu_id_validator = QRegExpValidator(stu_id_regx, self._ui.order_id_edit)
        self._ui.order_id_edit.setValidator(stu_id_validator)
        self._ui.order_id_edit.setText(str(self._model.cur_order))

        for client in self._model.get_clients():
            self._ui.client_box.addItem(client['ФИО'])

    @pyqtSlot(bool)
    def on_order_exists(self, order_exists):
        if order_exists:
            self._ui.info_label.setText("Заказ с таким номером существует")
            self._ui.create_order_btn.setDisabled(True)
        else:
            self._ui.info_label.setText("")
            self._ui.create_order_btn.setDisabled(False)

    @pyqtSlot()
    def on_order_empty(self):
        self._ui.info_label.setText("Введите номер заказа")
        self._ui.create_order_btn.setDisabled(True)

    @pyqtSlot(str)
    def on_create_order(self, value):
        msg_box = QMessageBox()
        msg_box.setText(f"Заказ с номером {value} сформирован (Типа)")
        msg_box.setWindowTitle("Успешно")
        msg_box.exec()

    @pyqtSlot()
    def on_cart_changed(self):
        text = "Список:\n" if len(self._model.cart) else "Список пуст"

        for good_id in self._model.cart:
            text += self._model.get_good_by_id(good_id)['Наименование'] + "\n"

        self._ui.goods_label.setText(text)
