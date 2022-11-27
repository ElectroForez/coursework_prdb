from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from views.personalAccountDesign import Ui_MainWindow

from models.PersonalAccountModel import PersonalAccountModel
from controllers.PersonalAccountController import PersonalAccountController


class PersonalAccountView(QMainWindow):

    def __init__(self, model: PersonalAccountModel):
        super().__init__()

        self._model = model
        self._controller = PersonalAccountController(self, self._model)
        self._ui = Ui_MainWindow()

        self.setAttribute(Qt.WA_DeleteOnClose)
        self._ui.setupUi(self)
        self.init_slots()
        self.init_data()

    def init_slots(self):
        self._ui.see_history.clicked.connect(self._controller.open_history)
        self._ui.create_order_btn.clicked.connect(self._controller.create_order)
        self._ui.deauth_btn.triggered.connect(self._controller.deauth)
        self._ui.exit_btn.triggered.connect(self._controller.close)
        # self._ui.create_order_btn.clicked.connect(self._controller)

    def init_data(self):
        fio = self._model.user['ФИО']
        position = self._model.user['Должность']

        lastname = fio.split()[0]
        photo = QPixmap(f"./img/{lastname}.jpeg")

        self._ui.photo_label.setPixmap(photo)
        self._ui.fio_label.setText(fio)
        self._ui.position_label.setText(position)

        if position != 'Администратор':
            self._ui.see_history.hide()
        else:
            # self._ui.create_order_btn.hide()
            pass
