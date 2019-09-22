from PyQt5.QtWidgets import QDialog

from app.views.designerPyFiles.convertDialogViewUI import Ui_convertFileDialog


class ConvertFileDialog(QDialog):

    def __init__(self, main_controller):
        super().__init__()
        self._controller = main_controller

        self._ui = Ui_convertFileDialog()
        self._ui.setupUi(self)

        self._ui.pushButtonConvert.clicked.connect(
            lambda: (self._controller.setParametersConvertFileDialog(
                self._ui.lineEditDelimiter.text(),
                self._ui.lineEditHeaderNames.text()
                ),
                self.close()
            )
        )


def convertToCSV(path: str, delimiter: str, names: str):
    nameFile, _ = path.split('.')
    with open(path, 'r') as infile, open('{}.csv'.format(nameFile), 'w') as outfile:
        outfile.write(names + "\n")
        for line in infile:
            outfile.write(line.replace(delimiter, ','))
