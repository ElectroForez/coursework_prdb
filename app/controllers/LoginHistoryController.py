from PyQt5.QtCore import QObject, pyqtSlot


class LoginHistoryController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self._model = model
        self._view = view

    @pyqtSlot(str)
    def filter_by_login(self, value):
        """Фильтр по логину"""
        self._model.history = self._model.get_history_by_login(value)
