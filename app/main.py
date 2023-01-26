#!/bin/python3
import sys

from PyQt5.QtWidgets import QApplication
from models.AuthorizeModel import AuthorizeModel
from views.AuthorizeView import AuthorizeView
from models.Db import Db


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        self.model = AuthorizeModel()
        self.view = AuthorizeView(self.model)
        self.view.show()


def init_db():
    db = Db()
    try:
        backup_sql = open("../res/db.sql").read()
        db.simple_cursor.execute(backup_sql)
        db.connection.commit()
    except:
        print('Database already exists')
    finally:
        db.connection.close()


#  Запускаем приложение
if __name__ == '__main__':
    init_db()
    app = App(sys.argv)
    sys.exit(app.exec_())
