from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon,QPixmap
import sys
from bs4 import BeautifulSoup
import requests
import css_code


def exit1():
    m2=QtWidgets.QMessageBox.question(program, 'Cps', 'هل تريد الخروج؟')
    if m2==QtWidgets.QMessageBox.Yes:
        exit()
def Ozone():
    l1.hide()
    b1.hide()
    b2.hide()
    b3.hide()
def weather():
    weater1=[]
    wind=[]
    weater3=[]
    weater4=[]
    l1.hide()
    b1.hide()
    b2.hide()
    b3.hide()
    l2=QtWidgets.QLabel(program)
    l2.setStyleSheet(css_code.css2)
    l2.move(300,80)
    l2.resize(200, 50)
    l3=QtWidgets.QLabel('درجه الحراره في دمنهور',program)
    l3.setStyleSheet(css_code.css2)
    l3.move(500, 40)
    l3.resize(500, 100)
    l3.show()
    l4=QtWidgets.QLabel('سرعه الرياح',program)
    l4.setStyleSheet(css_code.css2)
    l4.move(650, 200)
    l4.resize(500, 100)
    l4.show()
    l5=QtWidgets.QLabel(program)
    l5.setStyleSheet(css_code.css2)
    l5.move(640, 200)
    l5.resize(200, 100)
    l5.show()
    l6=QtWidgets.QLabel(program)
    i3=QPixmap('icons//wind.png').scaled(100,100)
    l6.setPixmap(i3)
    l6.resize(200,200)
    l6.move(1200,160)
    l6.show()
    try:
        r1=requests.get('https://www.msn.com/en-us/weather/forecast/in-Qesm-Damanhour,Al-Buhayrah?ocid=ansmsnweather&loc=eyJsIjoiUWVzbSBEYW1hbmhvdXIiLCJyIjoiQWwgQnVoYXlyYWgiLCJyMiI6IkRhbWFuaG91ciIsImMiOiJFZ3lwdCIsImkiOiJFRyIsImciOiJlbi11cyIsIngiOiIzMC40NjQiLCJ5IjoiMzEuMDMzIn0%3D&weadegreetype=C')
        r2=r1.content
        x1=BeautifulSoup(r2,'lxml')
        x2=x1.find_all('a',{"class":"summaryTemperatureCompact-E1_1 summaryTemperatureHover-E1_1"})
        for i in range(len(x2)):
            weater1.append(x2[i].text)
        l2.setText(weater1[0])
        l2.show()
        x3=x1.find_all('div',{"id":"CurrentDetailLineWindValue"})
        for i2 in range(len(x2)):
            wind.append(x3[i2].text)
        l5.setText(wind[0])
    except:
        l2.hide()
        l3.hide()
        l4.hide()
        l5.hide()
        l6.hide()
        b4.hide()
        m1=QtWidgets.QMessageBox.warning(program, 'Cps', 'حدث خطأ')
        exit()
#pushButton.setIconSize(QtCore.QSize(100, 100))
app=QtWidgets.QApplication(sys.argv)
program=QtWidgets.QMainWindow()
program.setWindowTitle('Cps')
program.setStyleSheet(css_code.css1)
l1=QtWidgets.QLabel(program)
i1=QPixmap('icons//Cps.png')
l1.setPixmap(i1)
l1.resize(400,300)
l1.move(500,10)
b1=QtWidgets.QPushButton('الطقس', program)
b1.setIcon(QIcon('icons//sun.png'))
b1.setIconSize(QtCore.QSize(50, 40))
b1.clicked.connect(weather)
b1.setStyleSheet(css_code.css4)
b1.resize(250, 50)
b1.move(10, 400)
b2=QtWidgets.QPushButton('الاوزون', program)
b2.setStyleSheet(css_code.css4)
b2.resize(200, 50)
b2.move(350, 400)
b2.setIcon(QIcon('icons//earth-1.png'))
b2.setIconSize(QtCore.QSize(50, 40))
b3=QtWidgets.QPushButton('الطول الموجي', program)
b3.setStyleSheet(css_code.css4)
b3.resize(250, 50)
b3.move(650, 400)
b3.setIcon(QIcon('icons//ozone-layer.png'))
b3.setIconSize(QtCore.QSize(50, 40))
b4=QtWidgets.QPushButton('خروج',program)
b4.setStyleSheet(css_code.css7)
b4.resize(150, 50)
b4.move(1220, 660)
b4.setIcon(QIcon('icons//exit.png'))
b4.setIconSize(QtCore.QSize(50, 40))
b4.show()
b4.clicked.connect(exit1)
program.showMaximized()
app.exec_()