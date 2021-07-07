# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QHeaderView, QAbstractItemView
from ui.ui_mainwindow import Ui_AnalysisTool
from src.core.delegate import Delegate
from datetime import datetime
from PyQt5.QtGui import QStandardItemModel, QStandardItem

HEAD_TABLE = ['Name', 'Fixed(%)', 'Antenna distance(m)', 'LeapSecond(s)']


class Tool(QMainWindow, Ui_AnalysisTool):

    def __init__(self, parent=None):
        super(Tool, self).__init__(parent)
        self.delegate = Delegate(time=datetime.now().date())
        self.setupUi(self)
        self.initTableView()
        self.initSingnal()

    def initTableView(self):
        self.tableModel = QStandardItemModel(1, 4)
        self.tableModel.setHorizontalHeaderLabels(HEAD_TABLE)
        self.tableView.setModel(self.tableModel)
        # 所有列自动拉伸，充满界面
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置只能选中一行
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)

    def initSingnal(self):
        self.searchTruth.clicked.connect(lambda: self.searchDataEvent(True))
        self.searchData.clicked.connect(lambda: self.searchDataEvent(False))
        self.startBtn.clicked.connect(self.startAnalysis)
        self.loadBtn.clicked.connect(self.loadDataEvent)
        self.exportBtn.clicked.connect(self.makeReport)

    def searchDataEvent(self, searchTrue):
        if searchTrue:
            filename, filetype = QFileDialog.getOpenFileName(self, "Select file", "./",
                                                             "All Files (*);;Text Files (*.txt)")
            if filename is not None:
                self.truthPathEdit.setText(filename)
            pass
        else:
            filenameList, filetype = QFileDialog.getOpenFileNames(self, "Select file", "./",
                                                                  "All Files (*);;Text Files (*.txt)")
            if filenameList is not None and len(filenameList) > 0:
                self.dataPathEdit.setText('\n'.join(filenameList))

    def loadDataEvent(self):
        self.delegate.clear()
        self.delegate.prepareData(self.truthPathEdit.text(), self.dataPathEdit.toPlainText().split('\n'))

        self.tableModel.clear()
        self.tableModel.setHorizontalHeaderLabels(HEAD_TABLE)
        dictInfo = self.delegate.getInfo()
        for key, value in dictInfo.items():
            self.tableModel.appendRow([
                QStandardItem(value[0]),
                QStandardItem(f"%0.2f" % value[1]),
                QStandardItem(str(0)),
                QStandardItem(str(18)),
            ])

    def startAnalysis(self):
        self.showStatus('开始分析数据...')
        self.delegate.close()
        tableInfo = self.readTable()

        """
        type1 : compare
        type2 :internal
        """
        if self.compareTab.isVisible():
            self.delegate.setConfig(tableInfo, self.getRule())
            self.delegate.draw()

        else:

            pass
        self.showStatus('数据分析完毕!')

    def readTable(self):
        '''
        :return: [[name,fixed percent,antenna distance,leapSecond]]
        '''
        infoList = []
        for i in range(self.tableModel.rowCount()):
            info = []
            for j in range(self.tableModel.columnCount()):
                info.append(self.tableModel.item(i, j).text())
            infoList.append(info)
        return infoList

    def showStatus(self, msg):
        self.statusbar.showMessage(msg)

    def makeReport(self):
        self.delegate.makeReport()
        self.showStatus('报告生成完毕')

    def getRule(self):
        if self.allEpoch.isChecked():
            return 'ALL'
        elif self.onlyTruthFixed.isChecked():
            return 'OnlyTruth'
        elif self.allDevFixedEpoch.isChecked():
            return 'ALL_FIXED'
