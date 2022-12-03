import datetime

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

import string
import random


class CapchaDialogModel(QObject):

    capcha_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._capcha = self.generate_capcha()

    @property
    def capcha(self):
        return self._capcha

    @capcha.setter
    def capcha(self, value):
        self._capcha = value
        self.capcha_changed.emit(self._capcha)

    def generate_capcha(self, length=5):
        """Сгенерировать содержание капчи"""
        vars = string.ascii_letters + string.digits
        capcha = ''.join(random.sample(vars, length))
        return capcha

