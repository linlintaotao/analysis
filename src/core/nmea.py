# coding= utf-8
from datetime import timedelta, datetime
from src.core import Gauss
import os
import math


# noinspection PyBroadException
class GNGGAFrame:

    def __init__(self, name, data, localTime, hz=1):
        self._name = name.split(os.sep)[-1]
        self._time = localTime
        self.hz = hz
        self._gga = None
        self.latitude = None
        self.fixAltitude = None
        self.fixState = None
        self.fixLongitude = None
        self.hour = 0
        self.parse_time = 0
        self.roundNum = None
        self.data = data

    def get_name(self):
        return self._name

    def getSolutionList(self):
        return self.getSolutionPercent(1), self.getSolutionPercent(2), self.getSolutionPercent(
            4), self.getSolutionPercent(5), self.getSolutionPercent(6)

    def nmeatime(self, date, leapsecond):
        strData = str(date).split('.')
        while len(strData[0]) < 6:
            strData[0] = '0' + strData[0]
        timeStr = strData[0] + "." + strData[1]
        time = datetime.strptime(timeStr, '%H%M%S.%f')

        microsecond_ = time.microsecond / 1000
        if microsecond_ > 950:
            time += timedelta(seconds=1)
            time = time.replace(microsecond=0)
        elif microsecond_ < 50:
            time = time.replace(microsecond=0)

        if leapsecond != 0:
            time -= timedelta(seconds=leapsecond)

        if time.hour == 0 and time.minute == 0 and time.second == 0 and time.microsecond == 0:
            self._time += timedelta(days=1)
        elif self.hour > time.hour:
            self._time += timedelta(days=1)
        self.hour = time.hour
        result = time.replace(year=self._time.year, month=self._time.month, day=self._time.day)
        return result

    def parseData(self, leapSecond=0, dataList=None):
        if self.data is None:
            return
        """
            check gngga data timestamp and update it's type to YYmmdd-hhmmss.f
        """
        temp = self.data.copy()
        temp.loc[:, '1'] = temp.loc[:, '1'].astype(str).apply(lambda t: self.nmeatime(t, leapSecond))
        if dataList:
            temp = temp.loc[temp['6'].astype(int) == 4, :]
            for data in dataList:
                fixLatitude = data.get_latitude(True)
                temp = temp[temp['1'].isin(fixLatitude.index)]

        # self.satNum = self._gga.loc[:, '7'].apply(lambda x: self.tofloat(x))
        # self.dAge = self._gga.loc[:, '13'].apply(lambda x: self.tofloatContainsNan(x))
        self._gga = temp.set_index('1')
        self.latitude = self._gga.loc[:, '2'].astype(float).apply(lambda x: self.dmTodd(x))
        self.longitude = self._gga.loc[:, '4'].astype(float).apply(lambda x: self.dmTodd(x))
        self.state = self._gga.loc[:, '6'].apply(lambda x: self.toint(x))
        self.altitude = self._gga.loc[:, '9'].apply(lambda x: self.tofloat(x)) + self._gga.loc[:, "11"].apply(
            lambda x: self.tofloat(x))
        self.altitude.name = '9'

        fixGGA = self._gga.loc[self._gga['6'].astype(int) == 4, :]
        self.fixLatitude = fixGGA.loc[:, '2'].astype(float).apply(lambda x: self.dmTodd(x))
        self.fixLatitude.name = '2'
        self.fixLongitude = fixGGA.loc[:, '4'].astype(float).apply(lambda x: self.dmTodd(x))
        self.fixLongitude.name = '4'
        self.fixAltitude = fixGGA.loc[:, '9'].apply(lambda x: self.tofloat(x)) + fixGGA.loc[:, '11'].apply(
            lambda x: self.tofloat(x))
        self.fixAltitude.name = '9'
        self.fixState = fixGGA.loc[:, '6'].astype(int)

    def getFixPercent(self):
        return self.getSolutionPercent(4)

    def getSolutionPercent(self, state):
        return 100 * len(self.data.loc[self.data['6'].astype(int) == state, :]) / len(self.data)

    @staticmethod
    def tofloat(x):
        try:
            return float(x)
        except Exception as e:
            return 0

    @staticmethod
    def tofloatContainsNan(x):
        try:
            result = float(x)
            if math.isnan(result):
                return -1
            else:
                return result
        except Exception as e:
            return 0

    @staticmethod
    def toint(x):
        try:
            return int(x)
        except Exception as e:
            return 0

    @staticmethod
    def dmTodd(dm):
        dd = int(dm / 100)
        res = dd + (dm % 100) / 60
        return res

    def get_sateNum(self):
        return self.satNum

    def getdAge(self):
        return self.dAge

    def get_state(self, onlyFix=False):
        if onlyFix:
            return self.fixState
        return self.state

    def get_latitude(self, onlyFix=False):
        if onlyFix:
            return self.fixLatitude
        return self.latitude

    def get_longitude(self, onlyFix=False):
        if onlyFix:
            return self.fixLongitude
        return self.longitude

    def get_altitude(self, onlyFix=False):
        if onlyFix:
            return self.fixAltitude
        return self.altitude

    def getPointTruth(self):
        fixList = self.get_state()
        for i in range(len(fixList)):
            if fixList[i] == 4:
                return [self.get_latitude()[i], self.get_longitude()[i], self.get_altitude()[i]]
        return None

    def get_scatter(self):
        latitude = self.get_latitude()
        longitude = self.get_longitude()
        fixState = self.get_state()
        xList, yList, xFixList, yFixList, fixList = list(), list(), list(), list(), list()
        for i in range(len(fixState)):
            try:
                x, y = Gauss.LatLon2XY(latitude[i], longitude[i])
                xList.append(x)
                yList.append(y)
                fixList.append(fixState[i])
                if fixState[i] == 4:
                    xFixList.append(x)
                    yFixList.append(y)
            except Exception as e:
                print(e)
                continue

        return xList, yList, xFixList, yFixList, fixList


