# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/LogWidgetTemplate.ui'
#
# Created: Fri Dec  2 19:52:45 2011
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
        Form.resize(633, 437)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setMargin(3)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.dirLabel = QtGui.QLabel(self.widget)
        self.dirLabel.setText(_fromUtf8(""))
        self.dirLabel.setObjectName(_fromUtf8("dirLabel"))
        self.gridLayout.addWidget(self.dirLabel, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(148, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.exportHtmlBtn = QtGui.QPushButton(self.widget)
        self.exportHtmlBtn.setObjectName(_fromUtf8("exportHtmlBtn"))
        self.gridLayout.addWidget(self.exportHtmlBtn, 0, 2, 1, 1)
        self.output = QtGui.QPlainTextEdit(self.widget)
        self.output.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.output.setUndoRedoEnabled(False)
        self.output.setReadOnly(True)
        self.output.setObjectName(_fromUtf8("output"))
        self.gridLayout.addWidget(self.output, 1, 0, 1, 3)
        self.widget1 = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.filterTree = TreeWidget(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterTree.sizePolicy().hasHeightForWidth())
        self.filterTree.setSizePolicy(sizePolicy)
        self.filterTree.setMinimumSize(QtCore.QSize(210, 0))
        self.filterTree.setMaximumSize(QtCore.QSize(8777205, 16777215))
        self.filterTree.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.filterTree.setProperty(_fromUtf8("showDropIndicator"), False)
        self.filterTree.setDragEnabled(True)
        self.filterTree.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.filterTree.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.filterTree.setObjectName(_fromUtf8("filterTree"))
        item_0 = QtGui.QTreeWidgetItem(self.filterTree)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        item_0.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_0 = QtGui.QTreeWidgetItem(self.filterTree)
        item_0.setCheckState(0, QtCore.Qt.Checked)
        item_0.setFlags(QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)
        item_1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)
        item_1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)
        item_1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)
        item_1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.verticalLayout.addWidget(self.filterTree)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setIndent(0)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.widget1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.importanceSlider = QtGui.QSlider(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importanceSlider.sizePolicy().hasHeightForWidth())
        self.importanceSlider.setSizePolicy(sizePolicy)
        self.importanceSlider.setMaximum(9)
        self.importanceSlider.setPageStep(0)
        self.importanceSlider.setTracking(True)
        self.importanceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.importanceSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.importanceSlider.setTickInterval(1)
        self.importanceSlider.setObjectName(_fromUtf8("importanceSlider"))
        self.verticalLayout.addWidget(self.importanceSlider)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.exportHtmlBtn.setText(QtGui.QApplication.translate("Form", "Export HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.filterTree.headerItem().setText(0, QtGui.QApplication.translate("Form", "Display:", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.filterTree.isSortingEnabled()
        self.filterTree.setSortingEnabled(False)
        self.filterTree.topLevelItem(0).setText(0, QtGui.QApplication.translate("Form", "Current directory only", None, QtGui.QApplication.UnicodeUTF8))
        self.filterTree.topLevelItem(1).setText(0, QtGui.QApplication.translate("Form", "All message types:", None, QtGui.QApplication.UnicodeUTF8))
        self.filterTree.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("Form", "user", None, QtGui.QApplication.UnicodeUTF8))
        self.filterTree.topLevelItem(1).child(1).setText(0, QtGui.QApplication.translate("Form", "status", None, QtGui.QApplication.UnicodeUTF8))
        self.filterTree.topLevelItem(1).child(2).setText(0, QtGui.QApplication.translate("Form", "warning", None, QtGui.QApplication.UnicodeUTF8))
        self.filterTree.topLevelItem(1).child(3).setText(0, QtGui.QApplication.translate("Form", "error", None, QtGui.QApplication.UnicodeUTF8))
        self.filterTree.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(QtGui.QApplication.translate("Form", "Low", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Importance Filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "High", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph.TreeWidget import TreeWidget
