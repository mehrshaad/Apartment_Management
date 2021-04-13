# Apartment 11 Management v3.1
# Copyright (c) 2020 Mehrshad Dadashzadeh
# </https://www.linkedin.com/in/mehrshad-dadashzadeh-7053491b3/>
#
# This program is free software,
# you can redistribute it and/or modify it.
#
# Used fonts:
#    B badr - B Badr Bold
#    B Nazanin
#    B Titr
#    Mikhak Medium

import math
import os
import pathlib
import platform as P
import sys
from glob import glob
from shutil import copy

from pynotifier import Notification
from PyQt5 import Qt, QtCore, QtGui, QtWidgets

import Apart11_css as css
import Apart11_rc
import Excel as E
import Json as J

if P.system() == 'Windows':
    if P.release() == '10':
        win10key = True
    else:
        win10key = False
else:
    win10key = False

AppName = "Apartment 11 Management"
DevText = "Developed by <strong>Mehrshad Dadashzadeh</strong>"
Version = os.path.basename(__file__).split(
    ' ')[-1][:-3]  # getting version from py file name
Data = J.read_from('Apart11_data.json')  # data in json
Data_2 = {  # texts and shadow data
    "Manabe": {
        b'\u0645\u0648\u062C\u0648\u062F\u06CC \u0646\u0642\u0644 \u0627\u0632 \u062F\u0648\u0631\u0647 \u0642\u0628\u0644'.decode('unicode-escape'): 2,
        b'\u0633\u0648\u062F \u062D\u0627\u0635\u0644 \u0627\u0632 \u0633\u067E\u0631\u062F\u0647 \u0633\u0631\u0645\u0627\u06CC\u0647 \u06AF\u0630\u0627\u0631\u06CC \u06A9\u0648\u062A\u0627\u0647 \u0645\u062F\u062A'.decode('unicode-escape'): 3,
        b'\u0645\u0648\u062C\u0648\u062F\u06CC \u062C\u0627\u0631\u06CC'.decode('unicode-escape'): 4
    },
    "Masaref": {
        b'\u0647\u0632\u06CC\u0646\u0647 \u0633\u0631\u0648\u06CC\u0633 \u0648 \u0646\u06AF\u0647 \u062F\u0627\u0631\u06CC \u0622\u0633\u0627\u0646\u0633\u0648\u0631 \u0648 \u0628\u06CC\u0645\u0647 \u0646\u0627\u0645\u0647'.decode('unicode-escape'): 6,
        b'\u0647\u0632\u06CC\u0646\u0647 \u0646\u0638\u0627\u0641\u062A \u0639\u0645\u0648\u0645\u06CC \u0633\u0627\u062E\u062A\u0645\u0627\u0646 (\u0633\u0647 \u0646\u0648\u0628\u062A \u0647\u0631 \u0645\u0627\u0647)'.decode('unicode-escape'): 7,
        b'\u0647\u0632\u06CC\u0646\u0647 \u0639\u06CC\u062F\u06CC \u06A9\u0627\u0631\u06AF\u0631\u0627\u0646 \u0634\u0647\u0631\u062F\u0627\u0631\u06CC'.decode('unicode-escape'): 8,
        b'\u0647\u0632\u06CC\u0646\u0647 \u0644\u0648\u0627\u0632\u0645 \u0634\u0648\u06CC\u0646\u062F\u0647'.decode('unicode-escape'): 9,
        b'\u0647\u0632\u06CC\u0646\u0647 \u0628\u0631\u0642 \u0645\u0635\u0631\u0641\u06CC - \u0642\u0628\u0636 \u0639\u0645\u0648\u0645\u06CC'.decode('unicode-escape'): 10,
        b'\u0647\u0632\u06CC\u0646\u0647 \u0622\u0628 \u0645\u0635\u0631\u0641\u06CC - \u0633\u0647\u0645 \u062E\u0627\u0646\u0648\u0627\u0631'.decode('unicode-escape'): 11,
        b'\u0647\u0632\u06CC\u0646\u0647 \u062E\u0631\u06CC\u062F \u06AF\u0644 \u0648 \u0628\u0627\u063A\u0628\u0627\u0646\u06CC (\u062D\u06CC\u0627\u0637 \u0648 \u0648\u0631\u0648\u062F\u06CC \u0633\u0627\u062E\u062A\u0645\u0627\u0646)'.decode(
            'unicode-escape'): 12,
        b'\u0647\u0632\u06CC\u0646\u0647 \u0647\u0627\u06CC \u0645\u0627\u0644\u06CC - \u06A9\u0627\u0631\u0645\u0632\u062F \u0628\u0627\u0646\u06A9\u06CC \u0648 \u0635\u062F\u0648\u0631 \u0635\u0648\u0631\u062A\u062D\u0633\u0627\u0628'.decode(
            'unicode-escape'): 13,
        b'\u0647\u0632\u06CC\u0646\u0647 \u062A\u0639\u0645\u06CC\u0631\u0627\u062A'.decode('unicode-escape'): 14,
        b'\u0634\u0627\u0631\u0698 \u0633\u06CC\u0645 \u06A9\u0627\u0631\u062A \u062A\u0644\u0641\u0646 \u0647\u0645\u0631\u0627\u0647 \u0633\u0627\u062E\u062A\u0645\u0627\u0646'.decode('unicode-escape'): 15,
        b'\u0644\u0648\u0627\u0632\u0645 \u0645\u0635\u0631\u0641\u06CC \u062A\u0627\u0633\u06CC\u0633\u0627\u062A\u06CC'.decode('unicode-escape'): 16
    },
    "1st6Month": {
        b'\u0641\u0631\u0648\u0631\u062F\u06CC\u0646'.decode('unicode-escape'): ['B', '01'],
        b'\u0627\u0631\u062F\u06CC\u0628\u0647\u0634\u062A'.decode('unicode-escape'): ['C', '02'],
        b'\u062E\u0631\u062F\u0627\u062F'.decode('unicode-escape'): ['D', '03'],
        b'\u062A\u06CC\u0631'.decode('unicode-escape'): ['E', '04'],
        b'\u0645\u0631\u062F\u0627\u062F'.decode('unicode-escape'): ['F', '05'],
        b'\u0634\u0647\u0631\u06CC\u0648\u0631'.decode('unicode-escape'): ['G', '06']
    },
    "2nd6Month": {
        b'\u0645\u0647\u0631'.decode('unicode-escape'): ['B', '07'],
        b'\u0622\u0628\u0627\u0646'.decode('unicode-escape'): ['C', '08'],
        b'\u0622\u0630\u0631'.decode('unicode-escape'): ['D', '09'],
        b'\u062F\u06CC'.decode('unicode-escape'): ['E', '10'],
        b'\u0628\u0647\u0645\u0646'.decode('unicode-escape'): ['F', '11'],
        b'\u0627\u0633\u0641\u0646\u062F'.decode('unicode-escape'): ['G', '12']
    },
    "Abyari": {},
    "Shadow": {
        'light': {'blurRadius': 5, 'xOffset': 0, 'yOffset': 0, 'color': Qt.QColor(27, 151, 243)},
        'dark': {'blurRadius': 5, 'xOffset': 0, 'yOffset': 0, 'color': Qt.QColor(237, 255, 153)},
        'start': {'blurRadius': 20, 'xOffset': 1, 'yOffset': 2, 'color': Qt.QColor(0, 0, 0, 60)}
    }
}
Data_3 = {  # empty data for storing in-app runtime data
    'manba': {},
    'kharj': {},
    'molahezat': {},
    'mablaghPardakht': {},
    'output': [],
    'donePages': {
        'ab': False,
        'sharj': False,
        'bilan': False,
        'abyari': False
    },
    'fileName': f"Excel\\1st 6 Month of {Data['ActiveYear']}.xlsx" if Data['Bilan6Month'] else f"Excel\\2nd 6 Month of {Data['ActiveYear']}.xlsx"
}

try:
    os.makedirs("Excel")  # creating a folder named "Excel"
except:
    pass
filesList = glob("Excel\\*.xlsx")  # gets a list of all excel files
E.defaultFilePath, E.defaultFileName = Data_3['fileName'].split(
    '\\')  # setting default path and name
if Data_3['fileName'] not in filesList:  # creating excel file if not existed
    copy('FreeForm.xlsx', Data_3['fileName'])
    filesList = glob("Excel\\*.xlsx")

sahmNafar = 0
sahmNafarRound = 0
month = 'این'  # current month (for preventing errors)
months = list(Data_2["1st6Month"].keys()) + \
    list(Data_2["2nd6Month"].keys())  # all months


def checkFiles():
    global Data, Data_3, filesList
    if Data['Bilan6Month']:
        Data_3['fileName'] = f"Excel\\1st 6 Month of {Data['ActiveYear']}.xlsx"
    else:
        Data_3['fileName'] = f"Excel\\2nd 6 Month of {Data['ActiveYear']}.xlsx"
    E.defaultFileName = Data_3['fileName'].split('\\')[-1]
    if Data_3['fileName'] not in filesList:
        copy('FreeForm.xlsx', Data_3['fileName'])
        filesList = glob("Excel\\*.xlsx")


def sumNafarat():
    global Data
    ans = 0
    for i in Data['Nafarat'].keys():
        ans += Data['Nafarat'][i]
    return ans


def saveJson(data={}):
    global Data
    if data == {}:
        data = Data
    J.write_to('Apart11_data.json', data)


def saveExcel(mode, data={}):
    global Data, Data_2, Data_3, month, filesList
    checkFiles()

    if mode == 'ab':
        sheet = 'سهم آب مصرفی'
        for i, j in data.items():
            E.set_cell_value(sheet, j, i, font='B Nazanin')
        for i, j in Data['Nafarat'].items():
            cell = f'C{int(i)+1}'
            E.set_cell_value(sheet, cell, j, font='B Nazanin')
        return 'done!'

    if mode == 'sharj':
        sheet = 'گزارش شارژ'
        if months.index(month) == 11:
            header = f"بسمه تعالی\nصورتحساب تامین منابع مالی بابت هزینه های ساختمان شماره 11\n{months[(months.index(month)+1)%12]} ماه {Data['ActiveYear']+1}"
            Data['ActiveYear'] += 1
            Data['Bilan6Month'] = not Data['Bilan6Month']
            saveJson()
        else:
            header = f"بسمه تعالی\nصورتحساب تامین منابع مالی بابت هزینه های ساختمان شماره 11\n{months[(months.index(month)+1)%12]} ماه {Data['ActiveYear']}"
        font = E.Font(name='B Nazanin', charset=178, family=None, b=True, i=False, strike=None, outline=None,
                      shadow=None, condense=None, color=None, extend=None, sz=12.0, u=None, vertAlign=None, scheme=None)
        E.set_cell_value(
            sheet, 'C2', Data['Sharj'], font='B Nazanin', bold=True)
        E.set_cell_value(
            sheet, 'E2', Data['HazineOmrani'], font='B Nazanin', bold=True)
        E.set_header(sheet, header, fontSize=11, font='B Nazanin')

        for i, j in Data['Bedehi'].items():
            cell = f'F{int(i)+1}'
            E.set_cell_value(sheet, cell, j, font='B Nazanin', bold=True)
        for i, j in Data_3['mablaghPardakht'].items():
            cell = f'G{int(i)+1}'
            E.set_cell_value(sheet, cell, j, font='B Nazanin', bold=True)
        for i in range(1, 14):
            cell = f'H{i+1}'
            E.set_cell_value(sheet, cell, '', customFont=font)
        for i, j in Data_3['molahezat'].items():
            cell = f'H{int(i)+1}'
            E.set_cell_value(sheet, cell, j, customFont=font)
        return 'done!'

    if mode == 'bilan':
        sheet = 'بیلان 6 ماهه'
        if months.index(month) == 11:
            header = f"بسمه تعالی\nصورتحساب تامین منابع مالی بابت هزینه های ساختمان شماره 11\n{months[(months.index(month)+1)%12]} ماه {Data['ActiveYear']+1}"
            Data['ActiveYear'] += 1
            Data['Bilan6Month'] = not Data['Bilan6Month']
            saveJson()
        else:
            header = f"بسمه تعالی\nصورتحساب تامین منابع مالی بابت هزینه های ساختمان شماره 11\n{months[(months.index(month)+1)%12]} ماه {Data['ActiveYear']}"
        E.set_header('گزارش شارژ', header, fontSize=11, font='B Nazanin')
        font = E.Font(name='B Titr', charset=178, family=None, b=False, i=False, strike=None, outline=None,
                      shadow=None, condense=None, color=None, extend=None, sz=12.0, u=None, vertAlign=None, scheme=None)

        if Data['Bilan6Month']:
            monthList = Data_2['1st6Month']
            cell = f'{Data_2["1st6Month"][month][0]}'
            date = f'{Data["ActiveYear"]}\{Data_2["1st6Month"][month][1]}\{"07"}'
            header = f"بیلان ساختمان در نیم سال اول {Data['ActiveYear']}"
            E.set_header(sheet, header, fontSize=18, font='B Badr')
        else:
            monthList = Data_2['2nd6Month']
            cell = f'{Data_2["2nd6Month"][month][0]}'
            date = f'{Data["ActiveYear"]}\{Data_2["2nd6Month"][month][1]}\{"07"}'
            header = f"بیلان ساختمان در نیم سال دوم {Data['ActiveYear']}"
            E.set_header(sheet, header, fontSize=18, font='B Badr')

        for i, j in monthList.items():
            c = f"{j[0]}1"
            text = f"{i} ماه (ریال)"
            E.set_cell_value(sheet, c, text, customFont=font)
        for i, j in Data_3['manba'].items():
            c = cell+str(Data_2['Manabe'][i])
            E.set_cell_value(sheet, c, j)
        for i, j in Data_3['kharj'].items():
            c = cell+str(Data_2['Masaref'][i])
            E.set_cell_value(sheet, c, j)
        return 'done!'

    if mode == 'abyari':
        sheet = 'آبیاری'
        vahed = list(set([int(i) for i in range(1, 14)]) -
                     set(Data['AbyariFilter']))
        font = E.Font(name='B Nazanin', charset=178, family=None, b=False, i=False, strike=None, outline=None,
                      shadow=None, condense=None, color=None, extend=None, sz=14.0, u=None, vertAlign=None, scheme=None)
        font2 = E.Font(name='B Nazanin', charset=178, family=None, b=True, i=False, strike=None, outline=None,
                       shadow=None, condense=None, color=None, extend=None, sz=12.0, u=None, vertAlign=None, scheme=None)

        Range = [Data['AbyariTurn1'][0], Data['AbyariTurn1'][1]]
        for a, b in zip(range(Range[0], Range[1]), vahed):
            c = str(b)
            E.set_cell_value(
                sheet, f'A{a}', f'واحد شماره {b}', customFont=font)
            E.set_cell_value(
                sheet, f'B{a}', Data_2['Abyari'][c]['1'][0], customFont=font2)
            E.set_cell_value(
                sheet, f'C{a}', Data_2['Abyari'][c]['1'][1], customFont=font2)

        Range = [int(Data['AbyariTurn2'][0]), int(Data['AbyariTurn2'][1])]
        for a, b in zip(range(Range[0], Range[1]), vahed):
            c = str(b)
            E.set_cell_value(
                sheet, f'A{a}', f'واحد شماره {b}', customFont=font)
            E.set_cell_value(
                sheet, f'B{a}', Data_2['Abyari'][c]['2'][0], customFont=font2)
            E.set_cell_value(
                sheet, f'C{a}', Data_2['Abyari'][c]['2'][1], customFont=font2)

        return 'done!'