class Satellite:

    def __init__(self, name, visible_Times, cn0):
        self._name = name
        self.visible_Times = visible_Times
        self._cn0 = cn0

    def get_name(self):
        return self._name

    def get_visible_Times(self):
        return self.visible_Times

    def get_mean_cn0(self):
        return self._cn0


GPGSV = '$GPGSV'
GBGSV = '$GBGSV'
GLGSV = '$GLGSV'
GAGSV = '$GAGSV'

GSVLIST = [GPGSV, GBGSV, GLGSV, GAGSV]
GSVNAME = ['G', 'C', 'R', 'E']


class GSV:
    """
        GPGSV Gps
        GBGSV Beidou
        GLGSV GLONASS
        GAGSV Galileo
        gsv = '$GPGSV, 3,1,10, 10,33,308,45, 12,02,143,39, 13,16,059,40, 15,47,059,49 *6A'
    """

    def __init__(self, name, gsv):
        self._name = name.split('.log')[0]
        self._satellites = self.parseGSV(gsv)
        # print(self._gsv)

    def parseGSV(self, data):
        satellites = []
        for i in range(len(GSVLIST)):
            gsv = data[data['0'] == GSVLIST[i]]
            gsd = gsv[['4', '7']].dropna()
            gsd.columns = ['s', 'n']
            gsd2 = gsv[['8', '11']].dropna()
            gsd2.columns = ['s', 'n']
            gsd3 = gsv[['12', '15']].dropna()
            gsd3.columns = ['s', 'n']
            gsd4 = gsv[['16', '19']].dropna()
            gsd4.columns = ['s', 'n']
            gsd4['n'] = gsd4['n'].apply(lambda x: int(self.getStr(x)))
            gsvsn = gsd.append([gsd2, gsd3, gsd4], ignore_index=True, sort=False)
            s = gsvsn.loc[:, 's'].astype(int)
            for name in set(s):
                cn0 = gsvsn.loc[gsvsn['s'].astype(int) == name].astype(int)
                satellites.append(Satellite(GSVNAME[i] + str(int(name)), len(cn0), int(cn0['n'].mean())))
        return sorted(satellites, key=lambda x: x.get_mean_cn0())

    def getStr(self, str):
        return str.split('*')[0]

    def get_satellites_status(self):

        return self._satellites

    def get_name(self):
        return self._name


if __name__ == '__main__':
    gnneam = GNGGAFrame("asdasd_asd", data=None, localTime=datetime.now().date())
    print(datetime.now().date())
    print(gnneam.nmeatime('235959.99'))
    print(gnneam.nmeatime('000000.02'))
