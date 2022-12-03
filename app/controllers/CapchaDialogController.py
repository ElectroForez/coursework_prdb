from PyQt5.QtCore import QObject, pyqtSlot
from common.pdf import print_widget


class CapchaDialogController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self._model = model
        self._view = view

    @pyqtSlot()
    def reload_capcha(self):
        """Обновить капчу"""
        capcha = self._model.generate_capcha()
        self._model.capcha = capcha

    @pyqtSlot(str)
    def check_capcha(self, value):
        """Проверить капчу"""
        if self._model.capcha != value:
            self._view.show_error()
            self._view._parent.on_block_auth()
        else:
            self._view._parent.on_good_capcha()
        self._view.close()

    @pyqtSlot()
    def download_capcha(self):
        print_widget(self._view._ui.capcha_label, 'output.pdf')
        pass