def roundNumber(n, decimals=-4, halfDown=True):
    if halfDown:
        multiplier = 10 ** decimals
        return math.ceil(n*multiplier - 0.5) / multiplier
    else:
        multiplier = 10 ** decimals
        return math.floor(n*multiplier + 0.5) / multiplier


def sendNotification(Text, Title='', Duration=10):
    global win10key, AppName
    if Title == '':
        Title = AppName
    if win10key:
        Notification(
            title=Title,
            description=Text,
            icon_path='Icon.ico',
            duration=Duration,
            urgency=Notification.URGENCY_CRITICAL
        ).send()


def setCurser(key):
    if key:
        return QtCore.Qt.PointingHandCursor
    else:
        return QtCore.Qt.ForbiddenCursor


def shadowEffect(item, object, mode='', remove=False, Filter=['ButtSettings', 'ButtBack'], onlyFilter=False):
    global Data
    if mode.lower() == 'light' or remove:
        for child in item.findChildren(object):
            if child.objectName() in Filter and not onlyFilter:
                continue
            if child.objectName() not in Filter and onlyFilter:
                continue
            if remove:
                child.setGraphicsEffect(None)
                continue
            shadow = Qt.QGraphicsDropShadowEffect(
                blurRadius=10, xOffset=2, yOffset=1, color=Qt.QColor('gray'))
            child.setGraphicsEffect(shadow)
    elif mode.lower() == 'dark':
        for child in item.findChildren(object):
            if child.objectName() in Filter and not onlyFilter:
                continue
            if child.objectName() not in Filter and onlyFilter:
                continue
            if remove:
                child.setGraphicsEffect(None)
                continue
            shadow = Qt.QGraphicsDropShadowEffect(
                blurRadius=20, xOffset=0, yOffset=0, color=Qt.QColor(237, 255, 153))
            child.setGraphicsEffect(shadow)


def sortList(ls):
    global Data
    Filter = Data['AbyariFilter']
    ans = sorted([int(i) for i in ls])
    ans = [str(i) for i in ans if i not in Filter]
    return ans


class Windows:
    def __init__(self):
        if Data['ShowLoading']:
            self.start = Ui_startapp()
            self.start.setupUi(self.start.window)
            self.start.window.show()
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.show_main)
            self.timer.start(Data['LoadingDelay'])
        else:   
            self.main = Ui_main()
            self.settings = Ui_settings()
            self.bilan = Ui_bilan()
            self.ab = Ui_ab()
            self.sharj = Ui_sharj()
            self.abyari = Ui_abyari()
            self.output = Ui_output()

    def check_Style(self):
        try:
            self.ab.check_Style()
        except:
            pass
        try:
            self.bilan.check_Style()
        except:
            pass
        try:
            self.sharj.check_Style()
        except:
            pass
        try:
            self.abyari.check_Style()
        except:
            pass
        try:
            self.output.check_Style()
        except:
            pass
        try:
            self.main.check_Style()
        except:
            pass

    def show_main(self):
        if Data['ShowLoading']:
            self.start.progressBar.setValue(int(self.start.counter))
            if self.start.counter > 100:
                self.main = Ui_main()
                self.settings = Ui_settings()
                self.bilan = Ui_bilan()
                self.ab = Ui_ab()
                self.sharj = Ui_sharj()
                self.abyari = Ui_abyari()
                self.output = Ui_output()
                self.timer.stop()
                self.start.window.close()
                self.main.setupUi(self.main.window)
                self.main.window.show()
            self.start.counter += 1
        else:
            self.main.setupUi(self.main.window)
            self.main.window.show()

    def show_settings(self):
        self.settings.setupUi(self.settings.window)
        self.settings.window.show()

    def close_settings(self):
        self.settings.window.close()

    def show_output(self, DontAllow=False):
        global Data_3
        if not any(Data_3['donePages'].values()) and DontAllow:
            sendNotification('ابتدا صفحات دیگر را کامل کنید')
        else:
            self.output.setupUi(self.output.window)
            self.output.window.show()

    def close_output(self):
        self.output.window.close()

    def from_main_bilan(self):
        if Data['AllowEnterDonePages'] or not Data_3['donePages']['bilan']:
            self.main.window.close()
            self.bilan.setupUi(self.bilan.window)
            self.bilan.window.show()
        else:
            sendNotification('شما قبلا اطلاعات این صفحه را کامل کرده اید!')

    def from_bilan_main(self):
        self.bilan.window.close()
        self.main.setupUi(self.main.window)
        self.main.window.show()

    def from_main_ab(self):
        if Data['AllowEnterDonePages'] or not Data_3['donePages']['ab']:
            self.main.window.close()
            self.ab.setupUi(self.ab.window)
            self.ab.window.show()
        else:
            sendNotification('شما قبلا اطلاعات این صفحه را کامل کرده اید!')

    def from_ab_main(self):
        self.ab.window.close()
        self.main.setupUi(self.main.window)
        self.main.window.show()

    def from_main_sharj(self):
        if Data_3['donePages']['ab']:
            if Data['AllowEnterDonePages'] or not Data_3['donePages']['sharj']:
                self.main.window.close()
                self.sharj.setupUi(self.sharj.window)
                self.sharj.window.show()
            else:
                sendNotification('شما قبلا اطلاعات این صفحه را کامل کرده اید!')
        else:
            sendNotification('ابتدا گزارش آب را وارد کنید')

    def from_sharj_main(self):
        self.sharj.window.close()
        self.main.setupUi(self.main.window)
        self.main.window.show()

    def from_main_abyari(self):
        if Data['OpenAbyari']:
            if Data['AllowEnterDonePages'] or not Data_3['donePages']['abyari']:
                self.main.window.close()
                self.abyari.setupUi(self.abyari.window)
                self.check_Style()
                self.abyari.window.show()
            else:
                sendNotification('شما قبلا اطلاعات این صفحه را کامل کرده اید!')
        else:
            sendNotification('Coming Soon!')

    def from_abyari_main(self):
        self.abyari.window.close()
        self.main.setupUi(self.main.window)
        self.main.window.show()


