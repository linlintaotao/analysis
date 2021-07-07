import pandas as pd
from src.core.draw import FmiChart
from src.core.nmea import GNGGAFrame
from src.report.compareReport import Reporter


class Delegate:

    def __init__(self, time):
        self.truthData = None
        self.compareDataList = []
        self.testStartTime = time
        self.path = './data/'
        self.antennaDistance = []
        self.fmiChart = None
        self.useFix = True
        self.mergeTruthData = False
        self.data = None
        self.describeList = []

    def readFile(self, fileName):
        df = pd.read_table(fileName, sep=',',
                           encoding='unicode_escape',
                           header=None,
                           names=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                  '11', '12', '13', '14'],
                           error_bad_lines=False,
                           warn_bad_lines=False,
                           low_memory=False
                           )

        # 删除异常数据
        df = df.drop(index=df.loc[(df['1'].isna())].index)
        df = df.drop(index=df.loc[(df['6'].isna())].index)
        df = df.drop(index=df.loc[(df['6'].astype(str) == '0')].index)

        ggaEntity = GNGGAFrame(fileName,
                               df.loc[(df['0'].astype(str) == '$GNGGA') |
                                      (df['0'].astype(str) == '$GPGGA')].copy(),
                               self.testStartTime)
        return ggaEntity

    def prepareData(self, truthpath, comparePathList):
        self.truthData = self.readFile(truthpath)

        for path in comparePathList:
            self.compareDataList.append(self.readFile(path))

    def getInfo(self):
        '''
        dict:{
         key : path name
         value : ['name','fix percent']
         }
        :return: dict
        '''
        infoDict = {}
        if self.truthData is not None:
            infoDict[self.truthData.get_name()] = [self.truthData.get_name(), self.truthData.getFixPercent()]

        for data in self.compareDataList:
            infoDict[data.get_name()] = [data.get_name(), data.getFixPercent()]
        print(infoDict)
        return infoDict

    def draw(self):
        if len(self.compareDataList) <= 0 or self.truthData is None:
            return
        if len(self.configList) <= 0:
            return
        self.fmiChart = FmiChart(path=self.path)

        """
        setConfig : leapSecond
        """
        leapSecondTruth = int(self.configList[0][3])
        for i in range(len(self.compareDataList)):
            self.compareDataList[i].parseData(leapSecond=int(self.configList[i + 1][3]) - leapSecondTruth)

        self.truthData.parseData(leapSecond=0, dataList=self.compareDataList if self.mergeTruthData else None)

        self.describeList = self.fmiChart.drawCdf(self.compareDataList, self.truthData, onlyFix=self.useFix,
                                                  distanceList=self.antennaDistance)

        print(self.describeList)
        self.data = [self.truthData]
        self.data.extend(self.compareDataList)
        self.fmiChart.drawSolution(dataList=self.data)

        self.fmiChart.show()

    def setConfig(self, configList, rule):
        '''
            configList:[0:trurhData,1:?,and so on]

            rule : ALL、TRUTH_FIXED、ALL_FIXED
        '''
        self.antennaDistance.clear()
        self.mergeTruthData = False
        self.configList = configList
        for i in range(1, len(self.configList)):
            self.antennaDistance.append(self.configList[i][2])

        # rules to analysis Data
        if rule is 'ALL':
            self.useFix = False
        elif rule is 'ALL_FIXED':
            self.mergeTruthData = True

    def makeReport(self):
        report = Reporter(self.path, configList=self.configList, rules=self.getRules(),
                          cdf=self.describeList)
        report.makeReport()

    def getRules(self):
        if not self.useFix:
            return '比较所有的历元'
        if self.mergeTruthData:
            return '比较所有设备都进入固定解的历元'
        return '比较真值设备为固定解的历元'

    def clear(self):
        self.truthData = None
        self.compareDataList.clear()
        self.describeList.clear()

    def close(self):
        if self.fmiChart:
            self.fmiChart.close()
