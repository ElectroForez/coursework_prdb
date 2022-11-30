from PyQt5.QtCore import pyqtSignal, QObject

from models.CreateOrderModel import CreateOrderModel
from models.Db import db


class AddGoodModel(QObject):

    good_added = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.db = db

    def get_last_good_id(self):
        self.db.cursor.execute('SELECT MAX("id") FROM goods')
        result = self.db.cursor.fetchone()['max']
        return result

    def add_good(self, good):
        if '' in (good['title'], good['hour_cost'], good['full_cost'], good['category']):
            return

        good['id'] = self.get_last_good_id() + 1

        db.cursor.execute(f'insert into goods '
                          f'VALUES '
                          f'('
                          f'%s, %s, %s, %s, %s, %s, %s, %s'
                          f')',
                          (
                              good['id'],
                              good['title'],
                              good['img'],
                              good['hour_cost'],
                              good['full_cost'],
                              good['description'],
                              good['count'],
                              good['category']
                          )
        )
        self.good_added.emit()
