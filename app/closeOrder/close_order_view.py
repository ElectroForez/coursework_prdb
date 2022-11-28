import os.path

from PyQt5.QtCore import pyqtSlot, Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QMessageBox
from closeOrder.design import Ui_Form

from closeOrder.close_order_contrl import CloseOrderController
from closeOrder.close_order_model import CloseOrderModel


class CloseOrderView(QWidget):

    def __init__(self, model: CloseOrderModel, parent=None):
        super().__init__(parent)

        self._parent = parent
        self._model = model
        self._controller = CloseOrderController(self, self._model)
        self._ui = Ui_Form()

        self.setWindowFlags(Qt.Window)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self._ui.setupUi(self)
        self.init_slots()
        self.init_data()

    def init_slots(self):
        self._ui.order_id_edit.textChanged.connect(self._controller.change_order_id)
        self._model.order_empty.connect(self.on_order_empty)
        self._model.order_exists.connect(self.on_order_exists)
        self._model.order_already_close.connect(self.on_order_already_close)
        self._ui.close_order_btn.clicked\
            .connect(lambda: self._controller.close_order(self._ui.order_id_edit.text()))
        self._model.order_close\
            .connect(self.on_created_order)

    def init_data(self):
        stu_id_regx = QRegExp('^[0-9]{10}$')
        stu_id_validator = QRegExpValidator(stu_id_regx, self._ui.order_id_edit)
        self._ui.order_id_edit.setValidator(stu_id_validator)

    @pyqtSlot(bool)
    def on_order_exists(self, order_exists):
        if not order_exists:
            self._ui.info_label.setText("Заказ с таким номером отсутствует")
            self._ui.close_order_btn.setDisabled(True)
        else:
            self._ui.info_label.setText("")
            self._ui.close_order_btn.setDisabled(False)

    @pyqtSlot()
    def on_order_empty(self):
        self._ui.info_label.setText("Введите номер заказа")
        self._ui.close_order_btn.setDisabled(True)

    @pyqtSlot()
    def on_order_already_close(self):
        self._ui.info_label.setText("Заказ уже закрыт")
        self._ui.close_order_btn.setDisabled(True)

    @pyqtSlot(str)
    def on_created_order(self, order_id):
        msg_box = QMessageBox()
        msg_box.setText(f"Заказ с номером {order_id} закрыт")
        msg_box.setWindowTitle("Успешно")
        msg_box.exec()
        self._controller.success_close_order()
