from PyQt5.QtCore import pyqtSlot, QTimer, Qt, QPoint
from PyQt5.QtGui import QPixmap, QPainter, QKeySequence, QPaintEvent, QColor, QFont
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QMessageBox, QWidget, QAction, QLabel
from PyQt5.uic.properties import QtGui
from random import randint
from views.capchaDialogDesign import Ui_Form

from controllers.CapchaDialogController import CapchaDialogController


class CapchaDialogView(QWidget):
    def __init__(self, model, parent=None):
        super().__init__(parent)

        self._parent = parent
        self._model = model
        self._controller = CapchaDialogController(self, self._model)

        self._ui = Ui_Form()

        self.setWindowFlags(Qt.Window)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)

        self._ui.setupUi(self)
        self.init_slots()
        self.init_data()

    def init_slots(self):
        self._ui.generate_new_btn.clicked.connect(self._controller.reload_capcha)
        self._model.capcha_changed.connect(self.draw_capcha)
        self._ui.confirm_button.clicked\
            .connect(lambda: self._controller.check_capcha(self._ui.capcha_edit.text()))
        self._ui.download_pdf_btn.clicked.connect(self._controller.download_capcha)
        pass

    def init_data(self):
        self.draw_capcha(self._model.capcha)
        pass

    def clear_capcha(self):
        self._ui.capcha_edit.clear()

        label = self._ui.capcha_label
        size = label.size()

        canvas = QPixmap(size)
        canvas.fill(QColor("white"))
        label.setPixmap(canvas)

    @pyqtSlot(str)
    def draw_capcha(self, capcha):
        self.clear_capcha()
        painter = QPainter(self._ui.capcha_label.pixmap())
        font_size = 25
        painter.setFont(QFont("Times", font_size, QFont.Bold))
        canvas_size = self._ui.capcha_label.pixmap().size()
        canvas_width = canvas_size.width()
        canvas_height = canvas_size.height()

        last_x = 0
        last_y = 0
        for symbol in capcha:
            x = randint(last_x, (canvas_width + last_x) // 2)
            y = randint(font_size, canvas_height - font_size)
            point = QPoint(x, y)
            painter.drawText(point, symbol)
            painter.drawLine(
                randint(0, canvas_width),
                randint(0, canvas_height),
                randint(0, canvas_width),
                randint(0, canvas_height),
            )
            last_x = x
            last_y = y
        painter.end()

    def show_error(self):
        msg_box = QMessageBox()
        msg_box.setText("Неверно введённая капча. Возможность входа заблокирована на 10 секунд")
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("СТОЙ! СТРЕЛЯТЬ БУДУ!")
        msg_box.exec()
