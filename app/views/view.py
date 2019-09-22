from PyQt5.QtWidgets import QMainWindow

from app.views.designerPyFiles.mainViewUI import Ui_MainWindow

CSV = "CSV(*.csv)"


class MainView(QMainWindow):

    def __init__(self, model, controller, fileDialog, convertFileDialog):
        super().__init__()
        self._model = model
        self._controller = controller
        self._fileDialog = fileDialog
        self._convertFileDialog = convertFileDialog

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # add actions to tool button objects
        self._ui.toolButtonObjectsSettings.addAction(self._ui.actionPreviewObjects)
        self._ui.toolButtonObjectsSettings.addAction(self._ui.actionDeleteObjects)
        self._ui.toolButtonObjectsSettings.addAction(self._ui.actionShiftData)
        self._ui.toolButtonObjectsSettings.addAction(self._ui.actionStandartizeData)
        self._ui.toolButtonObjectsSettings.addAction(self._ui.actionLogData)
        self._ui.toolButtonObjectsSettings.addAction(self._ui.actionDeleteAbnormalData)
        # designer is not allowed close widgets at the begins
        self._ui.dockWidgetDataView.close()
        self._ui.dockWidgetProtocol.close()
        # connect actions to controller
        self._ui.actionConvertToCSV.triggered.connect(
            lambda: self._controller.setOpenPathConvertFile(
                self._fileDialog.openFileNameDialog()
            )
        )
        self._ui.actionOpen.triggered.connect(
            lambda: self._controller.setPathOpenFileDialog(
                self._fileDialog.openFileNameDialog(filetype=CSV)
            )
        )
        self._ui.actionSave.triggered.connect(self._fileDialog.saveFileDialog)
        # connect widgets to controller
        # self._convertFileDialog.lineEditDelimiter.textChanged.connect()
        # self._convertFileDialog.lineEditHeaderNames.textChanged.connect()
        # self._convertFileDialog.pushButtonConvert.clicked.connect()
        # self._convertFileDialog.pushButtonCancel.clicked.connect()
        # listen for models event signals
        # self._model.filePathAdded.connect(self.showDataViewItems)
        self._model.pathFileOpenAdded.connect(self._ui.dockWidgetDataView.show)
        self._model.pathConvertFileAdded.connect(self._convertFileDialog.show)
