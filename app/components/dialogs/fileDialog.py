from PyQt5.QtWidgets import QFileDialog


class FileDialog(QFileDialog):

    def __init__(self, controller):
        super().__init__()
        self._controller = controller

    def openFileNameDialog(self, filetype=""):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Оберіть файл", "", filetype,
                                                  options=options)
        if fileName:
            return fileName

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Зберегти файл", "", "CSV(*.csv)",
                                                  options=options)
        if fileName:
            self._controller.setPathSaveFileDialog(fileName)
