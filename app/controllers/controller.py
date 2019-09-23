from PyQt5.QtCore import QObject, pyqtSlot, Qt
from PyQt5.QtGui import QStandardItem


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

    @pyqtSlot(QStandardItem)
    def listDataChangeCountSelectedItems(self, item: QStandardItem):
        if item.checkState() == Qt.Checked:
            self._model.countCheckedItems += 1
        else:
            self._model.countCheckedItems -= 1
