from PyQt5.QtCore import QObject, pyqtSlot


class AddGoodController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self._model = model
        self._view = view

    @pyqtSlot(dict)
    def add_good(self, good):
        """Добавить товар"""
        self._model.add_good(good)

    @pyqtSlot()
    def on_added_good(self):
        """Слот при успшеном добавлении товара"""
        self._view.close()
