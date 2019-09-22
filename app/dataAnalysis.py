from PyQt5.QtWidgets import QApplication

from app.controllers.controller import MainController
from app.models.model import Model
from app.other.Dialogs.convertFileDialog import ConvertFileDialog
from app.other.Dialogs.fileDialog import FileDialog
from app.views.view import MainView


class App(QApplication):

    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        self.model = Model()
        self.controller = MainController(self.model)
        self.fileDialog = FileDialog(self.controller)
        self.convertFileDialog = ConvertFileDialog(self.controller)
        self.view = MainView(self.model, self.controller, self.fileDialog, self.convertFileDialog)
        self.view.show()


def main():
    import sys

    app = App(sys.argv)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
