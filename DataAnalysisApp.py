import sys
from PyQt5.QtWidgets import QApplication
from model.model import Model
from controllers.mainCtrl import MainController
from views.mainView import MainView


class App(QApplication):

    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        self.model = Model()
        self.mainController = MainController(self.model)
        self.mainView = MainView(self.model, self.mainController)
        self.mainView.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
