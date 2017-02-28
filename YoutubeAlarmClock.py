#! /Python34
#! -*- coding: utf-8 -*-

"""
https://www.reddit.com/r/beginnerprojects/comments/4n9hne/project_idea_alarm_clock/
Paul Bosonetto
2/22/2017

Alarm Clock, accessed through a PyQt5 Gui, that displays a random Youtube video
(chosen from links in a text file), upon a user specified time.

"""

import sys, random, ytAlarmClockGUI
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication, QPushButton,
    QFrame, QHBoxLayout, QVBoxLayout, QSplitter, QStyleFactory, QTableWidget,
    QTableWidgetItem, QHeaderView, QGridLayout, QFileDialog, QAction)
from PyQt5.QtCore import Qt



class AlarmClock():

    def __init__(self):
        super().__init__()
        self.ui = ytAlarmClockGUI.MainUI()

        self.linksList = []
        self.linkFile = ''
        self.ui.button2.clicked.connect(self.getLinksFile)


    def getLinksFile(self):

        filename = QFileDialog.getOpenFileName()

        if filename[0]:
            self.linkFile += filename[0]
            print (self.linkFile)

        self.parseLinks()


    def parseLinks(self):

        #case 1: links seperated by newline '\n'
        with open(self.linkFile, 'r') as f:
            for row in f:
                self.linksList.append(row.split())

        for item in self.linksList:
            print (item)

        self.popLinkTable()

    def popLinkTable(self):
        self.ui.hLabels2[0] += self.linkFile
        self.ui.table2.setHorizontalHeaderLabels(self.ui.hLabels2)
        for i in range(len(self.linksList)):
            for j in range(0,8):
                item = QTableWidgetItem(self.linksList[i][0])
                self.ui.table2.setItem(0,j,item)




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
