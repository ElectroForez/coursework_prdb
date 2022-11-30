import os.path
import sys
from random import randint

from PyQt5 import QtPrintSupport
from PyQt5.QtCore import pyqtSlot, QRegExp, Qt, QPoint
from PyQt5.QtGui import QPixmap, QRegExpValidator, QColor, QPainter, QFont
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QWidget, QMessageBox, QApplication, QTableWidgetItem, \
    QLabel, QTableWidget

from models.CreateOrderModel import CreateOrderModel
from views.createOrderDesign import Ui_Form
from models.PersonalAccountModel import PersonalAccountModel

from controllers.CreateOrderController import CreateOrderController
from common.pdf import print_widget


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
            .connect(self.on_create_order)
        self._model.order_create.connect(self.on_created_order)
        self._model.order_empty.connect(self.on_order_empty)
        self._model.cart_changed.connect(self.on_order_changed)
        self._ui.add_goods.clicked.connect(self._controller.add_goods)
        self._ui.hours_count_box.textChanged.connect(self.on_order_changed)

    def init_data(self):
        stu_id_regx = QRegExp('^[0-9]{10}$')
        stu_id_validator = QRegExpValidator(stu_id_regx, self._ui.order_id_edit)
        self._ui.order_id_edit.setValidator(stu_id_validator)
        self._ui.order_id_edit.setText(str(self._model.cur_order))

        for client in self._model.get_clients():
            self._ui.client_box.addItem(client['fullname'])

        self.draw_list()

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

    @pyqtSlot()
    def on_create_order(self):
        order = dict()
        order['id'] = int(self._ui.order_id_edit.text())
        order['arenda_hours'] = int(self._ui.hours_count_box.text().split()[0])
        order['client_fullname'] = self._ui.client_box.currentText()
        order['cart'] = self._model.cart
        self._controller.create_order(order)

    @pyqtSlot(int)
    def on_created_order(self, order_id):
        self.print_pdf()
        msg_box = QMessageBox()
        msg_box.setText(f"Заказ с номером {order_id} сформирован")
        msg_box.setWindowTitle("Успешно")
        msg_box.exec()
        self._controller.success_create_order()

    @pyqtSlot()
    def on_order_changed(self):
        self.draw_list()

    def draw_list(self):
        cart = self._model.cart
        table = self._ui.goods_table
        table.clearContents()

        table.setRowCount(len(cart))

        total_sum = 0
        for i in range(len(cart)):
            good = self._model.get_good_by_id(cart[i])
            table.setItem(i, 0, QTableWidgetItem(str(good['title'])))
            table.setItem(i, 1, QTableWidgetItem(str(good['cost_per_hour'])))
            s = good['cost_per_hour'] * int(self._ui.hours_count_box.text().split()[0])
            total_sum += s
            table.setItem(i, 2, QTableWidgetItem(str(s)))

        self._ui.total_value_lbl.setText(str(total_sum) + " руб.")
        # table.resizeColumnsToContents()
        table.setSortingEnabled(True)

    def print_pdf(self):
        text = f"""
Номер заказа: {self._ui.order_id_edit.text()}
Клиент: {self._ui.client_box.currentText()}
Количество часов проката: {self._ui.hours_count_box.text()}
        
Список товаров:
        
"""
        cart = self._model.cart
        cart_text = ""
        for good_id in cart:
            good = self._model.get_good_by_id(good_id)
            cart_text += f"{good['title']}, {good['cost_per_hour']} руб.)\n"
        text += cart_text

        text += f"Итого: {self._ui.total_value_lbl.text()}"
        text = text.replace('\n', '\n    ')
        label = QLabel(text)
        label.setStyleSheet('background-color: #FFF')
        print_widget(label, os.path.join('../res/reports/', f'{self._ui.order_id_edit.text()}.pdf'))