class Ui_startapp(object):

    def __init__(self):
        self.window = QtWidgets.QMainWindow()
        self.counter = 0

    def setupUi(self, startapp):
        global Data
        startapp.setObjectName("startapp")
        startapp.resize(480, 320)
        startapp.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        startapp.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        startapp.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(startapp)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGraphicsEffect(Qt.QGraphicsDropShadowEffect(blurRadius=Data_2['Shadow']['start']['blurRadius'], xOffset=Data_2['Shadow']['start']['xOffset'],
                                                                          yOffset=Data_2['Shadow']['start']['yOffset'], color=Data_2['Shadow']['start']['color']))
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 2, 471, 311))
        self.bg.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.bg.setStyleSheet(css.background_start)
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 0, 451, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet("color:rgb(0, 50, 20);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(10, 80, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(8)
        font.setItalic(True)
        self.description.setFont(font)
        self.description.setStyleSheet("color: rgb(79, 79, 79);")
        self.description.setAlignment(QtCore.Qt.AlignCenter)
        self.description.setObjectName("description")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 180, 411, 23))
        self.progressBar.setStyleSheet(css.bar_start)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.loading = QtWidgets.QLabel(self.centralwidget)
        self.loading.setGeometry(QtCore.QRect(10, 200, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(8)
        font.setKerning(True)
        self.loading.setFont(font)
        self.loading.setStyleSheet("color: rgb(79, 79, 79);")
        self.loading.setAlignment(QtCore.Qt.AlignCenter)
        self.loading.setObjectName("loading")
        self.mehrshad = QtWidgets.QLabel(self.centralwidget)
        self.mehrshad.setGeometry(QtCore.QRect(10, 280, 451, 21))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(7)
        self.mehrshad.setFont(font)
        self.mehrshad.setStyleSheet("color:rgb(0, 50, 20);")
        self.mehrshad.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.mehrshad.setObjectName("mehrshad")
        startapp.setCentralWidget(self.centralwidget)

        self.retranslateUi(startapp)
        QtCore.QMetaObject.connectSlotsByName(startapp)

    def retranslateUi(self, startapp):
        _translate = QtCore.QCoreApplication.translate
        startapp.setWindowTitle(_translate("startapp", "MainWindow"))
        self.title.setText(_translate(
            "startapp", "<strong>Apartment 11</strong> Management"))
        self.description.setText(_translate(
            "startapp", "An easier way to manage your apartment"))
        self.loading.setText(_translate("startapp", "loading..."))
        self.mehrshad.setText(_translate(
            "startapp", "<strong>CREATED BY</strong> Mehrshad Dadashzadeh"))


class Ui_main(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, main):
        global Data
        main.setObjectName("main")
        main.resize(480, 640)
        main.setMinimumSize(QtCore.QSize(480, 640))
        main.setMaximumSize(QtCore.QSize(480, 640))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        main.setFont(font)
        main.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pics/.Images/Icon/euro.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(main)
        self.label.setGeometry(QtCore.QRect(70, 10, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.ButtExit = QtWidgets.QPushButton(main)
        self.ButtExit.setGeometry(QtCore.QRect(10, 560, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ButtExit.setFont(font)
        self.ButtExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtExit.setObjectName("ButtExit")
        self.ButtBilan = QtWidgets.QPushButton(main)
        self.ButtBilan.setGeometry(QtCore.QRect(130, 85, 321, 56))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ButtBilan.setFont(font)
        self.ButtBilan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtBilan.setObjectName("ButtBilan")
        self.ButtAb = QtWidgets.QPushButton(main)
        self.ButtAb.setGeometry(QtCore.QRect(30, 165, 321, 56))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ButtAb.setFont(font)
        self.ButtAb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtAb.setObjectName("ButtAb")
        self.ButtAbyari = QtWidgets.QPushButton(main)
        self.ButtAbyari.setGeometry(QtCore.QRect(30, 325, 321, 56))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ButtAbyari.setFont(font)
        self.ButtAbyari.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtAbyari.setObjectName("ButtAbyari")
        self.ButtSharj = QtWidgets.QPushButton(main)
        self.ButtSharj.setGeometry(QtCore.QRect(130, 245, 321, 56))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ButtSharj.setFont(font)
        self.ButtSharj.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtSharj.setObjectName("ButtSharj")
        self.ButtPDF = QtWidgets.QPushButton(main)
        self.ButtPDF.setGeometry(QtCore.QRect(130, 405, 321, 56))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ButtPDF.setFont(font)
        self.ButtPDF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtPDF.setObjectName("ButtPDF")
        self.ButtExcel = QtWidgets.QPushButton(main)
        self.ButtExcel.setGeometry(QtCore.QRect(30, 485, 321, 56))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ButtExcel.setFont(font)
        self.ButtExcel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtExcel.setObjectName("ButtExcel")
        self.label_2 = QtWidgets.QLabel(main)
        self.label_2.setGeometry(QtCore.QRect(20, 615, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(9)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ButtSettings = QtWidgets.QPushButton(main)
        self.ButtSettings.setGeometry(QtCore.QRect(420, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ButtSettings.setFont(font)
        self.ButtSettings.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtSettings.setStyleSheet(css.butt_transparent)
        self.ButtSettings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            ":/pics/.Images/Icon/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtSettings.setIcon(icon1)
        self.ButtSettings.setIconSize(QtCore.QSize(48, 48))
        self.ButtSettings.setObjectName("ButtSettings")
        self.ButtSettings.setStyleSheet(css.butt_transparent)
        self.progressBar = QtWidgets.QProgressBar(main)
        self.progressBar.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setMinimum(Data['AbyariTurn1'][0])
        self.progressBar.setMaximum(Data['AbyariTurn2'][1]-1)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.label_2.raise_()
        self.label.raise_()
        self.ButtExit.raise_()
        self.ButtBilan.raise_()
        self.ButtAb.raise_()
        self.ButtSharj.raise_()
        self.ButtPDF.raise_()
        self.ButtExcel.raise_()
        self.ButtSettings.raise_()
        self.ButtAbyari.raise_()
        self.progressBar.raise_()
        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)
        main.setTabOrder(self.ButtBilan, self.ButtAb)
        main.setTabOrder(self.ButtAb, self.ButtSharj)
        main.setTabOrder(self.ButtSharj, self.ButtAbyari)
        main.setTabOrder(self.ButtAbyari, self.ButtPDF)
        main.setTabOrder(self.ButtPDF, self.ButtExcel)
        main.setTabOrder(self.ButtExcel, self.ButtExit)

        self.name = main
        self.check_Style()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getDates)
        self.ButtBilan.clicked.connect(Page.from_main_bilan)
        self.ButtAb.clicked.connect(Page.from_main_ab)
        self.ButtSharj.clicked.connect(Page.from_main_sharj)
        self.ButtSettings.clicked.connect(Page.show_settings)
        self.ButtPDF.clicked.connect(Page.show_output)
        self.ButtExcel.clicked.connect(self.showExcel)
        self.ButtExit.clicked.connect(sys.exit)
        self.ButtAbyari.clicked.connect(self.getDates)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", AppName))
        self.label.setText(_translate("main", "برنامه مدیریت ساختمان"))
        self.ButtExit.setText(_translate("main", "خروج"))
        self.ButtBilan.setText(_translate("main", "بیلان 6 ماهه"))
        self.ButtAb.setText(_translate("main", "سهم آب مصرفی"))
        self.ButtAbyari.setText(_translate("main", "نوبت آبیاری"))
        self.ButtSharj.setText(_translate("main", "گزارش شارژ"))
        self.ButtPDF.setText(_translate("main", "PDF دریافت خروجی"))
        self.ButtExcel.setText(_translate("main", "Excel نمایش فایل"))
        self.label_2.setText(_translate("main", DevText))
        self.ButtSettings.setWhatsThis(_translate(
            "main", "<html><head/><body><p align=\"center\">تنظیمات</p></body></html>"))
        self.ButtSettings.setToolTip('تنظیمات')

    def check_Style(self):
        global Data, Data_2
        if not Data['DarkMode']:
            self.name.setStyleSheet(css.background_light)
            self.label.setStyleSheet(css.label_light)
            self.label_2.setStyleSheet(css.label_light)
            self.ButtExit.setStyleSheet(css.exit_butt_light)
            self.ButtBilan.setStyleSheet(css.butt_main_light)
            self.ButtAb.setStyleSheet(css.butt_main_light)
            self.ButtSharj.setStyleSheet(css.butt_main_light)
            self.ButtAbyari.setStyleSheet(css.butt_main_light)
            self.ButtPDF.setStyleSheet(css.butt_main_light)
            self.ButtExcel.setStyleSheet(css.butt_main_light)
            self.progressBar.setStyleSheet(css.bar_light)

            if Data['ShadowEffect']:
                shadowEffect(self.name, QtWidgets.QPushButton, 'light')
                self.label.setGraphicsEffect(
                    Qt.QGraphicsDropShadowEffect(blurRadius=Data_2['Shadow']['light']['blurRadius'], xOffset=Data_2['Shadow']['light']['xOffset'],
                                                 yOffset=Data_2['Shadow']['light']['yOffset'], color=Data_2['Shadow']['light']['color']))
            else:
                shadowEffect(self.name, QtWidgets.QPushButton, remove=True)
                self.label.setGraphicsEffect(None)
        else:
            self.name.setStyleSheet(css.background_dark)
            self.label.setStyleSheet(css.label_dark)
            self.label_2.setStyleSheet(css.label_dark)
            self.ButtExit.setStyleSheet(css.exit_butt_dark)
            self.ButtBilan.setStyleSheet(css.butt_main_dark)
            self.ButtAb.setStyleSheet(css.butt_main_dark)
            self.ButtSharj.setStyleSheet(css.butt_main_dark)
            self.ButtAbyari.setStyleSheet(css.butt_main_dark)
            self.ButtPDF.setStyleSheet(css.butt_main_dark)
            self.ButtExcel.setStyleSheet(css.butt_main_dark)
            self.progressBar.setStyleSheet(css.bar_dark)

            if Data['ShadowEffect']:
                shadowEffect(self.name, QtWidgets.QPushButton, 'dark')
                self.label.setGraphicsEffect(
                    Qt.QGraphicsDropShadowEffect(blurRadius=Data_2['Shadow']['dark']['blurRadius'], xOffset=Data_2['Shadow']['dark']['xOffset'],
                                                 yOffset=Data_2['Shadow']['dark']['yOffset'], color=Data_2['Shadow']['dark']['color']))
            else:
                shadowEffect(self.name, QtWidgets.QPushButton, remove=True)
                self.label.setGraphicsEffect(None)

    def getDates(self):
        global Data, Data_2, Data_3
        if Data_2['Abyari'] != {} or not Data['OpenAbyari']:
            Page.from_main_abyari()
            return
        self.ButtAbyari.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        checkFiles()
        sendNotification('در حال خواندن داده ها')
        self.progressBar.setGeometry(QtCore.QRect(33, 328, 315, 50))
        self.timer.start(Data['AbyariTurn2'][1]-Data['AbyariTurn1'][0])
        self.progressBar.setValue(Data['AbyariTurn1'][0])

        sheet = 'آبیاری'
        vahed = list(set([int(i) for i in range(1, 14)]) -
                     set(Data['AbyariFilter']))
        font = E.Font(name='B Nazanin', charset=178, family=None, b=False, i=False, strike=None, outline=None,
                      shadow=None, condense=None, color=None, extend=None, sz=14.0, u=None, vertAlign=None, scheme=None)

        try:
            Range = [Data['AbyariTurn1'][0], Data['AbyariTurn1'][1]]
            for a, b in zip(range(Range[0], Range[1]), vahed):
                c = str(b)
                Data_2['Abyari'][c] = {}
                Data_2['Abyari'][c]['1'] = []
                Data_2['Abyari'][c]['1'].append(
                    E.get_cell_value(sheet, f'B{a}'))
                Data_2['Abyari'][c]['1'].append(
                    E.get_cell_value(sheet, f'C{a}'))
                self.progressBar.setValue(a)

            Range = [int(Data['AbyariTurn2'][0]), int(Data['AbyariTurn2'][1])]
            for a, b in zip(range(Range[0], Range[1]), vahed):
                c = str(b)
                Data_2['Abyari'][c]['2'] = []
                Data_2['Abyari'][c]['2'].append(
                    E.get_cell_value(sheet, f'B{a}'))
                Data_2['Abyari'][c]['2'].append(
                    E.get_cell_value(sheet, f'C{a}'))
                self.progressBar.setValue(a)
        except:
            sendNotification(
                'خطایی رخ داده است\n(اگر فایل اکسل باز است آن را ببندید)')

        self.timer.stop()
        self.progressBar.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.ButtAbyari.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Page.from_main_abyari()

    def showExcel(self):
        global Data_3
        try:
            os.startfile(Data_3['fileName'])
        except:
            sendNotification('خطایی رخ داده است')


class Ui_settings(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, settings):
        global Data, Data_3
        settings.setObjectName("settings")
        settings.resize(320, 240)
        settings.setMinimumSize(QtCore.QSize(317, 240))
        settings.setMaximumSize(QtCore.QSize(320, 240))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pics/.Images/Icon/euro.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        settings.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(settings)
        self.label.setGeometry(QtCore.QRect(80, 0, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.ButtBack = QtWidgets.QPushButton(settings)
        self.ButtBack.setGeometry(QtCore.QRect(10, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ButtBack.setFont(font)
        self.ButtBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtBack.setStyleSheet(css.butt_transparent)
        self.ButtBack.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pics/.Images/Icon/back.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtBack.setIcon(icon1)
        self.ButtBack.setIconSize(QtCore.QSize(36, 36))
        self.ButtBack.setObjectName("ButtBack")
        self.ButtBack.setStyleSheet(css.butt_transparent)
        self.label_2 = QtWidgets.QLabel(settings)
        self.label_2.setGeometry(QtCore.QRect(0, 210, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(8)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.CheckPDF = QtWidgets.QCheckBox(settings)
        self.CheckPDF.setGeometry(QtCore.QRect(10, 180, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(12)
        self.CheckPDF.setFont(font)
        self.CheckPDF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CheckPDF.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CheckPDF.setChecked(Data['ShowPDF'])
        self.CheckPDF.setObjectName("CheckPDF")
        self.CheckDarkMode = QtWidgets.QCheckBox(settings)
        self.CheckDarkMode.setGeometry(QtCore.QRect(10, 120, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(12)
        self.CheckDarkMode.setFont(font)
        self.CheckDarkMode.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CheckDarkMode.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CheckDarkMode.setChecked(Data['DarkMode'])
        self.CheckDarkMode.setObjectName("CheckDarkMode")
        self.CheckBilan6Month = QtWidgets.QCheckBox(settings)
        self.CheckBilan6Month.setGeometry(QtCore.QRect(10, 60, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(12)
        self.CheckBilan6Month.setFont(font)
        self.CheckBilan6Month.setCursor(QtGui.QCursor(
            setCurser(not Data_3['donePages']['bilan'])))
        self.CheckBilan6Month.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CheckBilan6Month.setChecked(Data['Bilan6Month'])
        self.CheckBilan6Month.setCheckable(not Data_3['donePages']['bilan'])
        self.CheckBilan6Month.setObjectName("CheckBilan6Month")
        self.CheckChangeBy1000 = QtWidgets.QCheckBox(settings)
        self.CheckChangeBy1000.setGeometry(QtCore.QRect(10, 90, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(12)
        self.CheckChangeBy1000.setFont(font)
        self.CheckChangeBy1000.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CheckChangeBy1000.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CheckChangeBy1000.setChecked(Data['ChangeBy1000'])
        self.CheckChangeBy1000.setObjectName("CheckChangeBy1000")
        self.CheckEffect = QtWidgets.QCheckBox(settings)
        self.CheckEffect.setGeometry(QtCore.QRect(10, 150, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(12)
        self.CheckEffect.setFont(font)
        self.CheckEffect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CheckEffect.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CheckEffect.setChecked(Data['ShadowEffect'])
        self.CheckEffect.setObjectName("CheckEffect")
        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)
        settings.setTabOrder(self.CheckBilan6Month, self.CheckChangeBy1000)
        settings.setTabOrder(self.CheckChangeBy1000, self.CheckDarkMode)
        settings.setTabOrder(self.CheckDarkMode, self.CheckEffect)
        settings.setTabOrder(self.CheckEffect, self.CheckPDF)
        settings.setTabOrder(self.CheckPDF, self.ButtBack)

        self.name = settings
        self.check_Style()
        self.ButtBack.clicked.connect(Page.close_settings)
        self.CheckBilan6Month.clicked.connect(self.check_Bilan)
        self.CheckChangeBy1000.clicked.connect(self.check_1000)
        self.CheckDarkMode.clicked.connect(self.check_Style)
        self.CheckEffect.clicked.connect(self.check_Style)
        self.CheckPDF.clicked.connect(self.check_PDF)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "Settings"))
        self.label.setText(_translate("settings", "تنظیمات"))
        self.ButtBack.setWhatsThis(_translate(
            "settings", "<html><head/><body><p align=\"center\">برگشت</p></body></html>"))
        self.label_2.setText(_translate("settings", Version))
        self.CheckPDF.setText(_translate(
            "settings", "نمایش داده شود PDF بعد از دریافت خروجی"))
        self.CheckDarkMode.setText(_translate(
            "settings", "حالت تیره - Dark Mode"))
        self.CheckBilan6Month.setText(
            _translate("settings", "بیلان 6 ماه نخست"))
        self.CheckChangeBy1000.setText(_translate(
            "settings", "اعداد 1000 تایی تغییر کند"))
        self.CheckEffect.setText(_translate("settings", "افکت های گرافیکی"))
        self.ButtBack.setToolTip('برگشت')

    def check_Style(self):
        global Data, Data_2
        Data['DarkMode'] = bool(self.CheckDarkMode.checkState())
        Data['ShadowEffect'] = bool(self.CheckEffect.checkState())
        # self.name.setWindowFlags(QtCore.Qt.FramelessWindowHint) #for making window bar invisible
        if not Data['DarkMode']:
            self.name.setStyleSheet(css.background_light)
            self.CheckChangeBy1000.setStyleSheet(css.label_light)
            self.CheckBilan6Month.setStyleSheet(css.label_light)
            self.CheckDarkMode.setStyleSheet(css.label_light)
            self.CheckPDF.setStyleSheet(css.label_light)
            self.CheckEffect.setStyleSheet(css.label_light)
            self.label_2.setStyleSheet(css.label_light)
            self.label.setStyleSheet(css.label_light)

            if Data['ShadowEffect']:
                shadowEffect(self.name, QtWidgets.QPushButton, 'light')
                self.label.setGraphicsEffect(
                    Qt.QGraphicsDropShadowEffect(blurRadius=Data_2['Shadow']['light']['blurRadius'], xOffset=Data_2['Shadow']['light']['xOffset'],
                                                 yOffset=Data_2['Shadow']['light']['yOffset'], color=Data_2['Shadow']['light']['color']))
            else:
                shadowEffect(self.name, QtWidgets.QPushButton, remove=True)
                self.label.setGraphicsEffect(None)
        else:
            self.name.setStyleSheet(css.background_dark)
            self.CheckChangeBy1000.setStyleSheet(css.label_dark)
            self.CheckBilan6Month.setStyleSheet(css.label_dark)
            self.CheckDarkMode.setStyleSheet(css.label_dark)
            self.CheckPDF.setStyleSheet(css.label_dark)
            self.CheckEffect.setStyleSheet(css.label_dark)
            self.label_2.setStyleSheet(css.label_dark)
            self.label.setStyleSheet(css.label_dark)

            if Data['ShadowEffect']:
                shadowEffect(self.name, QtWidgets.QPushButton, 'dark')
                self.label.setGraphicsEffect(
                    Qt.QGraphicsDropShadowEffect(blurRadius=Data_2['Shadow']['dark']['blurRadius'], xOffset=Data_2['Shadow']['dark']['xOffset'],
                                                 yOffset=Data_2['Shadow']['dark']['yOffset'], color=Data_2['Shadow']['dark']['color']))
            else:
                shadowEffect(self.name, QtWidgets.QPushButton, remove=True)
                self.label.setGraphicsEffect(None)
        saveJson()
        Page.check_Style()

    def check_Bilan(self):
        global Data, filesList
        obj = self.CheckBilan6Month
        if bool(obj.isCheckable()):
            Data['Bilan6Month'] = bool(obj.checkState())
            checkFiles()
            saveJson()
        try:
            Page.bilan.comboBox_Update(Type='month')
        except:
            pass

    def check_PDF(self):
        global Data
        Data['ShowPDF'] = bool(self.CheckPDF.checkState())
        saveJson()

    def check_1000(self):
        global Data
        Data['ChangeBy1000'] = bool(self.CheckChangeBy1000.checkState())
        saveJson()
        try:
            Page.ab.update()
        except:
            print('error!')


class Ui_bilan(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, bilan):
        global month
        bilan.setObjectName("bilan")
        bilan.resize(480, 640)
        bilan.setMinimumSize(QtCore.QSize(480, 640))
        bilan.setMaximumSize(QtCore.QSize(480, 640))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        bilan.setFont(font)
        bilan.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pics/.Images/Icon/euro.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        bilan.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(bilan)
        self.label.setGeometry(QtCore.QRect(70, 10, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.ButtExit = QtWidgets.QPushButton(bilan)
        self.ButtExit.setGeometry(QtCore.QRect(10, 560, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ButtExit.setFont(font)
        self.ButtExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtExit.setObjectName("ButtExit")
        self.label_2 = QtWidgets.QLabel(bilan)
        self.label_2.setGeometry(QtCore.QRect(20, 615, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(9)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ButtSettings = QtWidgets.QPushButton(bilan)
        self.ButtSettings.setGeometry(QtCore.QRect(420, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ButtSettings.setFont(font)
        self.ButtSettings.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtSettings.setStyleSheet(css.butt_transparent)
        self.ButtSettings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            ":/pics/.Images/Icon/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtSettings.setIcon(icon1)
        self.ButtSettings.setIconSize(QtCore.QSize(48, 48))
        self.ButtSettings.setObjectName("ButtSettings")
        self.ButtBack = QtWidgets.QPushButton(bilan)
        self.ButtBack.setGeometry(QtCore.QRect(10, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ButtBack.setFont(font)
        self.ButtBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtBack.setStyleSheet(css.butt_transparent)
        self.ButtBack.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pics/.Images/Icon/back.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtBack.setIcon(icon2)
        self.ButtBack.setIconSize(QtCore.QSize(48, 48))
        self.ButtBack.setObjectName("ButtBack")
        self.label_3 = QtWidgets.QLabel(bilan)
        self.label_3.setGeometry(QtCore.QRect(130, 80, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.ComboMonth = QtWidgets.QComboBox(bilan)
        self.ComboMonth.setGeometry(QtCore.QRect(10, 150, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ComboMonth.setFont(font)
        self.ComboMonth.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ComboMonth.setEditable(False)
        self.ComboMonth.setMaxVisibleItems(12)
        self.ComboMonth.setMaxCount(12)
        self.ComboMonth.setFrame(False)
        self.ComboMonth.setObjectName("ComboMonth")
        self.label_4 = QtWidgets.QLabel(bilan)
        self.label_4.setGeometry(QtCore.QRect(400, 230, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.ComboManba = QtWidgets.QComboBox(bilan)
        self.ComboManba.setGeometry(QtCore.QRect(10, 230, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ComboManba.setFont(font)
        self.ComboManba.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ComboManba.setEditable(False)
        self.ComboManba.setMaxVisibleItems(12)
        self.ComboManba.setMaxCount(12)
        self.ComboManba.setFrame(False)
        self.ComboManba.setObjectName("ComboManba")
        self.spinBoxManba = QtWidgets.QSpinBox(bilan)
        self.spinBoxManba.setGeometry(QtCore.QRect(10, 290, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.spinBoxManba.setFont(font)
        self.spinBoxManba.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBoxManba.setFrame(False)
        self.spinBoxManba.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxManba.setReadOnly(False)
        self.spinBoxManba.setMaximum(2147483647)
        self.spinBoxManba.setSingleStep(10000)
        self.spinBoxManba.setObjectName("spinBoxManba")
        self.ComboKharj = QtWidgets.QComboBox(bilan)
        self.ComboKharj.setGeometry(QtCore.QRect(10, 370, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ComboKharj.setFont(font)
        self.ComboKharj.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ComboKharj.setEditable(False)
        self.ComboKharj.setMaxVisibleItems(12)
        self.ComboKharj.setMaxCount(12)
        self.ComboKharj.setFrame(False)
        self.ComboKharj.setObjectName("ComboKharj")
        self.label_5 = QtWidgets.QLabel(bilan)
        self.label_5.setGeometry(QtCore.QRect(400, 370, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.spinBoxKharj = QtWidgets.QSpinBox(bilan)
        self.spinBoxKharj.setGeometry(QtCore.QRect(10, 430, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.spinBoxKharj.setFont(font)
        self.spinBoxKharj.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBoxKharj.setFrame(False)
        self.spinBoxKharj.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxKharj.setReadOnly(False)
        self.spinBoxKharj.setMaximum(2147483647)
        self.spinBoxKharj.setSingleStep(10000)
        self.spinBoxKharj.setObjectName("spinBoxKharj")
        self.ButtSabt = QtWidgets.QPushButton(bilan)
        self.ButtSabt.setGeometry(QtCore.QRect(10, 500, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ButtSabt.setFont(font)
        self.ButtSabt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtSabt.setObjectName("ButtSabt")
        self.label_3.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.ButtExit.raise_()
        self.ButtSettings.raise_()
        self.ButtBack.raise_()
        self.ComboMonth.raise_()
        self.label_4.raise_()
        self.ComboManba.raise_()
        self.spinBoxManba.raise_()
        self.ComboKharj.raise_()
        self.label_5.raise_()
        self.spinBoxKharj.raise_()
        self.ButtSabt.raise_()
        self.retranslateUi(bilan)
        self.ComboMonth.setCurrentIndex(0)
        self.ComboManba.setCurrentIndex(0)
        self.ComboKharj.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(bilan)
        bilan.setTabOrder(self.ComboMonth, self.ComboManba)
        bilan.setTabOrder(self.ComboManba, self.spinBoxManba)
        bilan.setTabOrder(self.spinBoxManba, self.ComboKharj)
        bilan.setTabOrder(self.ComboKharj, self.spinBoxKharj)
        bilan.setTabOrder(self.spinBoxKharj, self.ButtSabt)
        bilan.setTabOrder(self.ButtSabt, self.ButtExit)
        bilan.setTabOrder(self.ButtExit, self.ButtSettings)
        bilan.setTabOrder(self.ButtSettings, self.ButtBack)

        self.name = bilan
        self.check_Style()
        self.comboBox_Update(Everything=True)
        self.ButtBack.clicked.connect(Page.from_bilan_main)
        self.ButtSettings.clicked.connect(Page.show_settings)
        self.ButtExit.clicked.connect(sys.exit)
        self.ButtSabt.clicked.connect(self.done)
        self.ComboManba.currentIndexChanged.connect(
            lambda: self.updateData('manba', True))
        self.ComboKharj.currentIndexChanged.connect(
            lambda: self.updateData('kharj', True))
        self.spinBoxManba.valueChanged.connect(
            lambda: self.updateData('manba', False))
        self.spinBoxKharj.valueChanged.connect(
            lambda: self.updateData('kharj', False))

    def retranslateUi(self, bilan):
        _translate = QtCore.QCoreApplication.translate
        bilan.setWindowTitle(_translate("bilan", AppName))
        self.label.setText(_translate("bilan", "بیلان 6 ماهه"))
        self.ButtExit.setText(_translate("bilan", "خروج"))
        self.label_2.setText(_translate("bilan", DevText))
        self.ButtSettings.setWhatsThis(_translate(
            "bilan", "<html><head/><body><p align=\"center\">تنظیمات</p></body></html>"))
        self.ButtBack.setWhatsThis(_translate(
            "bilan", "<html><head/><body><p align=\"center\">بازگشت</p></body></html>"))
        self.label_3.setText(_translate("bilan", "ماه جاری"))
        self.label_4.setText(_translate("bilan", "منابع"))
        self.label_5.setText(_translate("bilan", "مصارف"))
        self.ButtSabt.setText(_translate("bilan", "ثبت"))
        self.ButtBack.setToolTip('برگشت')
        self.ButtSettings.setToolTip('تنظیمات')

    def check_Style(self):
        global Data, Data_2
        if not Data['DarkMode']:
            self.name.setStyleSheet(css.background_light)
            self.ButtExit.setStyleSheet(css.exit_butt_light)
            self.ButtSabt.setStyleSheet(css.butt_sabt_light)
            self.label.setStyleSheet(css.label_light)
            self.label_2.setStyleSheet(css.label_light)
            self.label_3.setStyleSheet(css.other_light)
            self.label_4.setStyleSheet(css.other_light)
            self.label_5.setStyleSheet(css.other_light)
            self.spinBoxManba.setStyleSheet(css.other_light)
            self.spinBoxKharj.setStyleSheet(css.other_light)
            self.ComboMonth.setStyleSheet(css.other_light)
            self.ComboManba.setStyleSheet(css.other_light)
            self.ComboKharj.setStyleSheet(css.other_light)

            if Data['ShadowEffect']:
                shadowEffect(self.name, QtWidgets.QPushButton, 'light')
                self.label.setGraphicsEffect(
                    Qt.QGraphicsDropShadowEffect(blurRadius=Data_2['Shadow']['light']['blurRadius'], xOffset=Data_2['Shadow']['light']['xOffset'],
                                                 yOffset=Data_2['Shadow']['light']['yOffset'], color=Data_2['Shadow']['light']['color']))
            else:
                shadowEffect(self.name, QtWidgets.QPushButton, remove=True)
                self.label.setGraphicsEffect(None)
        else:
            self.name.setStyleSheet(css.background_dark)
            self.ButtExit.setStyleSheet(css.exit_butt_dark)
            self.ButtSabt.setStyleSheet(css.butt_sabt_dark)
            self.label.setStyleSheet(css.label_dark)
            self.label_2.setStyleSheet(css.label_dark)
            self.label_3.setStyleSheet(css.other_dark)
            self.label_4.setStyleSheet(css.other_dark)
            self.label_5.setStyleSheet(css.other_dark)
            self.spinBoxManba.setStyleSheet(css.other_dark)
            self.spinBoxKharj.setStyleSheet(css.other_dark)
            self.ComboMonth.setStyleSheet(css.other_dark)
            self.ComboManba.setStyleSheet(css.other_dark)
            self.ComboKharj.setStyleSheet(css.other_dark)

            if Data['ShadowEffect']:
                shadowEffect(self.name, QtWidgets.QPushButton, 'dark')
                self.label.setGraphicsEffect(
                    Qt.QGraphicsDropShadowEffect(blurRadius=Data_2['Shadow']['dark']['blurRadius'], xOffset=Data_2['Shadow']['dark']['xOffset'],
                                                 yOffset=Data_2['Shadow']['dark']['yOffset'], color=Data_2['Shadow']['dark']['color']))
            else:
                shadowEffect(self.name, QtWidgets.QPushButton, remove=True)
                self.label.setGraphicsEffect(None)

    def comboBox_Update(self, Type='', Everything=False):
        global Data, Data_2
        self.check_Style()
        if Type == 'month' or Everything:
            box = self.ComboMonth
            box.clear()
            temp = '2nd6Month'
            if Data['Bilan6Month']:
                temp = '1st6Month'
            box.addItems(list(Data_2[temp].keys()))
        if Type == 'manba' or Everything:
            box = self.ComboManba
            box.clear()
            box.addItems(list(Data_2['Manabe'].keys()))
        if Type == 'kharj' or Everything:
            box = self.ComboKharj
            box.clear()
            box.addItems(list(Data_2['Masaref'].keys()))

    def done(self):
        global Data_3, month
        self.ButtSabt.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        try:
            month = self.ComboMonth.currentText()
            Data_3['donePages']['bilan'] = True
            saveExcel('bilan')
            sendNotification('ثبت شد')
            Page.from_bilan_main()
        except:
            sendNotification(
                'خطایی رخ داده است\n(اگر فایل اکسل باز است آن را ببندید)')
        self.ButtSabt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def updateData(self, s, key):
        global Data_3, month
        if s == 'manba':
            box = self.ComboManba.currentText()
            val = self.spinBoxManba.value()
            combo = self.spinBoxManba
        elif s == 'kharj':
            box = self.ComboKharj.currentText()
            val = self.spinBoxKharj.value()
            combo = self.spinBoxKharj
        if not key and val != 0:
            Data_3[s][box] = val
        else:
            if box in Data_3[s].keys():
                combo.setValue(Data_3[s][box])
            else:
                combo.setValue(0)


class Ui_ab(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, ab):
        global Data
        ab.setObjectName("ab")
        ab.resize(480, 640)
        ab.setMinimumSize(QtCore.QSize(480, 640))
        ab.setMaximumSize(QtCore.QSize(480, 640))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        ab.setFont(font)
        ab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pics/.Images/Icon/euro.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ab.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(ab)
        self.label.setGeometry(QtCore.QRect(70, 10, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.ButtExit = QtWidgets.QPushButton(ab)
        self.ButtExit.setGeometry(QtCore.QRect(10, 560, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ButtExit.setFont(font)
        self.ButtExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtExit.setObjectName("ButtExit")
        self.label_2 = QtWidgets.QLabel(ab)
        self.label_2.setGeometry(QtCore.QRect(20, 615, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(9)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ButtSettings = QtWidgets.QPushButton(ab)
        self.ButtSettings.setGeometry(QtCore.QRect(420, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ButtSettings.setFont(font)
        self.ButtSettings.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtSettings.setStyleSheet(css.butt_transparent)
        self.ButtSettings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            ":/pics/.Images/Icon/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtSettings.setIcon(icon1)
        self.ButtSettings.setIconSize(QtCore.QSize(48, 48))
        self.ButtSettings.setObjectName("ButtSettings")
        self.ButtBack = QtWidgets.QPushButton(ab)
        self.ButtBack.setGeometry(QtCore.QRect(10, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ButtBack.setFont(font)
        self.ButtBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtBack.setStyleSheet(css.butt_transparent)
        self.ButtBack.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pics/.Images/Icon/back.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtBack.setIcon(icon2)
        self.ButtBack.setIconSize(QtCore.QSize(48, 48))
        self.ButtBack.setObjectName("ButtBack")
        self.label_3 = QtWidgets.QLabel(ab)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ab)
        self.label_4.setGeometry(QtCore.QRect(250, 210, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.spinBoxNafar = QtWidgets.QSpinBox(ab)
        self.spinBoxNafar.setGeometry(QtCore.QRect(10, 270, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.spinBoxNafar.setFont(font)
        self.spinBoxNafar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBoxNafar.setFrame(False)
        self.spinBoxNafar.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxNafar.setReadOnly(False)
        self.spinBoxNafar.setMaximum(10)
        self.spinBoxNafar.setSingleStep(1)
        self.spinBoxNafar.setValue(Data['Nafarat']['1'])
        self.spinBoxNafar.setObjectName("spinBoxNafar")
        self.label_5 = QtWidgets.QLabel(ab)
        self.label_5.setGeometry(QtCore.QRect(250, 340, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.ButtSabt = QtWidgets.QPushButton(ab)
        self.ButtSabt.setGeometry(QtCore.QRect(10, 500, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ButtSabt.setFont(font)
        self.ButtSabt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtSabt.setObjectName("ButtSabt")
        self.spinBoxAb = QtWidgets.QSpinBox(ab)
        self.spinBoxAb.setGeometry(QtCore.QRect(10, 140, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.spinBoxAb.setFont(font)
        self.spinBoxAb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBoxAb.setFrame(False)
        self.spinBoxAb.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxAb.setReadOnly(False)
        self.spinBoxAb.setMaximum(2147483647)
        self.spinBoxAb.setSingleStep(10000)
        self.spinBoxAb.setValue(0)
        self.spinBoxAb.setObjectName("spinBoxAb")
        self.label_6 = QtWidgets.QLabel(ab)
        self.label_6.setGeometry(QtCore.QRect(250, 270, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.spinBoxVahed = QtWidgets.QSpinBox(ab)
        self.spinBoxVahed.setGeometry(QtCore.QRect(10, 210, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.spinBoxVahed.setFont(font)
        self.spinBoxVahed.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBoxVahed.setFrame(False)
        self.spinBoxVahed.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxVahed.setReadOnly(False)
        self.spinBoxVahed.setMinimum(1)
        self.spinBoxVahed.setMaximum(13)
        self.spinBoxVahed.setSingleStep(1)
        self.spinBoxVahed.setObjectName("spinBoxVahed")
        self.label_7 = QtWidgets.QLabel(ab)
        self.label_7.setGeometry(QtCore.QRect(250, 400, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lcdNumberSahm = QtWidgets.QLCDNumber(ab)
        self.lcdNumberSahm.setGeometry(QtCore.QRect(10, 340, 231, 51))
        self.lcdNumberSahm.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lcdNumberSahm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumberSahm.setDigitCount(7)
        self.lcdNumberSahm.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumberSahm.setProperty("intValue", 0)
        self.lcdNumberSahm.setObjectName("lcdNumberSahm")
        self.lcdNumberSahmRound = QtWidgets.QLCDNumber(ab)
        self.lcdNumberSahmRound.setGeometry(QtCore.QRect(10, 400, 231, 51))
        self.lcdNumberSahmRound.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lcdNumberSahmRound.setDigitCount(7)
        self.lcdNumberSahmRound.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumberSahmRound.setProperty("intValue", 0)
        self.lcdNumberSahmRound.setObjectName("lcdNumberSahmRound")
        self.ButtPlus100 = QtWidgets.QPushButton(ab)
        self.ButtPlus100.setGeometry(QtCore.QRect(129, 455, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(12)
        self.ButtPlus100.setFont(font)
        self.ButtPlus100.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtPlus100.setStyleSheet("QPushButton{\n"
                                       "background-color:rgb(55, 167, 148);\n"
                                       "border: 0px solid black;\n"
                                       "color:white;\n"
                                       "border-radius: 10px}\n"
                                       "QPushButton:hover{\n"
                                       "color:rgb(0, 255, 0);}")
        self.ButtPlus100.setObjectName("ButtPlus100")
        self.ButtMine100 = QtWidgets.QPushButton(ab)
        self.ButtMine100.setGeometry(QtCore.QRect(20, 455, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(12)
        self.ButtMine100.setFont(font)
        self.ButtMine100.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtMine100.setStyleSheet("QPushButton{\n"
                                       "background-color:rgb(55, 167, 148);\n"
                                       "border: 0px solid black;\n"
                                       "color:white;\n"
                                       "border-radius: 10px}\n"
                                       "QPushButton:hover{\n"
                                       "color:rgb(255, 0, 0);}")
        self.ButtMine100.setObjectName("ButtMine100")
        self.label_8 = QtWidgets.QLabel(ab)
        self.label_8.setGeometry(QtCore.QRect(10, 400, 231, 91))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_8.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.ButtExit.raise_()
        self.ButtSettings.raise_()
        self.ButtBack.raise_()
        self.label_4.raise_()
        self.spinBoxNafar.raise_()
        self.label_5.raise_()
        self.ButtSabt.raise_()
        self.spinBoxAb.raise_()
        self.label_6.raise_()
        self.spinBoxVahed.raise_()
        self.label_7.raise_()
        self.lcdNumberSahm.raise_()
        self.lcdNumberSahmRound.raise_()
        self.ButtMine100.raise_()
        self.ButtPlus100.raise_()
        self.retranslateUi(ab)
        QtCore.QMetaObject.connectSlotsByName(ab)
        ab.setTabOrder(self.spinBoxAb, self.spinBoxVahed)
        ab.setTabOrder(self.spinBoxVahed, self.spinBoxNafar)
        ab.setTabOrder(self.spinBoxNafar, self.ButtPlus100)
        ab.setTabOrder(self.ButtPlus100, self.ButtMine100)
        ab.setTabOrder(self.ButtMine100, self.ButtSabt)
        ab.setTabOrder(self.ButtSabt, self.ButtExit)
        ab.setTabOrder(self.ButtExit, self.ButtBack)
        ab.setTabOrder(self.ButtBack, self.ButtSettings)

        self.name = ab
        shadowEffect(self.name, QtWidgets.QPushButton, 'light', Filter=[
                     'ButtPlus100', 'ButtMine100'], onlyFilter=True)
        self.check_Style()
        self.ButtBack.clicked.connect(Page.from_ab_main)
        self.ButtSettings.clicked.connect(Page.show_settings)
        self.ButtExit.clicked.connect(sys.exit)
        self.ButtSabt.clicked.connect(self.done)
        self.spinBoxAb.valueChanged.connect(self.calculate)
        self.spinBoxVahed.valueChanged.connect(lambda: self.spinBoxNafar.setValue(
            Data['Nafarat'][str(self.spinBoxVahed.value())]))
        self.spinBoxNafar.valueChanged.connect(lambda: self.update(nafar=True))
        self.ButtPlus100.clicked.connect(
            lambda: self.update(button=True, sign='+'))
        self.ButtMine100.clicked.connect(
            lambda: self.update(button=True, sign='-'))

    def retranslateUi(self, ab):
        global Data
        _translate = QtCore.QCoreApplication.translate
        ab.setWindowTitle(_translate("ab", AppName))
        self.label.setText(_translate("ab", "سهم آب مصرفی"))
        self.ButtExit.setText(_translate("ab", "خروج"))
        self.label_2.setText(_translate("ab", DevText))
        self.label_3.setText(_translate("ab", "مبلغ قبض آب را وارد کنید"))
        self.label_4.setText(_translate("ab", "شماره واحد"))
        self.label_5.setText(_translate("ab", "سهم هر نفر"))
        self.ButtSabt.setText(_translate("ab", "ثبت"))
        self.label_6.setText(_translate("ab", "تعداد نفرات"))
        self.label_7.setText(_translate("ab", "سهم هر نفر زند شده"))
        self.ButtBack.setToolTip('برگشت')
        self.ButtSettings.setToolTip('تنظیمات')
        if Data['ChangeBy1000']:
            self.ButtPlus100.setText(_translate("ab", "+1000"))
            self.ButtMine100.setText(_translate("ab", "-1000"))
        else:
            self.ButtPlus100.setText(_translate("ab", "+100"))
            self.ButtMine100.setText(_translate("ab", "-100"))

    def check_Style(self):
        global Data
        if not Data['DarkMode']:
            self.name.setStyleSheet(css.background_light)
            self.ButtExit.setStyleSheet(css.exit_butt_light)
            self.label.setStyleSheet(css.label_light)
            self.label_2.setStyleSheet(css.label_light)
            self.label_3.setStyleSheet(css.other_light)
            self.label_4.setStyleSheet(css.other_light)
            self.label_5.setStyleSheet(css.other_light)
            self.label_6.setStyleSheet(css.other_light)
            self.label_7.setStyleSheet(css.other_light)
            self.spinBoxNafar.setStyleSheet(css.other_light)
            self.ButtSabt.setStyleSheet(css.butt_sabt_light)
            self.spinBoxAb.setStyleSheet(css.other_light)
            self.spinBoxVahed.setStyleSheet(css.other_light)
            self.lcdNumberSahm.setStyleSheet(css.other_light)
            self.lcdNumberSahmRound.setStyleSheet(css.other_light)
            self.label_8.setStyleSheet(css.other_light)

            if Data['ShadowEffect']:
                shadowEffect(self.name, QtWidgets.QPushButton, 'light', Filter=[
                             'ButtPlus100', 'ButtMine100', 'ButtSettings', 'ButtBack'])
                self.label.setGraphicsEffect(
                    Qt.QGraphicsDropShadowEffect(blurRadius=Data_2['Shadow']['light']['blurRadius'], xOffset=Data_2['Shadow']['light']['xOffset'],
                                                 yOffset=Data_2['Shadow']['light']['yOffset'], color=Data_2['Shadow']['light']['color']))
            else:
                shadowEffect(self.name, QtWidgets.QPushButton, remove=True)
                self.label.setGraphicsEffect(None)
        else:
            self.name.setStyleSheet(css.background_dark)
            self.ButtExit.setStyleSheet(css.exit_butt_dark)
            self.label.setStyleSheet(css.label_dark)
            self.label_2.setStyleSheet(css.label_dark)
            self.label_3.setStyleSheet(css.other_dark)
            self.label_4.setStyleSheet(css.other_dark)
            self.spinBoxNafar.setStyleSheet(css.other_dark)
            self.label_5.setStyleSheet(css.other_dark)
            self.ButtSabt.setStyleSheet(css.butt_sabt_dark)
            self.spinBoxAb.setStyleSheet(css.other_dark)
            self.label_6.setStyleSheet(css.other_dark)
            self.spinBoxVahed.setStyleSheet(css.other_dark)
            self.label_7.setStyleSheet(css.other_dark)
            self.lcdNumberSahm.setStyleSheet(css.other_dark)
            self.lcdNumberSahmRound.setStyleSheet(css.other_dark)
            self.label_8.setStyleSheet(css.other_dark)

            if Data['ShadowEffect']:
                shadowEffect(self.name, QtWidgets.QPushButton, 'dark', Filter=[
                             'ButtPlus100', 'ButtMine100', 'ButtSettings', 'ButtBack'])
                self.label.setGraphicsEffect(
                    Qt.QGraphicsDropShadowEffect(blurRadius=Data_2['Shadow']['dark']['blurRadius'], xOffset=Data_2['Shadow']['dark']['xOffset'],
                                                 yOffset=Data_2['Shadow']['dark']['yOffset'], color=Data_2['Shadow']['dark']['color']))
            else:
                shadowEffect(self.name, QtWidgets.QPushButton, remove=True)
                self.label.setGraphicsEffect(None)

    def calculate(self):
        num = int(self.spinBoxAb.value())
        Lcd = self.lcdNumberSahm
        Lcd.setProperty("intValue", int(num/sumNafarat()))
        self.round_num()

    def round_num(self):
        num = int(self.lcdNumberSahm.value())
        obj = self.lcdNumberSahmRound
        obj.setProperty("intValue", int(roundNumber(num)))

    def update(self, button=False, nafar=False, value=100, sign='+'):
        global Data
        if button:
            if Data['ChangeBy1000']:
                value = 1000
            else:
                value = 100
            if sign == '+':
                self.lcdNumberSahmRound.setProperty(
                    "intValue", int(self.lcdNumberSahmRound.value())+value)
            if sign == '-':
                self.lcdNumberSahmRound.setProperty(
                    "intValue", int(self.lcdNumberSahmRound.value())-value)
        elif nafar:
            vahed = str(self.spinBoxVahed.value())
            nafar = int(self.spinBoxNafar.value())
            Data['Nafarat'][vahed] = nafar
            saveJson()
            self.calculate()
        else:
            _translate = QtCore.QCoreApplication.translate
            if Data['ChangeBy1000']:
                self.ButtPlus100.setText(_translate("ab", "+1000"))
                self.ButtMine100.setText(_translate("ab", "-1000"))
            else:
                self.ButtPlus100.setText(_translate("ab", "+100"))
                self.ButtMine100.setText(_translate("ab", "-100"))

    def done(self):
        global sahmNafarRound, sahmNafar, Data_3
        self.ButtSabt.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        try:
            num = int(self.spinBoxAb.value())
            sahmNafar = int(self.lcdNumberSahm.value())
            sahmNafarRound = int(self.lcdNumberSahmRound.value())
            saveExcel(mode='ab', data={num: "D2",
                                       sahmNafar: "E2", sahmNafarRound: "F2"})
            Data_3['donePages']['ab'] = True
            sendNotification('ثبت شد')
            Page.from_ab_main()
        except:
            sendNotification(
                'خطایی رخ داده است\n(اگر فایل اکسل باز است آن را ببندید)')
        self.ButtSabt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


class Ui_sharj(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, sharj):
        global Data, sahmNafarRound
        sharj.setObjectName("sharj")
        sharj.resize(480, 640)
        sharj.setMinimumSize(QtCore.QSize(480, 640))
        sharj.setMaximumSize(QtCore.QSize(480, 640))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        sharj.setFont(font)
        sharj.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pics/.Images/Icon/euro.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sharj.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(sharj)
        self.label.setGeometry(QtCore.QRect(70, 10, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(sharj)
        self.label_2.setGeometry(QtCore.QRect(20, 615, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(9)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ButtSettings = QtWidgets.QPushButton(sharj)
        self.ButtSettings.setGeometry(QtCore.QRect(420, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ButtSettings.setFont(font)
        self.ButtSettings.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtSettings.setStyleSheet(css.butt_transparent)
        self.ButtSettings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            ":/pics/.Images/Icon/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtSettings.setIcon(icon1)
        self.ButtSettings.setIconSize(QtCore.QSize(48, 48))
        self.ButtSettings.setObjectName("ButtSettings")
        self.ButtBack = QtWidgets.QPushButton(sharj)
        self.ButtBack.setGeometry(QtCore.QRect(10, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ButtBack.setFont(font)
        self.ButtBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtBack.setStyleSheet(css.butt_transparent)
        self.ButtBack.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pics/.Images/Icon/back.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtBack.setIcon(icon2)
        self.ButtBack.setIconSize(QtCore.QSize(48, 48))
        self.ButtBack.setObjectName("ButtBack")
        self.label_3 = QtWidgets.QLabel(sharj)
        self.label_3.setGeometry(QtCore.QRect(250, 80, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(sharj)
        self.label_4.setGeometry(QtCore.QRect(250, 200, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lcdNumberHazineAb = QtWidgets.QLCDNumber(sharj)
        self.lcdNumberHazineAb.setGeometry(QtCore.QRect(10, 260, 231, 51))
        self.lcdNumberHazineAb.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lcdNumberHazineAb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumberHazineAb.setDigitCount(7)
        self.lcdNumberHazineAb.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumberHazineAb.setProperty("intValue", 0)
        self.lcdNumberHazineAb.setObjectName("lcdNumberHazineAb")
        self.label_5 = QtWidgets.QLabel(sharj)
        self.label_5.setGeometry(QtCore.QRect(250, 320, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.ButtSabt = QtWidgets.QPushButton(sharj)
        self.ButtSabt.setGeometry(QtCore.QRect(10, 560, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ButtSabt.setFont(font)
        self.ButtSabt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtSabt.setObjectName("ButtSabt")
        self.spinBoxSharj = QtWidgets.QSpinBox(sharj)
        self.spinBoxSharj.setGeometry(QtCore.QRect(10, 80, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.spinBoxSharj.setFont(font)
        self.spinBoxSharj.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBoxSharj.setFrame(False)
        self.spinBoxSharj.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxSharj.setReadOnly(False)
        self.spinBoxSharj.setMaximum(2147483647)
        self.spinBoxSharj.setSingleStep(10000)
        self.spinBoxSharj.setProperty("value", 400000)
        self.spinBoxSharj.setObjectName("spinBoxSharj")
        self.label_6 = QtWidgets.QLabel(sharj)
        self.label_6.setGeometry(QtCore.QRect(250, 260, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.spinBoxVahed = QtWidgets.QSpinBox(sharj)
        self.spinBoxVahed.setGeometry(QtCore.QRect(10, 200, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.spinBoxVahed.setFont(font)
        self.spinBoxVahed.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBoxVahed.setFrame(False)
        self.spinBoxVahed.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxVahed.setReadOnly(False)
        self.spinBoxVahed.setMinimum(1)
        self.spinBoxVahed.setMaximum(13)
        self.spinBoxVahed.setSingleStep(1)
        self.spinBoxVahed.setObjectName("spinBoxVahed")
        self.label_7 = QtWidgets.QLabel(sharj)
        self.label_7.setGeometry(QtCore.QRect(250, 380, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lcdNumberMablagh = QtWidgets.QLCDNumber(sharj)
        self.lcdNumberMablagh.setGeometry(QtCore.QRect(10, 500, 231, 51))
        self.lcdNumberMablagh.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lcdNumberMablagh.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumberMablagh.setDigitCount(7)
        self.lcdNumberMablagh.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumberMablagh.setProperty("intValue", 0)
        self.lcdNumberMablagh.setObjectName("lcdNumberMablagh")
        self.label_8 = QtWidgets.QLabel(sharj)
        self.label_8.setGeometry(QtCore.QRect(250, 440, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(sharj)
        self.label_9.setGeometry(QtCore.QRect(250, 140, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.spinBoxOmrani = QtWidgets.QSpinBox(sharj)
        self.spinBoxOmrani.setGeometry(QtCore.QRect(10, 140, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.spinBoxOmrani.setFont(font)
        self.spinBoxOmrani.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBoxOmrani.setFrame(False)
        self.spinBoxOmrani.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxOmrani.setReadOnly(False)
        self.spinBoxOmrani.setMaximum(2147483647)
        self.spinBoxOmrani.setSingleStep(10000)
        self.spinBoxOmrani.setProperty("value", 0)
        self.spinBoxOmrani.setObjectName("spinBoxOmrani")
        self.label_10 = QtWidgets.QLabel(sharj)
        self.label_10.setGeometry(QtCore.QRect(250, 500, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.spinBoxBedehi = QtWidgets.QSpinBox(sharj)
        self.spinBoxBedehi.setGeometry(QtCore.QRect(10, 320, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.spinBoxBedehi.setFont(font)
        self.spinBoxBedehi.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBoxBedehi.setFrame(False)
        self.spinBoxBedehi.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxBedehi.setReadOnly(False)
        self.spinBoxBedehi.setMaximum(2147483647)
        self.spinBoxBedehi.setSingleStep(10000)
        self.spinBoxBedehi.setProperty("value", 0)
        self.spinBoxBedehi.setObjectName("spinBoxBedehi")
        self.spinBoxMolahezat = QtWidgets.QSpinBox(sharj)
        self.spinBoxMolahezat.setGeometry(QtCore.QRect(10, 440, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.spinBoxMolahezat.setFont(font)
        self.spinBoxMolahezat.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBoxMolahezat.setFrame(False)
        self.spinBoxMolahezat.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxMolahezat.setReadOnly(False)
        self.spinBoxMolahezat.setMinimum(-2147483647)
        self.spinBoxMolahezat.setMaximum(2147483647)
        self.spinBoxMolahezat.setSingleStep(10000)
        self.spinBoxMolahezat.setProperty("value", 0)
        self.spinBoxMolahezat.setObjectName("spinBoxMolahezat")
        self.lineEditMolahezat = QtWidgets.QLineEdit(sharj)
        self.lineEditMolahezat.setGeometry(QtCore.QRect(10, 380, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.lineEditMolahezat.setFont(font)
        self.lineEditMolahezat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditMolahezat.setLocale(QtCore.QLocale(
            QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.lineEditMolahezat.setMaxLength(50)
        self.lineEditMolahezat.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditMolahezat.setClearButtonEnabled(True)
        self.lineEditMolahezat.setObjectName("lineEditMolahezat")
        self.label_3.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.ButtSettings.raise_()
        self.ButtBack.raise_()
        self.label_4.raise_()
        self.lcdNumberHazineAb.raise_()
        self.label_5.raise_()
        self.ButtSabt.raise_()
        self.spinBoxSharj.raise_()
        self.label_6.raise_()
        self.spinBoxVahed.raise_()
        self.label_7.raise_()
        self.lcdNumberMablagh.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.spinBoxOmrani.raise_()
        self.label_10.raise_()
        self.spinBoxBedehi.raise_()
        self.spinBoxMolahezat.raise_()
        self.lineEditMolahezat.raise_()
        self.retranslateUi(sharj)
        QtCore.QMetaObject.connectSlotsByName(sharj)
        sharj.setTabOrder(self.spinBoxSharj, self.spinBoxOmrani)
        sharj.setTabOrder(self.spinBoxOmrani, self.spinBoxVahed)
        sharj.setTabOrder(self.spinBoxVahed, self.spinBoxBedehi)
        sharj.setTabOrder(self.spinBoxBedehi, self.lineEditMolahezat)
        sharj.setTabOrder(self.lineEditMolahezat, self.spinBoxMolahezat)
        sharj.setTabOrder(self.spinBoxMolahezat, self.ButtSabt)
        sharj.setTabOrder(self.ButtSabt, self.ButtBack)
        sharj.setTabOrder(self.ButtBack, self.ButtSettings)

        self.name = sharj
        self.check_Style()
        self.spinBoxSharj.setValue(Data['Sharj'])
        self.spinBoxOmrani.setValue(Data['HazineOmrani'])
        self.lcdNumberHazineAb.setProperty(
            "intValue", Data['Nafarat']['1']*sahmNafarRound)
        self.updateData(key='vahed')
        self.ButtBack.clicked.connect(Page.from_sharj_main)
        self.ButtSettings.clicked.connect(Page.show_settings)
        self.ButtSabt.clicked.connect(self.done)
        self.spinBoxSharj.valueChanged.connect(
            lambda: self.updateData(key='sharj'))
        self.spinBoxOmrani.valueChanged.connect(
            lambda: self.updateData(key='omrani'))
        self.spinBoxBedehi.valueChanged.connect(
            lambda: self.updateData(key='bedehi'))
        self.spinBoxVahed.valueChanged.connect(
            lambda: self.updateData(key='vahed'))
        self.spinBoxMolahezat.valueChanged.connect(
            lambda: self.updateData(key='molahezat'))
        self.lineEditMolahezat.textChanged.connect(
            lambda: self.updateData(key='lineMolahezat'))

    def retranslateUi(self, sharj):
        _translate = QtCore.QCoreApplication.translate
        sharj.setWindowTitle(_translate("sharj", AppName))
        self.label.setText(_translate("sharj", "گزارش شارژ ماهیانه"))
        self.label_2.setText(_translate("sharj", DevText))
        self.ButtSettings.setWhatsThis(_translate(
            "sharj", "<html><head/><body><p align=\"center\">تنظیمات</p></body></html>"))
        self.ButtBack.setWhatsThis(_translate(
            "sharj", "<html><head/><body><p align=\"center\">بازگشت</p></body></html>"))
        self.label_3.setText(_translate("sharj", "شارژ ماهیانه"))
        self.label_4.setText(_translate("sharj", "شماره واحد"))
        self.label_5.setText(_translate("sharj", "بدهی نقل از قبل"))
        self.ButtSabt.setText(_translate("sharj", "ثبت"))
        self.label_6.setText(_translate("sharj", "هزینه آب مصرفی"))
        self.label_7.setText(_translate("sharj", "ملاحظات"))
        self.label_8.setText(_translate("sharj", "مبلغ ملاحظات"))
        self.label_9.setText(_translate("sharj", "هزینه عمرانی"))
        self.label_10.setText(_translate("sharj", "مبلغ قابل پرداخت"))
        self.lineEditMolahezat.setPlaceholderText(
            _translate("sharj", "میتوانید خالی بگذارید"))
        self.ButtBack.setToolTip('برگشت')
        self.ButtSettings.setToolTip('تنظیمات')

    def check_Style(self):
        global Data
        if not Data['DarkMode']:
            self.name.setStyleSheet(css.background_light)
            self.label.setStyleSheet(css.label_light)
            self.label_2.setStyleSheet(css.label_light)
            self.label_3.setStyleSheet(css.other_light)
            self.label_4.setStyleSheet(css.other_light)
            self.label_5.setStyleSheet(css.other_light)
            self.label_6.setStyleSheet(css.other_light)
            self.label_7.setStyleSheet(css.other_light)
            self.label_8.setStyleSheet(css.other_light)
            self.label_9.setStyleSheet(css.other_light)
            self.label_10.setStyleSheet(css.other_light)
            self.spinBoxOmrani.setStyleSheet(css.other_light)
            self.spinBoxSharj.setStyleSheet(css.other_light)
            self.spinBoxVahed.setStyleSheet(css.other_light)
            self.spinBoxBedehi.setStyleSheet(css.other_light)
            self.spinBoxMolahezat.setStyleSheet(css.other_light)
            self.ButtSabt.setStyleSheet(css.butt_sabt_light)
            self.lineEditMolahezat.setStyleSheet(css.line_light)
            self.lcdNumberMablagh.setStyleSheet(css.other_light)
            self.lcdNumberHazineAb.setStyleSheet(css.other_light)

            if Data['ShadowEffect']:
                shadowEffect(self.name, QtWidgets.QPushButton, 'light')
                self.label.setGraphicsEffect(
                    Qt.QGraphicsDropShadowEffect(blurRadius=Data_2['Shadow']['light']['blurRadius'], xOffset=Data_2['Shadow']['light']['xOffset'],
                                                 yOffset=Data_2['Shadow']['light']['yOffset'], color=Data_2['Shadow']['light']['color']))
            else:
                shadowEffect(self.name, QtWidgets.QPushButton, remove=True)
                self.label.setGraphicsEffect(None)
        else:
            self.name.setStyleSheet(css.background_dark)
            self.label.setStyleSheet(css.label_dark)
            self.label_2.setStyleSheet(css.label_dark)
            self.label_3.setStyleSheet(css.other_dark)
            self.label_4.setStyleSheet(css.other_dark)
            self.label_5.setStyleSheet(css.other_dark)
            self.label_6.setStyleSheet(css.other_dark)
            self.label_7.setStyleSheet(css.other_dark)
            self.label_8.setStyleSheet(css.other_dark)
            self.label_9.setStyleSheet(css.other_dark)
            self.label_10.setStyleSheet(css.other_dark)
            self.spinBoxOmrani.setStyleSheet(css.other_dark)
            self.spinBoxSharj.setStyleSheet(css.other_dark)
            self.spinBoxVahed.setStyleSheet(css.other_dark)
            self.spinBoxBedehi.setStyleSheet(css.other_dark)
            self.spinBoxMolahezat.setStyleSheet(css.other_dark)
            self.ButtSabt.setStyleSheet(css.butt_sabt_light)
            self.lineEditMolahezat.setStyleSheet(css.line_dark)
            self.lcdNumberMablagh.setStyleSheet(css.other_dark)
            self.lcdNumberHazineAb.setStyleSheet(css.other_dark)

            if Data['ShadowEffect']:
                shadowEffect(self.name, QtWidgets.QPushButton, 'dark')
                self.label.setGraphicsEffect(
                    Qt.QGraphicsDropShadowEffect(blurRadius=Data_2['Shadow']['dark']['blurRadius'], xOffset=Data_2['Shadow']['dark']['xOffset'],
                                                 yOffset=Data_2['Shadow']['dark']['yOffset'], color=Data_2['Shadow']['dark']['color']))
            else:
                shadowEffect(self.name, QtWidgets.QPushButton, remove=True)
                self.label.setGraphicsEffect(None)

    def updateData(self, key=''):
        global Data, sahmNafarRound, Data_3
        if key == 'sharj':
            val = self.spinBoxSharj.value()
            Data['Sharj'] = val
            saveJson()
            self.updateData(key='vahed')
        elif key == 'omrani':
            val = self.spinBoxOmrani.value()
            Data['HazineOmrani'] = val
            saveJson()
            self.updateData(key='vahed')
        elif key == 'bedehi':
            val1 = str(self.spinBoxVahed.value())
            val2 = self.spinBoxBedehi.value()
            Data['Bedehi'][val1] = val2
            saveJson()
            self.updateData(key='vahed')
        elif key == 'molahezat':
            val1 = str(self.spinBoxVahed.value())
            val2 = self.spinBoxMolahezat.value()
            Data['Molahezat'][val1] = val2
            saveJson()
            self.updateData(key='vahed')
        elif key == 'lineMolahezat':
            val = str(self.spinBoxVahed.value())
            txt = str(self.lineEditMolahezat.text())
            Data_3['molahezat'][val] = txt
        elif key == 'vahed':
            val = str(self.spinBoxVahed.value())
            self.spinBoxMolahezat.setValue(Data['Molahezat'][val])
            hazine = [Data['Nafarat'][val]*sahmNafarRound, Data['Bedehi'][val],
                      self.spinBoxMolahezat.value(), self.spinBoxSharj.value(), self.spinBoxOmrani.value()]
            self.spinBoxBedehi.setValue(hazine[1])
            self.lcdNumberHazineAb.setProperty("intValue", hazine[0])
            self.lcdNumberMablagh.setProperty(
                "intValue", int(sum(hazine))+int(val))
            if val in Data_3['molahezat'].keys():
                self.lineEditMolahezat.setText(Data_3['molahezat'][val])
                if Data_3['molahezat'][val] == '':
                    del Data_3['molahezat'][val]
                    self.lineEditMolahezat.clear()
            else:
                self.lineEditMolahezat.clear()

    def done(self):
        global Data_3
        self.ButtSabt.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        try:
            Data_3['donePages']['sharj'] = True
            val = str(self.spinBoxVahed.value())
            val2 = self.spinBoxOmrani.value()
            for i in range(1, 14):
                val = str(i)
                Data_3['mablaghPardakht'][val] = sum(
                    [Data['Nafarat'][val]*sahmNafarRound, Data['Bedehi'][val], Data['Molahezat'][val], Data['Sharj'], int(val), val2])
            saveExcel('sharj')
            sendNotification('ثبت شد')
            Page.from_sharj_main()
        except:
            sendNotification(
                'خطایی رخ داده است\n(اگر فایل اکسل باز است آن را ببندید)')
        self.ButtSabt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


class Ui_abyari(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, abyari):
        global Data
        abyari.setObjectName("abyari")
        abyari.resize(480, 640)
        abyari.setMinimumSize(QtCore.QSize(480, 640))
        abyari.setMaximumSize(QtCore.QSize(480, 640))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        abyari.setFont(font)
        abyari.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pics/.Images/Icon/euro.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        abyari.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(abyari)
        self.label.setGeometry(QtCore.QRect(70, 10, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(abyari)
        self.label_2.setGeometry(QtCore.QRect(20, 615, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(9)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ButtSettings = QtWidgets.QPushButton(abyari)
        self.ButtSettings.setGeometry(QtCore.QRect(420, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ButtSettings.setFont(font)
        self.ButtSettings.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtSettings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            ":/pics/.Images/Icon/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtSettings.setIcon(icon1)
        self.ButtSettings.setIconSize(QtCore.QSize(48, 48))
        self.ButtSettings.setStyleSheet(css.butt_transparent)
        self.ButtSettings.setObjectName("ButtSettings")
        self.ButtBack = QtWidgets.QPushButton(abyari)
        self.ButtBack.setGeometry(QtCore.QRect(10, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ButtBack.setFont(font)
        self.ButtBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtBack.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pics/.Images/Icon/back.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtBack.setIcon(icon2)
        self.ButtBack.setIconSize(QtCore.QSize(48, 48))
        self.ButtBack.setStyleSheet(css.butt_transparent)
        self.ButtBack.setObjectName("ButtBack")
        self.label_3 = QtWidgets.QLabel(abyari)
        self.label_3.setGeometry(QtCore.QRect(120, 80, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.ComboVahed = QtWidgets.QComboBox(abyari)
        self.ComboVahed.setGeometry(QtCore.QRect(20, 140, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ComboVahed.setFont(font)
        self.ComboVahed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ComboVahed.setEditable(False)
        self.ComboVahed.setMaxVisibleItems(13)
        self.ComboVahed.setMaxCount(13)
        self.ComboVahed.setFrame(False)
        self.ComboVahed.setObjectName("ComboVahed")
        self.label_4 = QtWidgets.QLabel(abyari)
        self.label_4.setGeometry(QtCore.QRect(260, 220, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.ComboNobat = QtWidgets.QComboBox(abyari)
        self.ComboNobat.setGeometry(QtCore.QRect(20, 220, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ComboNobat.setFont(font)
        self.ComboNobat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ComboNobat.setEditable(False)
        self.ComboNobat.setMaxVisibleItems(2)
        self.ComboNobat.setMaxCount(2)
        self.ComboNobat.setFrame(False)
        self.ComboNobat.setObjectName("ComboNobat")
        self.ButtSabt = QtWidgets.QPushButton(abyari)
        self.ButtSabt.setGeometry(QtCore.QRect(10, 560, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ButtSabt.setFont(font)
        self.ButtSabt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtSabt.setObjectName("ButtSabt")
        self.label_5 = QtWidgets.QLabel(abyari)
        self.label_5.setGeometry(QtCore.QRect(90, 300, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lineEditTarikh1 = QtWidgets.QLineEdit(abyari)
        self.lineEditTarikh1.setGeometry(QtCore.QRect(20, 360, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(16)
        self.lineEditTarikh1.setFont(font)
        self.lineEditTarikh1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditTarikh1.setLocale(QtCore.QLocale(
            QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.lineEditTarikh1.setMaxLength(50)
        self.lineEditTarikh1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditTarikh1.setClearButtonEnabled(True)
        self.lineEditTarikh1.setObjectName("lineEditTarikh1")
        self.label_6 = QtWidgets.QLabel(abyari)
        self.label_6.setGeometry(QtCore.QRect(90, 430, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lineEditTarikh2 = QtWidgets.QLineEdit(abyari)
        self.lineEditTarikh2.setGeometry(QtCore.QRect(20, 490, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(16)
        self.lineEditTarikh2.setFont(font)
        self.lineEditTarikh2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditTarikh2.setLocale(QtCore.QLocale(
            QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.lineEditTarikh2.setMaxLength(50)
        self.lineEditTarikh2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditTarikh2.setClearButtonEnabled(True)
        self.lineEditTarikh2.setObjectName("lineEditTarikh2")
        self.label_3.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.ButtSettings.raise_()
        self.ButtBack.raise_()
        self.ComboVahed.raise_()
        self.label_4.raise_()
        self.ComboNobat.raise_()
        self.ButtSabt.raise_()
        self.label_5.raise_()
        self.lineEditTarikh1.raise_()
        self.label_6.raise_()
        self.lineEditTarikh2.raise_()
        self.retranslateUi(abyari)
        self.ComboVahed.setCurrentIndex(0)
        self.ComboNobat.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(abyari)
        abyari.setTabOrder(self.ComboVahed, self.ComboNobat)
        abyari.setTabOrder(self.ComboNobat, self.lineEditTarikh1)
        abyari.setTabOrder(self.lineEditTarikh1, self.lineEditTarikh2)
        abyari.setTabOrder(self.lineEditTarikh2, self.ButtSabt)
        abyari.setTabOrder(self.ButtSabt, self.ButtBack)
        abyari.setTabOrder(self.ButtBack, self.ButtSettings)

        self.name = abyari
        self.check_Style()
        self.ComboVahed.addItems(sortList(Data['Nafarat'].keys()))
        self.ComboNobat.addItems(['اول', 'دوم'])
        self.updateData()
        self.ButtBack.clicked.connect(Page.from_abyari_main)
        self.ButtSabt.clicked.connect(self.done)
        self.ButtSettings.clicked.connect(Page.show_settings)
        self.ComboVahed.currentIndexChanged.connect(
            lambda: self.updateData(False))
        self.ComboNobat.currentIndexChanged.connect(
            lambda: self.updateData(False))
        self.lineEditTarikh1.textEdited.connect(lambda: self.updateData(True))
        self.lineEditTarikh2.textEdited.connect(lambda: self.updateData(True))

    def retranslateUi(self, abyari):
        _translate = QtCore.QCoreApplication.translate
        abyari.setWindowTitle(_translate("abyari", AppName))
        self.label.setText(_translate("abyari", "زمانبندی آبیاری فضای سبز"))
        self.label_2.setText(_translate("abyari", DevText))
        self.ButtSettings.setWhatsThis(_translate(
            "abyari", "<html><head/><body><p align=\"center\">تنظیمات</p></body></html>"))
        self.ButtBack.setWhatsThis(_translate(
            "abyari", "<html><head/><body><p align=\"center\">بازگشت</p></body></html>"))
        self.label_3.setText(_translate("abyari", "شماره واحد"))
        self.label_4.setText(_translate("abyari", "نوبت"))
        self.ButtSabt.setText(_translate("abyari", "ثبت"))
        self.label_5.setText(_translate("abyari", "از تاریخ"))
        self.lineEditTarikh1.setPlaceholderText(
            _translate("abyari", "[روز] [ماه] - مثال: 17 خرداد"))
        self.label_6.setText(_translate("abyari", "تا تاریخ"))
        self.lineEditTarikh2.setPlaceholderText(
            _translate("abyari", "[روز] [ماه] - مثال: 23 خرداد"))
        self.ButtBack.setToolTip('برگشت')
        self.ButtSettings.setToolTip('تنظیمات')

    def check_Style(self):
        global Data
        if not Data['DarkMode']:
            self.name.setStyleSheet(css.background_light)
            self.ButtSabt.setStyleSheet(css.butt_sabt_light)
            self.label.setStyleSheet(css.label_light)
            self.label_2.setStyleSheet(css.label_light)
            self.label_3.setStyleSheet(css.other_light)
            self.label_4.setStyleSheet(css.other_light)
            self.label_5.setStyleSheet(css.other_light)
            self.label_6.setStyleSheet(css.other_light)
            self.ComboVahed.setStyleSheet(css.other_light)
            self.ComboNobat.setStyleSheet(css.other_light)
            self.lineEditTarikh1.setStyleSheet(css.line_light)
            self.lineEditTarikh2.setStyleSheet(css.line_light)

            if Data['ShadowEffect']:
                shadowEffect(self.name, QtWidgets.QPushButton, 'light')
                self.label.setGraphicsEffect(
                    Qt.QGraphicsDropShadowEffect(blurRadius=Data_2['Shadow']['light']['blurRadius'], xOffset=Data_2['Shadow']['light']['xOffset'],
                                                 yOffset=Data_2['Shadow']['light']['yOffset'], color=Data_2['Shadow']['light']['color']))
            else:
                shadowEffect(self.name, QtWidgets.QPushButton, remove=True)
                self.label.setGraphicsEffect(None)
        else:
            self.name.setStyleSheet(css.background_dark)
            self.ButtSabt.setStyleSheet(css.butt_sabt_light)
            self.label.setStyleSheet(css.label_dark)
            self.label_2.setStyleSheet(css.label_dark)
            self.label_3.setStyleSheet(css.other_dark)
            self.label_4.setStyleSheet(css.other_dark)
            self.label_5.setStyleSheet(css.other_dark)
            self.label_6.setStyleSheet(css.other_dark)
            self.ComboVahed.setStyleSheet(css.other_dark)
            self.ComboNobat.setStyleSheet(css.other_dark)
            self.lineEditTarikh1.setStyleSheet(css.line_dark)
            self.lineEditTarikh2.setStyleSheet(css.line_dark)

            if Data['ShadowEffect']:
                shadowEffect(self.name, QtWidgets.QPushButton, 'dark')
                self.label.setGraphicsEffect(
                    Qt.QGraphicsDropShadowEffect(blurRadius=Data_2['Shadow']['dark']['blurRadius'], xOffset=Data_2['Shadow']['dark']['xOffset'],
                                                 yOffset=Data_2['Shadow']['dark']['yOffset'], color=Data_2['Shadow']['dark']['color']))
            else:
                shadowEffect(self.name, QtWidgets.QPushButton, remove=True)
                self.label.setGraphicsEffect(None)

    def updateData(self, key=False):
        global Data_2
        temp = {
            'اول': '1',
            "دوم": '2'
        }
        d1 = self.lineEditTarikh1
        d2 = self.lineEditTarikh2
        vahed = self.ComboVahed.currentText()
        nobat = temp[self.ComboNobat.currentText()]
        if key:
            Data_2['Abyari'][vahed][nobat][0] = d1.text()
            Data_2['Abyari'][vahed][nobat][1] = d2.text()
            return
        d1.setText(Data_2['Abyari'][vahed][nobat][0])
        d2.setText(Data_2['Abyari'][vahed][nobat][1])

    def done(self):
        global Data_3
        self.ButtSabt.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        try:
            saveExcel('abyari')
            Data_3['donePages']['abyari'] = True
            sendNotification('ثبت شد')
            Page.from_abyari_main()
        except:
            sendNotification(
                'خطایی رخ داده است\n(اگر فایل اکسل باز است آن را ببندید)')
        self.ButtSabt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


class Ui_output(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, output):
        global Data_3
        output.setObjectName("output")
        output.resize(320, 280)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(output.sizePolicy().hasHeightForWidth())
        output.setSizePolicy(sizePolicy)
        output.setMinimumSize(QtCore.QSize(320, 280))
        output.setMaximumSize(QtCore.QSize(320, 280))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pics/.Images/Icon/euro.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        output.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(output)
        self.label.setGeometry(QtCore.QRect(60, 0, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.ButtBack = QtWidgets.QPushButton(output)
        self.ButtBack.setGeometry(QtCore.QRect(10, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ButtBack.setFont(font)
        self.ButtBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtBack.setStyleSheet(css.butt_transparent)
        self.ButtBack.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pics/.Images/Icon/back.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtBack.setIcon(icon1)
        self.ButtBack.setIconSize(QtCore.QSize(36, 36))
        self.ButtBack.setObjectName("ButtBack")
        self.label_2 = QtWidgets.QLabel(output)
        self.label_2.setGeometry(QtCore.QRect(0, 250, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(8)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.CheckAbyari = QtWidgets.QCheckBox(output)
        self.CheckAbyari.setGeometry(QtCore.QRect(200, 180, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(12)
        self.CheckAbyari.setFont(font)
        self.CheckAbyari.setCursor(QtGui.QCursor(
            setCurser(Data_3['donePages']['abyari'])))
        self.CheckAbyari.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CheckAbyari.setChecked(False)
        self.CheckAbyari.setCheckable(Data_3['donePages']['abyari'])
        self.CheckAbyari.setObjectName("CheckAbyari")
        self.CheckAb = QtWidgets.QCheckBox(output)
        self.CheckAb.setGeometry(QtCore.QRect(130, 140, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(12)
        self.CheckAb.setFont(font)
        self.CheckAb.setCursor(QtGui.QCursor(
            setCurser(Data_3['donePages']['ab'])))
        self.CheckAb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CheckAb.setChecked(False)
        self.CheckAb.setCheckable(Data_3['donePages']['ab'])
        self.CheckAb.setObjectName("CheckAb")
        self.CheckBilan6Month = QtWidgets.QCheckBox(output)
        self.CheckBilan6Month.setGeometry(QtCore.QRect(150, 60, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(12)
        self.CheckBilan6Month.setFont(font)
        self.CheckBilan6Month.setCursor(QtGui.QCursor(
            setCurser(Data_3['donePages']['bilan'])))
        self.CheckBilan6Month.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CheckBilan6Month.setChecked(False)
        self.CheckBilan6Month.setCheckable(Data_3['donePages']['bilan'])
        self.CheckBilan6Month.setObjectName("CheckBilan6Month")
        self.CheckSharj = QtWidgets.QCheckBox(output)
        self.CheckSharj.setGeometry(QtCore.QRect(160, 100, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(12)
        self.CheckSharj.setFont(font)
        self.CheckSharj.setCursor(QtGui.QCursor(
            setCurser(Data_3['donePages']['sharj'])))
        self.CheckSharj.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CheckSharj.setChecked(False)
        self.CheckSharj.setCheckable(Data_3['donePages']['sharj'])
        self.CheckSharj.setObjectName("CheckSharj")
        self.ButtSabt = QtWidgets.QPushButton(output)
        self.ButtSabt.setGeometry(QtCore.QRect(10, 210, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.ButtSabt.setFont(font)
        self.ButtSabt.setCursor(QtGui.QCursor(setCurser(False)))
        self.ButtSabt.setObjectName("ButtSabt")
        self.retranslateUi(output)
        QtCore.QMetaObject.connectSlotsByName(output)
        output.setTabOrder(self.CheckBilan6Month, self.CheckSharj)
        output.setTabOrder(self.CheckSharj, self.CheckAb)
        output.setTabOrder(self.CheckAb, self.CheckAbyari)
        output.setTabOrder(self.CheckAbyari, self.ButtSabt)
        output.setTabOrder(self.ButtSabt, self.ButtBack)

        self.name = output
        self.temp = [self.CheckBilan6Month.checkState(), self.CheckSharj.checkState(),
                     self.CheckAb.checkState(), self.CheckAbyari.checkState()]
        self.check_Style()
        self.ButtBack.clicked.connect(Page.close_output)
        self.ButtSabt.clicked.connect(self.done)
        self.CheckBilan6Month.clicked.connect(lambda: self.updateData(
            self.CheckBilan6Month.checkState(), 1, 'بیلان 6 ماهه'))
        self.CheckSharj.clicked.connect(lambda: self.updateData(
            self.CheckSharj.checkState(), 2, 'گزارش شارژ'))
        self.CheckAb.clicked.connect(lambda: self.updateData(
            self.CheckAb.checkState(), 3, 'سهم آب مصرفی'))
        self.CheckAbyari.clicked.connect(lambda: self.updateData(
            self.CheckAbyari.checkState(), 4, 'آبیاری'))

    def retranslateUi(self, output):
        _translate = QtCore.QCoreApplication.translate
        output.setWindowTitle(_translate("output", "Output PDF"))
        self.label.setText(_translate("output", "دریافت خروجی PDF"))
        self.ButtBack.setWhatsThis(_translate(
            "output", "<html><head/><body><p align=\"center\">برگشت</p></body></html>"))
        self.label_2.setText(_translate("output", DevText))
        self.CheckAbyari.setText(_translate("output", "صفحه آبیاری"))
        self.CheckAb.setText(_translate("output", "صفحه سهم آب مصرفی"))
        self.CheckBilan6Month.setText(
            _translate("output", "صفحه بیلان 6 ماهه"))
        self.CheckSharj.setText(_translate("output", "صفحه گزارش شارژ"))
        self.ButtSabt.setText(_translate("output", "ثبت"))
        self.ButtBack.setToolTip('برگشت')

    def check_Style(self):
        global Data
        # self.name.setWindowFlags(QtCore.Qt.FramelessWindowHint) # frame around setting page
        if not Data['DarkMode']:
            self.name.setStyleSheet(css.background_light)
            self.CheckSharj.setStyleSheet(css.label_light)
            self.CheckBilan6Month.setStyleSheet(css.label_light)
            self.CheckAb.setStyleSheet(css.label_light)
            self.CheckAbyari.setStyleSheet(css.label_light)
            self.label_2.setStyleSheet(css.label_light)
            self.label.setStyleSheet(css.label_light)
            self.ButtSabt.setStyleSheet(css.butt_sabt_light)

            if Data['ShadowEffect']:
                shadowEffect(self.name, QtWidgets.QPushButton, 'light')
                self.label.setGraphicsEffect(
                    Qt.QGraphicsDropShadowEffect(blurRadius=Data_2['Shadow']['light']['blurRadius'], xOffset=Data_2['Shadow']['light']['xOffset'],
                                                 yOffset=Data_2['Shadow']['light']['yOffset'], color=Data_2['Shadow']['light']['color']))
            else:
                shadowEffect(self.name, QtWidgets.QPushButton, remove=True)
                self.label.setGraphicsEffect(None)
        else:
            self.name.setStyleSheet(css.background_dark)
            self.CheckAb.setStyleSheet(css.label_dark)
            self.CheckBilan6Month.setStyleSheet(css.label_dark)
            self.CheckSharj.setStyleSheet(css.label_dark)
            self.CheckAbyari.setStyleSheet(css.label_dark)
            self.label_2.setStyleSheet(css.label_dark)
            self.label.setStyleSheet(css.label_dark)
            self.ButtSabt.setStyleSheet(css.butt_sabt_dark)

            if Data['ShadowEffect']:
                shadowEffect(self.name, QtWidgets.QPushButton, 'dark')
                self.label.setGraphicsEffect(
                    Qt.QGraphicsDropShadowEffect(blurRadius=Data_2['Shadow']['dark']['blurRadius'], xOffset=Data_2['Shadow']['dark']['xOffset'],
                                                 yOffset=Data_2['Shadow']['dark']['yOffset'], color=Data_2['Shadow']['dark']['color']))
            else:
                shadowEffect(self.name, QtWidgets.QPushButton, remove=True)
                self.label.setGraphicsEffect(None)

    def updateData(self, key, index, sheet, bySheetName=False):
        global Data_3
        self.temp = [self.CheckBilan6Month.checkState(), self.CheckSharj.checkState(),
                     self.CheckAb.checkState(), self.CheckAbyari.checkState()]
        if bySheetName:
            if key:
                Data_3['output'].append(sheet)
            elif sheet in Data_3['output']:
                del Data_3['output'][Data_3['output'].index(sheet)]
        else:
            if key:
                Data_3['output'].append(index)
            elif index in Data_3['output']:
                del Data_3['output'][Data_3['output'].index(index)]
        self.ButtSabt.setCursor(QtGui.QCursor(setCurser(any(self.temp))))

    def done(self):
        global Data, Data_3
        if any(self.temp):
            self.ButtSabt.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
            try:
                temp = {}
                for i in Data_3['output']:
                    temp[i] = Data['PagesSize'][i-1]
                text = E.convert_to_pdf(Data['PDF_outputName'], temp)
                if Data['ShowPDF']:
                    path = os.path.join(os.path.join(
                        os.environ['USERPROFILE']), 'Desktop')
                    path = f'{path}\\{Data["PDF_outputName"]}.pdf'
                    os.startfile(path)
                sendNotification(f'ثبت شد\n{text}')
                Page.close_output()
            except:
                sendNotification('خطا')
            self.ButtSabt.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        else:
            sendNotification(
                'حداقل یکی از صفحات باید انتخاب شود\n(اگر به شما اجازه داده نمیشود باید صفحه مورد نظر را کامل کنید)')


app = QtWidgets.QApplication(sys.argv)
Page = Windows()
Page.show_main()
sys.exit(app.exec_())
