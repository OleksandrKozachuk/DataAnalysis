from PyQt5.QtCore import QObject, pyqtSignal
import numpy as np
from app.other.storage import DataFrame


class Model(QObject):
    convertParametersAdded = pyqtSignal(tuple)
    pathConvertFileAdded = pyqtSignal(str)
    pathFileOpenAdded = pyqtSignal(str)
    pathFileSaveAdded = pyqtSignal(str)
    fileDataAdded = pyqtSignal(list)
    listDataCountSelectedItemsChanged = pyqtSignal(int)

    def __init__(self):
        super(Model, self).__init__()
        self._pathFileOpen = None
        self._pathFileSave = None
        self._countCheckedItems = 0
        # parameters for convert file dialog
        self._pathConvertFile = None
        self._parametersConvertFileDialog = None
        # storage of data
        self._dataFrame = DataFrame()
        # connect into otherModels models
        self.pathFileOpenAdded.connect(self.onFilePathAdded)
        self.convertParametersAdded.connect(self.onConvertParametersAdded)

    @property
    def dataFrame(self):
        return self._dataFrame

    @property
    def pathFileOpen(self):
        return self._pathFileOpen

    @pathFileOpen.setter
    def pathFileOpen(self, path: str):
        self._pathFileOpen = path
        self.pathFileOpenAdded.emit(path)

    @property
    def pathFileSave(self):
        return self._pathFileSave

    @pathFileSave.setter
    def pathFileSave(self, path: str):
        self._pathFileSave = path
        self.pathFileSaveAdded.emit(path)

    @property
    def pathConvertFile(self):
        return self._pathConvertFile

    @pathConvertFile.setter
    def pathConvertFile(self, path: str):
        self._pathConvertFile = path
        self.pathConvertFileAdded.emit(path)

    @property
    def parametersConvertFileDialog(self):
        return self._parametersConvertFileDialog

    @parametersConvertFileDialog.setter
    def parametersConvertFileDialog(self, values: tuple):
        self._parametersConvertFileDialog = values
        self.convertParametersAdded.emit(values)

    @property
    def countCheckedItems(self):
        return self._countCheckedItems

    @countCheckedItems.setter
    def countCheckedItems(self, count: int):
        self._countCheckedItems = count
        self.listDataCountSelectedItemsChanged.emit(count)

    def onConvertParametersAdded(self):
        from app.other.Dialogs.convertFileDialog import convertToCSV

        delimiter, names = self.parametersConvertFileDialog
        try:
            convertToCSV(
                path=self.pathConvertFile,
                delimiter=delimiter,
                names=names
            )
        except Exception as e:
            raise e

    def onFilePathAdded(self):
        # set extracted content from file into storage
        content = self.dataFrame.getContentFromFile(self.pathFileOpen)
        self.dataFrame.frame = content
        # emit field names in file into view
        fieldNames = self.dataFrame.getFieldNames().tolist()
        self.fileDataAdded.emit(fieldNames)
