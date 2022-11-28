from PyQt5.QtCore import QObject, pyqtSlot


class AddGoodController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self._model = model
        self._view = view

    @pyqtSlot(dict)
    def add_good(self, good):
        self._model.add_good(good)

    @pyqtSlot()
    def on_added_good(self):
        self._view.close()