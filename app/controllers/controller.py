from PyQt5.QtCore import QObject, pyqtSlot, Qt
from PyQt5.QtGui import QStandardItemModel


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

    @pyqtSlot(QStandardItemModel)
    def setNameSelectedItem(self, model: QStandardItemModel):
        namesSelectedItems = []
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.checkState() == Qt.Checked:
                namesSelectedItems.append(item.text())

        self._model.namesCheckedItems = namesSelectedItems

    def setParametersConvertFileDialog(self, delimiter: str, names: str):
        if delimiter and names:
            self._model.parametersConvertFileDialog = delimiter, names

    def setSignificanceLevel(self, alpha: str):
        try:
            self._model.signLevel = float(alpha)
        except ValueError:
            return
