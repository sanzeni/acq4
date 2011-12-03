# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/devices/Scanner/ProtocolTemplate.ui'
#
# Created: Fri Dec  2 19:52:49 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(918, 541)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QtGui.QGridLayout(Form)
        self.gridLayout_4.setMargin(3)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.cameraCombo = QtGui.QComboBox(Form)
        self.cameraCombo.setObjectName(_fromUtf8("cameraCombo"))
        self.horizontalLayout_3.addWidget(self.cameraCombo)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.laserCombo = QtGui.QComboBox(Form)
        self.laserCombo.setObjectName(_fromUtf8("laserCombo"))
        self.horizontalLayout_4.addWidget(self.laserCombo)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 2)
        self.simulateShutterCheck = QtGui.QCheckBox(Form)
        self.simulateShutterCheck.setObjectName(_fromUtf8("simulateShutterCheck"))
        self.gridLayout.addWidget(self.simulateShutterCheck, 2, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setMargin(3)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.sizeFromCalibrationRadio = QtGui.QRadioButton(self.groupBox_2)
        self.sizeFromCalibrationRadio.setChecked(True)
        self.sizeFromCalibrationRadio.setObjectName(_fromUtf8("sizeFromCalibrationRadio"))
        self.gridLayout_2.addWidget(self.sizeFromCalibrationRadio, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.sizeCustomRadio = QtGui.QRadioButton(self.groupBox_2)
        self.sizeCustomRadio.setObjectName(_fromUtf8("sizeCustomRadio"))
        self.horizontalLayout_2.addWidget(self.sizeCustomRadio)
        self.sizeSpin = SpinBox(self.groupBox_2)
        self.sizeSpin.setSuffix(_fromUtf8(""))
        self.sizeSpin.setMinimum(0.0)
        self.sizeSpin.setMaximum(100000.0)
        self.sizeSpin.setSingleStep(1e-06)
        self.sizeSpin.setProperty(_fromUtf8("value"), 0.0)
        self.sizeSpin.setObjectName(_fromUtf8("sizeSpin"))
        self.horizontalLayout_2.addWidget(self.sizeSpin)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 2)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.addPointBtn = QtGui.QPushButton(Form)
        self.addPointBtn.setObjectName(_fromUtf8("addPointBtn"))
        self.gridLayout_5.addWidget(self.addPointBtn, 0, 0, 1, 1)
        self.addOcclusionBtn = QtGui.QPushButton(Form)
        self.addOcclusionBtn.setObjectName(_fromUtf8("addOcclusionBtn"))
        self.gridLayout_5.addWidget(self.addOcclusionBtn, 0, 1, 1, 1)
        self.addGridBtn = QtGui.QPushButton(Form)
        self.addGridBtn.setObjectName(_fromUtf8("addGridBtn"))
        self.gridLayout_5.addWidget(self.addGridBtn, 1, 0, 1, 1)
        self.addProgramBtn = QtGui.QPushButton(Form)
        self.addProgramBtn.setEnabled(False)
        self.addProgramBtn.setObjectName(_fromUtf8("addProgramBtn"))
        self.gridLayout_5.addWidget(self.addProgramBtn, 1, 1, 1, 1)
        self.deleteBtn = QtGui.QPushButton(Form)
        self.deleteBtn.setObjectName(_fromUtf8("deleteBtn"))
        self.gridLayout_5.addWidget(self.deleteBtn, 2, 0, 1, 1)
        self.deleteAllBtn = QtGui.QPushButton(Form)
        self.deleteAllBtn.setObjectName(_fromUtf8("deleteAllBtn"))
        self.gridLayout_5.addWidget(self.deleteAllBtn, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 4, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(83, 59, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(190, 210))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setMargin(3)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.minTimeSpin = SpinBox(self.groupBox)
        self.minTimeSpin.setSuffix(_fromUtf8(""))
        self.minTimeSpin.setDecimals(2)
        self.minTimeSpin.setMaximum(1000000.0)
        self.minTimeSpin.setObjectName(_fromUtf8("minTimeSpin"))
        self.gridLayout_3.addWidget(self.minTimeSpin, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.minDistSpin = SpinBox(self.groupBox)
        self.minDistSpin.setSuffix(_fromUtf8(""))
        self.minDistSpin.setMaximum(1000000.0)
        self.minDistSpin.setObjectName(_fromUtf8("minDistSpin"))
        self.gridLayout_3.addWidget(self.minDistSpin, 2, 1, 1, 1)
        self.recomputeBtn = QtGui.QPushButton(self.groupBox)
        self.recomputeBtn.setObjectName(_fromUtf8("recomputeBtn"))
        self.gridLayout_3.addWidget(self.recomputeBtn, 3, 0, 1, 1)
        self.autoRecomputeCheck = QtGui.QCheckBox(self.groupBox)
        self.autoRecomputeCheck.setEnabled(False)
        self.autoRecomputeCheck.setObjectName(_fromUtf8("autoRecomputeCheck"))
        self.gridLayout_3.addWidget(self.autoRecomputeCheck, 3, 1, 1, 1)
        self.tdPlotWidget = PlotWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tdPlotWidget.sizePolicy().hasHeightForWidth())
        self.tdPlotWidget.setSizePolicy(sizePolicy)
        self.tdPlotWidget.setObjectName(_fromUtf8("tdPlotWidget"))
        self.gridLayout_3.addWidget(self.tdPlotWidget, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 6, 0, 1, 2)
        self.timeLabel = QtGui.QLabel(Form)
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.gridLayout.addWidget(self.timeLabel, 7, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 3, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_4.addWidget(self.label_5, 0, 1, 1, 2)
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 0, 3, 1, 1)
        self.itemTree = TreeWidget(Form)
        self.itemTree.setObjectName(_fromUtf8("itemTree"))
        self.gridLayout_4.addWidget(self.itemTree, 1, 1, 1, 2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.addLineScanBtn = QtGui.QPushButton(Form)
        self.addLineScanBtn.setEnabled(False)
        self.addLineScanBtn.setObjectName(_fromUtf8("addLineScanBtn"))
        self.verticalLayout.addWidget(self.addLineScanBtn)
        self.addCircleScanBtn = QtGui.QPushButton(Form)
        self.addCircleScanBtn.setEnabled(False)
        self.addCircleScanBtn.setObjectName(_fromUtf8("addCircleScanBtn"))
        self.verticalLayout.addWidget(self.addCircleScanBtn)
        self.addSpiralScanBtn = QtGui.QPushButton(Form)
        self.addSpiralScanBtn.setEnabled(False)
        self.addSpiralScanBtn.setObjectName(_fromUtf8("addSpiralScanBtn"))
        self.verticalLayout.addWidget(self.addSpiralScanBtn)
        self.deleteStepBtn = QtGui.QPushButton(Form)
        self.deleteStepBtn.setEnabled(False)
        self.deleteStepBtn.setObjectName(_fromUtf8("deleteStepBtn"))
        self.verticalLayout.addWidget(self.deleteStepBtn)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.previewBtn = QtGui.QPushButton(Form)
        self.previewBtn.setEnabled(False)
        self.previewBtn.setObjectName(_fromUtf8("previewBtn"))
        self.verticalLayout.addWidget(self.previewBtn)
        self.gridLayout_4.addLayout(self.verticalLayout, 1, 3, 1, 1)
        self.programTable = QtGui.QTableWidget(Form)
        self.programTable.setObjectName(_fromUtf8("programTable"))
        self.programTable.setColumnCount(0)
        self.programTable.setRowCount(0)
        self.gridLayout_4.addWidget(self.programTable, 1, 4, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.hideCheck = QtGui.QCheckBox(Form)
        self.hideCheck.setEnabled(True)
        self.hideCheck.setChecked(False)
        self.hideCheck.setObjectName(_fromUtf8("hideCheck"))
        self.horizontalLayout_5.addWidget(self.hideCheck)
        self.hideMarkerBtn = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hideMarkerBtn.sizePolicy().hasHeightForWidth())
        self.hideMarkerBtn.setSizePolicy(sizePolicy)
        self.hideMarkerBtn.setObjectName(_fromUtf8("hideMarkerBtn"))
        self.horizontalLayout_5.addWidget(self.hideMarkerBtn)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 2, 1, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 2, 3, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Camera Module:", None, QtGui.QApplication.UnicodeUTF8))
        self.cameraCombo.setToolTip(QtGui.QApplication.translate("Form", "Selects the camera module to use with the scanner. This, along with the laser device, determines which calibration files will be used.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Laser Device:", None, QtGui.QApplication.UnicodeUTF8))
        self.laserCombo.setToolTip(QtGui.QApplication.translate("Form", "Selects the laser to be used.", None, QtGui.QApplication.UnicodeUTF8))
        self.simulateShutterCheck.setText(QtGui.QApplication.translate("Form", "Simulate Shutter", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Spot Display Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeFromCalibrationRadio.setToolTip(QtGui.QApplication.translate("Form", "Causes target spots to be displayed at the size determined by the calibration file. Does not affect how data is collected.", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeFromCalibrationRadio.setText(QtGui.QApplication.translate("Form", "Use size from calibration", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeCustomRadio.setToolTip(QtGui.QApplication.translate("Form", "Lets the user change the display size of target spots. Does not change the way data is collected.", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeCustomRadio.setText(QtGui.QApplication.translate("Form", "Use custom size:", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeSpin.setToolTip(QtGui.QApplication.translate("Form", "Specifies the display size of the target spots. Does not change the way data is collected.", None, QtGui.QApplication.UnicodeUTF8))
        self.addPointBtn.setToolTip(QtGui.QApplication.translate("Form", "Add a target point to the canvas.", None, QtGui.QApplication.UnicodeUTF8))
        self.addPointBtn.setText(QtGui.QApplication.translate("Form", "Add Point", None, QtGui.QApplication.UnicodeUTF8))
        self.addOcclusionBtn.setToolTip(QtGui.QApplication.translate("Form", "Add an occlusion. Occlusions can be placed over points that the user doesn\'t want included in the protocol. (For example, points that lie over a pipette.)", None, QtGui.QApplication.UnicodeUTF8))
        self.addOcclusionBtn.setText(QtGui.QApplication.translate("Form", "Add Occlusion", None, QtGui.QApplication.UnicodeUTF8))
        self.addGridBtn.setToolTip(QtGui.QApplication.translate("Form", "Add a grid of points to the canvas.", None, QtGui.QApplication.UnicodeUTF8))
        self.addGridBtn.setText(QtGui.QApplication.translate("Form", "Add Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.addProgramBtn.setText(QtGui.QApplication.translate("Form", "Add Program", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteBtn.setToolTip(QtGui.QApplication.translate("Form", "Delete the selected item.", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteBtn.setText(QtGui.QApplication.translate("Form", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteAllBtn.setToolTip(QtGui.QApplication.translate("Form", "Delete all the items in the canvas.", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteAllBtn.setText(QtGui.QApplication.translate("Form", "Delete All", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Spot Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Minimum time", None, QtGui.QApplication.UnicodeUTF8))
        self.minTimeSpin.setToolTip(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">When stimulating a sequence of points, this is the minimum amount of time that must pass before stimulating the same spot a second time. Points farther away will require smaller delays. Points farther than the minimum distance (specified below) will require no delay.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Minimum distance", None, QtGui.QApplication.UnicodeUTF8))
        self.minDistSpin.setToolTip(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">When stimulating a sequence of points, this is the minimum distance between two spots such that no time delay is required between stimulating them. Points closer than this distance will require some delay, which is determined in part by the minimum time specified above.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.recomputeBtn.setText(QtGui.QApplication.translate("Form", "Recompute", None, QtGui.QApplication.UnicodeUTF8))
        self.autoRecomputeCheck.setText(QtGui.QApplication.translate("Form", "Auto recompute", None, QtGui.QApplication.UnicodeUTF8))
        self.timeLabel.setText(QtGui.QApplication.translate("Form", "Total Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Items", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Program Controls:", None, QtGui.QApplication.UnicodeUTF8))
        self.itemTree.headerItem().setText(0, QtGui.QApplication.translate("Form", "Item", None, QtGui.QApplication.UnicodeUTF8))
        self.itemTree.headerItem().setText(1, QtGui.QApplication.translate("Form", "Grid Spacing", None, QtGui.QApplication.UnicodeUTF8))
        self.itemTree.headerItem().setText(2, QtGui.QApplication.translate("Form", "Grid Layout", None, QtGui.QApplication.UnicodeUTF8))
        self.itemTree.headerItem().setText(3, QtGui.QApplication.translate("Form", "# of points", None, QtGui.QApplication.UnicodeUTF8))
        self.addLineScanBtn.setText(QtGui.QApplication.translate("Form", "Add Line Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.addCircleScanBtn.setText(QtGui.QApplication.translate("Form", "Add Circle Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.addSpiralScanBtn.setText(QtGui.QApplication.translate("Form", "Add Spiral Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteStepBtn.setText(QtGui.QApplication.translate("Form", "Delete Step", None, QtGui.QApplication.UnicodeUTF8))
        self.previewBtn.setText(QtGui.QApplication.translate("Form", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.programTable.setSortingEnabled(True)
        self.hideCheck.setToolTip(QtGui.QApplication.translate("Form", "Hide all items from view.", None, QtGui.QApplication.UnicodeUTF8))
        self.hideCheck.setText(QtGui.QApplication.translate("Form", "Hide items", None, QtGui.QApplication.UnicodeUTF8))
        self.hideMarkerBtn.setText(QtGui.QApplication.translate("Form", "Hide Spot Marker", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph.TreeWidget import TreeWidget
from pyqtgraph.PlotWidget import PlotWidget
from pyqtgraph.SpinBox import SpinBox
