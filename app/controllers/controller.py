from PyQt5.QtCore import QObject, pyqtSlot


class MainController(QObject):

    def __init__(self, model):
        super().__init__()
        self._model = model

    @pyqtSlot(str)
    def setPathOpenFileDialog(self, path):
        if isinstance(path, str):
            self._model.pathFileOpen = path

    @pyqtSlot(str)
    def setOpenPathConvertFile(self, path):
        if isinstance(path, str):
            self._model.pathConvertFile = path

    @pyqtSlot(str)
    def setPathSaveFileDialog(self, path):
        if isinstance(path, str):
            self._model.pathFileSave = path

    def setParametersConvertFileDialog(self, delimiter: str, names: str):
        if delimiter and names:
            self._model.parametersConvertFileDialog = delimiter, names
