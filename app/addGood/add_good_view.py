import os.path
import shutil

from PyQt5.QtCore import pyqtSlot, Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog

from addGood.add_good_contrl import AddGoodController
from addGood.add_good_model import AddGoodModel
from addGood.design import Ui_Form


class AddGoodView(QWidget):

    def __init__(self, model: AddGoodModel, parent=None):
        super().__init__(parent)

        self._parent = parent
        self._model = model
        self._controller = AddGoodController(self, self._model)
        self._ui = Ui_Form()

        self.setWindowFlags(Qt.Window)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self._ui.setupUi(self)
        self.init_slots()
        self.init_data()

    def init_slots(self):
        self._ui.choice_img_btn.clicked.connect(self.choice_img)
        self._ui.add_btn.clicked.connect(self.on_add_good_click)
        self._model.good_added.connect(self._controller.on_added_good)
        pass

    def init_data(self):
        stu_id_regx = QRegExp('^[0-9]{10}$')
        stu_id_validator = QRegExpValidator(stu_id_regx, self._ui.cost_hour_edit)
        self._ui.cost_hour_edit.setValidator(stu_id_validator)

        stu_id_regx = QRegExp('^[0-9]{10}$')
        stu_id_validator = QRegExpValidator(stu_id_regx, self._ui.full_cost_edit)
        self._ui.full_cost_edit.setValidator(stu_id_validator)

    @pyqtSlot()
    def choice_img(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "",
                                                  "png (*.png);;jpeg (*.jpg);;All Files (*);;")
        basename = os.path.basename(filename)
        shutil.copy(filename, os.path.join('img/', basename))
        self._ui.imgname_edit.setText(basename)

    @pyqtSlot()
    def on_add_good_click(self):
        good = dict()
        good['title'] = self._ui.title_edit.text()
        good['hour_cost'] = self._ui.cost_hour_edit.text()
        good['full_cost'] = self._ui.full_cost_edit.text()
        good['img'] = self._ui.imgname_edit.text()
        good['description'] = self._ui.description_edit.toPlainText()
        good['category'] = self._ui.type_box.currentText()
        good['count'] = self._ui.count_box.text().split()[0]

        self._controller.add_good(good)

