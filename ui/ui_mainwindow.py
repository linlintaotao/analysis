# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnalysisTool(object):
    def setupUi(self, AnalysisTool):
        AnalysisTool.setObjectName("AnalysisTool")
        AnalysisTool.resize(557, 524)
        self.centralwidget = QtWidgets.QWidget(AnalysisTool)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loadBtn.setObjectName("loadBtn")
        self.horizontalLayout.addWidget(self.loadBtn)
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout.addWidget(self.startBtn)
        self.optionBtn = QtWidgets.QPushButton(self.centralwidget)
        self.optionBtn.setObjectName("optionBtn")
        self.horizontalLayout.addWidget(self.optionBtn)
        self.exportBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exportBtn.setObjectName("exportBtn")
        self.horizontalLayout.addWidget(self.exportBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.compareTab = QtWidgets.QWidget()
        self.compareTab.setObjectName("compareTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.compareTab)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dataPathEdit = QtWidgets.QTextEdit(self.compareTab)
        self.dataPathEdit.setObjectName("dataPathEdit")
        self.horizontalLayout_3.addWidget(self.dataPathEdit)
        self.searchData = QtWidgets.QPushButton(self.compareTab)
        self.searchData.setObjectName("searchData")
        self.horizontalLayout_3.addWidget(self.searchData)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.compareTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.truthPathEdit = QtWidgets.QLineEdit(self.compareTab)
        self.truthPathEdit.setObjectName("truthPathEdit")
        self.horizontalLayout_2.addWidget(self.truthPathEdit)
        self.searchTruth = QtWidgets.QPushButton(self.compareTab)
        self.searchTruth.setObjectName("searchTruth")
        self.horizontalLayout_2.addWidget(self.searchTruth)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.compareTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.compareTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.allEpoch = QtWidgets.QRadioButton(self.frame)
        self.allEpoch.setObjectName("allEpoch")
        self.verticalLayout.addWidget(self.allEpoch)
        self.onlyTruthFixed = QtWidgets.QRadioButton(self.frame)
        self.onlyTruthFixed.setChecked(True)
        self.onlyTruthFixed.setObjectName("onlyTruthFixed")
        self.verticalLayout.addWidget(self.onlyTruthFixed)
        self.allDevFixedEpoch = QtWidgets.QRadioButton(self.frame)
        self.allDevFixedEpoch.setObjectName("allDevFixedEpoch")
        self.verticalLayout.addWidget(self.allDevFixedEpoch)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 5, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.compareTab)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 4, 0, 1, 1)
        self.gridLayout_2.setRowStretch(3, 1)
        self.gridLayout_2.setRowStretch(4, 2)
        self.tabWidget.addTab(self.compareTab, "")
        self.internalTab = QtWidgets.QWidget()
        self.internalTab.setObjectName("internalTab")
        self.tabWidget.addTab(self.internalTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        AnalysisTool.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AnalysisTool)
        self.statusbar.setObjectName("statusbar")
        AnalysisTool.setStatusBar(self.statusbar)

        self.retranslateUi(AnalysisTool)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AnalysisTool)

    def retranslateUi(self, AnalysisTool):
        _translate = QtCore.QCoreApplication.translate
        AnalysisTool.setWindowTitle(_translate("AnalysisTool", "MainWindow"))
        self.loadBtn.setText(_translate("AnalysisTool", "load"))
        self.startBtn.setText(_translate("AnalysisTool", "start"))
        self.optionBtn.setText(_translate("AnalysisTool", "option"))
        self.exportBtn.setText(_translate("AnalysisTool", "export"))
        self.searchData.setText(_translate("AnalysisTool", "..."))
        self.label_2.setText(_translate("AnalysisTool", "Compare Data Paths:"))
        self.searchTruth.setText(_translate("AnalysisTool", "..."))
        self.label.setText(_translate("AnalysisTool", "Truth Data Path:"))
        self.label_4.setText(_translate("AnalysisTool", "Compare Rules???"))
        self.allEpoch.setText(_translate("AnalysisTool", "every epoch will be counted"))
        self.onlyTruthFixed.setText(_translate("AnalysisTool", "only truth value fixed epoch will be counted"))
        self.allDevFixedEpoch.setText(_translate("AnalysisTool", "the epoch all device in fixed state will be counted"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.compareTab), _translate("AnalysisTool", "compare"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.internalTab), _translate("AnalysisTool", "internal"))
