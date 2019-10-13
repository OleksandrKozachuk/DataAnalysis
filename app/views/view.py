from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QToolButton

from app.views.designerPyFiles.mainViewUI import Ui_MainWindow

CSV = "CSV(*.csv)"


class MainView(QMainWindow):

    def __init__(self, model, controller, fileDialog, convertFileDialog, previewDataDialog):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._model = model
        self._controller = controller
        self._fileDialog = fileDialog
        self._convertFileDialog = convertFileDialog
        self._previewDataDialog = previewDataDialog
        # create tool buttons for analysis tool bars
        self.toolButtonGraphicsMultiDimAnalysis = QToolButton()
        self.toolButtonCorrelationMultiDimAnalysis = QToolButton()
        # init tool buttons
        self.initToolButtonActionsOnData()
        self.initToolButtonMultiDimGraphics()
        self.initToolButtonCorrelationMultiDimAnalysis()
        # init tool bars
        self.initToolBarMultiDim()
        # init QtListView as widget
        self.modelListView = QStandardItemModel(self._ui.listViewObjects)
        self._ui.listViewObjects.setModel(self.modelListView)
        # close widgets, coz QtDesigner is not allowed close widgets
        self._ui.dockWidgetDataView.close()
        self._ui.dockWidgetProtocol.close()
        self.closeToolBars()
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
        self._ui.actionPreviewObjects.triggered.connect(
            lambda: self.showSelectedItems(self._model.namesCheckedItems)
        )
        self._ui.actionDeleteObjects.triggered.connect(
            lambda: (
                self._model.dataFrame.removeColumns(self._model.namesCheckedItems),
                self.showDataViewItems(self._model.dataFrame.getFieldNames().tolist())
            )
        )
        self._ui.actionStandardizeData.triggered.connect(
            lambda: (
                self._model.dataFrame.standardizeSelected(self._model.namesCheckedItems),
                self.showDataViewItems(self._model.dataFrame.getFieldNames().tolist())
            )
        )
        self._ui.actionDeleteAbnormalData.triggered.connect(
            lambda: (
                self._model.dataFrame.deleteAbnormalSelected(self._model.namesCheckedItems),
                self.showDataViewItems(self._model.dataFrame.getFieldNames().tolist())
            )
        )
        self._ui.actionShiftData.triggered.connect(
            lambda: (
                self._model.dataFrame.shiftSelected(self._model.namesCheckedItems),
                self.showDataViewItems(self._model.dataFrame.getFieldNames().tolist())
            )
        )
        self._ui.actionLogData.triggered.connect(
            lambda: (
                self._model.dataFrame.logSelected(self._model.namesCheckedItems),
                self.showDataViewItems(self._model.dataFrame.getFieldNames().tolist())
            )
        )
        self._ui.actionPCA.triggered.connect(
            lambda: (
                self._model.dataFrame.principalComponentAnalysis(self._model.namesCheckedItems),
                self.showDataViewItems(self._model.dataFrame.getFieldNames().tolist())
            )
        )
        self.modelListView.itemChanged.connect(
            lambda: self._controller.setNameSelectedItem(self.modelListView)
        )
        self._ui.lineEditSignificanceLevel.textChanged.connect(
            self._controller.setSignificanceLevel
        )
        # listen for models event signals
        self._model.pathFileOpenAdded.connect(self._ui.dockWidgetDataView.show)
        self._model.pathConvertFileAdded.connect(self._convertFileDialog.show)
        self._model.fileDataAdded.connect(self.showDataViewItems)
        self._model.listDataNamesSelectedItemsChanged.connect(self.showAnalysisToolBar)

    def initToolBarMultiDim(self):
        self._ui.toolBarMultiDimAnalysis.addWidget(self.toolButtonGraphicsMultiDimAnalysis)
        self._ui.toolBarMultiDimAnalysis.addWidget(self.toolButtonCorrelationMultiDimAnalysis)
        self._ui.toolBarMultiDimAnalysis.addAction(self._ui.actionRegressionAnalysis)
        self._ui.toolBarMultiDimAnalysis.addAction(self._ui.actionPCA)
        self._ui.toolBarMultiDimAnalysis.addAction(self._ui.actionFactorAnalysis)

    def initToolButtonActionsOnData(self):
        # add actions into QtTooButton
        self._ui.toolButtonObjectsSettings.addAction(self._ui.actionPreviewObjects)
        self._ui.toolButtonObjectsSettings.addAction(self._ui.actionDeleteObjects)
        self._ui.toolButtonObjectsSettings.addAction(self._ui.actionShiftData)
        self._ui.toolButtonObjectsSettings.addAction(self._ui.actionStandardizeData)
        self._ui.toolButtonObjectsSettings.addAction(self._ui.actionLogData)
        self._ui.toolButtonObjectsSettings.addAction(self._ui.actionDeleteAbnormalData)

    def initToolButtonMultiDimGraphics(self):
        self.setDefaultSettingToolButton(
            button=self.toolButtonGraphicsMultiDimAnalysis,
            imagePath=":/imgRc/images/graphics.png"
        )
        # add graphics action into toolButtonGraphics
        self.toolButtonGraphicsMultiDimAnalysis.addAction(self._ui.actionMatrixScatterDiagrams)
        self.toolButtonGraphicsMultiDimAnalysis.addAction(self._ui.actionDiagramParallelCoordinates)
        self.toolButtonGraphicsMultiDimAnalysis.addAction(self._ui.actionBubbleDiagram)
        self.toolButtonGraphicsMultiDimAnalysis.addAction(self._ui.actionDiagnosticChart)

    def initToolButtonCorrelationMultiDimAnalysis(self):
        self.setDefaultSettingToolButton(
            button=self.toolButtonCorrelationMultiDimAnalysis,
            imagePath=":/imgRc/images/correlation.png"
        )
        # add actions action into toolButtonGraphics
        self.toolButtonCorrelationMultiDimAnalysis.addAction(
            self._ui.actionMultipleCorrelationCoefficient
        )
        self.toolButtonCorrelationMultiDimAnalysis.addAction(
            self._ui.actionPartialCorrelationCoefficient
        )

    @staticmethod
    def setDefaultSettingToolButton(button: QToolButton, imagePath: str):
        icon = QIcon(imagePath)
        icon.addPixmap(QPixmap(), QIcon.Normal, QIcon.Off)
        button.setIcon(icon)
        # set default setting tool button graphics
        button.setContextMenuPolicy(Qt.DefaultContextMenu)
        button.setAutoFillBackground(False)
        button.setPopupMode(QToolButton.InstantPopup)
        button.setToolButtonStyle(Qt.ToolButtonIconOnly)
        button.setAutoRaise(True)

    @pyqtSlot(list)
    def showDataViewItems(self, names: list):
        self.modelListView.clear()
        # update list widget, add field names into list
        for name in names:
            item = QStandardItem(name)
            # add a checkbox to it
            item.setCheckable(True)
            self.modelListView.appendRow(item)

    def closeToolBars(self):
        self._ui.toolBar1DAnalysis.close()
        self._ui.toolBar2DAnalysis.close()
        self._ui.toolBarMultiDimAnalysis.close()

    @pyqtSlot(list)
    def showAnalysisToolBar(self, names: list):
        # close all visible toolbars
        self.closeToolBars()
        count = len(names)
        # if count checkable data column equal to analysis, show toolbar
        if count == 1:
            self._ui.toolBar1DAnalysis.show()
        elif count == 2:
            self._ui.toolBar2DAnalysis.show()
        elif count >= 3 and not self._ui.toolBarMultiDimAnalysis.isVisible():
            self._ui.toolBarMultiDimAnalysis.show()
        else:
            return

    @pyqtSlot(list)
    def showSelectedItems(self, names: list):
        dataInfo = self._model.dataFrame.frame[names].to_string()
        self._previewDataDialog.showDataSet(dataInfo)
        self._previewDataDialog.show()
