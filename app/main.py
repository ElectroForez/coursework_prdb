import sys

from PyQt5.QtWidgets import QApplication
from models.AuthorizeModel import AuthorizeModel
from views.AuthorizeView import AuthorizeView


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        self.model = AuthorizeModel()
        self.view = AuthorizeView(self.model)
        self.view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
