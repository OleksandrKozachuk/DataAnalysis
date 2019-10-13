from PyQt5.QtWidgets import QDialog

from app.views.designerPyFiles.previewDataDialogViewUI import Ui_FormDataView


class PreviewDataDialog(QDialog):

    def __init__(self, main_controller):
        super().__init__()
        self._controller = main_controller

        self._ui = Ui_FormDataView()
        self._ui.setupUi(self)

    def showDataSet(self, dataInfo: str):
        self._ui.plainTextEditDataView.clear()
        self._ui.plainTextEditDataView.setPlainText(dataInfo)
