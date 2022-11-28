from PyQt5.QtCore import QObject, pyqtSlot


class CloseOrderController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self._model = model
        self._view = view

    @pyqtSlot(str)
    def change_order_id(self, id):
        self._model.cur_order = id

    @pyqtSlot(str)
    def close_order(self, order_id):
        self._model.close_order_by_id(order_id)

    @pyqtSlot()
    def success_close_order(self):
        self._view.close()
