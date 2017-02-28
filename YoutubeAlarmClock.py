#! /Python34
#! -*- coding: utf-8 -*-

"""
https://www.reddit.com/r/beginnerprojects/comments/4n9hne/project_idea_alarm_clock/
Paul Bosonetto
2/22/2017

Alarm Clock, accessed through a PyQt5 Gui, that displays a random Youtube video
(chosen from links in a text file), upon a user specified time.

"""

import sys, random
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication, QPushButton,
    QFrame, QHBoxLayout, QVBoxLayout, QSplitter, QStyleFactory, QTableWidget,
    QHeaderView, QGridLayout)
from PyQt5.QtCore import Qt


class LinkPopup(QWidget):
    def __init__(self):
        super().__init__()

        self.initPopup()

    def initPopup(self):

        browseBtn = QPushButton(self)
        #table or list with links
        #need a label to show 'links list' location

        self.setGeometry(400,400,400,300)
        self.setWindowTitle('Link List')
        self.show()


class NewAlarmPopup(QWidget):
    def __init__(self):
        super().__init__()

        self.initPopup()

    def initPopup(self):
        self.setGeometry(300,300,400,300)
        self.setWindowTitle('Add new alarm')
        self.show()

class AlarmClock(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    #TODO put all the GUI stuff in another file and import it?
    #set up GUI
    def initUI(self):

        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)

        button1 = QPushButton('Add New Alarm')
        button1.clicked.connect(self.openNewAlarmWindow)
        button2 = QPushButton('Update Links File')
        button2.clicked.connect(self.openLinkUpdatePopup)

        table1 = QTableWidget(mainWidget)
        #setRowCount number of columns for number of entries for that day
        table1.setRowCount(8)
        table1.setColumnCount(1)
        vLabels = ['Monday','', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday',
                  'Sunday']
        hLabels = ['Alarms']
        table1.setVerticalHeaderLabels(vLabels)
        table1.setHorizontalHeaderLabels(hLabels)

        #make horizontal label fill panel
        headerH = table1.horizontalHeader()
        headerH.setSectionResizeMode(QHeaderView.Stretch)

        headerV = table1.verticalHeader()
        headerV.setSectionResizeMode(QHeaderView.Stretch)

        table2 = QTableWidget(mainWidget)
        #setRowCount number of columns for number of entries for that day
        table2.setRowCount(8)
        table2.setColumnCount(1)
        hLabels2 = ['Video Link File: ']
        table2.setHorizontalHeaderLabels(hLabels2)

        headerH2 = table2.horizontalHeader()
        headerH2.setSectionResizeMode(QHeaderView.Stretch)

        headerV2 = table2.verticalHeader()
        headerV2.setSectionResizeMode(QHeaderView.Stretch)

        widge1 =  QWidget()
        vbox = QVBoxLayout(mainWidget)
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        widge1.setLayout(vbox)

        hbox = QHBoxLayout(mainWidget)
        hbox.addWidget(table1)
        hbox.addWidget(widge1)
        hbox.addWidget(table2)


        self.setGeometry(300,300,800,600)
        self.setFixedSize(800,600)
        self.setWindowTitle('Youtube Alarm Clock')
        self.show()


    def openNewAlarmWindow(self):
        self.popup = NewAlarmPopup()
        self.show()

    def openLinkUpdatePopup(self):
        self.linkPopup = LinkPopup()
        self.show()

"""
    def addAlarm(self):

        #addAlarm Gui
        #new window
        #select days with checkbox #specify time
        #pushbutton 'add alarm'


        #add new alarm to alarms
        #refresh displayAlarms()


    def displayAlarms(self):



    def addAlarmtoDict(self):


    def sortAlarms(self):

        #iterate through dictionary of alarms and sort the list entries
        #chronologically for each key


    def updateLinksList(self, link):

        #add parsed links to list


    def parseVideoLinks(self):

        #read in text file of links seperated by either newline, space, or
        #by commas. Read function must be robust, or change all entries
        #to similar forms with regexs.

        #read in file line by line
        #seperate link on either newline, space or commas
        #send seperated link to updateLinksList


"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    al = AlarmClock()
    sys.exit(app.exec_())
