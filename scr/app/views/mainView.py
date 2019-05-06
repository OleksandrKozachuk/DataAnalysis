from PyQt5.QtWidgets import QMainWindow
from scr.app.views.mainViewUI import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self.showMaximized()
        # designer is not allowed close widgets at the begins
        self._ui.dockWidgetDataView.close()
        self._ui.dockWidgetProtocol.close()
        self._ui.groupBoxProtocolDetails.close()
        self._ui.groupBoxFileData.close()
